# Queue 12: Repair what limits authoring throughput

Source: observed fleet measurement, 2026-09-10 → 2026-09-11. Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) surface.

These are not corpus defects. They are defects in the surfaces that tell a stream what is
left to do, and each one costs authoring time directly. Take them before taking cards from
Queue C: a stream that fixes 12.1 stops several streams from re-solving solved cards.

## Open items

- [ ] 12.1 `queues/C-unsolved-cards.md` reports solved cards as unsolved — 729 of 829.

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

## Why these are ahead of Queue C

Measured 2026-09-10 05:35 → 2026-09-11 05:36, from the generated queue at each end:
remaining problem cards fell 3,588 → 829. That rate finishes the problem corpus within a
day or two. The binding constraint on this repository is no longer how fast cards get
solved; it is that 12.1 makes roughly 88% of the remaining list false, and 12.2 leaves a
seventh of the corpus outside every measurement. Both distort what a stream picks up next.
