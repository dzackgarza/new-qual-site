---
schema: qual/card@1
id: P-2WRUJ
kind: problem
title: The identity $\sum_{m=k}^n\binom{m}{k}=\binom{n+1}{k+1}$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Combinatorics
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $k$ be a nonnegative integer.
Prove by mathematical induction that for all $n \geq k$ we have $$\sum_{m=k}^{n} \binom{m}{k} = \binom{n+1}{k+1}.$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/grad_prelim_Fall07.pdf` and no solutions sheet accompanies it, so the induction below is the card's own. The statement asks for a proof by induction and the proof is one; the only identity used besides the induction hypothesis is Pascal's rule, which is verified here from the factorial formula rather than quoted.

Throughout $k$ is a fixed nonnegative integer, $\binom{m}{k}\coloneqq\dfrac{m!}{k!\,(m-k)!}$ for $0\leq k\leq m$, and $P(n)$ denotes the assertion $\sum_{m=k}^{n}\binom{m}{k}=\binom{n+1}{k+1}$ for $n\geq k$.

::: pf

::: {.pf-step #pascal}
For integers $0\leq s\leq r$ one has $\binom{r+1}{s+1}=\binom{r}{s}+\binom{r}{s+1}$.

::: pf-proof
By the factorial formula,
$$
\binom{r}{s}+\binom{r}{s+1}=\frac{r!}{s!\,(r-s)!}+\frac{r!}{(s+1)!\,(r-s-1)!}
=\frac{r!\,(s+1)+r!\,(r-s)}{(s+1)!\,(r-s)!},
$$
putting the two fractions over the common denominator $(s+1)!\,(r-s)!$; the numerator is $r!\,(r+1)$ and so the sum equals $\dfrac{(r+1)!}{(s+1)!\,((r+1)-(s+1))!}=\binom{r+1}{s+1}$.
:::

:::

::: {.pf-step #base}
$P(k)$ holds.

::: pf-proof
The sum $\sum_{m=k}^{k}\binom{m}{k}$ has the single term $\binom{k}{k}=1$, and $\binom{k+1}{k+1}=1$ as well.
:::

:::

::: {.pf-step #step}
For every $n\geq k$, $P(n)$ implies $P(n+1)$.

::: pf-proof
Assume $P(n)$ and split the sum at $n$:
$$
\sum_{m=k}^{n+1}\binom{m}{k}=\sum_{m=k}^{n}\binom{m}{k}+\binom{n+1}{k}=\binom{n+1}{k+1}+\binom{n+1}{k},
$$
the second equality by the induction hypothesis. Step [](#pascal){.pf-ref} with $r=n+1$ and $s=k$ applies because $k\leq n+1$, and gives $\binom{n+1}{k+1}+\binom{n+1}{k}=\binom{n+2}{k+1}$, which is $P(n+1)$.
:::

:::

::: pf-step
Therefore $\sum_{m=k}^{n}\binom{m}{k}=\binom{n+1}{k+1}$ for every $n\geq k$.

::: pf-proof
$P(k)$ holds by step [](#base){.pf-ref}, and step [](#step){.pf-ref} carries $P(n)$ to $P(n+1)$ for every $n\geq k$; by the principle of induction, $P(n)$ holds for all integers $n\geq k$.
:::

:::

:::

:::
