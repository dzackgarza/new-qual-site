---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-05
kind: problem
title: Homology of the complement of two unlinked circles in $\mathbb{R}^3$
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Corrected the Alexander-duality compactification. For a complement in R^3 one must dualize against A together with the point at infinity; this changes H_2 from Z to Z^2.
---

::: {.problem}
(Arizona Aug ’06) Compute the singular homology groups $H_*(X,\mathbb Z)$ of the space $X=\mathbb R^3\setminus A$, where $A$ is a subset of $\mathbb R^3$ homeomorphic to the disjoint union of two unlinked circles.
:::

::: {.solution}
<1>1. Regard $X=\RR^3\setminus A$ as a complement in $S^3$.
::: {.proof}
Let $\infty$ denote the point at infinity in the one-point compactification $S^3=\RR^3\cup\{\infty\}$ and put
\[
K=A\sqcup\{\infty\}.
\]
Then
\[
X=S^3\setminus K.
\]
The set $K$ is compact and locally contractible, so Alexander duality gives
\[
\widetilde H_k(X;\ZZ)
\cong
\widetilde H^{\,2-k}(K;\ZZ)
\]
for every $k$.
:::

<1>2. The reduced cohomology of $K=S^1\sqcup S^1\sqcup\{\infty\}$ is
\[
\widetilde H^j(K;\ZZ)
\cong
\begin{cases}
\ZZ^2,&j=0,\\
\ZZ^2,&j=1,\\
0,&j\ge2.
\end{cases}
\]
::: {.proof}
The space $K$ has three connected components, so $\widetilde H^0(K;\ZZ)\cong\ZZ^{3-1}=\ZZ^2$.
Each circle contributes one copy of $\ZZ$ in degree $1$, while the isolated point contributes none, hence $H^1(K;\ZZ)\cong\ZZ^2$.
There is no cohomology in higher degrees.
:::

<1>3. Alexander duality therefore gives
\[
\widetilde H_0(X;\ZZ)=0,
\qquad
H_1(X;\ZZ)\cong\ZZ^2,
\qquad
H_2(X;\ZZ)\cong\ZZ^2,
\]
::: {.proof}
Apply <1>1 to the groups in <1>2: $\widetilde H_0(X)\cong\widetilde H^2(K)=0$, $H_1(X)=\widetilde H_1(X)\cong\widetilde H^1(K)=\ZZ^2$, and $H_2(X)=\widetilde H_2(X)\cong\widetilde H^0(K)=\ZZ^2$.
For $k\ge3$, the corresponding cohomological degree is negative, so the homology group is zero.
:::

<1>4. Thus the singular homology groups of $X=\RR^3\setminus(S^1\sqcup S^1)$ are
\[
H_k(X;\ZZ)
\cong
\begin{cases}
\ZZ,&k=0,\\
\ZZ^2,&k=1,\\
\ZZ^2,&k=2,\\
0,&k\ge3.
\end{cases}
\]
::: {.proof}
Since $\widetilde H_0(X)=0$, one has $H_0(X)\cong\ZZ$; the remaining groups are exactly those computed in <1>3.
:::
:::
