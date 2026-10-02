#!/usr/bin/env python3
"""locked-run: single-touch wrapper for locked-test-set bench runs.

Enforces test-lock discipline mechanically: verifies dataset SHA, refuses
repeat runs of the same tag without a logged reason, executes the wrapped
command, and appends an audit row. Command-agnostic: inference code stays in
the caller's runner; this wrapper owns ONLY access control + lineage.

Usage:
    python3 locked-run.py --data locked.json --data-sha <hex> --tag <arm>
        --model-id <string> --out <ledger.jsonl> --reason "<why>" -- <command...>

Rules (mirror frozen-spec test-lock):
- Data SHA mismatch -> refuse (fail fast, no run).
- Tag already in ledger + no --reason -> refuse (one touch by default).
- Tag already in ledger + --reason -> run, reason logged (auditable override
  for crashed runs; never silent).
- Every execution appends: tag, timestamp (UTC), data-sha, model-id, command
  fingerprint (argv hash), exit code, reason.
- Ledger itself is append-only; the wrapper never edits past rows.

Python stdlib only. Exit codes: 0 = wrapped command exit 0; otherwise the
wrapped command's exit code; 2 = wrapper refusal/error (pre-run).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_ledger(path: Path) -> list:
    if not path.exists():
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser(prog="locked-run")
    ap.add_argument("--data", required=True, help="locked dataset file")
    ap.add_argument("--data-sha", required=True, help="expected SHA-256 of data file")
    ap.add_argument("--tag", required=True, help="arm tag (e.g. base, tuned)")
    ap.add_argument("--model-id", required=True, help="model identifier + revision (recorded, see below)")
    ap.add_argument("--out", required=True, help="ledger JSONL path (appended)")
    ap.add_argument("--reason", default="", help="required for reruns of an already-run tag")
    ap.add_argument("command", nargs=argparse.REMAINDER, help="wrapped command after --")
    args = ap.parse_args(argv)

    if not args.command or args.command[0] == "--":
        cmd = [c for c in args.command if c != "--"]
    else:
        cmd = args.command
    if not cmd:
        print("locked-run: no wrapped command given (usage: ... -- <command...>)", file=sys.stderr)
        return 2

    data_path = Path(args.data)
    if not data_path.is_file():
        print(f"locked-run: data file missing: {args.data}", file=sys.stderr)
        return 2
    actual_sha = sha256_file(data_path)
    if actual_sha != args.data_sha:
        print(f"locked-run: REFUSED — data SHA mismatch: expected {args.data_sha}, got {actual_sha}", file=sys.stderr)
        return 2

    ledger_path = Path(args.out)
    prior = [r for r in load_ledger(ledger_path) if r.get("tag") == args.tag]
    if prior and not args.reason:
        print(
            f"locked-run: REFUSED — tag '{args.tag}' already ran {len(prior)}× "
            f"(ledger {ledger_path}); re-run requires --reason (logged).",
            file=sys.stderr,
        )
        return 2

    cmd_fp = hashlib.sha256(" ".join(cmd).encode()).hexdigest()[:16]
    proc = subprocess.run(cmd)
    row = {
        "tag": args.tag,
        "ts": datetime.now(timezone.utc).isoformat(),
        "data": str(data_path),
        "data_sha": actual_sha,
        "model_id": args.model_id,
        "command_fp": cmd_fp,
        "exit": proc.returncode,
        "reason": args.reason or ("first-run" if not prior else "rerun"),
    }
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    with open(ledger_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
