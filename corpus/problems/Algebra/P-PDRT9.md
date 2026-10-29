---
schema: qual/card@1
id: P-PDRT9
kind: problem
title: Intermediate fields of a Galois extension with group $\ZZ_{42}$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Cyclic Groups
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Let $L/K$ be a finite Galois extension with
$$\Gal(L/K)\cong C_{42}.$$
List the proper nontrivial intermediate fields and their degrees over $K$.
:::

::: {.solution}

::: pf

::: {.pf-step #correspondence}
An intermediate field $E$ with $K\subsetneq E\subsetneq L$ corresponds to a proper nontrivial subgroup $H\le C_{42}$, namely $H=\Gal(L/E)$, and $[E:K]=[C_{42}:H]=42/\abs{H}$.

::: pf-proof
This is the fundamental theorem of Galois theory: $E\mapsto\Gal(L/E)$ is an inclusion-reversing bijection from intermediate fields to subgroups, and $[L:E]=\abs{\Gal(L/E)}$, so $[E:K]=[L:K]/[L:E]=42/\abs{H}$.
:::

:::

::: {.pf-step #subgroups}
$C_{42}$ has exactly one subgroup of each order $d\mid 42$, and the proper nontrivial orders are $d=2,3,6,7,14,21$.

::: pf-proof
A cyclic group of order $n$ has exactly one subgroup of order $d$ for each divisor $d$ of $n$. The divisors of $42=2\cdot3\cdot7$ other than $1$ and $42$ are $2,3,6,7,14,21$.
:::

:::

::: pf-step
There is $\boxed{\text{exactly one intermediate field of each degree } 2,3,6,7,14,21}$ over $K$, and no others.

::: pf-proof
By step [](#subgroups){.pf-ref} the proper nontrivial subgroups have orders $2,3,6,7,14,21$, one of each. By step [](#correspondence){.pf-ref} their fixed fields have degrees $21,14,7,6,3,2$ over $K$, one of each.
:::

:::

:::

:::
