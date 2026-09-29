---
schema: qual/card@1
id: P-BKF08-8B
kind: problem
title: Asymptotic number of throws of an $N$-sided die needed to see a marked side with probability $1/2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the strict logarithmic threshold, the least-integer rounding
    bound, and the squeeze estimate for -N log(1-1/N).
---

::: {.problem}
We have a fair $N$-sided die.
One side is black and all the others are white.
Let $n(N)$ be the smallest number of throws for which the probability of getting at least one black result is greater than $1/2$.
Compute
$$
\lim_{N\to\infty}\frac{n(N)}N.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

After $m$ throws, the probability of seeing at least one black
result is
$$
1-\left(1-\frac1N\right)^m.
$$

::: pf-proof

Each throw is white with probability $1-1/N$. Independence gives
probability $(1-1/N)^m$ that all $m$ throws are white. Taking the
complement gives the displayed probability.

:::

:::

::: {.pf-step #s2}

For $N>1$, put
$$
a_N\coloneqq
\frac{\log2}{-\log(1-1/N)}.
$$
Then $n(N)$ is the least integer strictly larger than $a_N$, and hence
$$
0<n(N)-a_N\le1.
$$

::: pf-proof

By step [](#s1){.pf-ref}, the required probability exceeds $1/2$ exactly when
$$
\left(1-\frac1N\right)^m<\frac12.
$$
Taking logarithms gives
$$
m\log\left(1-\frac1N\right)<-\log2.
$$
Since $\log(1-1/N)<0$, division reverses the inequality and yields
$$
m>a_N.
$$
Thus $n(N)=\lfloor a_N\rfloor+1$, which gives the stated bound even when
$a_N$ is an integer.

:::

:::

::: {.pf-step #s3}

One has
$$
N\left[-\log\left(1-\frac1N\right)\right]\longrightarrow1.
$$

::: pf-proof

For $0<x<1$,
$$
x\le-\log(1-x)\le\frac{x}{1-x}.
$$
Indeed,
$$
-\log(1-x)=\int_0^x\frac{dt}{1-t},
$$
and on $0\le t\le x$ the integrand lies between $1$ and
$1/(1-x)$. Taking $x=1/N$ gives
$$
1
\le
N\left[-\log\left(1-\frac1N\right)\right]
\le
\frac{N}{N-1}.
$$
The squeeze theorem proves the claim.

:::

:::

::: {.pf-step #s4}

The logarithmic threshold satisfies
$$
\frac{a_N}{N}\longrightarrow\log2.
$$

::: pf-proof

By definition,
$$
\frac{a_N}{N}
=\frac{\log2}
{N[-\log(1-1/N)]}.
$$
The denominator tends to $1$ by step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
\lim_{N\to\infty}\frac{n(N)}N=\log2
}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
0<\frac{n(N)}N-\frac{a_N}{N}\le\frac1N.
$$
The right-hand side tends to $0$, while step [](#s4){.pf-ref} gives
$a_N/N\to\log2$. Hence $n(N)/N\to\log2$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the requested limit.

:::

:::

:::
