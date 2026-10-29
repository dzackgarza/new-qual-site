---
schema: qual/card@1
id: P-A4O6K
kind: problem
title: A divergent series of positive terms with $a_n\to 0$ has a subseries summing
  to any $x>0$
classification:
  areas:
  - real-analysis
  topics:
  - Series of Numbers
  - Sequences of Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Suppose $\{a_n\}$ is a sequence of positive real numbers such that $\lim_{n\to\infty}a_n=0$ and $\sum a_n$ diverges.
Prove that for all $x>0$ there exist integers $n(1)<n(2)<\ldots$ such that $\sum_{k=1}^\infty a_{n(k)}=x$.

> (Note: Many variations on this problem are possible including more general rearrangements.
> You may also wish to show that if $\sum a_n$ converges conditionally then given any $x\in\RR$ there is a rearrangement $\{b_n\}$ of $\{a_n\}$ such that $\sum b_n=x$.
> See Rudin Thm.
> 3.54 for a further generalization.)
:::

::: {.solution}
Fix $x>0$ and set $s_0=0$, $n(0)=0$.

::: pf

::: {.pf-step #s1}

There are recursively defined indices $n(1)<n(2)<\cdots$ such that $s_k=\sum_{j=1}^{k}a_{n(j)}<x$ for every $k$.

::: pf-proof

Assume $s_{k-1}<x$ and define $n(k)$ to be the least integer $n>n(k-1)$ satisfying $a_n<x-s_{k-1}$. Such an integer exists because $a_n\to0$ and $x-s_{k-1}>0$. Positivity yields $s_{k-1}<s_k=s_{k-1}+a_{n(k)}<x$. The induction starts at $s_0=0<x$ and continues indefinitely.

:::

:::

::: {.pf-step #s2}

The sequence $(s_k)$ has a limit $s\leq x$.

::: pf-proof

By step [](#s1){.pf-ref}, the partial sums are increasing and bounded above by $x$. They therefore converge to a real number $s\leq x$.

:::

:::

::: {.pf-step #s3}

The limit from step [](#s2){.pf-ref} equals $x$.

::: pf-proof

Suppose $s<x$ and put $\eta=x-s>0$. Choose $N$ such that $a_n<\eta$ for all $n\geq N$, and choose $k_0$ with $n(k_0)\geq N$. Since $s_k\leq s$, every residual satisfies $x-s_k\geq\eta$. Consequently the least admissible index after $n(k)$ is exactly $n(k)+1$ whenever $k\geq k_0$. It follows that every index after $n(k_0)$ occurs in the selected subsequence, so
$$
s_k=s_{k_0}+\sum_{n=n(k_0)+1}^{n(k)}a_n
$$
for $k>k_0$. The right-hand side tends to $+\infty$, since the series of positive terms $\sum_n a_n$ diverges and $n(k)\to\infty$. This contradicts $s_k<x$. Hence $s=x$.

:::

:::

::: pf-step

The strictly increasing indices $n(1)<n(2)<\cdots$ of step [](#s1){.pf-ref} satisfy $\sum_{k=1}^{\infty}a_{n(k)}=x$.

::: pf-proof

The partial sums of the selected subseries are precisely $s_k$ from step [](#s1){.pf-ref}, whose limit is $x$ by step [](#s3){.pf-ref}.

:::

:::

:::

:::
