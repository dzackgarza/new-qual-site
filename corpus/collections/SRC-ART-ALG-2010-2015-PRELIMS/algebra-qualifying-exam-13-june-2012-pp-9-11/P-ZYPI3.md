---
schema: qual/card@1
id: P-ZYPI3
kind: problem
title: Finitely generated modules over a PID, groups of order $72$, and rational canonical
  form
classification:
  areas:
  - prelim
  topics:
  - Structure Theorem
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
a. State the structure theorem for finitely generated modules over a PID. You may state either the invariant factors or elementary divisors version.

b. Determine all abelian groups of size 72 up to isomorphism.
Explain how this relates to part (a).

c. Determine all conjugacy classes of 3x3 matrices over $\mathbb{Q}$ with characteristic polynomial $x^3 - 2x^2 + x$.
Explain how this relates to part (a).
:::

::: {.solution}
<1>1. In part (a): let $R$ be a principal ideal domain and $M$ a finitely generated $R$-module. Then
$$
M\cong R^r\oplus R/(a_1)\oplus\cdots\oplus R/(a_k)
$$
for an integer $r\ge0$ and nonzero nonunits $a_1\mid a_2\mid\cdots\mid a_k$ of $R$, and $r$ and the ideals $(a_1),\ldots,(a_k)$ are uniquely determined by $M$ [@DF04].

<1>2. In part (b), there are six abelian groups of order $72$:

| Elementary divisors | Invariant factors |
| --- | --- |
| $\ZZ_8\oplus\ZZ_9$ | $\ZZ_{72}$ |
| $\ZZ_8\oplus\ZZ_3\oplus\ZZ_3$ | $\ZZ_3\oplus\ZZ_{24}$ |
| $\ZZ_4\oplus\ZZ_2\oplus\ZZ_9$ | $\ZZ_2\oplus\ZZ_{36}$ |
| $\ZZ_4\oplus\ZZ_2\oplus\ZZ_3\oplus\ZZ_3$ | $\ZZ_6\oplus\ZZ_{12}$ |
| $\ZZ_2^{\oplus3}\oplus\ZZ_9$ | $\ZZ_2\oplus\ZZ_2\oplus\ZZ_{18}$ |
| $\ZZ_2^{\oplus3}\oplus\ZZ_3\oplus\ZZ_3$ | $\ZZ_2\oplus\ZZ_6\oplus\ZZ_6$ |

::: {.proof}
An abelian group is a $\ZZ$-module, and $\ZZ$ is a principal ideal domain; a group of order $72$ is finitely generated with $r=0$, so step <1>1 applies with $R=\ZZ$.
Since $72=2^3\cdot3^2$, the elementary-divisor form writes $G\cong G_2\oplus G_3$ with $\abs{G_2}=8$ and $\abs{G_3}=9$, and the isomorphism types of $G_2$ and $G_3$ correspond to the partitions $3$, $2+1$, $1+1+1$ of $3$ and $2$, $1+1$ of $2$.
The $3\cdot2=6$ combinations are the rows of the table; the invariant factors in each row are obtained by combining the largest $2$-power with the largest $3$-power, and so on, by the Chinese remainder theorem.
:::

<1>3. In part (c), there are two conjugacy classes, with invariant factors $x(x-1)^2$, respectively $x-1\mid x(x-1)$, and rational canonical forms
$$
\begin{pmatrix}0&0&0\\1&0&-1\\0&1&2\end{pmatrix},
\qquad
\begin{pmatrix}1&0&0\\0&0&0\\0&1&1\end{pmatrix}.
$$

::: {.proof}
A matrix $A\in M_3(\QQ)$ makes $V=\QQ^3$ a finitely generated torsion module over the principal ideal domain $\QQ[x]$ with $x\cdot v=Av$, and two matrices are conjugate exactly when these modules are isomorphic.
By step <1>1, $V\cong\QQ[x]/(f_1)\oplus\cdots\oplus\QQ[x]/(f_k)$ with monic $f_1\mid\cdots\mid f_k$ and $f_1\cdots f_k=\det(xI-A)=x(x-1)^2$.
Since each $f_i$ divides $f_k$, a factor $x$ appearing in $f_1$ would appear twice in the product; so $x$ divides only $f_k$, and either $k=1$ with $f_1=x(x-1)^2$, or $k=2$ with $f_1=x-1$ and $f_2=x(x-1)$.
The rational canonical forms are the block diagonal matrices of the companion matrices of the invariant factors.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 states the theorem for part (a). Steps <1>2 and <1>3 answer parts (b) and (c) as the cases $R=\ZZ$ and $R=\QQ[x]$ of that theorem.
:::
:::
