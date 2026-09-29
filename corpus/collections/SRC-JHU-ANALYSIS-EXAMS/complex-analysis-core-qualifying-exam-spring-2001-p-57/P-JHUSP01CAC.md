---
schema: qual/card@1
id: P-JHUSP01CAC
kind: problem
title: Convergence on a dense subset implies pointwise convergence for bounded holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Identity Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Question 3. Assume that $f _ { n }$ is holomorphic in $| z | < 1$ and $| f _ { n } | \leq 1 0$ . Assume also that $\lim_{n\to\infty} f_n(2^{-j})$ exists for each $j = 1 , 2 , \dots$ . Prove that $\lim_{n\to\infty} f_n(z)$ exists for all z with $| z | < 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every subsequence of $(f_n)$ has a further subsequence converging uniformly on compact subsets of $\DD$ to a holomorphic function.

::: pf-proof

The family is uniformly bounded by $10$, so Montel's theorem applies.

:::

:::

::: {.pf-step #s2}

Any two such limits $f$ and $g$ are equal.

::: pf-proof

Both equal $\lim_nf_n(2^{-j})$ at each point $2^{-j}$, and these points accumulate at $0\in\DD$, so $f=g$ by the identity theorem.

:::

:::

::: pf-qed

Let $f$ be the common limit of step [](#s2){.pf-ref} and fix $z\in\DD$. If $f_n(z)\not\to f(z)$, some subsequence stays at distance at least $\eps>0$ from $f(z)$, and by step [](#s1){.pf-ref} a further subsequence converges at $z$ to $f(z)$, a contradiction. So $\lim_nf_n(z)=f(z)$ exists.

:::

:::

:::
