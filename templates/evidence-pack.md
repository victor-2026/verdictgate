# Evidence Pack — what to attach to your PR / release record

1. **results.csv** — the recorded input, raw and unedited
2. **<stem>.verdict.md + <stem>.verdict.json** — the calculator output, scorer version stamped
3. **Raw run logs / screenshots** for every seeded mutant — lineage, not belief
4. **Sign-off table filled** (in the verdict md): Reviewer of record, Independent Assessor (signed comment wherever a signal fired), Engineering owner
5. **Reproducibility note**: anyone with the same results.csv and the same scorer version gets the same verdict, byte-identical

When disputing a vendor's green report: the verdict is reproducible by a third
party from the same CSV — that is the point of the evidence pack.
