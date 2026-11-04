---
schema: qual/card@1
id: E-HAT-4.3-17
kind: problem
title: "$\\Omega X$ is an H-space"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 17; corrected the stored subject from X to ΩX.
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
Show that $\Omega X$ is an H-space with multiplication the composition of loops.
:::

::: {.solution}
The based loop space $\Omega X$ has multiplication by concatenation:
$$
(\alpha*\beta)(t)=
\begin{cases}
\alpha(2t),&0\le t\le\tfrac12,\\
\beta(2t-1),&\tfrac12\le t\le1.
\end{cases}
$$
The constant loop is a two-sided unit up to the standard reparametrization homotopies. Concatenating three loops in the two possible parenthesizations differs only by a piecewise-linear reparametrization of $I$, hence is homotopic through based loops. Thus multiplication is associative up to homotopy. Reversal of loops gives a homotopy inverse. Therefore
$$
\boxed{\Omega X\text{ is an H-space}.}
$$
:::
