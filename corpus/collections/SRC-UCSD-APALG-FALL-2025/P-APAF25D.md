---
schema: qual/card@1
id: P-APAF25D
kind: problem
title: Compatible vector norm and eigenvalue bound by a consistent matrix norm
classification:
  areas:
  - applied-algebra
  topics:
  - Norms
relations: []
review: draft
---

::: {.problem}
Given $n\geq 1$ and $\|\cdot\|$ a matrix norm of $M_n(\mathbb{C})=\mathbb{C}^{n\times n}$ that is consistent (meaning $\|AB\|\leq\|A\|\|B\|$), let $A\in M_n(\mathbb{C})$.

(a) Find a vector norm $\|\cdot\|_0$ of $\mathbb{C}^n$ that is compatible with $\|\cdot\|$ (meaning $\|Ax\|_0\leq\|A\|\|x\|_0$).

(b) Prove, for all eigenvalues $\lambda$ of $A$, that $|\lambda|\leq\|A\|$.
:::

::: {.solution}
Fix the first standard basis vector \(e_1\in\mathbb C^n\), regarded as a column vector, and define
\[
\|x\|_0:=\|x e_1^H\|
\qquad(x\in\mathbb C^n).
\]
Here \(xe_1^H\in M_n(\mathbb C)\) is the matrix whose first column is \(x\) and whose remaining columns are zero.

<1>1. The function \(\|\cdot\|_0\) is a vector norm on \(\mathbb C^n\).
::: {.proof}
For \(x,y\in\mathbb C^n\) and \(c\in\mathbb C\), the matrix norm axioms give
\[
\|x+y\|_0
=\|(x+y)e_1^H\|
\le \|xe_1^H\|+\|ye_1^H\|
=\|x\|_0+\|y\|_0,
\]
and
\[
\|cx\|_0
=\|cxe_1^H\|
=|c|\,\|xe_1^H\|
=|c|\,\|x\|_0.
\]
Also \(\|x\|_0\ge0\). Finally, if \(\|x\|_0=0\), then \(xe_1^H=0\) because a matrix norm is definite, and hence its first column \(x\) is zero. Thus \(x=0\).
:::

<1>2. The vector norm \(\|\cdot\|_0\) is compatible with the given matrix norm:
\[
\|Ax\|_0\le \|A\|\,\|x\|_0
\qquad(A\in M_n(\mathbb C),\ x\in\mathbb C^n).
\]
::: {.proof}
Using associativity and consistency of the matrix norm,
\[
\|Ax\|_0
=\|(Ax)e_1^H\|
=\|A(xe_1^H)\|
\le \|A\|\,\|xe_1^H\|
=\|A\|\,\|x\|_0.
\]
This proves part (a).
:::

<1>3. Every eigenvalue \(\lambda\) of \(A\) satisfies
\[
|\lambda|\le \|A\|.
\]
::: {.proof}
Let \(0\ne x\in\mathbb C^n\) be an eigenvector with \(Ax=\lambda x\). By <1>2,
\[
|\lambda|\,\|x\|_0
=\|\lambda x\|_0
=\|Ax\|_0
\le \|A\|\,\|x\|_0.
\]
Since \(x\ne0\), one has \(\|x\|_0>0\). Dividing by \(\|x\|_0\) yields
\[
|\lambda|\le \|A\|.
\]
This proves part (b).
:::
:::
