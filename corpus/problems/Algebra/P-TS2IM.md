---
schema: qual/card@1
id: P-TS2IM
kind: problem
title: Conjugacy classes of $3\times 3$ rational matrices satisfying $A^4-A^3-A+1=0$
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Rational Canonical Form
  - Minimal and Characteristic Polynomials
relations: []
review: draft
---

::: {.problem}
Describe all conjugacy classes of $3\times3$ matrices $A\in M_3(\QQ)$ satisfying
$$
A^4-A^3-A+I=0.
$$
Give a representative of each class.
:::

::: {.solution}
View $\QQ^3$ as a $\QQ[x]$-module via $x\cdot v=Av$; conjugacy classes of $A$ correspond to isomorphism classes of these modules, which are determined by their elementary divisors.

::: pf

::: {.pf-step #minpoly}
The minimal polynomial of $A$ divides $(x-1)^2(x^2+x+1)$, and $x-1$ and $x^2+x+1$ are irreducible over $\QQ$.

::: pf-proof
$x^4-x^3-x+1=(x-1)(x^3-1)=(x-1)^2(x^2+x+1)$ annihilates $A$.
The quadratic $x^2+x+1$ has negative discriminant, so it has no rational root.
:::

:::

::: {.pf-step #divisors}
The elementary divisors of $A$ are $(x-1),(x-1),(x-1)$, or $(x-1)^2,(x-1)$, or $(x-1),(x^2+x+1)$.

::: pf-proof
By step [](#minpoly){.pf-ref} each elementary divisor is $x-1$, $(x-1)^2$, or $x^2+x+1$, with $x^2+x+1$ occurring at most once because $(x^2+x+1)^2$ does not divide the minimal polynomial, and their degrees sum to $3$.
These are all the ways to obtain total degree $3$.
:::

:::

::: pf-step
There are exactly three conjugacy classes, with representatives
$$
I_3,
\qquad
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix},
\qquad
\begin{pmatrix}
1&0&0\\
0&0&-1\\
0&1&-1
\end{pmatrix}.
$$

::: pf-proof
These matrices realize the three lists of step [](#divisors){.pf-ref}: the second has a $2\times2$ Jordan block for $1$, and the lower-right block of the third is the companion matrix of $x^2+x+1$.
Their minimal polynomials $x-1$, $(x-1)^2$ and $(x-1)(x^2+x+1)$ are distinct, so they are pairwise nonconjugate.
:::

:::

:::

:::
