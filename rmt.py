"""RMT-lite mutation engine for VerdictGate (W4 implementation, 2026-09-24).

Mutates Playwright assertions (not app code). Balanced-paren scanner —
no regex nesting traps. Runner-agnostic by construction: matches the text
form `expect(...).matcher(...)` (Playwright, Vitest + jest-dom, compat shims).
Unwraps `.soft` / `.element` chain hops. Never emits no-op mutants (mutated ==
original rows are refused pre-seed, mirroring the verdictgate NOOP rule).
Version-stamped: every mutant carries `rmt_version` (see RMT_VERSION).
Pilot scope: toBeVisible / toHaveText / toHaveLength / toBeHidden.
Standalone: `python3 rmt.py FILE --tier B2 --format summary|json`.
Importable: `from rmt import generate_mutants_for_file`.
CLI: integrated as `verdictgate rmt` (W2).
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

RMT_VERSION = "0.1.0"
# First version-stamped engine. Batches seeded before this stamp are pre-0.1.0
# (no NO-OP guard, no expect.soft, no chain-unwrap). One verdict batch = one
# engine version — never mix stamps inside a batch.

# Matcher -> (operator, mutator of the full call text)
MATCHERS = ("toBeVisible", "toHaveText", "toHaveLength", "toBeHidden")

# Chain hops unwrapped before the terminal matcher (compat shims).
CHAIN_HOPS = ("soft", "element")

OPERATOR_SETS = {
    "B0": ["EQ_NEGATION"],
    "B1": ["EQ_NEGATION"],
    "B2": ["EQ_NEGATION", "COLLECTION_EMPTY"],  # Pilot scope
    "B3": [],  # by design: trend-only tier, nothing seeded
}

# matcher -> operator (only what the pilot implements)
MATCHER_OPERATOR = {
    "toBeVisible": "EQ_NEGATION",
    "toHaveText": "EQ_NEGATION",
    "toHaveLength": "COLLECTION_EMPTY",
    "toBeHidden": "EQ_NEGATION",
}


def balanced_span(text: str, open_idx: int) -> int | None:
    """Return index just past the paren matching text[open_idx] == '('.

    Skips over single/double-quoted and template strings. None if unbalanced.
    """
    depth = 0
    i = open_idx
    n = len(text)
    quote = None
    while i < n:
        ch = text[i]
        if quote:
            if ch == "\\":
                i += 2
                continue
            if ch == quote:
                quote = None
        elif ch in ("'", '"', "`"):
            quote = ch
        elif ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return None


def find_assertions(content: str) -> list:
    """Yield (expect_start, call_end, matcher) for each expect-chain ending in a known matcher.

    Parses segment by segment: `expect(...)` args, then `.name(args)` hops.
    Known chain hops (`.soft`, `.element` — Vitest / compat shims) are unwrapped;
    the terminal matcher must be in MATCHER_OPERATOR. Unknown hops and `.not`
    chains (no paren after `not`) end the chain with no mutant — already-negated
    assertions are never double-mutated.

    NOTE: a single balanced_span from expect's `(` cannot be used here — it would
    swallow `.element(option)` as nested parens. Hence the segment walk.
    """
    out = []
    for m in re.finditer(r"expect(?=\.|\()", content):
        start = m.start()
        pos = m.end()
        # Optional expect() args.
        if content[pos : pos + 1] == "(":
            close = balanced_span(content, pos)
            if close is None:
                continue
            pos = close
        # Chain segments.
        while True:
            mm = re.match(r"\.(\w+)\(", content[pos:])
            if not mm:
                break
            name = mm.group(1)
            seg_close = balanced_span(content, pos + len(mm.group(0)) - 1)
            if seg_close is None:
                break
            if name in MATCHER_OPERATOR:
                out.append((start, seg_close, name))
                break
            if name in CHAIN_HOPS:
                pos = seg_close
                continue
            break
    return out


def apply_mutation(call: str, operator: str) -> str:
    """Return mutated assertion text."""
    if operator == "EQ_NEGATION":
        if re.search(r"\.not\.(toBeVisible|toHaveText|toBeHidden)\(", call):
            return call  # already negated — do not double-mutate
        return re.sub(
            r"\.(toBeVisible|toHaveText|toBeHidden)\(",
            r".not.\1(",
            call,
            count=1,
        )
    if operator == "COLLECTION_EMPTY":
        return re.sub(r"\.toHaveLength\(\d+\)", ".toHaveLength(0)", call, count=1)
    raise ValueError(f"unknown operator: {operator}")


def get_applicable_operators(assertion_text: str, tier: str) -> list:
    """Operators applicable to one assertion string at tier."""
    allowed = OPERATOR_SETS.get(tier, [])
    found = []
    for _start, _end, matcher in find_assertions(assertion_text):
        op = MATCHER_OPERATOR[matcher]
        if op in allowed and op not in found:
            found.append(op)
    return found


def generate_mutants_for_file(file_path: str, tier: str = "B2") -> list:
    """Generate mutants for all assertions in a test file.

    NO-OP guard: a mutant identical to the original (e.g. COLLECTION_EMPTY on
    an already-empty `toHaveLength(0)`) is a seeder defect — refused pre-seed,
    never emitted. Mirrors the verdictgate NOOP input rule (exit 2 downstream).
    """
    content = Path(file_path).read_text(encoding="utf-8")
    mutants = []
    for start, end, matcher in find_assertions(content):
        original = content[start:end]
        for op in get_applicable_operators(original, tier):
            mutated = apply_mutation(original, op)
            if mutated == original:
                continue  # no-op mutant — seeder defect, refuse pre-seed
            line = content.count("\n", 0, start) + 1
            mutants.append(
                {
                    "operator": op,
                    "original": original,
                    "mutated": mutated,
                    "file": file_path,
                    "line": line,
                    "tier": tier,
                    "rmt_version": RMT_VERSION,
                }
            )
    return mutants


def get_line_number(content: str, substring: str) -> int:
    """Get line number of substring in content (utility for external callers)."""
    return content.count("\n", 0, content.find(substring)) + 1


def run_rmt(args) -> int:
    """Run RMT-lite mutation generation over a test file or directory.

    Takes an argparse namespace with `input`, `tier`, `format`, and optional
    `exclude`. Shared by standalone `rmt.py` and `verdictgate rmt` (single
    implementation — the verdictgate.py copy was removed in the split).
    Uses `line`/`tier` as returned by `generate_mutants_for_file` (no recompute).
    """
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: input path does not exist: {args.input}", file=sys.stderr)
        return 2
    tier = args.tier
    if input_path.is_file():
        files = [input_path]
    elif input_path.is_dir():
        exclude = getattr(args, "exclude", "node_modules")
        exclude_dirs = set(exclude.split(",")) if exclude else {"node_modules"}
        files = []
        for ext in ("*.test.ts", "*.test.js", "*.spec.ts", "*.spec.js"):
            for f in input_path.rglob(ext):
                if not any(excl in f.parts for excl in exclude_dirs):
                    files.append(f)
        if not files:
            print("No test files found", file=sys.stderr)
            return 1
    else:
        print(f"Error: input path is not a file or directory: {args.input}", file=sys.stderr)
        return 1
    all_mutants = []
    for file_path in files:
        try:
            all_mutants.extend(generate_mutants_for_file(str(file_path), tier))
        except Exception as e:
            print(f"Error processing {file_path}: {e}", file=sys.stderr)
    if args.format == "json":
        print(json.dumps(all_mutants, indent=2, ensure_ascii=False))
    elif args.format == "csv":
        writer = csv.writer(sys.stdout)
        writer.writerow(["file", "operator", "original", "mutated"])
        for mu in all_mutants:
            writer.writerow([mu["file"], mu["operator"], mu["original"], mu["mutated"]])
    else:
        print(f"{len(all_mutants)} mutants @ {tier} from {len(files)} file(s)")
        for mu in all_mutants:
            print(f"- L{mu['line']} [{mu['operator']}]")
            print(f"    - {mu['original']}")
            print(f"    + {mu['mutated']}")
    print(f"\nTotal: {len(all_mutants)} mutants @ {tier} from {len(files)} file(s)", file=sys.stderr)
    return 0


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(prog="rmt")
    ap.add_argument("input", help="test file to mutate")
    ap.add_argument("--tier", default="B2", choices=["B0", "B1", "B2", "B3"],
                    help="risk tier for mutation depth (B3 yields no mutants by design: trend-only tier)")
    ap.add_argument("--format", default="summary", choices=["summary", "json", "csv"])
    args = ap.parse_args(argv)
    return run_rmt(args)


if __name__ == "__main__":
    sys.exit(main())
