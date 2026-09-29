---
schema: qual/card@1
id: P-OUQ2Q
kind: problem
title: $\mathbb{Q}[x]$-modules from order-$6$ matrices in $M_4(\mathbb{Q})$, and groups
  of order $24$
classification:
  areas:
  - prelim
  topics:
  - Rational Canonical Form
  - Modules
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $A \in M_4(\mathbb{Q})$ is a 4-by-4 matrix of multiplicative order 6. We use $A$ to give $\mathbb{Q}^4$ the structure of a $\mathbb{Q}[x]$-module in the usual way, by setting $x \cdot v = Av$ for $v \in \mathbb{Q}^4$.

a. What are all of the isomorphism classes of $\mathbb{Q}[x]$-modules that can arise this way?

b. For each of your answers above, write down the rational canonical form of the corresponding matrix $A$.

c. What are all the of the abelian groups of size 24 (up to isomorphism)?
:::

::: {.solution}
Over $\QQ$,
$$
x^6-1=\Phi_1\Phi_2\Phi_3\Phi_6=(x-1)(x+1)(x^2+x+1)(x^2-x+1),
$$
a product of distinct monic irreducibles. For a monic polynomial $p$, write $C(p)$ for its companion matrix, with ones on the subdiagonal and last column the negated lower coefficients of $p$.

::: pf

::: {.pf-step #s1}

The $\QQ[x]$-module $V=\QQ^4$ is isomorphic to
$$
V_{a}=\bigoplus_{d\in\{1,2,3,6\}}\bigl(\QQ[x]/(\Phi_d)\bigr)^{a_d},
\qquad a_1+a_2+2a_3+2a_6=4,
$$
for unique multiplicities $a_d\ge0$, and $A$ has order exactly $6$ if and only if $a_6\ge1$, or $a_2\ge1$ and $a_3\ge1$.

::: pf-proof

Since $A^6=I$, the module is annihilated by the squarefree polynomial $x^6-1$, so by the structure theorem over the PID $\QQ[x]$ it is a direct sum of modules $\QQ[x]/(\Phi_d)$ with $d\mid6$, with unique multiplicities [@DF04]; dimensions give $a_1+a_2+2a_3+2a_6=4$.
On $\QQ[x]/(\Phi_d)$, $x$ acts with order exactly $d$, so the order of $A$ is the least common multiple of the $d$ with $a_d\ge1$.
This least common multiple is $6$ exactly when $6$ occurs, or both $2$ and $3$ occur.

:::

:::

::: {.pf-step #s2}

For part (a), there are exactly seven classes, listed by $(a_1,a_2,a_3,a_6)$:
$$
(0,0,0,2),\ (2,0,0,1),\ (0,2,0,1),\ (1,1,0,1),\ (0,0,1,1),\ (1,1,1,0),\ (0,2,1,0).
$$

::: pf-proof

If $a_6=2$, the others vanish. If $a_6=1$, then $a_1+a_2+2a_3=2$, with the four solutions $(2,0,0)$, $(1,1,0)$, $(0,2,0)$, $(0,0,1)$.
If $a_6=0$, then $a_2,a_3\ge1$ and $a_1+a_2+2a_3=4$ force $a_3=1$ and $(a_1,a_2)\in\{(1,1),(0,2)\}$.
By step [](#s1){.pf-ref} these seven modules are pairwise nonisomorphic and are exactly the modules that arise.

:::

:::

::: {.pf-step #s3}

For part (b), the rational canonical forms are given by the invariant factors in the table.

| $(a_1,a_2,a_3,a_6)$ | Invariant factors | Rational canonical form |
| --- | --- | --- |
| $(0,0,0,2)$ | $x^2-x+1,\ x^2-x+1$ | $\operatorname{diag}\bigl(C(x^2-x+1),C(x^2-x+1)\bigr)$ |
| $(2,0,0,1)$ | $x-1,\ x^3-2x^2+2x-1$ | $\operatorname{diag}\bigl(1,C(x^3-2x^2+2x-1)\bigr)$ |
| $(0,2,0,1)$ | $x+1,\ x^3+1$ | $\operatorname{diag}\bigl(-1,C(x^3+1)\bigr)$ |
| $(1,1,0,1)$ | $x^4-x^3+x-1$ | $C(x^4-x^3+x-1)$ |
| $(0,0,1,1)$ | $x^4+x^2+1$ | $C(x^4+x^2+1)$ |
| $(1,1,1,0)$ | $x^4+x^3-x-1$ | $C(x^4+x^3-x-1)$ |
| $(0,2,1,0)$ | $x+1,\ x^3+2x^2+2x+1$ | $\operatorname{diag}\bigl(-1,C(x^3+2x^2+2x+1)\bigr)$ |

Explicitly,
$$
C(x^2-x+1)=\begin{pmatrix}0&-1\\1&1\end{pmatrix},\quad
C(x^3-2x^2+2x-1)=\begin{pmatrix}0&0&1\\1&0&-2\\0&1&2\end{pmatrix},\quad
C(x^3+1)=\begin{pmatrix}0&0&-1\\1&0&0\\0&1&0\end{pmatrix},
$$
$$
C(x^3+2x^2+2x+1)=\begin{pmatrix}0&0&-1\\1&0&-2\\0&1&-2\end{pmatrix},\quad
C(x^4-x^3+x-1)=\begin{pmatrix}0&0&0&1\\1&0&0&-1\\0&1&0&0\\0&0&1&1\end{pmatrix},
$$
$$
C(x^4+x^2+1)=\begin{pmatrix}0&0&0&-1\\1&0&0&0\\0&1&0&-1\\0&0&1&0\end{pmatrix},\quad
C(x^4+x^3-x-1)=\begin{pmatrix}0&0&0&1\\1&0&0&1\\0&1&0&0\\0&0&1&-1\end{pmatrix}.
$$

::: pf-proof

The invariant factors are obtained by multiplying, from the largest down, one factor $\Phi_d$ for each $d$ with $a_d$ remaining; for instance $(0,2,1,0)$ gives $\Phi_2$ and $\Phi_2\Phi_3=(x+1)(x^2+x+1)=x^3+2x^2+2x+1$.
The rational canonical form is the block diagonal matrix of the companion matrices of the invariant factors [@DF04].

:::

:::

::: {.pf-step #s4}

For part (c), the abelian groups of order $24$ are $\ZZ/24$, $\ZZ/12\times\ZZ/2$, and $\ZZ/6\times(\ZZ/2)^2$.

::: pf-proof

Since $24=2^3\cdot3$, an abelian group of order $24$ is the product of its Sylow $2$-subgroup of order $8$ and its Sylow $3$-subgroup $\ZZ/3$ [@DF04].
The partitions $3$, $2+1$, $1+1+1$ give the Sylow $2$-subgroups $\ZZ/8$, $\ZZ/4\times\ZZ/2$, $(\ZZ/2)^3$.
By the Chinese remainder theorem the products with $\ZZ/3$ are the three listed groups.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer parts (a), (b), and (c).

:::

:::

:::
