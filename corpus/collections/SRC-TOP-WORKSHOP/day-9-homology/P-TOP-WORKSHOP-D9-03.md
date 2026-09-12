---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-03
kind: problem
title: Fundamental group and homology of $\mathbb{R}^4\setminus S^1$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homology
  - Homotopy
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(Michigan May ’09) Let $$S^1=\{(x,y,0,0)\in\mathbb R^4\mid x^2+y^2=1\}$$ be the unit circle and consider $M=\mathbb R^4\setminus S^1$.
Compute the fundamental group $\pi_1(M)$ and the homology groups $H_*(M)$ of $M$.
:::

::: {.solution}
First compute the fundamental group. Any loop in
\[
M=\mathbb R^4\setminus S^1
\]
bounds a disk in \(\mathbb R^4\), since \(\mathbb R^4\) is simply connected. By smooth or PL general position, the disk can be perturbed relative to its boundary to be disjoint from the embedded circle: the expected intersection dimension is
\[
2+1-4=-1.
\]
Thus every loop contracts in \(M\), and
\[
\pi_1(M)=0.
\]

For homology, compactify \(\mathbb R^4\) to \(S^4\). Then
\[
M\cong S^4\setminus A,
\qquad
A=S^1\sqcup\{\infty\}.
\]
Alexander duality gives
\[
\widetilde H_i(M;\mathbb Z)
\cong \widetilde H^{\,3-i}(A;\mathbb Z).
\]
The only nonzero reduced cohomology groups of \(A\) are
\[
\widetilde H^0(A)\cong\mathbb Z,
\qquad
H^1(A)\cong\mathbb Z.
\]
Hence
\[
\widetilde H_3(M)\cong\mathbb Z,
\qquad
\widetilde H_2(M)\cong\mathbb Z,
\]
and all other reduced homology groups vanish. Therefore
\[
H_i(M)\cong
\begin{cases}
\mathbb Z,&i=0,2,3,\\
0,&\text{otherwise}.
\end{cases}
\]
:::
