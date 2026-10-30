---
schema: qual/card@1
id: P-UCLAB09F-01
kind: problem
title: Pointwise subsequences and iterated limits
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2009.
---
::: {.problem}

::: pf

::: {.pf-step #p1-s1}

For each $n\in\NN$, let $f_n\colon\NN\to\RR$ satisfy $\abs{f_n(m)}\le 1$ for all $m,n\in\NN$.
Prove that there is an infinite subsequence of distinct positive integers $(n_i)$ such that, for each $m\in\NN$, the sequence $f_{n_i}(m)$ converges.

:::

::: pf-step

For $(n_i)$ as in step [](#p1-s1){.pf-ref}, assume in addition that

:::

:::

$$
\lim_{m\to\infty}\lim_{i\to\infty} f_{n_i}(m)=0.
$$
Prove or disprove that the reverse iterated limit
$$
\lim_{i\to\infty}\lim_{m\to\infty} f_{n_i}(m)
$$
also exists and equals $0$.
:::

::: {.solution}

::: pf

::: {.pf-step #p2-s1}

There is an infinite set
$$
N_1\subseteq\NN
$$
such that the sequence
$$
(f_n(1))_{n\in N_1}
$$
converges.

::: pf-proof

The real sequence
$$
(f_n(1))_{n\ge1}
$$
is bounded by $1$. By the Bolzano--Weierstrass theorem, it has a convergent subsequence. Let $N_1$ be the infinite set of indices of that subsequence.

:::

:::

::: {.pf-step #p2-s2}

Inductively, for each $m\ge1$, there is an infinite set
$$
N_{m+1}\subseteq N_m
$$
such that
$$
(f_n(m+1))_{n\in N_{m+1}}
$$
converges.

::: pf-proof

Suppose $N_m$ has already been chosen. The sequence
$$
(f_n(m+1))_{n\in N_m}
$$
is again bounded by $1$, so Bolzano--Weierstrass supplies an infinite subsequence on which it converges. Let $N_{m+1}$ be its index set.

:::

:::

::: {.pf-step #p2-s3}

There is a strictly increasing sequence of positive integers $(n_i)$ such that
$$
n_i\in N_i
$$
for every $i$.

::: pf-proof

Because
$$
N_{i+1}\subseteq N_i
$$
and every $N_i$ is infinite, choose $n_1\in N_1$, and after $n_i$ is chosen select
$$
n_{i+1}\in N_{i+1}
$$
with
$$
n_{i+1}>n_i.
$$
This gives a strictly increasing sequence of distinct positive integers with
$$
n_i\in N_i.
$$

:::

:::

::: {.pf-step #p2-s4}

For each fixed $m\in\NN$, the sequence
$$
f_{n_i}(m)
$$
converges as $i\to\infty$.

::: pf-proof

Fix $m$. For every $i\ge m$,
$$
n_i\in N_i\subseteq N_m.
$$
Hence the tail
$$
(f_{n_i}(m))_{i\ge m}
$$
is a subsequence of the convergent sequence
$$
(f_n(m))_{n\in N_m}
$$
constructed at stage $m$. Therefore it converges.

:::

:::

::: {.pf-step #p2-s5}

This proves part step [](#p2-s1){.pf-ref}.

::: pf-proof

The strictly increasing sequence $(n_i)$ from step [](#p2-s3){.pf-ref} is infinite and consists of distinct positive integers, and step [](#p2-s4){.pf-ref} gives convergence at every fixed $m$.

:::

:::

::: {.pf-step #p2-s6}

The assertion in part step [](#p2-s2){.pf-ref} is false in general.

::: pf-proof

Define
$$
f_n(m)=
\begin{cases}
0,&m<n,\\
1,&m\ge n.
\end{cases}
$$
Then
$$
\abs{f_n(m)}\le1
$$
for all $m,n$. Take
$$
n_i=i.
$$
For each fixed $m$, one has
$$
f_i(m)=0
$$
for all $i>m$, so
$$
\lim_{i\to\infty}f_i(m)=0.
$$
Therefore
$$
\lim_{m\to\infty}\lim_{i\to\infty}f_i(m)
=
\lim_{m\to\infty}0
=0.
$$

On the other hand, for each fixed $i$,
$$
f_i(m)=1
$$
for all $m\ge i$, so
$$
\lim_{m\to\infty}f_i(m)=1.
$$
Hence
$$
\lim_{i\to\infty}\lim_{m\to\infty}f_i(m)
=
\lim_{i\to\infty}1
=
1.
$$
Thus the reverse iterated limit exists but is not equal to $0$.

:::

:::

::: pf-qed

Step [](#p2-s5){.pf-ref} proves part step [](#p2-s1){.pf-ref}, and step [](#p2-s6){.pf-ref} disproves the assertion in part step [](#p2-s2){.pf-ref}.

:::

:::

:::
