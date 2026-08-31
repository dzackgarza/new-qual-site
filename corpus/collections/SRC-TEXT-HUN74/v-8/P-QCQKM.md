---
schema: qual/card@1
id: P-QCQKM
kind: problem
title: Hungerford 5.8.3
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $\phi$ be the Euler function.

1. $\phi(n)$ is even for $n>2$.

2. find all $n>0$ such that $\phi(n)=2$.
:::

::: {.solution}
<1>1. Part 1: Proof that $\phi(n)$ is even for all $n > 2$:
<2>1. Let $S = \{k \in \{1, 2, \ldots, n\} \mid \gcd(k, n) = 1\}$. By definition, $|S| = \phi(n)$.
::: {.proof}
definition of Euler’s totient function.
:::
<2>2. For any $k \in S$, we have $\gcd(n - k, n) = \gcd(k, n) = 1$, so $n - k \in S$.
::: {.proof}
properties of the Euclidean greatest common divisor.
:::
<2>3. A fixed point of the pairing $k \mapsto n - k$ satisfies $k = n - k \implies 2k = n \implies k = n/2$.
If $k = n/2 \in S$, then $\gcd(n/2, n) = n/2 = 1 \implies n = 2$.
Since $n > 2$, $k \neq n - k$ for all $k \in S$.
::: {.proof}
$n > 2 \implies n/2 > 1$.
:::
<2>4. Thus the map $k \mapsto n - k$ partitions $S$ into disjoint pairs $\{k, n - k\}$ of distinct elements.
Therefore $|S| = \phi(n)$ is a sum of 2s, hence is an even integer.
::: {.proof}
partition into 2-element equivalence classes.
:::

<1>2. Part 2: Determination of all $n > 0$ such that $\phi(n) = 2$:
<2>1. Let $n = 2^k p_1^{e_1} \cdots p_r^{e_r}$ be the prime factorization of $n$, where $p_i$ are distinct odd primes.
Then:
\[
\phi(n) = \phi(2^k) \prod_{i=1}^r p_i^{e_i - 1}(p_i - 1) = 2.
\]
::: {.proof}
multiplicativity of Euler’s totient function.
:::
<2>2. For each odd prime $p_i \mid n$, $(p_i - 1)$ divides $\phi(n) = 2$.
Thus $p_i - 1 \in \{1, 2\}$, which gives $p_i = 3$ as the only candidate odd prime factor.
::: {.proof}
$p_i - 1 \mid 2$ and $p_i > 2$.
:::
<2>3. - **Case 1: $n$ has an odd prime factor (so $p = 3$).**
  If $e_1 \ge 2$, then $3^{e_1 - 1}(3 - 1) \ge 3 \cdot 2 = 6 > 2$, so $e_1 = 1$.
  Then $\phi(n) = \phi(2^k) \cdot \phi(3) = \phi(2^k) \cdot 2 = 2 \implies \phi(2^k) = 1$.
  This gives $2^k \in \{1, 2\}$, yielding $n = 1 \cdot 3 = 3$ and $n = 2 \cdot 3 = 6$.
  Checking: $\phi(3) = 2$ and $\phi(6) = 2$.
- **Case 2: $n$ has no odd prime factors ($n = 2^k$).**
  Then $\phi(n) = \phi(2^k) = 2^{k-1} = 2 \implies k - 1 = 1 \implies k = 2$, yielding $n = 2^2 = 4$.
  Checking: $\phi(4) = 2$.
::: {.proof}
exhaustive case analysis.
:::

<1>3. Conclusion:
$\phi(n)$ is even for all $n > 2$, and the solutions to $\phi(n) = 2$ are precisely $n \in \{3, 4, 6\}$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
