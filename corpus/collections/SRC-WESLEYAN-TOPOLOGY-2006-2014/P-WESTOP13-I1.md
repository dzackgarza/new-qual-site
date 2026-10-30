---
schema: qual/card@1
id: P-WESTOP13-I1
kind: problem
title: Topological properties of a countable product of a disconnected subspace of $\RR$
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let $\omega$ be the cardinality of the natural numbers and let
$$
U=[-2,0)\cup[1,2]\subset\RR
$$
with the subspace topology. For the product space $U^\omega$, determine which of the following properties hold, giving a reason for each:

1. connected;
2. path-connected;
3. compact;
4. Hausdorff;
5. first countable;
6. metrizable;
7. completely regular;
8. normal.
:::

::: {.solution}

Write a point of $U^\omega$ as
$$
x=(x_1,x_2,\ldots).
$$

::: pf

::: {.pf-step #s1-1}

The space $U^\omega$ is not connected.


::: pf-proof

The subset
$$
[-2,0)
$$
is both open and closed in $U$: its complement in $U$ is $[1,2]$, and the gap $(0,1)$ separates the two pieces in the subspace topology. Therefore
$$
C=\{x\in U^\omega:x_1\in[-2,0)\}
$$
is a nonempty proper clopen subset of $U^\omega$, being the inverse image of $[-2,0)$ under the first-coordinate projection. Hence $U^\omega$ is disconnected.

:::

:::

::: {.pf-step #s1-2}

The space $U^\omega$ is not path-connected.


::: pf-proof

Every path-connected space is connected. Step [](#s1-1){.pf-ref} shows that $U^\omega$ is not connected, so it cannot be path-connected.

:::

:::

::: {.pf-step #s1-3}

The space $U^\omega$ is not compact.


::: pf-proof

The coordinate projection
$$
\pi_1:U^\omega\to U
$$
is continuous and surjective. If $U^\omega$ were compact, then its continuous image $U$ would be compact.

But $U$ is not compact. Indeed, the sequence
$$
-\frac1n\in[-2,0)\subset U
$$
has no convergent subsequence in $U$: its only possible limit in $\RR$ is $0$, and $0\notin U$. Since $U$ is metrizable, sequential compactness is equivalent to compactness, so $U$ is not compact. Therefore $U^\omega$ cannot be compact.

:::

:::

::: {.pf-step #s1-4}

Define
$$
d(x,y)
\coloneqq
\sum_{n=1}^{\infty}
2^{-n}\min\{1,\abs{x_n-y_n}\}.
$$
Then $d$ is a metric on $U^\omega$ that induces the product topology.


::: pf-proof

Each summand is nonnegative and bounded by $2^{-n}$, so the series converges. The triangle inequality follows termwise from the metric
$$
(s,t)\longmapsto\min\{1,\abs{s-t}\}
$$
on $U$. Also $d(x,y)=0$ implies $x_n=y_n$ for every $n$, so $x=y$.

To compare topologies, first let
$$
V=V_1\times\cdots\times V_N\times U\times U\times\cdots
$$
be a basic product neighborhood of $x$, with each $V_j$ open in $U$ and $x_j\in V_j$. Choose $\varepsilon_j>0$ such that
$$
B_U(x_j,\varepsilon_j)\subseteq V_j
$$
for $1\le j\le N$. Taking
$$
\delta<\min_{1\le j\le N}2^{-j}\min\{1,\varepsilon_j\}
$$
gives
$$
B_d(x,\delta)\subseteq V.
$$

Conversely, given $\varepsilon>0$, choose $N$ so large that
$$
\sum_{n>N}2^{-n}<\frac\varepsilon2.
$$
Choose $0<\eta\le1$ so small that
$$
\sum_{n=1}^N2^{-n}\eta<\frac\varepsilon2.
$$
Then the basic product neighborhood
$$
\prod_{n=1}^N B_U(x_n,\eta)\times\prod_{n>N}U
$$
is contained in $B_d(x,\varepsilon)$. Thus the metric and product topologies coincide.

:::

:::

::: {.pf-step #s1-5}

The space $U^\omega$ is Hausdorff, first countable, metrizable, completely regular, and normal.


::: pf-proof

Metrizability follows from step [](#s1-4){.pf-ref}. Every metric space is Hausdorff and first countable; metric balls of radii $1/m$ give a countable neighborhood basis at each point. Every metric space is also completely regular and normal by the standard metric-space separation theorems.

:::

:::

::: {.pf-step #s1-6}

Therefore the answers are
$$
\boxed{
\begin{array}{c|c}
\text{property}&\text{holds?}\\ \hline
\text{connected}&\text{no}\\
\text{path-connected}&\text{no}\\
\text{compact}&\text{no}\\
\text{Hausdorff}&\text{yes}\\
\text{first countable}&\text{yes}\\
\text{metrizable}&\text{yes}\\
\text{completely regular}&\text{yes}\\
\text{normal}&\text{yes}
\end{array}}
$$


::: pf-proof

This is the combination of steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives all eight requested determinations.

:::

:::

:::
