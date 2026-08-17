---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-BV4
kind: problem
title: 'Bounded variation of a point-mass function with absolutely summable weights'
classification:
  areas:
  - real-analysis
  topics:
  - variation
  - series-of-numbers
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2020, 6a) Let $\{a_n\}_{n=1}^{\infty}\subseteq\mathbb R$ and a strictly increasing sequence $\{x_n\}_{n=1}^{\infty}\subseteq(0,1)$ be given.
Assume that $\sum_{n=1}^{\infty}a_n$ is absolutely convergent, and define $\alpha:[0,1]\to\mathbb R$ by
$$
\alpha(x):=
\begin{cases}
a_n,&x=x_n,\\
0,&\text{otherwise}.
\end{cases}
$$
Prove or disprove: $\alpha$ has bounded variation on $[0,1]$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove or disprove: $\alpha(x) = a_n$ at $x = x_n$, else $0$, has bounded variation on $[0,1]$, given $\sum|a_n| < \infty$.

<1>1. True: $\alpha \in BV[0,1]$, and $V_0^1 \alpha \le 2\sum_{n=1}^{\infty}|a_n|$.

<1>2. Fix a partition $0 = t_0 < t_1 < \cdots < t_m = 1$.
<2>1. On each open interval $(t_{j-1}, t_j)$, the function $\alpha$ is constant except at the atoms $x_n$ it contains.
Proof: $\alpha$ is $0$ except at the points $x_n$, where it takes the value $a_n$.
<2>2. Each atom $x_n$ belongs to exactly one interval $(t_{j-1}, t_j)$ or equals some $t_j$.
Proof: the $t_j$'s partition $[0,1]$; atoms are points.
<2>3. The jump across $x_n$ contributes at most $2|a_n|$ to $\sum_j|\alpha(t_j) - \alpha(t_{j-1})|$.
Proof: as the partition sum passes over $x_n$, $\alpha$ changes from its value just left of $x_n$ (either $0$ or $a_m$ for the preceding atom) to $a_n$ and then to its value just right; the two adjacent differences involving $x_n$ are each bounded by $|a_n|$ plus the neighboring atom's contribution, and over the whole sum each atom appears in at most two adjacent differences, contributing $\le 2|a_n|$ in total.
<2>4. $\sum_{j=1}^m|\alpha(t_j) - \alpha(t_{j-1})| \le 2\sum_{n}|a_n|$.
Proof: <2>2 and <2>3: the total variation of the partition is the sum of the jumps at the atoms it crosses, each bounded by $2|a_n|$.

<1>3. $V_0^1 \alpha = \sup_{\text{partitions}} \sum_j|\alpha(t_j) - \alpha(t_{j-1})| \le 2\sum_n|a_n| < \infty$.
Proof: <1>2<2>4 bounds every partition sum by $2\sum|a_n|$, which is finite by hypothesis.

<1>4. Q.E.D. Proof: <1>3 shows $\alpha$ has finite total variation, so $\alpha \in BV[0,1]$.
(The factor $2$ is loose but harmless.)
:::
