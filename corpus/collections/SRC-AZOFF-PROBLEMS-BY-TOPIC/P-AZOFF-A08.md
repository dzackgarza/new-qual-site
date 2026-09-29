---
schema: qual/card@1
id: P-AZOFF-A08
kind: problem
title: Dini's theorem for decreasing sequences on $[0,1]$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 8, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For each epsilon, used the increasing open sets where f_n is below
    epsilon. Pointwise convergence makes them cover [0,1], compactness reduces
    to finitely many, and monotonicity replaces that finite subcover by one
    index N. All later f_n are then uniformly below epsilon. The source
    compilation contains no worked solution for this problem.
---

::: {.problem}
Suppose $(f_n)_{n\in\mathbb N}$ is a sequence of continuous functions $f_n:[0,1]\to\mathbb R$ satisfying
\[
f_n(x)\ge f_{n+1}(x)\ge0
\]
for all $n$ and $x$.
Prove that if $f_n\to0$ pointwise on $[0,1]$, then the convergence is uniform.
:::

::: {.solution}
Fix $\varepsilon>0$ and, for each $n$, define
$$
U_n=\{x\in[0,1]:f_n(x)<\varepsilon\}.
$$

::: pf

::: {.pf-step #s1}

Each $U_n$ is open in $[0,1]$, and
$$
U_n\subseteq U_{n+1}.
$$

::: pf-proof

Since $f_n$ is continuous,
$$
U_n=f_n^{-1}((-\infty,\varepsilon))
$$
is open in the subspace topology on $[0,1]$.

If $x\in U_n$, then
$$
f_{n+1}(x)\leq f_n(x)<\varepsilon,
$$
so $x\in U_{n+1}$. Hence the family is increasing.

:::

:::

::: {.pf-step #s2}

The sets $U_n$ cover $[0,1]$.

::: pf-proof

Fix $x\in[0,1]$. Since
$$
f_n(x)\longrightarrow0
$$
pointwise, there is an index $n$ such that
$$
f_n(x)<\varepsilon.
$$
Thus $x\in U_n$. Since $x$ was arbitrary,
$$
[0,1]=\bigcup_n U_n.
$$

:::

:::

::: {.pf-step #s3}

There is an index $N$ such that
$$
U_N=[0,1].
$$

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the sets $U_n$ form an open cover of the compact
interval $[0,1]$. Choose a finite subcover
$$
U_{n_1},\ldots,U_{n_r}.
$$
Let
$$
N=\max\{n_1,\ldots,n_r\}.
$$
Since the family is increasing by step [](#s1){.pf-ref},
$$
U_{n_j}\subseteq U_N
$$
for every $j$. Therefore
$$
[0,1]
=
\bigcup_{j=1}^r U_{n_j}
\subseteq
U_N
\subseteq
[0,1],
$$
so $U_N=[0,1]$.

:::

:::

::: {.pf-step #s4}

For every $n\geq N$ and every $x\in[0,1]$,
$$
\abs{f_n(x)}<\varepsilon.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives
$$
f_N(x)<\varepsilon
$$
for every $x\in[0,1]$. The hypotheses also give
$$
0\leq f_n(x)\leq f_N(x)
$$
whenever $n\geq N$. Hence
$$
\abs{f_n(x)}
=
f_n(x)
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s5}

The sequence $f_n$ converges uniformly to $0$ on $[0,1]$.

::: pf-proof

For each $\varepsilon>0$, step [](#s4){.pf-ref} supplies an index $N$ independent of
$x$ such that
$$
n\geq N
\quad\Longrightarrow\quad
\abs{f_n(x)-0}<\varepsilon
$$
for every $x\in[0,1]$. This is uniform convergence.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
