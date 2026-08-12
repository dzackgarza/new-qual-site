# Migration proof audit

## Result

The plan's completion proof is not established.

The current review records are aggregate assertions.
They do not provide the required direct evidence for every source item.

## Evidence boundary

This audit checked target commit `973d41c4`, the pinned source revisions named by the review records, the complete `sources/migration-ledger.jsonl`, the known untracked-artifact manifest, and the seven source-review records.

The ledger contains 2,335 rows:

- 1,826 `migrated`

- 142 `generated`

- 367 `dropped`

- 0 `queued`

The source-path sets match the 1,521, 542, 116, 3, and 153 tracked paths in the five pinned source trees.
The ledger has no duplicate `(repo, path)` keys.

These inventory counts do not prove migration.
The plan states that the ledger records work but does not prove that the work occurred.

## Findings

1. All 367 `dropped` rows have no `evidence` field.
   The plan's M2 acceptance requires a direct inspection note for every dropped item and forbids a generic reason, file extension, or directory name as the justification.

   The dropped reasons include 182 `editor config` rows, 139 `non-content file (no ext)` rows, and five `.bib` rows.
   The five pinned `.bib` files are empty, but the ledger does not record that direct inspection.
   Bibliographic content is explicitly in the plan scope.

2. The source-review records summarize batches.
   They do not name a direct inspection record for each dropped row.
   Therefore the records do not satisfy the plan's per-item M2 evidence contract, even where the stated disposition may be correct.

3. The `math-flashcards` source tree is not at its pinned worktree state.
   It has one modified tracked file and 81 untracked files.
   The manifest lists 82 artifacts, including `apkg/Vocabulary.apkg` as `modified-worktree`.

   The pinned `Vocabulary.apkg` SHA-1 is `8cc389dcce372cad962b2e508431a3f4b291b7d9`. The current worktree and its untracked target copy are `ee631dbe82a77e6d9230087612264e42d3b51000`. The review record is pinned to the former revision, so the current source boundary is not frozen by that review.

4. The cross-repository review is recorded at target commit `d5509f0a`, not the current target commit `973d41c4`. It relies on the source-review records that have the gaps above.

5. The MathQualBot review correctly limits its result to the 51 vendored images.
   It explicitly states that completeness of the unavailable original repository is unprovable.
   That is not proof for any wider MathQualBot source boundary.

## Consequence

The numeric ledger, replay, source-review PASS labels, and cross-review PASS label are supporting records only.
They do not prove the plan's “all content migrated” requirement.

M2 through M6 must remain open until the missing direct evidence is supplied and the source boundary is frozen.
Archive work remains blocked.
No migration verifier or migration automation was added by this audit.
