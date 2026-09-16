---
schema: qual/card@1
id: E-PER08-8.2
kind: problem
title: Simplicial homology of $T^2$, $\mathbb{RP}^2$, and the Klein bottle
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Compute Hsimp $\\ast$ for the spaces T 2, RP 2 and K2, each thought of as a $\\Delta$-complex with two 2-simplices (and some 1- and 0-simplices).
:::

::: {.solution}
For each standard two-triangle $\Delta$-complex, write the simplicial boundary matrices and reduce them over $\mathbb Z$ to Smith normal form.
The resulting homology is
\[
\boxed{H_*(T^2):\quad H_0=\mathbb Z,\ H_1=\mathbb Z^2,\ H_2=\mathbb Z,}
\]
\[
\boxed{H_*(\mathbb{RP}^2):\quad H_0=\mathbb Z,\ H_1=\mathbb Z/2,\ H_2=0,}
\]
and
\[
\boxed{H_*(K^2):\quad H_0=\mathbb Z,\ H_1=\mathbb Z\oplus\mathbb Z/2,\ H_2=0.}
\]
All groups above degree $2$ vanish.

<1>1. Torus.
::: {.proof}
After identifying the edges of a square and subdividing it by a diagonal, the two oriented $2$-simplices have boundaries whose difference leaves one independent relation among the three $1$-cell generators.
Thus $\ker\partial_2\cong\mathbb Z$, $\operatorname{im}\partial_2$ has rank $1$, and the $1$-cycle quotient is free of rank $2$.
:::

<1>2. Projective plane.
::: {.proof}
The edge identifications give a cellular-equivalent chain complex
\[
0\to\mathbb Z\xrightarrow{\;2\;}\mathbb Z\xrightarrow{0}\mathbb Z\to0.
\]
Its homology is $H_2=0$, $H_1=\mathbb Z/2$, $H_0=\mathbb Z$.
Row reduction of the two-triangle simplicial boundary matrices gives the same Smith form.
:::

<1>3. Klein bottle.
::: {.proof}
The edge identifications similarly reduce to
\[
0\to\mathbb Z\xrightarrow{(0,\,2)}\mathbb Z^2\xrightarrow{0}\mathbb Z\to0.
\]
Hence $H_2=0$ and
\[
H_1\cong\mathbb Z^2/\langle(0,2)\rangle\cong\mathbb Z\oplus\mathbb Z/2.
\]
:::
:::
