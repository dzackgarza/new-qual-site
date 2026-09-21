---
schema: qual/card@1
id: P-BKF78-2
kind: problem
title: Uniformly convergent subsequence of indefinite integrals
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Each indefinite integral G_n is uniformly bounded by 1 and is
    1-Lipschitz, since |G_n(x)-G_n(y)| is at most the length |x-y|.
    Thus {G_n} is a uniformly bounded equicontinuous family in C([0,1]),
    so Arzela--Ascoli yields a uniformly convergent subsequence.
---

::: {.problem}
Let $\{g_n\}$ be a sequence of Riemann-integrable functions from $[0,1]$ to $\mathbb R$ such that
\[
|g_n(x)|\le 1
\]
for every $n$ and $x$.
Define
\[
G_n(x)=\int_0^x g_n(t)\,dt.
\]
Prove that a subsequence of $\{G_n\}$ converges uniformly.
:::

::: {.solution}
<1>1. For every $n$ and every $x\in[0,1]$,
$$
\abs{G_n(x)}\le1.
$$

::: {.proof}
Using $\abs{g_n(t)}\le1$,
$$
\abs{G_n(x)}
=
\abs{\int_0^x g_n(t)\,dt}
\le
\int_0^x\abs{g_n(t)}\,dt
\le
x
\le
1.
$$
:::

<1>2. For every $n$ and every $x,y\in[0,1]$,
$$
\abs{G_n(x)-G_n(y)}
\le
\abs{x-y}.
$$

::: {.proof}
Assume first that $x\ge y$. Then
$$
G_n(x)-G_n(y)
=
\int_y^x g_n(t)\,dt,
$$
so
$$
\abs{G_n(x)-G_n(y)}
\le
\int_y^x\abs{g_n(t)}\,dt
\le
x-y.
$$
The case $y\ge x$ is identical after interchanging $x$ and $y$.
:::

<1>3. The family $\{G_n\}$ is uniformly bounded and equicontinuous
in $C([0,1])$.

::: {.proof}
Uniform boundedness is step <1>1. Step <1>2 shows that every $G_n$
is $1$-Lipschitz, so for every $\varepsilon>0$, choosing
$\delta=\varepsilon$ gives
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{G_n(x)-G_n(y)}<\varepsilon
$$
simultaneously for all $n$. Thus the family is equicontinuous.
The same Lipschitz estimate also shows that every $G_n$ is
continuous.
:::

<1>4. Some subsequence of $\{G_n\}$ converges uniformly on
$[0,1]$.

::: {.proof}
The interval $[0,1]$ is compact. By step <1>3, the sequence lies in
a uniformly bounded equicontinuous family of continuous functions.
The Arzelà--Ascoli theorem therefore supplies a subsequence
$\{G_{n_j}\}$ that converges uniformly on $[0,1]$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
