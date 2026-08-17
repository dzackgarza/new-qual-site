---
schema: qual/card@1
id: P-RA-WORKSHOP-D3-SEQ-10
kind: problem
title: 'Select a subseries summing to any positive target from a divergent positive series'
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - sequences-of-numbers
relations: []
review: draft
---

::: {.problem title="?"}
(January 2011 #5) Suppose $\{a_n\}$ is a sequence of positive real numbers such that $\lim_{n\to\infty}a_n=0$ and $\sum a_n$ diverges.
Prove that for all $x>0$ there exist integers $n(1)<n(2)<\cdots$ such that
$$
\sum_{k=1}^{\infty}a_{n(k)}=x.
$$
(Note: Many variations on this problem are possible including more general rearrangements.
You may also wish to show that if $\sum a_n$ converges conditionally then given any $x\in\mathbb R$ there is a rearrangement of $\{b_n\}$ of $\{a_n\}$ such that $\sum b_n=r$.
See Rudin Thm.
3.54 for a further generalization.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Greedy selection.
    Proof: fix $x > 0$. Since $\sum a_n$ diverges, its partial sums are unbounded, so there is a first index $n(1)$ with $\sum_{k=1}^{n(1)} a_k \ge x$; set $s(1) = \sum_{k=1}^{n(1)} a_k$. The overshoot is at most $a_{n(1)}$:
    \[0 \le s(1) - x \le a_{n(1)},\]
    because $s(1) - a_{n(1)} < x \le s(1)$.
<1>2. Iterate.
    Proof: define $s(0) = 0$ and, given $s(j)$ with $0 \le s(j) - x \le a_{n(j)}$, note that $\sum_{k > n(j)} a_k = \infty$ (a divergent series minus a finite initial part), so there is a first index $n(j+1) > n(j)$ with
    \[s(j) + \sum_{k=n(j)+1}^{n(j+1)} a_k \ge x.\]
    Set $s(j+1) = s(j) + \sum_{k=n(j)+1}^{n(j+1)} a_k$; then $0 \le s(j+1) - x \le a_{n(j+1)}$ by the same overshoot argument. This produces increasing indices $n(1) < n(2) < \cdots$.
<1>3. The selected subseries sums to $x$.
    Proof: by construction $0 \le s(j) - x \le a_{n(j)}$ for all $j$. Since $a_n \to 0$, the increments $a_{n(j)} \to 0$, so $s(j) - x \to 0$, i.e. $\sum_k a_{n(k)} = \lim_j s(j) = x$. (The infinite sum equals $\lim_j s(j)$ because each partial sum of the subseries is eventually between $s(j)$ and $s(j+1)$.)
<1>4. Q.E.D.
:::
