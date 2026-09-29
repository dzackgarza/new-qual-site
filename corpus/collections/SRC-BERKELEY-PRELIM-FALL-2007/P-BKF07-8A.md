---
schema: qual/card@1
id: P-BKF07-8A
kind: problem
title: Vanishing Cesàro means with $\limsup a_n/b_n=\infty$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the sparse-spike construction. The proof below
    chooses each new spike to dominate the total of all previous spikes,
    yielding a direct Cesaro estimate without first replacing b_n by a
    running maximum.
---

::: {.problem}
Suppose \((b_n)_{n\ge1}\) is a sequence of positive real numbers with
\[
b_n\to\infty,
\qquad
\frac{b_n}{n}\to0.
\]
Must there exist a sequence \((a_n)_{n\ge1}\) such that
\[
\frac{a_1+\cdots+a_n}{n}\to0
\]
and
\[
\limsup_{n\to\infty}\frac{a_n}{b_n}=\infty?
\]
Give a proof or counterexample.
:::

::: {.solution}

Yes.

For each $n\ge1$, set
$$
c_n=\sqrt{n b_n}.
$$

::: pf

::: {.pf-step #cn-to-infinity}
One has
$$
c_n\longrightarrow\infty.
$$

::: pf-proof
Since $b_n\to\infty$ and $n\to\infty$, their product $nb_n\to\infty$.
Taking positive square roots gives the claim.
:::

:::

::: {.pf-step #nk-selection}
There exists a strictly increasing sequence of indices
$$
n_1<n_2<\cdots
$$
such that for every $k\ge2$,
$$
c_{n_k}\ge\sum_{j=1}^{k-1}c_{n_j}.
$$

::: pf-proof
Choose $n_1$ arbitrarily.
Suppose $n_1<\cdots<n_{k-1}$ have been chosen.
The finite number
$$
\sum_{j=1}^{k-1}c_{n_j}
$$
is fixed, while $c_n\to\infty$ by step [](#cn-to-infinity){.pf-ref}. Hence some $n_k>n_{k-1}$ satisfies the required inequality.
:::

:::

::: {.pf-step #partial-sum-bound}
Define
$$
a_n=
\begin{cases}
c_{n_k},&n=n_k\text{ for some }k,\\
0,&\text{otherwise}.
\end{cases}
$$
Then, for every $k$,
$$
\sum_{j=1}^{k}c_{n_j}\le2c_{n_k}.
$$

::: pf-proof
For $k=1$ the inequality is immediate.
If $k\ge2$, step [](#nk-selection){.pf-ref} gives
$$
\sum_{j=1}^{k}c_{n_j}
=
\sum_{j=1}^{k-1}c_{n_j}+c_{n_k}
\le
2c_{n_k}.
$$
:::

:::

::: {.pf-step #cesaro-zero}
The Cesàro means of $(a_n)$ converge to zero:
$$
\boxed{
\frac{a_1+\cdots+a_n}{n}\longrightarrow0
}.
$$

::: pf-proof
If $n_k\le n<n_{k+1}$, then by step [](#partial-sum-bound){.pf-ref},
$$
\begin{aligned}
0
\le
\frac{a_1+\cdots+a_n}{n}
&=
\frac{\sum_{j=1}^{k}c_{n_j}}{n}
\\
&\le
\frac{2c_{n_k}}{n_k}
\\
&=
2\sqrt{\frac{b_{n_k}}{n_k}}.
\end{aligned}
$$
Since $b_n/n\to0$, the right-hand side tends to zero as $k\to\infty$.
Also $k\to\infty$ whenever $n\to\infty$, so the Cesàro means tend to zero.
:::

:::

::: {.pf-step #ratio-along-nk}
Along the indices $n_k$,
$$
\frac{a_{n_k}}{b_{n_k}}
=
\sqrt{\frac{n_k}{b_{n_k}}}
\longrightarrow\infty.
$$

::: pf-proof
By definition,
$$
a_{n_k}=c_{n_k}=\sqrt{n_kb_{n_k}},
$$
which gives the displayed ratio.
Since
$$
\frac{b_{n_k}}{n_k}\longrightarrow0
$$
and all terms are positive, its reciprocal square root tends to $\infty$.
:::

:::

::: {.pf-step #limsup-infinity}
Therefore
$$
\boxed{
\limsup_{n\to\infty}\frac{a_n}{b_n}=\infty
}.
$$

::: pf-proof
Step [](#ratio-along-nk){.pf-ref} shows that the ratio tends to infinity along the subsequence $n=n_k$.
Hence its limsup is infinite.
:::

:::

::: pf-qed
The sequence constructed in step [](#partial-sum-bound){.pf-ref} satisfies both required properties by steps [](#cesaro-zero){.pf-ref} and [](#limsup-infinity){.pf-ref}.
:::

:::

:::
