---
schema: qual/card@1
id: E-LVTFA
kind: problem
title: Homotopy equivalence is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Homotopy Equivalence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 58 Exercise 3, printed p. 366,
    with the definition of homotopy equivalence. Reflexivity, symmetry and transitivity, the last two by composing with the given homotopies; the card's composites $(gv)(uf)$ and $(uf)(gv)$ are the right ones. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Show that given a collection $\mathcal{C}$ of spaces, the relation of homotopy equivalence is an equivalence relation on $\mathcal{C}$.
:::

::: {.solution}
Reflexivity: every space $X$ is homotopy equivalent to itself via $\operatorname{id}_X$.

Symmetry: if $f:X\to Y$ and $g:Y\to X$ satisfy
$$
gf\simeq\operatorname{id}_X,\qquad fg\simeq\operatorname{id}_Y,
$$
then the same equations show that $g$ is a homotopy equivalence from $Y$ to $X$ with homotopy inverse $f$.

Transitivity: suppose $X\simeq Y$ via $f:X\to Y$, $g:Y\to X$, and $Y\simeq Z$ via $u:Y\to Z$, $v:Z\to Y$. Then $u f:X\to Z$ and $g v:Z\to X$ satisfy
$$
(gv)(uf)=g(vu)f\simeq g\,\operatorname{id}_Y f=gf\simeq\operatorname{id}_X,
$$
and similarly
$$
(uf)(gv)=u(fg)v\simeq u\,\operatorname{id}_Yv=uv\simeq\operatorname{id}_Z.
$$
Thus $X\simeq Z$. Hence homotopy equivalence is an equivalence relation.
:::
