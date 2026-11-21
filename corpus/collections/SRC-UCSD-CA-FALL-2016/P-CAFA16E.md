---
schema: qual/card@1
id: P-CAFA16E
kind: problem
title: "Normal family of functions vanishing at a point has a convergent subsequence"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof. The card was an extraction artefact: each step's claim carried the
    literal marker "*Proof:*" followed by its whole argument inside the claim, so no step had a proof
    block and the argument was not separated from the assertion. Each step is now a claim plus a
    pf-proof, and the Goal paragraph was removed. The mathematics is unchanged: local boundedness, Montel
    normality, the limit mapping into the closed disc with the maximum modulus principle excluding the
    boundary because $f(a)=0$, and the conclusion. Nothing in the statement was changed.

---

::: {.problem}
Let $U \subset \CC$ be a connected open set and let $a \in U$.
Let $f_n: U \to \DD$ be a sequence of analytic functions such that $f_n(a) = 0$ for all $n \geq 1$.
Prove that there exists an analytic function $f: U \to \DD$ and a subsequence $\{f_{n_k}\}$ of $\{f_n\}$ which converges uniformly to $f$ on compact subsets of $U$.
:::

::: {.solution}

::: pf

::: pf-step
The family is locally bounded.

::: pf-proof
Each $f_n$ maps $U$ into the unit disc, so on every compact subset of $U$ the family is bounded by $1$; this is what local boundedness means.
:::

:::

::: pf-step
Montel gives a compactly convergent subsequence.

::: pf-proof
By Montel's theorem a locally bounded family of holomorphic functions on a domain is normal, so it contains a subsequence converging uniformly on every compact subset to a holomorphic limit $f$.
:::

:::

::: pf-step
The limit again maps into the disc.

::: pf-proof
Fix $z\in U$. Uniform convergence on a compact neighbourhood of $z$ gives convergence of the values, so $\abs{f(z)}=\lim_k\abs{f_{n_k}(z)}\le1$. The maximum modulus principle rules out $\abs{f(z)}=1$ at an interior point unless $f$ is constant of modulus $1$; but $f(a)=\lim_k f_{n_k}(a)=0$, so $f$ is not such a constant. Hence $\abs{f(z)}<1$ for every $z\in U$.
:::

:::

::: pf-step
Conclusion.

::: pf-proof
The subsequence $f_{n_k}$ converges uniformly on compact subsets of $U$ to the analytic function $f:U\to\DD$, which is the assertion.
:::

:::

:::

:::
