---
schema: qual/card@1
id: P-EGKRW
kind: problem
title: The ideal $(2,x)$ in $\mathbb{Z}[x]$ is not a direct sum of nontrivial cyclic
  modules
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Ideals
  - Principal Ideal Domains
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
Let $I = (2, x)$ be an ideal in $R = \ZZ[x]$, and show that $I$ is not a direct sum of nontrivial cyclic $R\dash$modules.
:::


::: {.solution}
<1>1. The \(R\)-module \(I=(2,x)\) is torsion-free of rank \(1\).
::: {.proof}
Because \(R=\mathbb Z[x]\) is a domain and \(I\subseteq R\), the module \(I\) is torsion-free. Let \(K=\operatorname{Frac}(R)\). Since \(2\in I\) is nonzero,
\[
K\otimes_R I\neq0.
\]
But \(I\subseteq R\) gives an inclusion
\[
K\otimes_R I\subseteq K\otimes_R R\cong K,
\]
so \(K\otimes_R I\) is a one-dimensional \(K\)-vector space. Hence \(\operatorname{rank}_R I=1\).
:::

<1>2. Every nonzero cyclic submodule of \(I\) has rank \(1\).
::: {.proof}
If \(0\neq y\in I\), then the cyclic module \(Ry\) is isomorphic to \(R\): the map \(R\to Ry\), \(r\mapsto ry\), is injective because \(R\) is a domain and \(y\neq0\). Therefore \(\operatorname{rank}_R(Ry)=1\).
:::

<1>3. The ideal \(I\) cannot be a direct sum of two or more nonzero cyclic \(R\)-modules.
::: {.proof}
If
\[
I\cong C_1\oplus\cdots\oplus C_m
\]
with \(m\ge2\) and every \(C_i\) nonzero cyclic, then by <1>2 each \(C_i\) has rank \(1\). Rank is additive on direct sums, so
\[
\operatorname{rank}_R I=m\ge2,
\]
contradicting <1>1.
:::
:::
