---
schema: qual/card@1
id: P-TRIV-PR31
kind: problem
title: Sample size for testing coin-matching probability $2/3$ against $1/2$
classification:
  areas: [prelim]
  topics:
  - Hypothesis Testing
  - Sample Size
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
One may naively argue that in one toss of two coins the probability to have two heads or tails equals $2 / 3$ . Indeed, if we use the scheme with three elementary events (it fell two heads, or two tails, or one head and one tail), the probability that the coins fall equally may seem to be $2 / 3$ . The correct scheme, however, must contain four different events (head-head, tail-tail, head-tail, tail-head) with the probabilities equally distributed among them, and it gives the correct answer $1 / 2$ An experiment can be conducted to overcome the doubts about which scheme is more reasonable.
Let the first hypothesis claim that the correct value is $2 / 3$ and the second - that it is $1 / 2$ . Find how many coins tosses one should make to eliminate the first hypothesis with type I error 0.05 (probability to reject the second hypothesis when it is true) and type II error 0.05 (probability to accept the first hypothesis when it is false).
:::

::: {.solution}

Let $X$ be the number of matching outcomes (HH or TT) in $n$ independent trials. Test
$$
H_0:p=\frac12
\qquad\text{against}\qquad
H_1:p=\frac23.
$$
Because larger values of $X$ favor $H_1$, use a threshold rule: accept $H_1$ when $X\geq c$ and accept $H_0$ when $X<c$.

::: pf

::: {.pf-step #s1-1}

For fixed $n,c$, the two error probabilities are
$$
\alpha_{n,c}=P_{1/2}(X\geq c)
=2^{-n}\sum_{k=c}^{n}\binom nk
$$
and
$$
\beta_{n,c}=P_{2/3}(X<c)
=\sum_{k=0}^{c-1}\binom nk
\left(\frac23\right)^k
\left(\frac13\right)^{n-k}.
$$


::: pf-proof

Under either hypothesis, $X$ is binomial with parameters $n$ and the corresponding matching probability. The first error rejects $H_0$ when it is true, hence is the upper tail under $p=1/2$. The second accepts $H_0$ when $H_1$ is true, hence is the lower tail under $p=2/3$.

:::

:::

::: pf-step

The likelihood ratio is strictly increasing in $X$.


::: pf-proof

For an observation $X=k$,
$$
\frac{P_{2/3}(X=k)}{P_{1/2}(X=k)}
=\frac{(2/3)^k(1/3)^{n-k}}{(1/2)^n}
=\left(\frac23\right)^n2^k.
$$
Thus larger $k$ gives a larger likelihood ratio, so a threshold test is the likelihood-ratio form and no non-threshold rule can improve the tradeoff between the two simple hypotheses.

:::

:::

::: {.pf-step #s1-3}

For $n=98$ and $c=58$,
$$
\alpha_{98,58}\approx0.0427053<0.05,
\qquad
\beta_{98,58}\approx0.0484000<0.05.
$$


::: pf-proof

Substitution in the exact binomial sums of step [](#s1-1){.pf-ref} gives
$$
2^{-98}\sum_{k=58}^{98}\binom{98}{k}
\approx0.0427053
$$
and
$$
\sum_{k=0}^{57}\binom{98}{k}
\left(\frac23\right)^k
\left(\frac13\right)^{98-k}
\approx0.0484000.
$$

:::

:::

::: {.pf-step #s1-4}

No $n\leq97$ admits an integer threshold $c$ for which both error probabilities are at most $0.05$.


::: pf-proof

For each fixed $n$, $\alpha_{n,c}$ decreases as $c$ increases, while $\beta_{n,c}$ increases. Hence it suffices to take the smallest $c$ for which $\alpha_{n,c}\leq0.05$ and check whether its $\beta_{n,c}$ is also at most $0.05$. Exact evaluation of the finite binomial sums in step [](#s1-1){.pf-ref} for $1\leq n\leq97$ shows that none satisfies the second inequality. At $n=98$, step [](#s1-3){.pf-ref} gives the first feasible threshold, $c=58$.

:::

:::

::: {.pf-step #s1-5}

Therefore the minimum required number of two-coin trials is
$$
\boxed{n=98},
$$
with the decision rule
$$
\boxed{X\geq58\Rightarrow p=2/3,
\qquad X\leq57\Rightarrow p=1/2.}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} proves feasibility at $n=98$, and step [](#s1-4){.pf-ref} proves minimality.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the smallest sample size and an exact test meeting both requested error bounds.

:::

:::

:::
