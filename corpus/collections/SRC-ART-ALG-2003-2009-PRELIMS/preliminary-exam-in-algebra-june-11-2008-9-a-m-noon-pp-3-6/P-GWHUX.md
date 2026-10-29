---
schema: qual/card@1
id: P-GWHUX
kind: problem
title: Elementary divisors and invariant factors of $\ZZ_{15}\times\ZZ_{20}\times\ZZ_9$;
  abelian groups of order $2700$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Structure Theorem
relations: []
review: draft
---
::: {.problem}
a. Determine the elementary divisors and invariant factors of the Abelian group $\ZZ_{15}\times\ZZ_{20}\times\ZZ_9$ of order 2700.
b. Determine the number of nonisomorphic Abelian groups of order 2700.
:::

::: {.solution}
Let
$$
G=\ZZ/15\ZZ\times\ZZ/20\ZZ\times\ZZ/9\ZZ.
$$

::: pf

::: {.pf-step #s1}

The elementary divisors of $G$ are
$$
\boxed{4,\ 3,\ 9,\ 5,\ 5}.
$$

::: pf-proof

Using the Chinese remainder theorem,
$$
\ZZ/15\ZZ\cong\ZZ/3\ZZ\times\ZZ/5\ZZ
$$
and
$$
\ZZ/20\ZZ\cong\ZZ/4\ZZ\times\ZZ/5\ZZ.
$$
Therefore
$$
G\cong
\ZZ/4\ZZ
\times\ZZ/3\ZZ
\times\ZZ/9\ZZ
\times\ZZ/5\ZZ
\times\ZZ/5\ZZ.
$$
Each displayed cyclic factor has prime-power order, so these orders are
the elementary divisors.

:::

:::

::: {.pf-step #s2}

The invariant factors of $G$ are
$$
\boxed{15,\ 180}.
$$

::: pf-proof

Group the elementary-divisor decomposition by primes:
$$
G_{(2)}\cong\ZZ/4\ZZ,
\qquad
G_{(3)}\cong\ZZ/3\ZZ\times\ZZ/9\ZZ,
\qquad
G_{(5)}\cong\ZZ/5\ZZ\times\ZZ/5\ZZ.
$$
Pad the $2$-primary list by a trivial factor and align factors in
nondecreasing divisibility order:
$$
(1,4),\qquad(3,9),\qquad(5,5).
$$
Multiplying componentwise gives
$$
(1\cdot3\cdot5,\ 4\cdot9\cdot5)=(15,180).
$$
Since $15\mid180$, this is the invariant-factor decomposition
$$
G\cong\ZZ/15\ZZ\times\ZZ/180\ZZ.
$$

:::

:::

::: {.pf-step #s3}

There are
$$
\boxed{12}
$$
isomorphism classes of abelian groups of order $2700$.

::: pf-proof

The prime factorization is
$$
2700=2^2\,3^3\,5^2.
$$
By the structure theorem for finite abelian groups [@DF04], the
isomorphism type is determined independently by the partitions of the
exponents $2,3,2$. There are
$$
p(2)=2,
\qquad
p(3)=3,
\qquad
p(2)=2
$$
choices, corresponding explicitly to
$$
\ZZ/4\ZZ
\quad\text{or}\quad
(\ZZ/2\ZZ)^2,
$$
$$
\ZZ/27\ZZ,
\quad
\ZZ/9\ZZ\times\ZZ/3\ZZ,
\quad
(\ZZ/3\ZZ)^3,
$$
and
$$
\ZZ/25\ZZ
\quad\text{or}\quad
(\ZZ/5\ZZ)^2.
$$
The choices for the three primes are independent, so the total number is
$$
2\cdot3\cdot2=12.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} answer part (a), and step [](#s3){.pf-ref} answers part (b).

:::

:::

:::
