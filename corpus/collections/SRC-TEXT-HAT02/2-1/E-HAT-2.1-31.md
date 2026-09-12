---
schema: qual/card@1
id: E-HAT-2.1-31
kind: problem
title: Five-lemma example with zero outer maps and nonzero middle map
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
  - Five Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 31, including the source diagram on p. 133.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified by direct diagram algebra/exactness.
---

Using the notation of the five-lemma, give an example where the maps $\alpha, \beta, \delta$, and $\varepsilon$ are zero but $\gamma$ is nonzero.
This can be done with short exact sequences in which all the groups are either $\mathbb{Z}$ or $0$.

::: {.solution}
Use the five-lemma notation
\[
\begin{array}{ccccccccc}
A&\longrightarrow&B&\longrightarrow&C&\longrightarrow&D&\longrightarrow&E\\
\downarrow\alpha&&\downarrow\beta&&\downarrow\gamma&&\downarrow\delta&&\downarrow\varepsilon\\
A'&\longrightarrow&B'&\longrightarrow&C'&\longrightarrow&D'&\longrightarrow&E'.
\end{array}
\]
Take the upper exact sequence to be
\[
0\longrightarrow0\longrightarrow\mathbb Z
\xrightarrow{\operatorname{id}}\mathbb Z\longrightarrow0
\]
and the lower exact sequence to be
\[
0\longrightarrow\mathbb Z
\xrightarrow{\operatorname{id}}\mathbb Z
\longrightarrow0\longrightarrow0.
\]
Thus
\[
(A,B,C,D,E)=(0,0,\mathbb Z,\mathbb Z,0)
\]
and
\[
(A',B',C',D',E')=(0,\mathbb Z,\mathbb Z,0,0).
\]
Define
\[
\alpha=0,
\qquad
\beta=0,
\qquad
\gamma=\operatorname{id}_{\mathbb Z},
\qquad
\delta=0,
\qquad
\varepsilon=0.
\]

<1>1. Both rows are exact.
::: {.proof}
In the upper row, exactness is immediate at the zero groups, while at the two copies of $\mathbb Z$ it follows because the middle map is the identity. In the lower row the same argument applies to the identity map $\mathbb Z\to\mathbb Z$.
:::

<1>2. The diagram commutes.
::: {.proof}
Every square involving one of $\alpha,\beta,\delta,\varepsilon$ has both composites equal to zero. For the square containing $\gamma$, the upper map into $C$ is the zero map $0\to\mathbb Z$, so both composites there are zero; for the square leaving $C$, the lower map $C'\to D'$ is zero, so both composites are again zero.
:::

<1>3. The four outer vertical maps are zero but the middle map is nonzero.
::: {.proof}
By construction
\[
\alpha=\beta=\delta=\varepsilon=0,
\]
whereas
\[
\gamma=\operatorname{id}_{\mathbb Z}\ne0.
\]
:::

This gives the requested example using only the groups $\mathbb Z$ and $0$.
:::
