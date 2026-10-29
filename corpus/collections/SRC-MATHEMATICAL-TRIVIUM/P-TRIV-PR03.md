---
schema: qual/card@1
id: P-TRIV-PR03
kind: problem
title: De Méré's dice problem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
What is more probable - to get at least one 1 in throwing four dice, or to get at least two 1 in 24 throws of two dice?
:::

::: {.solution}

Interpret the first experiment as four independent throws of one die, and the second as 24 independent throws of a pair of dice, with success in the second experiment meaning that both dice show $1$ on a throw.

::: pf

::: {.pf-step #s1-1}

The probability of at least one $1$ in four single-die throws is
$$
p_1=1-\left(\frac56\right)^4
=\frac{671}{1296}
\approx0.517747.
$$


::: pf-proof

The complementary event is that none of the four independent throws shows $1$. Each throw avoids $1$ with probability $5/6$, so the complement has probability $(5/6)^4$.

:::

:::

::: {.pf-step #s1-2}

In one throw of two dice, the probability that both show $1$ is
$$
q=\frac1{36}.
$$


::: pf-proof

There are $36$ equally likely ordered outcomes for two fair dice, and only $(1,1)$ is a success.

:::

:::

::: {.pf-step #s1-3}

The probability of at least one double-$1$ in 24 pair-throws is
$$
p_2
=1-\left(\frac{35}{36}\right)^{24}.
$$


::: pf-proof

Here the phrase ``at least two 1'' means that in at least one throw of the pair, the two dice are both $1$. By step [](#s1-2){.pf-ref}, a pair-throw fails to be double-$1$ with probability $35/36$. Independence of the 24 pair-throws gives the displayed complement probability.

:::

:::

::: {.pf-step #s1-4}

Numerically,
$$
p_2\approx0.491404<p_1.
$$


::: pf-proof

Evaluating the expression in step [](#s1-3){.pf-ref} gives approximately $0.491404$, whereas step [](#s1-1){.pf-ref} gives approximately $0.517747$.

:::

:::

::: {.pf-step #s1-5}

Therefore the more probable event is
$$
\boxed{\text{at least one } 1 \text{ in four throws of one die}.}
$$


::: pf-proof

This follows from the strict comparison in step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} answers the comparison.

:::

:::

:::
