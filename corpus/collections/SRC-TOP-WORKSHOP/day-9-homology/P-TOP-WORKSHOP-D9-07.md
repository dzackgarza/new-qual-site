---
schema: qual/card@1
id: P-TOP-WORKSHOP-D9-07
kind: problem
title: Build a Δ-complex and chain complex after identifying the vertices of a 2-simplex
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
  - Quotient Spaces
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
(Jan ’12) Let $X$ be a space obtained by identifying the three vertices of a standard 2-simplex.

(a) Describe a structure of a $\Delta$-complex on $X$.

(b) Write down the chain complex corresponding to the $\Delta$-complex in (a).

(c) Compute the homology of $X$.
:::

::: {.solution}
Let the vertices of the standard \(2\)-simplex be \(v_0,v_1,v_2\), and identify all three to a single vertex \(v\). The three edges descend to three distinct \(1\)-simplices. Orient them by
\[
a=[v_0,v_1],\qquad b=[v_1,v_2],\qquad c=[v_0,v_2].
\]
The interior of the original triangle is one \(2\)-simplex \(\sigma=[v_0,v_1,v_2]\). This gives the desired \(\Delta\)-complex structure.

The simplicial chain groups are
\[
0\longrightarrow C_2\cong\mathbb Z
\xrightarrow{\partial_2}
C_1\cong\mathbb Z^3
\xrightarrow{\partial_1}
C_0\cong\mathbb Z
\longrightarrow0.
\]
Since every edge begins and ends at \(v\), \(\partial_1=0\). The oriented boundary of \(\sigma\) is
\[
\partial_2\sigma=[v_1,v_2]-[v_0,v_2]+[v_0,v_1]=a+b-c.
\]
Thus, in the indicated bases,
\[
\partial_2(1)=(1,1,-1),
\qquad
\partial_1=0.
\]
The vector \((1,1,-1)\) is primitive and nonzero, so \(\partial_2\) is injective and its cokernel is free of rank \(2\). Hence
\[
H_n(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=0,\\
\mathbb Z^2,&n=1,\\
0,&n\ge2.
\end{cases}
\]
:::
