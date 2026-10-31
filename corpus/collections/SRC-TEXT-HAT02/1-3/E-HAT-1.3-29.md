---
schema: qual/card@1
id: E-HAT-1.3-29
kind: problem
title: Orbit spaces are homeomorphic iff the groups are conjugate
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The book states 'iff'; the stored statement had 'if'.
- event: solution-reviewed
  by: claude-opus-5.5
  date: 2026-10-31
  note: 'Added the converse: a homeomorphism of orbit spaces lifts to a homeomorphism of Y that conjugates G_1 onto G_2.'
---

::: {.problem}
Let $Y$ be path-connected, locally path-connected, and simply-connected, and let $G_1$ and $G_2$ be subgroups of $\mathrm{Homeo}(Y)$ defining covering space actions on $Y$.
Show that the orbit spaces $Y/G_1$ and $Y/G_2$ are homeomorphic iff $G_1$ and $G_2$ are conjugate subgroups of $\mathrm{Homeo}(Y)$.
:::

::: {.solution}
Suppose
$$
G_2=hG_1h^{-1}
$$
for some homeomorphism
$$
h:Y\to Y.
$$
Let
$$
q_i:Y\to Y/G_i
$$
be the quotient maps.

::: pf

::: {.pf-step #s1}

The map $h$ sends $G_1$-orbits bijectively to $G_2$-orbits.

::: pf-proof

For $y\in Y$,
$$
h(G_1y)=\{hg(y):g\in G_1\}
=\{(hgh^{-1})h(y):g\in G_1\}
=G_2h(y).
$$
Thus points in the same $G_1$-orbit have images in the same $G_2$-orbit, and applying $h^{-1}$ gives the converse.

:::

:::

::: pf-step

Hence the formula
$$
\bar h([y]_{G_1})=[h(y)]_{G_2}
$$
defines a bijection
$$
\bar h:Y/G_1\to Y/G_2.
$$

::: pf-proof

Well-definedness and injectivity follow from step [](#s1){.pf-ref}, and surjectivity follows from surjectivity of $h$.

:::

:::

::: pf-step

The map $\bar h$ is a homeomorphism.

::: pf-proof

The relation
$$
\bar h\circ q_1=q_2\circ h
$$
shows that $\bar h$ is continuous because $q_1$ is a quotient map.
Applying the same argument to $h^{-1}$ gives continuity of the inverse map induced on orbit spaces.
Therefore $\bar h$ is a homeomorphism.

:::

:::

::: pf-step

Conversely, if $f:Y/G_1\to Y/G_2$ is a homeomorphism, then $G_1$ and $G_2$ are conjugate in $\mathrm{Homeo}(Y)$.

::: pf-proof

Each $q_i$ is a covering map, and since $Y$ is simply connected and locally path connected, the lifting criterion gives maps $h,k:Y\to Y$ with
$$
q_2\circ h=f\circ q_1,
\qquad
q_1\circ k=f^{-1}\circ q_2.
$$
Then $q_1\circ(k\circ h)=q_1$, so $k\circ h$ is a deck transformation of $q_1$.
Since $Y$ is path connected, Proposition 1.40 identifies the deck group of $q_1$ with $G_1$, so $k\circ h=g_1\in G_1$.
Likewise $h\circ k=g_2\in G_2$.
Hence $h$ has the left inverse $g_1^{-1}\circ k$ and the right inverse $k\circ g_2^{-1}$, so $h$ is a homeomorphism.
For $g\in G_1$,
$$
q_2\circ hgh^{-1}=f\circ q_1\circ g\circ h^{-1}=f\circ q_1\circ h^{-1}=q_2,
$$
so $hgh^{-1}$ is a deck transformation of $q_2$, that is, an element of $G_2$.
Thus $hG_1h^{-1}\subseteq G_2$.
The same argument with $f^{-1}$ and $h^{-1}$, using $q_1\circ h^{-1}=f^{-1}\circ q_2$, gives $h^{-1}G_2h\subseteq G_1$.
Hence $G_2=hG_1h^{-1}$.

:::

:::

:::

:::
