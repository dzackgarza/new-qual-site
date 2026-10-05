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
<1>1. For each $n\in\mathbb N$, let $f_n\colon\mathbb N\to\mathbb R$ satisfy $|f_n(m)|\le 1$ for all $m,n\in\mathbb N$.
Prove that there is an infinite subsequence of distinct positive integers $(n_i)$ such that, for each $m\in\mathbb N$, the sequence $f_{n_i}(m)$ converges.

<1>2. For $(n_i)$ as in <1>1, assume in addition that
\[
\lim_{m\to\infty}\lim_{i\to\infty} f_{n_i}(m)=0.
\]
Prove or disprove that the reverse iterated limit
\[
\lim_{i\to\infty}\lim_{m\to\infty} f_{n_i}(m)
\]
also exists and equals $0$.
:::

::: {.solution}
<1>1. There is an infinite set
\[
N_1\subseteq\mathbb N
\]
such that the sequence
\[
(f_n(1))_{n\in N_1}
\]
converges.

::: {.proof}
The real sequence
\[
(f_n(1))_{n\ge1}
\]
is bounded by $1$. By the Bolzano--Weierstrass theorem, it has a convergent subsequence. Let $N_1$ be the infinite set of indices of that subsequence.
:::

<1>2. Inductively, for each $m\ge1$, there is an infinite set
\[
N_{m+1}\subseteq N_m
\]
such that
\[
(f_n(m+1))_{n\in N_{m+1}}
\]
converges.

::: {.proof}
Suppose $N_m$ has already been chosen. The sequence
\[
(f_n(m+1))_{n\in N_m}
\]
is again bounded by $1$, so Bolzano--Weierstrass supplies an infinite subsequence on which it converges. Let $N_{m+1}$ be its index set.
:::

<1>3. There is a strictly increasing sequence of positive integers $(n_i)$ such that
\[
n_i\in N_i
\]
for every $i$.

::: {.proof}
Because
\[
N_{i+1}\subseteq N_i
\]
and every $N_i$ is infinite, choose $n_1\in N_1$, and after $n_i$ is chosen select
\[
n_{i+1}\in N_{i+1}
\]
with
\[
n_{i+1}>n_i.
\]
This gives a strictly increasing sequence of distinct positive integers with
\[
n_i\in N_i.
\]
:::

<1>4. For each fixed $m\in\mathbb N$, the sequence
\[
f_{n_i}(m)
\]
converges as $i\to\infty$.

::: {.proof}
Fix $m$. For every $i\ge m$,
\[
n_i\in N_i\subseteq N_m.
\]
Hence the tail
\[
(f_{n_i}(m))_{i\ge m}
\]
is a subsequence of the convergent sequence
\[
(f_n(m))_{n\in N_m}
\]
constructed at stage $m$. Therefore it converges.
:::

<1>5. This proves part <1>1.

::: {.proof}
The strictly increasing sequence $(n_i)$ from step <1>3 is infinite and consists of distinct positive integers, and step <1>4 gives convergence at every fixed $m$.
:::

<1>6. The assertion in part <1>2 is false in general.

::: {.proof}
Define
\[
f_n(m)=
\begin{cases}
0,&m<n,\\
1,&m\ge n.
\end{cases}
\]
Then
\[
|f_n(m)|\le1
\]
for all $m,n$. Take
\[
n_i=i.
\]
For each fixed $m$, one has
\[
f_i(m)=0
\]
for all $i>m$, so
\[
\lim_{i\to\infty}f_i(m)=0.
\]
Therefore
\[
\lim_{m\to\infty}\lim_{i\to\infty}f_i(m)
=
\lim_{m\to\infty}0
=0.
\]

On the other hand, for each fixed $i$,
\[
f_i(m)=1
\]
for all $m\ge i$, so
\[
\lim_{m\to\infty}f_i(m)=1.
\]
Hence
\[
\lim_{i\to\infty}\lim_{m\to\infty}f_i(m)
=
\lim_{i\to\infty}1
=
1.
\]
Thus the reverse iterated limit exists but is not equal to $0$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>5 proves part <1>1, and step <1>6 disproves the assertion in part <1>2.
:::
:::
