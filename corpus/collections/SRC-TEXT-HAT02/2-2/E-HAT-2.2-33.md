---
schema: qual/card@1
id: E-HAT-2.2-33
kind: problem
title: 'Nerve-type vanishing: $\tilde{H}_i(X) = 0$ for $i \geq n-1$ when intersections are acyclic'
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
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose the space $X$ is the union of open sets $A_1, \cdots, A_n$ such that each intersection $A_{i_1} \cap \cdots \cap A_{i_k}$ is either empty or has trivial reduced homology groups.
Show that $\tilde{H}_i(X) = 0$ for $i \geq n-1$, and give an example showing this inequality is best possible, for each $n$.
:::

::: {.solution}
We induct on the number of sets. For one set the assertion is the hypothesis. Suppose it holds for covers by fewer than $n$ sets, and put
$$
Y=A_1\cup\cdots\cup A_{n-1},
\qquad
Z=Y\cap A_n=\bigcup_{j=1}^{n-1}(A_j\cap A_n).
$$
Both are open in $X$. Every nonempty finite intersection in the cover of $Z$ is one of the intersections in the hypothesis. Hence induction gives
$$
\widetilde H_i(Y)=\widetilde H_i(Z)=0
\qquad (i\ge n-2).
$$
The same hypothesis gives $\widetilde H_i(A_n)=0$ for every $i$. For $i\ge n-1$, the reduced Mayer--Vietoris sequence for $X=Y\cup A_n$ therefore has the segment
$$
0=\widetilde H_i(Y)\oplus\widetilde H_i(A_n)
\longrightarrow \widetilde H_i(X)
\longrightarrow \widetilde H_{i-1}(Z)=0.
$$
Thus $\widetilde H_i(X)=0$ in the claimed range.

For sharpness when $n\ge2$, let $X=\partial\Delta^{n-1}\cong S^{n-2}$ and use barycentric coordinates $\lambda_1,\ldots,\lambda_n$. Set
$$
A_j=\{x\in X:\lambda_j(x)>0\}.
$$
These $n$ open sets cover $X$. Their total intersection is empty. For every proper nonempty set of indices $I$, the intersection $\bigcap_{j\in I}A_j$ contracts to the barycenter of the face spanned by $I$: the straight-line homotopy stays in $X$, since each point and that barycenter share a zero coordinate outside $I$, and all coordinates indexed by $I$ remain positive. Yet
$$
\widetilde H_{n-2}(X)\cong\ZZ.
$$
Thus the vanishing range cannot start at $n-2$. For $n=1$, the hypothesis itself says that the sole nonempty set is acyclic.
:::
