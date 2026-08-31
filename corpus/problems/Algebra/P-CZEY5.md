---
schema: qual/card@1
id: P-CZEY5
kind: problem
title: The integers $n$ with $\phi(n)=2$ are $3,4,6$
classification:
  areas:
  - algebra
  topics:
  - Number Theory
  - Cyclic Groups
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Suppose $\phi(n) = 2$.
:::

::: {.solution}
**Theorem.** If $\phi(n)=2$, then $n\in\{3,4,6\}$.

::: {.proof}

1. Let $n=\prod_{i=1}^r p_i^{\alpha_i}$ be the prime factorization. Then
   \[
   \phi(n)=\prod_{i=1}^r \phi(p_i^{\alpha_i})=2,\qquad
   \phi(p_i^{\alpha_i})=p_i^{\alpha_i-1}(p_i-1)\in\mathbb Z_{>0}.
   \]
2. Every factor $p_i^{\alpha_i-1}(p_i-1)$ equals $1$ or $2$, and exactly one factor equals $2$.
3. If one factor equals $2$ for an odd prime $p_i$, then $\alpha_i=1$ and $p_i-1=2$, so $p_i=3$.
4. If one factor equals $2$ for $p_i=2$, then $2^{\alpha_i-1}(2-1)=2$, hence $\alpha_i=2$ so $2^2\mid n$.
5. Any remaining factors equal $1$, so $\phi(p_i^{\alpha_i})=1$. This forces $p_i=2$ and $\alpha_i=1$.
6. Therefore
   - $n=3$ if the factor $2$ comes from $3$ and no extra $2$-factor appears;
   - $n=4$ if it comes from $2^2$;
   - $n=6$ if both $3$ and one factor of $2$ appear.
   No other primes can appear because they would contribute a factor $>2$.
7. Conversely, $\phi(3)=\phi(4)=\phi(6)=2$.

So the only integers with $\phi(n)=2$ are exactly $3,4,6$.
:::
:::
