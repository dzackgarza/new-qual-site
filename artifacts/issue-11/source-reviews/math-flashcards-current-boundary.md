# Direct review of the current math-flashcards boundary

## Boundary

The tracked source baseline is commit `69cecc401981fb2f897a6a3c29feb869d811013c` with 153 tracked paths.
The source worktree also contains 82 known APKG artifacts listed in `sources/math-flashcards-untracked-artifacts.json`.

The worktree has one modified tracked artifact, `apkg/Vocabulary.apkg`, and 81 untracked APKG artifacts.
The manifest records all 82 current source paths, their current SHA-1 values, and their permanent target paths.

## Direct review

I read the manifest and compared each current source artifact with its named target.
All 82 source and target SHA-1 values match.

The modified `Vocabulary.apkg` is included in the boundary.
Its current source and target SHA-1 is `ee631dbe82a77e6d9230087612264e42d3b51000`. Its pinned baseline SHA-1 was `8cc389dcce372cad962b2e508431a3f4b291b7d9`. The target retains both the pinned generated package and the current worktree package under separate paths.

The 153 tracked paths have exact ledger coverage.
The five dropped paths are repository tooling or editor configuration and are directly reviewed in `dropped-content-review.md`.

## Result

The current dirty source state is explicitly bounded by the 82-entry manifest.
No current APKG artifact is outside the target copy set, and no target hash differs from its current source hash.
