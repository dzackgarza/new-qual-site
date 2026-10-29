---
schema: qual/card@1
id: P-UCLAB05S-AN2
kind: problem
title: Accumulation points in the binary sequence space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 2 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $X$ be the set of all infinite sequences $(\sigma_n)_{n=1}^{\infty}$ of $0$'s and $1$'s, endowed with the metric
$$
\operatorname{dist}\bigl((\sigma_n),(\sigma_n')\bigr)
=\sum_{n=1}^{\infty}\frac{|\sigma_n-\sigma_n'|}{2^n}.
$$
Give a direct proof that every infinite subset of $X$ has an accumulation point.
:::

::: {.solution}

Let $A\subseteq X$ be infinite.

::: pf

::: {.pf-step #s1-1}

There are nested infinite subsets
$$
A=A_0\supseteq A_1\supseteq A_2\supseteq\cdots
$$
and bits $\tau_1,\tau_2,\ldots\in\{0,1\}$ such that every sequence in $A_n$ begins with
$$
\tau_1,\ldots,\tau_n.
$$


::: pf-proof

Among the elements of the infinite set $A_0=A$, infinitely many have first coordinate $0$ or infinitely many have first coordinate $1$. Choose such an infinite subfamily $A_1$ and call its common first coordinate $\tau_1$.

Inductively, suppose $A_n$ is infinite and all of its members have the same first $n$ coordinates. Partition $A_n$ according to the $(n+1)$st coordinate. One of the two parts is infinite. Choose it as $A_{n+1}$ and denote its common $(n+1)$st coordinate by $\tau_{n+1}$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
\tau\coloneqq(\tau_n)_{n=1}^{\infty}\in X.
$$
Every $\sigma\in A_n$ satisfies
$$
\operatorname{dist}(\sigma,\tau)\le2^{-n}.
$$


::: pf-proof

The first $n$ coordinates of $\sigma$ and $\tau$ agree by step [](#s1-1){.pf-ref}. Therefore
$$
\begin{aligned}
\operatorname{dist}(\sigma,\tau)
&=\sum_{k=n+1}^{\infty}\frac{|\sigma_k-\tau_k|}{2^k}\\
&\le\sum_{k=n+1}^{\infty}\frac1{2^k}\\
&=2^{-n}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The point $\tau$ is an accumulation point of $A$.


::: pf-proof

Let $\varepsilon>0$. Choose $n$ so large that $2^{-n}<\varepsilon$. By step [](#s1-2){.pf-ref}, every element of the infinite set $A_n$ lies in the open ball $B(\tau,\varepsilon)$. Hence that ball contains infinitely many points of $A$, and in particular contains a point of $A$ distinct from $\tau$. Since this holds for every $\varepsilon>0$, the point $\tau$ is an accumulation point of $A$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves that every infinite subset $A\subseteq X$ has an accumulation point.

:::

:::

:::
