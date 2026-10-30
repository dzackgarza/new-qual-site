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
Given $n\geq 1$ and $\norm{\cdot}$ a matrix norm of $M_n(\CC)=\CC^{n\times n}$ that is consistent (meaning $\norm{AB}\leq\norm{A}\norm{B}$), let $A\in M_n(\CC)$.

(a) Find a vector norm $\norm{\cdot}_0$ of $\CC^n$ that is compatible with $\norm{\cdot}$ (meaning $\norm{Ax}_0\leq\norm{A}\norm{x}_0$).

(b) Prove, for all eigenvalues $\lambda$ of $A$, that $\abs{\lambda}\leq\norm{A}$.
:::

::: {.solution}

Fix the first standard basis vector $e_1\in\CC^n$, regarded as a column vector, and define
$$
\norm{x}_0:=\norm{x e_1^H}
\qquad(x\in\CC^n).
$$
Here $xe_1^H\in M_n(\CC)$ is the matrix whose first column is $x$ and whose remaining columns are zero.

::: pf

::: pf-step
The function $\norm{\cdot}_0$ is a vector norm on $\CC^n$.

::: pf-proof
For $x,y\in\CC^n$ and $c\in\CC$, the matrix norm axioms give
$$
\norm{x+y}_0
=\norm{(x+y)e_1^H}
\le \norm{xe_1^H}+\norm{ye_1^H}
=\norm{x}_0+\norm{y}_0,
$$
and
$$
\norm{cx}_0
=\norm{cxe_1^H}
=\abs{c}\,\norm{xe_1^H}
=\abs{c}\,\norm{x}_0.
$$
Also $\norm{x}_0\ge0$. Finally, if $\norm{x}_0=0$, then $xe_1^H=0$ because a matrix norm is definite, and hence its first column $x$ is zero. Thus $x=0$.
:::

:::

::: {.pf-step #norm0-is-compatible}
The vector norm $\norm{\cdot}_0$ is compatible with the given matrix norm:
$$
\norm{Ax}_0\le \norm{A}\,\norm{x}_0
\qquad(A\in M_n(\CC),\ x\in\CC^n).
$$

::: pf-proof
Using associativity and consistency of the matrix norm,
$$
\norm{Ax}_0
=\norm{(Ax)e_1^H}
=\norm{A(xe_1^H)}
\le \norm{A}\,\norm{xe_1^H}
=\norm{A}\,\norm{x}_0.
$$
This proves part (a).
:::

:::

::: pf-step
Every eigenvalue $\lambda$ of $A$ satisfies
$$
\abs{\lambda}\le \norm{A}.
$$

::: pf-proof
Let $0\ne x\in\CC^n$ be an eigenvector with $Ax=\lambda x$. By step [](#norm0-is-compatible){.pf-ref},
$$
\abs{\lambda}\,\norm{x}_0
=\norm{\lambda x}_0
=\norm{Ax}_0
\le \norm{A}\,\norm{x}_0.
$$
Since $x\ne0$, one has $\norm{x}_0>0$. Dividing by $\norm{x}_0$ yields
$$
\abs{\lambda}\le \norm{A}.
$$
This proves part (b).
:::

:::

:::

:::
