# Fresh-clone source replay

Target revision: `510f68f84d41594949b88cf7e280a49821856a8c` Candidate ledger rows: 2285

Source revisions:

- `qual-wiki` `main` `e6686855d9db6dbe815432c3cb8b0597b7cc4fb6` via `git@github.com:dzackgarza/qual-wiki.git`

- `qual-review-and-solutions` `master` `590a8929b2326cc770a246e934ab36fb30b0c7ab` via `git@github.com:dzackgarza/qual-review-and-solutions.git`

- `make-me-a-qual` `master` `beba581e5b32f54ff469ed603a0885d51591e5fc` via `git@github.com:dzackgarza/make-me-a-qual.git`

- `Analysis-Qual-Compendium` `master` `15168d8df736c3bc99be57e8b48e0675e0cd4e2f` via `git@github.com:dzackgarza/Analysis-Qual-Compendium.git`

- `math-flashcards` `master` `69cecc401981fb2f897a6a3c29feb869d811013c` via `git@github.com:dzackgarza/math-flashcards.git`

The command cloned each source over SSH into a new temporary root, checked out the recorded commit, and verified a clean worktree.
It compared every tracked path with the committed ledger, then verified migrated targets and source hashes.
It also verified generated-source reasons, queued owners, dropped-source reasons, and the recorded G7 residual.

This proves source preservation and build-integrity inputs.
It does not prove that the mathematical wiki is complete.
