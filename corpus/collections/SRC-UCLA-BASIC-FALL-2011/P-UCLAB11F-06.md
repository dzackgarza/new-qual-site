---
schema: qual/card@1
id: P-UCLAB11F-06
kind: problem
title: Monotone pointwise convergence to zero is uniform
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 6. Let $(f_n)$ be a sequence of continuous functions on $[0,1]$.
Assume
$$
f_n(x)\ge f_{n+1}(x)\quad\text{for all }x\in[0,1],
$$
and
$$
\lim_{n\to\infty}f_n(x)=0\quad\text{for all }x\in[0,1].
$$
Prove, without merely quoting a theorem, that $f_n\to0$ uniformly on $[0,1]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $n$ and every $x\in[0,1]$,
$$
f_n(x)\ge0.
$$


::: pf-proof

For fixed $x$, the sequence
$$
f_1(x)\ge f_2(x)\ge\cdots
$$
is decreasing and converges to $0$. Every term of a decreasing sequence is at least its limit, so
$$
f_n(x)\ge0.
$$

:::

:::

::: {.pf-step #s1-2}

Fix $\varepsilon>0$ and define
$$
U_n=\{x\in[0,1]:f_n(x)<\varepsilon\}.
$$
Then each $U_n$ is open in $[0,1]$.


::: pf-proof

The function $f_n$ is continuous, and
$$
U_n=f_n^{-1}((-\infty,\varepsilon)).
$$
Thus $U_n$ is open in the subspace topology of $[0,1]$.

:::

:::

::: {.pf-step #s1-3}

The sets $U_n$ are increasing:
$$
U_n\subseteq U_{n+1}.
$$


::: pf-proof

If $x\in U_n$, then
$$
f_n(x)<\varepsilon.
$$
By the monotonicity hypothesis,
$$
f_{n+1}(x)\le f_n(x)<\varepsilon,
$$
so $x\in U_{n+1}$.

:::

:::

::: {.pf-step #s1-4}

The sets $U_n$ cover $[0,1]$:
$$
[0,1]=\bigcup_{n=1}^{\infty}U_n.
$$


::: pf-proof

Fix $x\in[0,1]$. Since
$$
f_n(x)\to0,
$$
there is $N$ such that
$$
f_N(x)<\varepsilon.
$$
Thus $x\in U_N$.

:::

:::

::: {.pf-step #s1-5}

There exists $N$ such that
$$
U_N=[0,1].
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref}, the family $(U_n)$ is an open cover of the compact interval $[0,1]$. Hence finitely many sets
$$
U_{n_1},\ldots,U_{n_r}
$$
cover $[0,1]$.
Let
$$
N=\max\{n_1,\ldots,n_r\}.
$$
By the nesting in step [](#s1-3){.pf-ref},
$$
U_{n_j}\subseteq U_N
$$
for every $j$. Therefore
$$
[0,1]
=
\bigcup_{j=1}^rU_{n_j}
\subseteq
U_N
\subseteq
[0,1],
$$
so $U_N=[0,1]$.

:::

:::

::: {.pf-step #s1-6}

For every $n\ge N$ and every $x\in[0,1]$,
$$
0\le f_n(x)<\varepsilon.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
f_N(x)<\varepsilon
$$
for every $x$. By monotonicity,
$$
f_n(x)\le f_N(x)
$$
for $n\ge N$, and step [](#s1-1){.pf-ref} gives nonnegativity.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{\norm{f_n}_\infty\to0}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} shows that for every $\varepsilon>0$, there exists $N$ such that for every $n\ge N$,
$$
\sup_{x\in[0,1]}\abs{f_n(x)}
<
\varepsilon.
$$
This is uniform convergence to zero.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
