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

Question 3. Assume that $f _ { n }$ is holomorphic in $| z | < 1$ and $| f _ { n } | \leq 1 0$ . Assume also that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } \left( 2 ^ { - j } \right)$ exists for each $j = 1 , 2 , \dots$ . Prove that $\scriptstyle \operatorname* { l i m } _ { n \to \infty } f _ { n } ( z )$ exists for all z with $| z | < 1$

::: {.solution}
<1>1. $\{f_n\}$ is uniformly bounded by $10$, hence normal (Montel).
::: {.proof}
Montel's theorem.
:::

<1>2. Any subsequence has a further subsequence converging uniformly on compacta to holomorphic $f$.
::: {.proof}
<1>1.
:::

<1>3. If $f,g$ are two subsequential limits, they agree on $\{2^{-j}\}$ (by hypothesis the limits exist there and coincide).
::: {.proof}
hypothesis.
:::

<1>4. $\{2^{-j}\}$ accumulates at $0\in\mathbb{D}$, so $f=g$ by identity theorem.
::: {.proof}
<1>3.
:::

<1>5. Hence all subsequential limits coincide, so the full sequence converges pointwise (Vitali).
::: {.proof}
<1>4 (normal family with unique subsequential limit converges).
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
