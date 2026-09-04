---
schema: qual/card@1
id: P-ETP6C
kind: problem
title: Relative homology $H_k(S^n,E)$ of the $n$-sphere and its equator
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-04
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-04
  note: Checked the equator-adapted relative CW complex, including the n=1 case.
---

::: problem
For any $n \geq 1$ let $S^n = \theset{(x_0 , \cdots , x_n )\mid \sum x_i^2 =1}$ denote the $n$ dimensional unit sphere and let $$E = \theset{(x_0 , . . . , x_n )\mid x_n = 0}$$ denote the "equator".

Find, for all $k$, the relative homology $H_k (S^n , E)$.
:::

::: {.solution}
<1>1. The equator is
\[
E=S^n\cap\{x_n=0\}\cong S^{n-1}.
\]
Give \(S^n\) a CW structure for which \(E\) is a subcomplex and the only cells of \(S^n\) not already in \(E\) are the two open \(n\)-cells
\[
e_+^n=\{x\in S^n:x_n>0\},
\qquad
e_-^n=\{x\in S^n:x_n<0\}.
\]
::: {.proof}
The closed upper and lower hemispheres
\[
D_+^n=\{x\in S^n:x_n\ge0\},
\qquad
D_-^n=\{x\in S^n:x_n\le0\}
\]
are each homeomorphic to \(D^n\), and both have boundary \(E\cong S^{n-1}\). Choose any CW structure on \(E\). Attaching the interiors of these two hemispheres to \(E\) gives the stated CW structure on \(S^n\). For \(n=1\), the equator is \(S^0\), and the same description says that the two open semicircles are the two relative \(1\)-cells.
:::

<1>2. The relative cellular chain groups are
\[
C_k(S^n,E)
\cong
\begin{cases}
\mathbb Z^2,&k=n,\\
0,&k\ne n.
\end{cases}
\]
::: {.proof}
For a CW pair \((X,A)\), the relative cellular chain group \(C_k(X,A)\) is free abelian on the \(k\)-cells of \(X\) that are not cells of \(A\). By <1>1, exactly two cells of \(S^n\) lie outside the subcomplex \(E\), and both have dimension \(n\). They are \(e_+^n\) and \(e_-^n\). Therefore the relative cellular chain group is \(\mathbb Z^2\) in degree \(n\) and zero in every other degree.
:::

<1>3. Every differential in the relative cellular chain complex is zero.
::: {.proof}
The only nonzero relative chain group is \(C_n(S^n,E)\). Its target under the boundary map is
\[
C_{n-1}(S^n,E)=0,
\]
so \(\partial_n=0\). All other differentials have zero domain.
:::

<1>4. Hence, for every \(n\ge1\),
\[
\boxed{
H_k(S^n,E;\mathbb Z)
\cong
\begin{cases}
\mathbb Z\oplus\mathbb Z,&k=n,\\
0,&k\ne n.
\end{cases}}
\]
::: {.proof}
Relative cellular homology computes the singular relative homology of a CW pair.
By <1>2--<1>3, its chain complex has \(\mathbb Z^2\) in degree \(n\), zero elsewhere, and zero differentials.
Its homology is therefore exactly the displayed group.
:::
:::
