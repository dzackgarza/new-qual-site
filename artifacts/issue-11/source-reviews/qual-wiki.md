# Closeout review: qual-wiki

Review role: closeout reviewer, separate from the migration editing pass.

Source revision: `e6686855d9db6dbe815432c3cb8b0597b7cc4fb6`.

Target migration revision: `f3e39d74468ce434d1f4765c70dbb993f19a7f7e`.

Inventory boundary: `git ls-files` returned 1,471 paths. The migration ledger has
1,471 rows for this source. The ledger SHA-256 at review was
`1576c28ef2f73742f8c11936b1e12b8237ebb5d151175881d4a6540de0e6ee6f`.

Disposition counts:

- 1,280 migrated.
- 23 generated.
- 168 operational, empty, or editor files dropped.
- 0 queued.

Review checks:

- Every tracked path has one ledger row.
- Every migrated SHA-1 row has an existing target. All native identity checks pass.
- 255 derived pages were compared with their source and referenced cards.
- Five pages retained exact native copies because their derived pages dropped TODO,
  query, checklist, or tag state. Their native targets are under
  `assets/ws9/qual-wiki/native/`.
- The remaining derived pages passed the normalized source-target comparison and
  their recorded card-link lower bounds.
- The dropped Markdown and TeX scan found no source page with hidden statement
  content. Dropped rows are configuration, empty placeholders, or build files.
- All generated reasons name their migrated source or build input.

Result: pass. The source content has permanent targets. The derived wiki remains a
separate presentation projection.
