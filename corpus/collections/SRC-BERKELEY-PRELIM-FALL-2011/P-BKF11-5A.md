---
schema: qual/card@1
id: P-BKF11-5A
kind: problem
title: Subseries sums fill $(0,L)$ when each term is at most the tail sum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 5A of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the tail-residual invariant, convergence of the selected partial
    sums to t, and the argument that infinitely many terms are selected.
---

::: {.problem}
Suppose $a_n>0$, $\sum_{n=1}^{\infty}a_n=L<\infty$, and for every $n$,
$$
a_n\le \sum_{m=n+1}^{\infty}a_m.
$$
Show that for every $t$ with $0<t<L$ there is a subseries $\sum_{i=1}^{\infty}a_{n_i}$ whose sum is $t$.
:::

::: {.solution}
Fix $t$ with $0<t<L$. For $n\ge0$, put
$$
R_n\coloneqq\sum_{m=n+1}^{\infty}a_m.
$$
Thus $R_0=L$, $R_{n-1}=a_n+R_n$ for $n\ge1$, and the hypothesis says
$a_n\le R_n$.

::: pf

::: {.pf-step #s1}

Define recursively $s_0=0$, $r_0=t$, and, for $n\ge1$,
$$
\varepsilon_n\coloneqq
\begin{cases}
1,&r_{n-1}>R_n,\\
0,&r_{n-1}\le R_n,
\end{cases}
$$
together with
$$
s_n\coloneqq s_{n-1}+\varepsilon_n a_n,
\qquad
r_n\coloneqq t-s_n.
$$
Then
$$
0<r_n\le R_n
$$
for every $n\ge0$.

::: pf-proof

For $n=0$,
$$
0<r_0=t<L=R_0.
$$
Assume $n\ge1$ and
$$
0<r_{n-1}\le R_{n-1}=a_n+R_n.
$$

If $r_{n-1}\le R_n$, then $\varepsilon_n=0$ and
$$
r_n=r_{n-1},
$$
so $0<r_n\le R_n$.

If $r_{n-1}>R_n$, then $\varepsilon_n=1$. Since the hypothesis gives
$a_n\le R_n$, one has $r_{n-1}>a_n$, and therefore
$$
r_n=r_{n-1}-a_n>0.
$$
The upper bound in the induction hypothesis gives
$$
r_n
=r_{n-1}-a_n
\le R_{n-1}-a_n
=R_n.
$$
Thus the invariant holds in both cases, and induction proves the claim.

:::

:::

::: {.pf-step #s2}

The selected partial sums satisfy
$$
s_n\longrightarrow t.
$$

::: pf-proof

Because $\sum a_n$ converges, its tails satisfy $R_n\to0$. By
step [](#s1){.pf-ref},
$$
0<r_n=t-s_n\le R_n.
$$
Hence $r_n\to0$, so $s_n=t-r_n\to t$.

:::

:::

::: {.pf-step #s3}

The set
$$
I\coloneqq\{n\ge1:\varepsilon_n=1\}
$$
is infinite.

::: pf-proof

Suppose $I$ were finite. Then there would be $N$ such that
$\varepsilon_n=0$ for every $n>N$, so $s_n=s_N$ and
$r_n=t-s_N$ for every $n>N$. Step [](#s1){.pf-ref} gives $r_N>0$, hence this
eventual constant residual is positive. But step [](#s1){.pf-ref} also gives
$r_n\le R_n\to0$, a contradiction. Thus $I$ is infinite.

:::

:::

::: {.pf-step #s4}

If
$$
I=\{n_1<n_2<n_3<\cdots\},
$$
then
$$
\boxed{\sum_{i=1}^{\infty}a_{n_i}=t}.
$$

::: pf-proof

For every $k$,
$$
\sum_{i=1}^k a_{n_i}=s_{n_k}.
$$
Since $n_k\to\infty$, step [](#s2){.pf-ref} gives
$$
s_{n_k}\longrightarrow t.
$$
Therefore the subseries indexed by $I$ converges to $t$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} shows that the selected indices form an infinite subsequence,
and step [](#s4){.pf-ref} gives the required sum.

:::

:::

:::
