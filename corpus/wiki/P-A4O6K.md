---
schema: qual/card@1
id: P-A4O6K
kind: problem
title: "Suppose $\\{a_n\\}$ is a sequence of positive real"
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - sequences-of-numbers
relations: []
review: draft
solved: true
---

::: problem
Suppose $\{a_n\}$ is a sequence of positive real numbers such that $\lim_{n\to\infty}a_n=0$ and $\sum a_n$ diverges.
Prove that for all $x>0$ there exist integers $n(1)<n(2)<\ldots$ such that $\sum_{k=1}^\infty a_{n(k)}=x$.\

> (Note: Many variations on this problem are possible including more general rearrangements.
> You may also wish to show that if $\sum a_n$ converges conditionally then given any $x\in\mathbb{R}$ there is a rearrangement of $\{b_n\}$ of $\{a_n\}$ such that $\sum b_n=r$.
> See Rudin Thm.
> 3.54 for a further generalization.)
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Construction: fix $x > 0$; define $n(1)$ as the smallest index with $a_{n(1)} \le x$, and inductively $n(k)$ as the smallest index $> n(k-1)$ with $a_{n(k)} \le x - \sum_{j<k}a_{n(j)}$ (stop if the sum equals $x$). Proof: such indices exist at every step: if no index $\ge n(k-1) + 1$ had $a_n \le x - s_{k-1} > 0$, then all remaining terms would be $> x - s_{k-1} > 0$, contradicting $a_n \to 0$.

<1>2. The partial sums $s_k = \sum_{j \le k}a_{n(j)}$ are nondecreasing and bounded above by $x$.
Proof: each added term satisfies $a_{n(k)} \le x - s_{k-1}$, so $s_k \le x$; hence $s_k \uparrow s^* \le x$.

<1>3. $s^* = x$.
Proof: suppose $s^* < x$; let $\eta = x - s^* > 0$.
Since $a_n \to 0$, eventually $a_n < \eta$; and since $s_k \to s^*$, eventually $x - s_{k-1} > x - s^* = \eta$... more precisely $x - s_{k-1} \ge \eta/2 > \eta/2$ for $k$ large.
Then every term $a_n$ beyond that point satisfies $a_n < \eta/2 \le x - s_{k-1}$, so the greedy construction adds all remaining terms: $s_k = s_N + \sum_{n=N}^{n(k)}a_n \to \infty$ (as $\sum a_n$ diverges), contradicting $s_k \le x$.
Hence $s^* = x$.

<1>4. Q.E.D. Proof: <1>2 and <1>3 give $\sum_{k=1}^\infty a_{n(k)} = x$.
:::
