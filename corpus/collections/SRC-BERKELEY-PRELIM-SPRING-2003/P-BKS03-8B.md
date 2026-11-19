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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Transcribed from the retained solution sheet — Berkeley preliminary examination, Spring
    2003, solutions, assets/attachments/s03solution.pdf, Problem 8B on PDF p. 6 — and
    restructured into steps; the card's prose was that sheet's argument. Checked step by step:
    the Chinese remainder decomposition, the reduction to elements of order dividing 3 in the
    cyclic group (Z/pZ)^*, and the count gcd(3,p-1); the sheet's phrasing 'the number of
    solutions to x^3 - 1 in Z/pZ' was read as the number of solutions of x^3 = 1, which is what
    the card states. The six values multiply to 9.
---

::: {.problem}
Let $N=30030$, the product of the first six primes.
How many integers $0\le x<N$ satisfy
$$
N\mid x^3-1?
$$
:::

::: {.solution}
The argument is the retained solution sheet's: **Berkeley preliminary examination, Spring 2003, solutions** (`assets/attachments/s03solution.pdf`), Problem 8B, PDF p. 6. Throughout $N = 30030 = 2\cdot3\cdot5\cdot7\cdot11\cdot13$ and $\mathcal{P} \coloneqq \theset{2,3,5,7,11,13}$.

::: pf

::: {.pf-step #crt}
$x^{3} \equiv 1 \pmod N$ holds exactly when $x^{3} \equiv 1 \pmod p$ for every $p \in \mathcal{P}$, and the number of solutions is $\prod_{p \in \mathcal{P}} n_{p}$, where $n_{p}$ is the number of solutions modulo $p$.

::: pf-proof
The Chinese remainder theorem identifies $\ZZ/N\ZZ$ with the product of the rings $\ZZ/p\ZZ$, $p \in \mathcal{P}$, through $x \mapsto (x \bmod p)_{p}$; an element is $1$ in the product exactly when each component is $1$, and a product of finite sets has as many elements as the product of their cardinalities.

:::

:::

::: {.pf-step #nonzero}
For a prime $p$ the solutions of $x^{3} = 1$ in $\ZZ/p\ZZ$ are the elements of the multiplicative group $(\ZZ/p\ZZ)^{\times}$ whose order divides $3$.

::: pf-proof
$0^{3} = 0 \ne 1$, so every solution is a unit; in the group of units $x^{3} = 1$ says exactly that the order of $x$ divides $3$.

:::

:::

::: {.pf-step #cyclic}
$n_{p} = \gcd(3, p-1)$, that is $3$ when $3$ divides $p-1$ and $1$ otherwise.

::: pf-proof
$(\ZZ/p\ZZ)^{\times}$ is cyclic of order $p-1$. In a cyclic group of order $m$ the elements whose order divides $3$ are the powers $g^{k}$ with $3k \equiv 0 \pmod m$, and there are exactly $\gcd(3,m)$ such $k$ modulo $m$.

:::

:::

::: {.pf-step #table}
$n_{2} = 1$, $n_{3} = 1$, $n_{5} = 1$, $n_{7} = 3$, $n_{11} = 1$, $n_{13} = 3$.

::: pf-proof
Apply step [](#cyclic){.pf-ref} to $p-1 = 1, 2, 4, 6, 10, 12$: the values of $\gcd(3,p-1)$ are $1, 1, 1, 3, 1, 3$ respectively, and $n_{p} = 1$ also covers $p = 3$, where $p - 1 = 2$ is not divisible by $3$.

:::

:::

::: pf-step
The number of integers $0 \le x < N$ with $N \mid x^{3}-1$ is $\boxed{9}$.

::: pf-proof
Step [](#crt){.pf-ref} turns the count into the product over $\mathcal{P}$, and step [](#table){.pf-ref} evaluates it: $1 \cdot 1 \cdot 1 \cdot 3 \cdot 1 \cdot 3 = 9$.

:::

:::

:::
:::
