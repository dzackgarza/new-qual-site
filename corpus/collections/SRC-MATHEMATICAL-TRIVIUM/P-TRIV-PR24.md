---
schema: qual/card@1
id: P-TRIV-PR24
kind: problem
title: Normal approximation to the number of sixes in 12000 dice throws
classification:
  areas: [prelim]
  topics:
  - Central Limit Theorem
  - Normal Approximation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
The dice is thrown 12000 times.
Find the probability that the total number of 6’s lies between 1800 and 2100.
:::

::: {.solution}

Let $X$ be the number of sixes in the $12000$ independent throws. Then
$$
X\sim\operatorname{Binomial}\left(12000,\frac16\right).
$$

::: pf

::: {.pf-step #s1-1}

The mean and variance of $X$ are
$$
\mu=2000,
\qquad
\sigma^2=\frac{5000}{3},
\qquad
\sigma=\sqrt{\frac{5000}{3}}\approx40.8248.
$$


::: pf-proof

For a binomial random variable with parameters $n,p$,
$$
\mathbf EX=np,
\qquad
\mathbf DX=np(1-p).
$$
Substitute $n=12000$ and $p=1/6$.

:::

:::

::: {.pf-step #s1-2}

With the continuity correction, the event $1800\leq X\leq2100$ is approximated by
$$
1799.5<Y<2100.5,
$$
where $Y\sim N(2000,5000/3)$.


::: pf-proof

The central limit theorem approximates the binomial law by the normal law with the same mean and variance. The half-unit extension is the standard continuity correction for the inclusive integer interval.

:::

:::

::: {.pf-step #s1-3}

Standardizing gives
$$
P(1800\leq X\leq2100)
\approx
\Phi\left(\frac{100.5}{\sigma}\right)
-\Phi\left(\frac{-200.5}{\sigma}\right).
$$


::: pf-proof

Subtract the mean $2000$ from the two endpoints in step [](#s1-2){.pf-ref} and divide by the standard deviation $\sigma$ from step [](#s1-1){.pf-ref}.

:::

:::

::: pf-step

The standardized endpoints are approximately
$$
\frac{100.5}{\sigma}\approx2.4616,
\qquad
\frac{-200.5}{\sigma}\approx-4.9114.
$$


::: pf-proof

Insert $\sigma=\sqrt{5000/3}$ from step [](#s1-1){.pf-ref} and evaluate the two quotients.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
P(1800\leq X\leq2100)
\approx \Phi(2.4616)-\Phi(-4.9114)
\approx0.9931.}
$$


::: pf-proof

The lower-tail term $\Phi(-4.9114)$ is about $4.5\times10^{-7}$, while $\Phi(2.4616)$ is about $0.9931$. Substitution into step [](#s1-3){.pf-ref} gives the displayed approximation.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested normal approximation to the binomial probability.

:::

:::

:::
