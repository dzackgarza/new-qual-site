---
schema: qual/card@1
id: P-BKS03-8B
kind: problem
title: Counting cube roots of $1$ modulo $30030$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $N=30030$, the product of the first six primes.
How many integers $0\le x<N$ satisfy
\[
N\mid x^3-1?
\]
:::

::: {.solution}
We want the number of solutions to $x^3=1$ in the ring $\ZZ/N\ZZ$. By the Chinese remainder theorem, $\ZZ/N\ZZ$ is isomorphic as a ring to $\prod_{p\in\{2,3,5,7,11,13\}}\ZZ/p\ZZ$. Thus the answer is $\prod_{p\in\{2,3,5,7,11,13\}}n_p$, where $n_p$ is the number of solutions to $x^3=1$ in $\ZZ/p\ZZ$. Now $n_p$ is the number of elements of order dividing $3$ in the multiplicative group $(\ZZ/p\ZZ)^*$. Since $(\ZZ/p\ZZ)^*$ is cyclic of order $p-1$, we have $n_p=3$ if $3$ divides $p-1$, and $n_p=1$ otherwise.
Thus the answer is

$$
n_2n_3n_5n_7n_{11}n_{13}=1\cdot1\cdot1\cdot3\cdot1\cdot3=9.
$$
:::
