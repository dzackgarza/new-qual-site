---
schema: qual/card@1
id: E-HAT-4.2-37
kind: problem
title: "Whitehead products vanish in H-spaces"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 37; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that all Whitehead products in a path-connected H-space are trivial.
:::

::: {.solution}
A Whitehead product
$$
[f,g]\in\pi_{p+q-1}(X)
$$
measures the obstruction to extending
$$
f\vee g:S^p\vee S^q\to X
$$
over $S^p\times S^q$, whose top cell is attached by $[\iota_p,\iota_q]$.

If $X$ is an H-space with multiplication $\mu:X\times X\to X$, define
$$
F:S^p\times S^q\to X,
\qquad
F(x,y)=\mu(f(x),g(y)).
$$
On the two coordinate axes this restricts, up to the unit homotopies of the H-space, to $f$ and $g$. Using the homotopy extension property, adjust $F$ near the wedge so that its restriction is exactly $f\vee g$. Thus $f\vee g$ extends over the product, so the obstruction vanishes:
$$
\boxed{[f,g]=0.}
$$
Since $f$ and $g$ were arbitrary, every Whitehead product in a path-connected H-space is trivial.
:::
