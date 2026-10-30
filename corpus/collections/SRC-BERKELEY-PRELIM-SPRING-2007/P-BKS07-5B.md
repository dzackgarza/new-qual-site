---
schema: qual/card@1
id: P-BKS07-5B
kind: problem
title: The center of $\operatorname{SL}_n(\FF_q)$ is trivial if and only if $\gcd(n,q-1)=1$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
---

::: {.problem}
Let $\FF_{q}$ denote the finite field with $q$ elements, where $q$ is a power of a prime.
Let $\SL_{n}(\FF_{q})$ be the group of $n \times n$ matrices with entries in $\FF_{q}$ and determinant $1$, under matrix multiplication.
Determine (with proof) a simple necessary and sufficient condition on $n$ and $q$ for the center of $\SL_{n}(\FF_{q})$ to be trivial.
:::

::: {.solution}

The center is trivial if and only if $\gcd(n,q-1)=1$.

::: pf

::: {.pf-step #s1}

The center of $\SL_n(\FF_q)$ is the set of scalar matrices $xI$ with $x^n=1$.

::: pf-proof

Scalar matrices are central, and $\det(xI)=x^n$. Conversely, let $A$ be central and let $E_{ij}$ be the matrix unit. For $i\ne j$, $I+E_{ij}\in\SL_n(\FF_q)$, so $A$ commutes with $E_{ij}$. Comparing entries of $E_{ij}A$ and $AE_{ij}$ shows that the only nonzero entry of row $j$ of $A$ is $A_{jj}$, the only nonzero entry of column $i$ is $A_{ii}$, and $A_{ii}=A_{jj}$. Taking all pairs $i\ne j$ shows $A=xI$. For $n=1$, the group is trivial and the claim holds.

:::

:::

::: {.pf-step #s2}

The equation $x^n=1$ has exactly $\gcd(n,q-1)$ solutions in $\FF_q$.

::: pf-proof

The group $\FF_q^\times$ is cyclic of order $q-1$, and a cyclic group of order $m$ has exactly $\gcd(n,m)$ elements whose order divides $n$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the center has $\gcd(n,q-1)$ elements, so it is trivial exactly when $\gcd(n,q-1)=1$.

:::

:::

:::
