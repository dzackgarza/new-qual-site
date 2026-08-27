# Queue 7: Complete source-preservation closeout

Source: `TODO.md` §5 "Complete source-preservation closeout"
Owner: [issue #11](https://github.com/dzackgarza/new-qual-site/issues/11) (COMPLETED 2026-08-26)

## Open items

- [ ] 7.1 M4: record reviewer identity, assignment, revisions, exclusions, and task separation.
  - Validity: PARTIALLY DONE. The "Independent review found one real gap" comment records the review method, scope, and the one gap found (`PSets.zip`). It does not explicitly name the reviewer's identity or record explicit task separation between migrator and reviewer beyond "someone who did not do the migrating." The content is checked; the record-keeping is incomplete.

- [x] 7.2 M5: obtain an independent criterion-to-evidence review.
  - Validity: DONE. The "Independent review found one real gap, now closed" comment describes a fresh review session "given the pinned sources and the plan but no prior completion record" that checked all five repositories (inventory, 369 dropped rows, byte identity for 1,968 target rows, six-word-shingle presence for 616 text sources, 145 `.apkg` opened, 533 PDFs through `pdftotext`, 15 side ledgers). This satisfies M5.

- [ ] 7.3 M6: reconcile the issue, handoff, and parent-plan claims.
  - Validity: NOT DONE. Issue #11 was reopened once ("prior closure did not verify this issue against the current repository and rendered artifact") then re-closed. No explicit reconciliation of issue claims vs. handoff document vs. parent-plan claims is recorded in the comments.

- [x] 7.4 Decide `retain` or `archive` for each of the five source repositories.
  - Validity: DONE. "Archive applied — M7 closed" comment: all five archived (qual-wiki `3fe1f58`, qual-review-and-solutions `590a892`, make-me-a-qual `beba581`, Analysis-Qual-Compendium `15168d8`, math-flashcards `69cecc4`).

- [x] 7.5 Add a forwarding pointer before archiving any repository.
  - Validity: DONE. "Each carries a README forwarding pointer to this repository naming the revision its content was checked at."

- [x] 7.6 Record the resulting state of each archived repository.
  - Validity: DONE. Recorded in the "Archive applied" comment with pinned revisions and archive status.

## Verification (2026-08-27)

Issue #11 closed COMPLETED 2026-08-26. The substantive review work (M5) is done. The remaining items 7.1 (M4) and 7.3 (M6) are record-keeping, not content work — the review happened but was not fully documented in the format the milestones specify.