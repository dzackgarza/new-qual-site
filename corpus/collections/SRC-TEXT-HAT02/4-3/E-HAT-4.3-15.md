---
schema: qual/card@1
id: E-HAT-4.3-15
kind: problem
title: "Homotopy equivalence fibration is fiber homotopy trivial"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

---

::: {.problem}
If the fibration $p: E \to B$ is a homotopy equivalence, show that $p$ is a fiber homotopy equivalence of $E$ with the trivial fibration $\id: B \to B$.
:::

::: {.solution}
The fibration $p:E\to B$ and the identity fibration
$$
1_B:B\to B
$$
represent the same element of $\mathcal M(B)$: the map
$$
p:E\to B
$$
is itself a homotopy equivalence and satisfies
$$
p=1_B\circ p.
$$
By the bijection of Exercise 14, equal classes in $\mathcal M(B)$ correspond to the same class in $\mathcal F(B)$. Thus
$$
\boxed{p:E\to B\text{ is fiber homotopy equivalent to }1_B:B\to B.}
$$
:::
