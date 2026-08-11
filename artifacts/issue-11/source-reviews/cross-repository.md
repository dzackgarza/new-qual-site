# Cross-repository direct evidence record

This record reports the assembled evidence. It is not the independent
cross-repository review required by the plan.

The boundary is five pinned source revisions with 2,285 tracked paths, 82
observed untracked APKG artifacts, and 51 vendored MathQualBot images. The
ledger has 2,285 rows: 1,773 migrated, 142 generated, 370 dropped, and 0
queued. Generated artifacts have permanent verbatim targets under
`assets/ws9/`; the 82 APKG files and 51 images have separate manifests and
native copies.

The QRS authored review document has 949 routed statement records and four
retained source blocks. The block line ranges and SHA-1 values are recorded in
`sources/unrouted-source-blocks.jsonl`; the complete native source is retained
under `assets/ws9/qual-review-and-solutions/native/`.

The plan explicitly forbids new migration automation, replay tools, checkers,
and scripts. The earlier verifier and its generated report were therefore
removed. A ledger, replay, or build result cannot prove complete migration.

An independent reviewer must now inspect the five full inventories, the
untracked and vendored manifests, all target mappings, and the retained QRS
blocks. Until that review is recorded, the plan's all-content and archive gates
remain open.
