# Fresh-clone source replay

Target revision: `510f68f84d41594949b88cf7e280a49821856a8c` Candidate ledger rows: 2285

Source revisions:

- `qual-wiki` `main` `064e3e8815c69d763469e5384b9f85c767f9b9b6` via `git@github.com:dzackgarza/qual-wiki.git`

- `qual-review-and-solutions` `master` `590a8929b2326cc770a246e934ab36fb30b0c7ab` via `git@github.com:dzackgarza/qual-review-and-solutions.git`

- `make-me-a-qual` `master` `beba581e5b32f54ff469ed603a0885d51591e5fc` via `git@github.com:dzackgarza/make-me-a-qual.git`

- `Analysis-Qual-Compendium` `master` `15168d8df736c3bc99be57e8b48e0675e0cd4e2f` via `git@github.com:dzackgarza/Analysis-Qual-Compendium.git`

- `math-flashcards` `master` `cecb473ed7627603d95a9ed6a8e11537711905ef` via `git@github.com:dzackgarza/math-flashcards.git`

The command cloned each source over SSH into a new temporary root, checked out the recorded commit, verified a clean worktree, compared every tracked path with the committed ledger, and verified migrated targets, source hashes, generated-source reasons, queued owners, dropped-source reasons, and the recorded G7 residual.

This proves source preservation and build-integrity inputs.
It does not prove that the mathematical wiki is complete.
