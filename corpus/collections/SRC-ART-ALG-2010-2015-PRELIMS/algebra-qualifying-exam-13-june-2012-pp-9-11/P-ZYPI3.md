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

c. Determine all conjugacy classes of 3x3 matrices over $\QQ$ with characteristic polynomial $x^3 - 2x^2 + x$.
Explain how this relates to part (a).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The invariant-factor form of the structure theorem is as follows:
if $R$ is a PID and $M$ is a finitely generated $R$-module, then
$$
M\cong
R^r\oplus R/(a_1)\oplus\cdots\oplus R/(a_k),
$$
where $r\ge0$, the $a_i$ are nonzero nonunits, and
$$
a_1\mid a_2\mid\cdots\mid a_k.
$$
The integer $r$ and the ideals $(a_i)$ are uniquely determined by $M$.

::: pf-proof

This is the structure theorem for finitely generated modules over a PID
[@DF04]. It answers part (a).

:::

:::

::: {.pf-step #s2}

The abelian groups of order $72$ are exactly
$$
\boxed{
\begin{aligned}
&\ZZ/72,\\
&\ZZ/3\oplus\ZZ/24,\\
&\ZZ/2\oplus\ZZ/36,\\
&\ZZ/6\oplus\ZZ/12,\\
&(\ZZ/2)^2\oplus\ZZ/18,\\
&\ZZ/2\oplus\ZZ/6\oplus\ZZ/6.
\end{aligned}}
$$

::: pf-proof

An abelian group is a $\ZZ$-module, and $\ZZ$ is a PID. Since
$$
72=2^3\cdot3^2,
$$
the elementary-divisor form of step [](#s1){.pf-ref} gives three possibilities for
the $2$-primary part,
$$
\ZZ/8,qquad
\ZZ/4\oplus\ZZ/2,qquad
(\ZZ/2)^3,
$$
and two possibilities for the $3$-primary part,
$$
\ZZ/9,qquad
(\ZZ/3)^2.
$$
Taking all six products and combining coprime cyclic factors gives the
six displayed invariant-factor decompositions. Uniqueness in step [](#s1){.pf-ref}
shows that they are pairwise nonisomorphic and exhaustive.

:::

:::

::: {.pf-step #s3}

For part (c), conjugacy classes of matrices
$A\in M_3(\QQ)$ with characteristic polynomial
$$
\chi_A(x)=x^3-2x^2+x=x(x-1)^2
$$
are in bijection with invariant-factor decompositions of the
$\QQ[x]$-module $\QQ^3$ defined by $x\cdot v=Av$.

::: pf-proof

Two matrices are conjugate over $\QQ$ exactly when the corresponding
$\QQ[x]$-modules are isomorphic. Since $\QQ[x]$ is a PID, step [](#s1){.pf-ref}
applies. If the invariant factors are
$f_1\mid\cdots\mid f_k$, then their product is the characteristic
polynomial and the largest is the minimal polynomial.

:::

:::

::: {.pf-step #s4}

There are exactly two possible invariant-factor lists:
$$
\boxed{
\bigl(x(x-1)^2\bigr)
}
$$
and
$$
\boxed{
(x-1),\quad x(x-1)
}.
$$

::: pf-proof

The elementary divisors are one copy of $x$ and two copies of $x-1$.
If the two $x-1$ factors belong to one invariant factor, the divisibility
condition forces the $x$ factor into the same invariant factor, giving
$x(x-1)^2$.

If the two $x-1$ factors lie in separate invariant factors, the factor
$x$ must be placed in the larger one in order to preserve divisibility,
giving
$$
(x-1)\mid x(x-1).
$$
No other distribution of the elementary divisors yields a divisibility
chain.

:::

:::

::: {.pf-step #s5}

Representatives of the two conjugacy classes are
$$
\boxed{
C\bigl(x^3-2x^2+x\bigr)
=
\begin{pmatrix}
0&0&0\\
1&0&-1\\
0&1&2
\end{pmatrix}}
$$
and
$$
\boxed{
\operatorname{diag}
\left(
1,
C(x^2-x)
\right)
=
\begin{pmatrix}
1&0&0\\
0&0&0\\
0&1&1
\end{pmatrix}}.
$$

::: pf-proof

The rational canonical form attached to an invariant-factor list is the
block diagonal matrix of the companion matrices of those factors.
Applying this to the two lists in step [](#s4){.pf-ref} gives the displayed matrices.
Distinct invariant-factor lists give nonconjugate matrices, while every
matrix with the prescribed characteristic polynomial has one of these
lists by step [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a), step [](#s2){.pf-ref} answers part (b), and
steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} answer part (c).

:::

:::

:::
