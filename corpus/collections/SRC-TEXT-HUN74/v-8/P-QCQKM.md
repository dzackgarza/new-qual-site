---
schema: qual/card@1
id: P-QCQKM
kind: problem
title: $\phi(n)$ is even for $n>2$, and $\phi(n)=2$ exactly for $n=3,4,6$
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
<1>1. (1) For $n>2$, $\phi(n)$ is even.

::: {.proof}
Let $S = \{k \in \{1, \ldots, n\} : \gcd(k, n) = 1\}$, so $|S| = \phi(n)$. For $k\in S$, $\gcd(n - k, n) = \gcd(k, n) = 1$, so the involution $k \mapsto n - k$ maps $S$ to itself; here $k=n$ is not in $S$ because $\gcd(n,n)=n>1$. A fixed point would satisfy $n=2k$ and $\gcd(n/2,n)=n/2=1$, that is, $n=2$. Since $n>2$, the involution has no fixed points, so it partitions $S$ into two-element sets $\{k,n-k\}$ and $|S|$ is even.
:::

<1>2. (2) $\phi(n)=2$ if and only if $n\in\boxed{\{3,4,6\}}$.

<2>1. If $\phi(n)=2$, then the only possible odd prime factor of $n$ is $3$, and $9\nmid n$.

::: {.proof}
Write $n = 2^k p_1^{e_1} \cdots p_r^{e_r}$ with distinct odd primes $p_i$ and $e_i\ge1$. By multiplicativity,
$$\phi(n) = \phi(2^k) \prod_{i=1}^r p_i^{e_i - 1}(p_i - 1).$$
Each $p_i-1$ divides $\phi(n)=2$ and $p_i>2$, so $p_i=3$. If $e_1 \ge 2$, then $3^{e_1 - 1}(3 - 1) \ge 6 > 2$.
:::

<2>2. If $3\mid n$ and $\phi(n)=2$, then $n\in\{3,6\}$.

::: {.proof}
By step <2>1, $n=2^k\cdot3$, so $\phi(n) = \phi(2^k) \cdot 2$ and $\phi(2^k) = 1$. Hence $k\in\{0,1\}$ and $n\in\{3,6\}$.
:::

<2>3. If $3\nmid n$ and $\phi(n)=2$, then $n=4$.

::: {.proof}
By step <2>1, $n = 2^k$. Then $\phi(1)=1$, and for $k\ge1$, $\phi(2^k) = 2^{k-1}$, which equals $2$ only for $k=2$.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>2 and <2>3 show that $\phi(n)=2$ forces $n\in\{3,4,6\}$, and conversely $\phi(3)=\phi(4)=\phi(6)=2$.
:::
:::
