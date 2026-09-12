---
schema: qual/card@1
id: E-TPZHJ
kind: problem
title: $\sum(-1)^{i}\dim V_{i}=0$ for a finite exact sequence of vector spaces
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Vector Spaces
  - Rank and Nullity
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
1. For a division ring $D$, let $V_{i}$ be a finite dimensional vector space over $D$ for $i \in\{1, \ldots, k\}$.
   Suppose the sequence
\[
0 \longrightarrow V_{1} \longrightarrow V_{2} \longrightarrow \cdots V_{k} \longrightarrow 0
\]
is exact.
Prove that $\sum_{i=1}^{k}(-1)^{i} \operatorname{dim}_{D} V_{i}=0$.
:::

::: {.solution}
Let
\[
d_i:V_i\longrightarrow V_{i+1}
\]
be the maps in the exact sequence, with $V_0=V_{k+1}=0$ and the evident zero maps at the ends.

<1>1. For every $1\le i\le k$,
\[
\dim_D V_i=\dim_D\ker d_i+\dim_D\operatorname{im}d_i.
\]
::: {.proof}
This is rank-nullity over the division ring $D$. Equivalently, choose a basis of $\ker d_i$, extend it to a basis of $V_i$, and observe that the images of the added basis vectors form a basis of $\operatorname{im}d_i$.
:::

<1>2. Exactness gives
\[
\ker d_i=\operatorname{im}d_{i-1}
\qquad(1\le i\le k).
\]
::: {.proof}
This is exactly the definition of exactness at $V_i$.
:::

<1>3. Hence
\[
\dim_D V_i
=\dim_D\operatorname{im}d_{i-1}
 +\dim_D\operatorname{im}d_i.
\]
::: {.proof}
Substitute <1>2 into <1>1.
:::

<1>4. The alternating sum telescopes to zero:
\[
\sum_{i=1}^k(-1)^i\dim_DV_i=0.
\]
::: {.proof}
Using <1>3,
\[
\begin{aligned}
\sum_{i=1}^k(-1)^i\dim_DV_i
&=\sum_{i=1}^k(-1)^i\dim_D\operatorname{im}d_{i-1}
 +\sum_{i=1}^k(-1)^i\dim_D\operatorname{im}d_i\\
&=-\sum_{j=0}^{k-1}(-1)^j\dim_D\operatorname{im}d_j
 +\sum_{j=1}^{k}(-1)^j\dim_D\operatorname{im}d_j.
\end{aligned}
\]
All interior terms cancel. The remaining boundary terms vanish because
\[
\operatorname{im}d_0=0,
\qquad
\operatorname{im}d_k=0.
\]
Therefore the sum is zero.
:::
:::
