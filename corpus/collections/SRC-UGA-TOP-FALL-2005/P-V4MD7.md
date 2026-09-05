---
schema: qual/card@1
id: P-V4MD7
kind: problem
title: $H_0$ and $H_1$ of the complete graph $K_5$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Cell Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 5 of the official UGA Fall 2005 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the pseudo-Lamport presentation by a cellular-chain computation of both requested groups.
---

::: problem
Compute the integer homology groups $H_0(K_5; \mathbb{Z})$ and $H_1(K_5; \mathbb{Z})$ of the **complete graph** $K_5$ on 5 vertices.
:::

::: {.solution}
<1>1. Give $K_5$ its natural one-dimensional CW structure.
::: {.proof}
There are five vertices and one edge for each unordered pair of distinct vertices, hence
\[
\#E=\binom52=10.
\]
Thus its cellular chain complex is
\[
0\longrightarrow \ZZ^{10}\xrightarrow{\partial_1}\ZZ^5\longrightarrow0.
\]
Orient every edge arbitrarily.
For an oriented edge from vertex $v_i$ to vertex $v_j$,
\[
\partial_1(e_{ij})=v_j-v_i.
\]
:::

<1>2. The image of $\partial_1$ is the subgroup
\[
A=\left\{(n_1,\ldots,n_5)\in\ZZ^5:\sum_{i=1}^5n_i=0\right\}.
\]
::: {.proof}
Every boundary $v_j-v_i$ has coordinate sum zero, so $\operatorname{im}\partial_1\subseteq A$.
Conversely, fix $v_1$.
Because $K_5$ contains the edge from $v_1$ to every $v_i$, the image contains
\[
v_i-v_1\qquad(2\le i\le5).
\]
These four elements generate $A$: if $\sum_i n_i=0$, then
\[
\sum_{i=1}^5n_iv_i=\sum_{i=2}^5 n_i(v_i-v_1).
\]
Hence $\operatorname{im}\partial_1=A\cong\ZZ^4$.
:::

<1>3. One has
\[
H_0(K_5;\ZZ)\cong\ZZ.
\]
::: {.proof}
Cellular homology gives
\[
H_0(K_5;\ZZ)=\ZZ^5/A.
\]
The coordinate-sum homomorphism
\[
\ZZ^5\longrightarrow\ZZ,
\qquad
(n_1,\ldots,n_5)\longmapsto\sum_i n_i,
\]
is surjective and has kernel $A$.
The first isomorphism theorem therefore gives $\ZZ^5/A\cong\ZZ$.
:::

<1>4. One has
\[
H_1(K_5;\ZZ)\cong\ZZ^6.
\]
::: {.proof}
There are no $2$-cells, so
\[
H_1(K_5;\ZZ)=\ker\partial_1.
\]
The exact sequence
\[
0\longrightarrow\ker\partial_1
\longrightarrow\ZZ^{10}
\xrightarrow{\partial_1}A
\longrightarrow0
\]
has free abelian target $A\cong\ZZ^4$, so it splits.
Therefore
\[
\ZZ^{10}\cong\ker\partial_1\oplus\ZZ^4.
\]
Moreover, $\ker\partial_1$ is a subgroup of the free abelian group $\ZZ^{10}$ and is therefore free abelian.
Ranks add in the displayed decomposition, so its rank is $10-4=6$.
Hence
\[
H_1(K_5;\ZZ)\cong\ZZ^6.
\]
:::
:::
