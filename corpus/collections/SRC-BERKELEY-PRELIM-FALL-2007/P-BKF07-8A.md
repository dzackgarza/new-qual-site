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

<1>1. One has
$$
c_n\longrightarrow\infty.
$$

::: {.proof}
Since $b_n\to\infty$ and $n\to\infty$, their product $nb_n\to\infty$.
Taking positive square roots gives the claim.
:::

<1>2. There exists a strictly increasing sequence of indices
$$
n_1<n_2<\cdots
$$
such that for every $k\ge2$,
$$
c_{n_k}\ge\sum_{j=1}^{k-1}c_{n_j}.
$$

::: {.proof}
Choose $n_1$ arbitrarily.
Suppose $n_1<\cdots<n_{k-1}$ have been chosen.
The finite number
$$
\sum_{j=1}^{k-1}c_{n_j}
$$
is fixed, while $c_n\to\infty$ by step <1>1. Hence some $n_k>n_{k-1}$ satisfies the required inequality.
:::

<1>3. Define
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

::: {.proof}
For $k=1$ the inequality is immediate.
If $k\ge2$, step <1>2 gives
$$
\sum_{j=1}^{k}c_{n_j}
=
\sum_{j=1}^{k-1}c_{n_j}+c_{n_k}
\le
2c_{n_k}.
$$
:::

<1>4. The Cesàro means of $(a_n)$ converge to zero:
$$
\boxed{
\frac{a_1+\cdots+a_n}{n}\longrightarrow0
}.
$$

::: {.proof}
If $n_k\le n<n_{k+1}$, then by step <1>3,
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

<1>5. Along the indices $n_k$,
$$
\frac{a_{n_k}}{b_{n_k}}
=
\sqrt{\frac{n_k}{b_{n_k}}}
\longrightarrow\infty.
$$

::: {.proof}
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

<1>6. Therefore
$$
\boxed{
\limsup_{n\to\infty}\frac{a_n}{b_n}=\infty
}.
$$

::: {.proof}
Step <1>5 shows that the ratio tends to infinity along the subsequence $n=n_k$.
Hence its limsup is infinite.
:::

<1>7. Q.E.D.

::: {.proof}
The sequence constructed in step <1>3 satisfies both required properties by steps <1>4 and <1>6.
:::
:::
