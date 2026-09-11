# Queue 12: Repair what limits authoring throughput

Source: observed fleet measurement, 2026-09-10 → 2026-09-11. Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) surface.

These are not corpus defects. They are defects in the surfaces that tell a stream what is
left to do, and each one costs authoring time directly. Take them before taking cards from
Queue C: a stream that fixes 12.1 stops several streams from re-solving solved cards.

## Open items

- [x] 12.1 `queues/C-unsolved-cards.md` reports solved cards as unsolved — 729 of 829.

  **Closed 2026-09-11: the discrepancy is gone, and not by the route this item predicted.**
  A regenerated queue now reports `0 problem cards have no solution section`, and an
  independent recount over the corpus agrees exactly — 7,375 `kind: problem` cards, none
  without a solution fence. The 729 were real at the time of writing and are all solved
  now; the streams finished the corpus while this sat open. No parser defect was
  demonstrated and none should be assumed: the hypothesis below was never tested against a
  green queue, so it is retained as a record of what was observed, not as a finding.

  Two things this leaves genuinely open, both moved into 12.2 and 12.3 rather than kept
  here. If the generator *had* been wrong, the same fault would now read as "corpus
  complete" and nobody would notice — an always-zero queue and a correct-zero queue are
  indistinguishable without a second measurement. And a queue that can only be trusted
  when it is non-empty is worth one independent recount at the moment it first hits zero,
  which is now.

  The queue is the only list that tells a stream which cards need work, and it is wrong by
  about a factor of eight. Regenerate it and read it against the corpus:

  ```
  just unsolved
  ```

  It emits `829 problem cards have no solution section`. Of those 829 ids, **729 contain a
  solution fence in their own file**. The first four in the file are a fair sample — all in
  `corpus/collections/SRC-TEXT-HK71/10-1/`:

  | Card | Solution fence | Audit trail |
  | --- | --- | --- |
  | `E-HK-101-11` | `::: solution` at line 34 | `solution-written` and `solution-reviewed`, 2026-09-11 |
  | `E-HK-101-12` | `::: solution` at line 39 | same |
  | `E-HK-101-14` | `::: solution` at line 41 | same |
  | `E-HK-101-2` | `::: solution` at line 48 | same |

  These carry complete authored proofs. A stream drawing from Queue C will write a second
  solution for a card that already has one, and will keep doing it: the card does not leave
  the list when the solution lands.

  Fence spelling is **not** the discriminator, so do not fix this by normalising fences:

  - 2,196 cards the queue counts as *solved* use the same bare `::: solution` form.
  - 82 cards the queue counts as *unsolved* use the attribute form `::: {.solution}`.
  - 280 of the 729 nest a same-depth `::: proof` inside the solution; so do 679 cards the
    queue counts as solved.

  The corpus itself validates — `just check` reports `9125 cards and 260 wiki pages OK` —
  so this is not the YAML-parse class from 1.R1. The split is between what the fence text
  says and what `qualc`'s section parse yields for `ParsedCard.sections`; `tools/unsolved_queue.py`
  asks only `any(kind == "solution" for kind, _text in item.sections)`.

  Root-cause which side is wrong before changing either. If the parser is dropping real
  solution sections, the same sections are likely missing from the rendered site, which
  makes this a reader-facing defect and not only a queue defect — check one of the four
  cards above on the built page before closing.

  Acceptance: every card whose file carries an authored solution is absent from a freshly
  generated `queues/C-unsolved-cards.md`, and the count is a true remaining-work figure.
  If some of the 729 turn out to be genuinely unsolved under a correct reading, say how
  many and why, rather than adjusting the count.

