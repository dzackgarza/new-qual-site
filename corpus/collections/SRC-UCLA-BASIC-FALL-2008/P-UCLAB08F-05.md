---
schema: qual/card@1
id: P-UCLAB08F-05
kind: problem
title: Rearrange the alternating harmonic series to converge to pi
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
A rearrangement of a series $\sum_{n=1}^\infty a_n$ is a series $\sum_{k=1}^\infty a_{n(k)}$, where $n\colon\NN\to\NN$ is a bijection.
Show that there is a rearrangement of
$$
\sum_{n=1}^\infty \frac{(-1)^n}{n}
$$
which converges to $\pi$.
:::

::: {.solution}

Write the positive terms as
$$
p_k=\frac1{2k}
$$
and the negative terms as
$$
q_k=-\frac1{2k-1}.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
\sum_{k=1}^{\infty}p_k=+\infty
\qquad\text{and}\qquad
\sum_{k=1}^{\infty}q_k=-\infty.
$$


::: pf-proof

For the positive terms,
$$
\sum_{k=1}^{\infty}p_k
=
\frac12\sum_{k=1}^{\infty}\frac1k
=+\infty.
$$
For the negative terms,
$$
-q_k=\frac1{2k-1}\ge\frac1{2k},
$$
so
$$
\sum_{k=1}^{\infty}(-q_k)=+\infty.
$$
Hence the negative subseries diverges to $-\infty$.

:::

:::

::: pf-step

Construct a rearrangement by taking unused positive terms in order until the partial sum first exceeds $\pi$, then unused negative terms in order until it first falls below $\pi$, and repeat indefinitely.


::: pf-proof

Step [](#s1-1){.pf-ref} guarantees that each positive block and each negative block terminates after finitely many terms. Within each sign, terms are used in their original order and never repeated.

:::

:::

::: {.pf-step #s1-3}

Every original term appears exactly once in the rearrangement.


::: pf-proof

Every positive block contains at least one new positive term, because it begins with the partial sum below $\pi$. Hence after $m$ positive blocks at least the first $m$ positive terms have been used, so every $p_k$ eventually occurs.

Likewise, every negative block contains at least one new negative term, so every $q_k$ eventually occurs. No term is repeated by construction. Therefore the ordering defines a bijection
$$
n:\NN\to\NN.
$$

:::

:::

::: pf-step

The overshoot above $\pi$ after a positive block tends to $0$, and the undershoot below $\pi$ after a negative block tends to $0$.


::: pf-proof

At the end of a positive block, if the last term added is $p_k$, then the preceding partial sum was at most $\pi$, so
$$
0<S-\pi\le p_k.
$$
As the blocks proceed, the indices $k$ tend to infinity by step [](#s1-3){.pf-ref}, and therefore $p_k\to0$.

Similarly, if a negative block ends with $q_k$, then
$$
0<\pi-S\le -q_k,
$$
and $q_k\to0$.

:::

:::

::: {.pf-step #s1-5}

The rearranged series converges to
$$
\boxed{\pi}.
$$


::: pf-proof

Fix $\varepsilon>0$. Choose $K$ such that
$$
p_k<\varepsilon
\qquad\text{and}\qquad
-q_k<\varepsilon
$$
for all $k\ge K$. By step [](#s1-3){.pf-ref}, eventually every newly used term has index at least $K$ within its positive or negative subsequence.

From that point onward, every endpoint of a positive block lies in
$$
(\pi,\pi+\varepsilon),
$$
and every endpoint of a negative block lies in
$$
(\pi-\varepsilon,\pi).
$$
Within a positive block the partial sums increase between these two bounds; within a negative block they decrease between them. Hence every sufficiently late partial sum lies in
$$
(\pi-\varepsilon,\pi+\varepsilon).
$$
Thus the rearranged series converges to $\pi$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives a rearrangement, and step [](#s1-5){.pf-ref} proves that its sum is $\pi$.

:::

:::

:::
