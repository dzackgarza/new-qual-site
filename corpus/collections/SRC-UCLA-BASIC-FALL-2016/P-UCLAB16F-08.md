---
schema: qual/card@1
id: P-UCLAB16F-08
kind: problem
title: Diagonal subsequences and interchange of double limits
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
(i) For each $n \in \NN$ let $f_n : \NN \to \RR$ be a function with $\abs{f_n(m)} \leq 1$ for all $m, n \in \NN$. Prove that there is an infinite subsequence of distinct positive integers $n_i$, such that for each $m \in \NN$, $f_{n_i}(m)$ converges.

(ii) For $n_i$ as in (i), assume that in addition $\lim_{m \to \infty} \lim_{i \to \infty} f_{n_i}(m)$ exists and equals $0$. Prove or disprove: The same holds for the reverse double limit $\lim_{i \to \infty} \lim_{m \to \infty} f_{n_i}(m)$.
:::

::: {.solution}

::: pf

::: pf-step

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

The values satisfy
$$
\abs{f_n(1)}\le1.
$$
Thus the sequence is bounded in $\RR$.
By Bolzano--Weierstrass, it has a convergent subsequence.
Let $N_1$ be its infinite index set.

:::

:::

::: pf-step

Inductively, for every $m\ge1$, there is an infinite set
$$
N_{m+1}\subseteq N_m
$$
such that
$$
(f_n(m+1))_{n\in N_{m+1}}
$$
converges.


::: pf-proof

Suppose $N_m$ has been chosen.
The sequence
$$
(f_n(m+1))_{n\in N_m}
$$
is bounded by $1$ in absolute value.
Bolzano--Weierstrass gives an infinite convergent subsequence.
Take $N_{m+1}$ to be its index set.

:::

:::

::: {.pf-step #s1-3}

There is a strictly increasing sequence of positive integers
$$
n_1<n_2<\cdots
$$
with
$$
n_i\in N_i
$$
for every $i$.


::: pf-proof

Choose any
$$
n_1\in N_1.
$$
After choosing $n_i$, the set $N_{i+1}$ is infinite, so choose
$$
n_{i+1}\in N_{i+1}
$$
with
$$
n_{i+1}>n_i.
$$

:::

:::

::: {.pf-step #s1-4}

For every fixed $m\in\NN$,
$$
f_{n_i}(m)
$$
converges as $i\to\infty$.


::: pf-proof

If $i\ge m$, then
$$
n_i\in N_i\subseteq N_m
$$
because the sets are nested.
Hence the tail
$$
(f_{n_i}(m))_{i\ge m}
$$
is a subsequence of the convergent sequence
$$
(f_n(m))_{n\in N_m}.
$$
Therefore it converges.

:::

:::

::: {.pf-step #s1-5}

This proves part (i).


::: pf-proof

The indices $n_i$ are distinct by step [](#s1-3){.pf-ref}, and step [](#s1-4){.pf-ref} gives convergence for every fixed $m$.

:::

:::

::: {.pf-step #s1-6}

The assertion in part (ii) is false.


::: pf-proof

Define
$$
f_n(m)
=
\begin{cases}
0,&m<n,\\
1,&m\ge n.
\end{cases}
$$
Then
$$
\abs{f_n(m)}\le1.
$$
Take
$$
n_i=i.
$$

For fixed $m$, once $i>m$ one has
$$
f_i(m)=0.
$$
Thus
$$
\lim_{i\to\infty}f_i(m)=0
$$
for every $m$, and consequently
$$
\lim_{m\to\infty}
\lim_{i\to\infty}
f_i(m)
=0.
$$

On the other hand, for fixed $i$, one has
$$
f_i(m)=1
$$
for all $m\ge i$.
Hence
$$
\lim_{m\to\infty}f_i(m)=1,
$$
so
$$
\lim_{i\to\infty}
\lim_{m\to\infty}
f_i(m)
=1.
$$
Thus the reverse iterated limit exists but is not equal to $0$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (i), and step [](#s1-6){.pf-ref} disproves the assertion in part (ii).

:::

:::

:::