- [ ] 12.2 Decide what measures the non-problem cards, or record that nothing does.

  Queue C covers `kind: problem` and nothing else, by construction. The corpus holds 1,364
  cards of other kinds — 548 definition, 298 proposition, 295 theorem, 144 fact, 28
  corollary, 22 example, 16 lemma, 6 strategy — and **1,342 of them carry no solution,
  proof or answer section**. No queue counts them and no generator regenerates a list of
  them, so the repository currently has no measure of whether that part of the corpus is
  finished.

  This is a scope question, not a defect report, and `AGENTS.md` already answers half of
  it: a statement card that resolves to an external oracle is correct with no local proof,
  and card kind is explicitly not a heuristic for judging that. So the work here is to
  decide the criterion and make it measurable — not to write 1,342 proofs.

  Acceptance: either a generated queue with a stated criterion for which non-problem cards
  are incomplete, or a recorded decision in this queue that statement cards have no
  completion obligation, with the reasoning. Either outcome ends the ambiguity; the
  present state is that nobody can say how much of the corpus is left.

- [ ] 12.3 Queue C has reached zero; confirm that is completion and not a broken measurement.

  This queue is the repository's only statement of how much authoring remains, and it has
  just gone empty. An always-zero generator and a genuinely finished corpus are
  indistinguishable from the queue alone, so the reading needs one independent check that
  does not share the generator's code path. A recount on 2026-09-11 over `corpus/**` — card
  `kind: problem`, presence of a `:::`-fenced solution — returned 7,375 problem cards and
  zero without a solution, matching the generator exactly. That is the confirmation; this
  item exists so the check is recorded rather than assumed, and so the same comparison is
  repeated the next time the count moves sharply.

  Acceptance: the zero is corroborated by a measurement independent of
  `tools/unsolved_queue.py`, and the result recorded here. If the two ever disagree, the
  disagreement is the finding and Queue C stops being authoritative until it is explained.

- [ ] 12.4 `_unsolved-if-staged` makes a pathspec commit impossible while any corpus file is staged.

  Every stream shares this checkout and therefore shares one index, so `AGENTS.md`'s
  own rule is to commit by explicit pathspec and never carry another stream's staged work.
  That rule and this hook are incompatible.

  `just _unsolved-if-staged` runs `git add queues/C-unsolved-cards.md` inside `pre-commit`.
  During `git commit -- <pathspec>` git holds the index lock for the duration of the hooks,
  so that `git add` cannot acquire it and the recipe exits 128, failing the gate. The branch
  is selected by `git diff --cached --quiet -- corpus`, which reads the *shared* index — so
  the trigger is any corpus file staged by anyone, not by the committer.

  Reproduced 2026-09-11 with no other stream active: a pathspec commit touching only
  `queues/` failed repeatedly with `Recipe _unsolved-if-staged failed with exit code 128`
  while another stream's `corpus/collections/SRC-WESLEYAN-RA-SUMMER-2008/index.md` sat
  staged. The same pathspec commit had succeeded earlier the same day when nothing under
  `corpus` was staged, taking the `no staged corpus change` branch instead. Running
  `just _unsolved-if-staged` outside a commit succeeds, which is why this does not show up
  in isolation.

  The effect is that a stream is locked out of committing anything at all whenever a
  sibling has corpus work staged, which on a shared checkout is most of the time.

  Acceptance: a pathspec-scoped commit succeeds while unrelated corpus files are staged by
  another stream, and the regenerated queue still lands in the commit that changed the
  corpus. Regenerating outside the index — or staging the queue in `post-commit` rather than
  `pre-commit` — would both satisfy this; do not solve it by dropping the pathspec rule,
  which exists to stop streams committing each other's work.

## Why these are ahead of Queue C

Measured 2026-09-10 05:35 → 2026-09-11 05:36, from the generated queue at each end:
remaining problem cards fell 3,588 → 829. That rate finishes the problem corpus within a
day or two. The binding constraint on this repository is no longer how fast cards get
solved; it is that 12.1 makes roughly 88% of the remaining list false, and 12.2 leaves a
seventh of the corpus outside every measurement. Both distort what a stream picks up next.
