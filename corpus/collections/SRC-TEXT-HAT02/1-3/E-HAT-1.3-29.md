---
schema: qual/card@1
id: E-HAT-1.3-29
kind: problem
title: "Conjugate subgroups give homeomorphic orbit spaces"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 29; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Showed that a conjugating homeomorphism descends to a homeomorphism of orbit spaces.
---

Let $Y$ be path-connected, locally path-connected, and simply-connected, and let $G_1$ and $G_2$ be subgroups of $\mathrm{Homeo}(Y)$ defining covering space actions on $Y$.
Show that the orbit spaces $Y/G_1$ and $Y/G_2$ are homeomorphic if $G_1$ and $G_2$ are conjugate subgroups of $\mathrm{Homeo}(Y)$.


::: {.solution}
Suppose
\[
G_2=hG_1h^{-1}
\]
for some homeomorphism
\[
h:Y\to Y.
\]
Let
\[
q_i:Y\to Y/G_i
\]
be the quotient maps.

<1>1. The map $h$ sends $G_1$-orbits bijectively to $G_2$-orbits.
::: {.proof}
For $y\in Y$,
\[
h(G_1y)=\{hg(y):g\in G_1\}
=\{(hgh^{-1})h(y):g\in G_1\}
=G_2h(y).
\]
Thus points in the same $G_1$-orbit have images in the same $G_2$-orbit, and applying $h^{-1}$ gives the converse.
:::

<1>2. Hence the formula
\[
\bar h([y]_{G_1})=[h(y)]_{G_2}
\]
defines a bijection
\[
\bar h:Y/G_1\to Y/G_2.
\]
::: {.proof}
Well-definedness and injectivity follow from <1>1, and surjectivity follows from surjectivity of $h$.
:::

<1>3. The map $\bar h$ is a homeomorphism.
::: {.proof}
The relation
\[
\bar h\circ q_1=q_2\circ h
\]
shows that $\bar h$ is continuous because $q_1$ is a quotient map.
Applying the same argument to $h^{-1}$ gives continuity of the inverse map induced on orbit spaces.
Therefore $\bar h$ is a homeomorphism.
:::
:::
