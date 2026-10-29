---
schema: qual/card@1
id: P-K5JBF
kind: problem
title: Isomorphism type of $\ZZ^3/\langle(0,4,2),(-1,-4,-1),(0,0,-2)\rangle$
classification:
  areas:
  - prelim
  topics:
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
Form an abelian group $M$ as the quotient of $\ZZ^3$ by the elements $(0,4,2)$, $(-1,-4,-1)$, and $(0,0,-2)$.
What abelian group is $M$?
(That is, find its isomorphism type).
:::

::: {.solution}
Let
$$
A=
\begin{pmatrix}
0&4&2\\
-1&-4&-1\\
0&0&-2
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

The group $M$ is the cokernel of the homomorphism
$A^{\mathsf T}:\ZZ^3\to\ZZ^3$.

::: pf-proof

The columns of $A^{\mathsf T}$ are precisely
$$
(0,4,2),\qquad(-1,-4,-1),\qquad(0,0,-2),
$$
so the image of $A^{\mathsf T}$ is the subgroup by which the problem
quotients $\ZZ^3$. Hence
$$
M\cong\operatorname{coker}(A^{\mathsf T}).
$$

:::

:::

::: {.pf-step #s2}

The Smith invariant factors of $A^{\mathsf T}$ are
$$
1,\ 2,\ 4.
$$

::: pf-proof

Transpose does not change the determinantal divisors, so it is enough to
compute them from $A$.

The first determinantal divisor is the gcd of all entries. Since $A$
contains the entry $-1$,
$$
\Delta_1=1.
$$
The nonzero $2\times2$ minors include
$$
4,quad2,quad4,quad-8,quad2,quad8,
$$
and every $2\times2$ minor is even. Therefore
$$
\Delta_2=2.
$$
Finally,
$$
\Delta_3=|\det A|
=8.
$$
For Smith invariant factors $d_1\mid d_2\mid d_3$,
$$
d_1=\Delta_1,
\qquad
d_1d_2=\Delta_2,
\qquad
d_1d_2d_3=\Delta_3.
$$
Hence
$$
d_1=1,qquad d_2=2,qquad d_3=4.
$$

:::

:::

::: {.pf-step #s3}

The isomorphism type of $M$ is
$$
\boxed{M\cong\ZZ/2\ZZ\oplus\ZZ/4\ZZ}.
$$

::: pf-proof

By the Smith normal form theorem, step [](#s2){.pf-ref} gives
$$
\operatorname{coker}(A^{\mathsf T})
\cong
\ZZ/1\ZZ\oplus\ZZ/2\ZZ\oplus\ZZ/4\ZZ.
$$
The first summand is trivial, and step [](#s1){.pf-ref} identifies this cokernel with
$M$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested isomorphism type.

:::

:::

:::
