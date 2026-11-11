---
schema: qual/card@1
id: E-CFNT7
kind: problem
title: Countable unions in Baire spaces
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: "Solutions to exercises for Mathematics 205A" (University
    of California, Riverside, Fall 2014), Part 3, section "III.3: Implications of completeness", answer to
    Munkres §48 Exercise 1 (printed p. 298) on the set's own printed p. 6 (in tmp/sources/munkres-solutions-ucr-math205-gentop.pdf,
    PDF p. 47; the file names no author, so the course and the file are the attribution). Checked against
    Munkres, Topology (2000), §48 Exercise 1, printed p. 298, with the definition of a Baire space and of a
    nowhere dense set in §48: the answer is the set's one sentence, that if the interior of the closure of each
    B_n were empty then each B_n would be nowhere dense and X would be of the first category. The card writes
    the same argument, adding the observation that the union of the closures is X because the B_n cover X, and
    the nonemptiness of X is what makes the open set X itself the witness required by the definition. Nothing
    needed correction.
---

::: {.exercise}

Let $X$ equal the countable union $\bigcup B_n$.
Show that if $X$ is a nonempty Baire space, at least one of the sets $\overline{B}_n$ has a nonempty interior.
:::

::: {.solution}
If every $\overline{B_n}$ had empty interior, then the closed sets $\overline{B_n}$ would all be nowhere dense. But
$$
X=\bigcup_nB_n\subset\bigcup_n\overline{B_n}=X,
$$
so $X$ would be a countable union of nowhere dense sets. This contradicts the Baire property for the nonempty open set $X$ itself. Hence some $\overline{B_n}$ has nonempty interior.
:::
