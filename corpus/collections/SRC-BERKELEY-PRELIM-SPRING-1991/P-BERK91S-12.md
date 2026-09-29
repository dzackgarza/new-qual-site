---
schema: qual/card@1
id: P-BERK91S-12
kind: problem
title: Kempner's series over integers whose decimal expansion avoids the digit nine
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared the positive-integer domain, excluded decimal digit, and reciprocal series with Problem 12 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $A$ be the set of positive integers whose decimal expansions do not contain the digit $9$. Prove that
$$
\sum_{a\in A}\frac1a<\infty.
$$
:::

::: {.solution}
For each integer $k\ge1$, let
$$
A_k\coloneqq\{a\in A:10^{k-1}\le a<10^k\}.
$$
Thus $A_k$ consists of the members of $A$ with exactly $k$
decimal digits, and $A$ is the disjoint union of these sets.

::: pf

::: {.pf-step #s1}

For every $k\ge1$, the set $A_k$ has $8\cdot9^{k-1}$ elements.

::: pf-proof

The leading digit has eight choices, namely $1,\ldots,8$.
Each of the remaining $k-1$ digits has nine choices, namely
$0,\ldots,8$. Every such digit string represents exactly one
member of $A_k$, so multiplying the numbers of choices gives
$\#A_k=8\cdot9^{k-1}$.

:::

:::

::: {.pf-step #s2}

For every $k\ge1$,
$$
\sum_{a\in A_k}\frac1a\le8\left(\frac9{10}\right)^{k-1}.
$$

::: pf-proof

Each $a\in A_k$ satisfies $a\ge10^{k-1}$, and therefore
$1/a\le10^{-(k-1)}$. Step [](#s1){.pf-ref} bounds the sum by
$$
\frac{\#A_k}{10^{k-1}}
=8\left(\frac9{10}\right)^{k-1}.
$$

:::

:::

::: {.pf-step #s3}

The partial sums of $\sum_{a\in A}1/a$ are bounded by $80$.

::: pf-proof

For any positive integer $M$, choose $N\ge1$ such that $M<10^N$.
Every member of $A$ not exceeding $M$ lies in
$A_1\cup\cdots\cup A_N$. Since all summands are nonnegative,
step [](#s2){.pf-ref} gives
$$
\sum_{\substack{a\in A\\a\le M}}\frac1a
\le\sum_{k=1}^{N}\sum_{a\in A_k}\frac1a
\le8\sum_{k=1}^{N}\left(\frac9{10}\right)^{k-1}
=80\left(1-\left(\frac9{10}\right)^N\right)
<80.
$$

:::

:::

::: pf-qed

The partial sums in step [](#s3){.pf-ref} are nondecreasing because all
summands are positive. Being bounded above, they converge to
a finite limit. Hence $\sum_{a\in A}1/a\le80<\infty$.

:::

:::

:::
