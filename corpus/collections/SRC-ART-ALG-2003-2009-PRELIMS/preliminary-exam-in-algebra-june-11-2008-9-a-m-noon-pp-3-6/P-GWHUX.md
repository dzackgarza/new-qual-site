---
schema: qual/card@1
id: P-GWHUX
kind: problem
title: Elementary divisors and invariant factors of $\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$;
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
a. Determine the elementary divisors and invariant factors of the Abelian group $\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$ of order 2700.
b. Determine the number of nonisomorphic Abelian groups of order 2700.
:::

::: {.solution}
Let $G=\mathbf{Z}_{15}\times\mathbf{Z}_{20}\times\mathbf{Z}_9$.

::: pf

::: {.pf-step #s1}

The elementary divisors of $G$ are $2^2,3,3^2,5,5$, and its invariant factors are $15\mid180$.

::: pf-proof

If $\gcd(a,b)=1$, then $\mathbf{Z}_a\times\mathbf{Z}_b\cong\mathbf{Z}_{ab}$.
Hence $\mathbf{Z}_{15}\cong\mathbf{Z}_3\times\mathbf{Z}_5$, $\mathbf{Z}_{20}\cong\mathbf{Z}_{2^2}\times\mathbf{Z}_5$, and
$$
G\cong\mathbf{Z}_{2^2}\times\mathbf{Z}_3\times\mathbf{Z}_{3^2}\times\mathbf{Z}_5\times\mathbf{Z}_5,
$$
which lists the elementary divisors.
Grouping the largest prime powers gives $\mathbf{Z}_{2^2}\times\mathbf{Z}_{3^2}\times\mathbf{Z}_5\cong\mathbf{Z}_{180}$, and the rest gives $\mathbf{Z}_3\times\mathbf{Z}_5\cong\mathbf{Z}_{15}$.
Thus $G\cong\mathbf{Z}_{15}\times\mathbf{Z}_{180}$ with $15\mid180$, and by uniqueness of invariant factors [@DF04] these are the invariant factors of $G$.

:::

:::

::: {.pf-step #s2}

There are $\boxed{12}$ nonisomorphic abelian groups of order $2700$.

::: pf-proof

Since $2700=2^2\cdot3^3\cdot5^2$, an abelian group of order $2700$ is determined up to isomorphism by one partition of each exponent, the parts giving the orders of its cyclic primary factors [@DF04].
The exponent $2$ has the $2$ partitions $(2),(1,1)$, and the exponent $3$ has the $3$ partitions $(3),(2,1),(1,1,1)$.
The number of groups is therefore $2\cdot3\cdot2=12$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a) and step [](#s2){.pf-ref} answers part (b).

:::

:::

:::
