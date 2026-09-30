---
schema: qual/card@1
id: E-ALTNF
kind: problem
title: Comparing five topologies on the real line
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the following topologies on $\mathbb{R}$:

$\mathcal{T}_1$ = the standard topology,

$\mathcal{T}_2$ = the topology of $\mathbb{R}_K$,

$\mathcal{T}_3$ = the finite complement topology,

$\mathcal{T}_4$ = the upper limit topology, having all sets $(a, b]$ as basis,

$\mathcal{T}_5$ = the topology having all sets $(-\infty, a) = \theset{x \mid x < a}$ as basis.

Determine, for each of these topologies, which of the others it contains.
:::

::: {.solution}
Write $K=\{1/n : n\in\mathbb Z_+\}$, so that $\mathcal T_2$ has basis the open intervals $(a,b)$ and the sets $(a,b)\setminus K$.

::: pf

::: {.pf-step #s1}

$\mathcal T_3\subseteq\mathcal T_1$ and $\mathcal T_5\subseteq\mathcal T_1$.

::: pf-proof

A nonempty $\mathcal T_3$-open set is $\mathbb R\setminus\{x_1,\ldots,x_k\}=\bigcap_i(\mathbb R\setminus\{x_i\})$, a finite intersection of standard open sets.
A basis element of $\mathcal T_5$ is $(-\infty,a)=\bigcup_{n\ge1}(a-n,a)$.

:::

:::

::: {.pf-step #s2}

$\mathcal T_1\subseteq\mathcal T_2\subseteq\mathcal T_4$.

::: pf-proof

The basis of $\mathcal T_2$ contains every open interval, so $\mathcal T_1\subseteq\mathcal T_2$.
Each $(a,b)=\bigcup_{n}(a,b-1/n]$ is $\mathcal T_4$-open.
For $(a,b)\setminus K$, let $x$ be a point of it.
If $x\le0$, then $(a,x]\subseteq(a,b)\setminus K$.
If $x>1$, then $(\max(a,1),x]\subseteq(a,b)\setminus K$.
If $0<x<1$, choose $n$ with $\frac1{n+1}<x<\frac1n$; then $(\max(a,\frac1{n+1}),x]\subseteq(a,b)\setminus K$.
So $(a,b)\setminus K$ is $\mathcal T_4$-open, and $\mathcal T_2\subseteq\mathcal T_4$.

:::

:::

::: {.pf-step #s3}

$\mathcal T_3$ and $\mathcal T_5$ are incomparable.

::: pf-proof

The ray $(-\infty,0)\in\mathcal T_5$ has infinite complement, so it is not in $\mathcal T_3$.
$\mathbb R\setminus\{0\}\in\mathcal T_3$, while every nonempty union of rays $(-\infty,a)$ is $\mathbb R$ or a ray $(-\infty,c)$, so $\mathbb R\setminus\{0\}\notin\mathcal T_5$.

:::

:::

::: {.pf-step #s4}

$\mathcal T_1\not\subseteq\mathcal T_3$, $\mathcal T_1\not\subseteq\mathcal T_5$, $\mathcal T_2\not\subseteq\mathcal T_1$, and $\mathcal T_4\not\subseteq\mathcal T_2$.

::: pf-proof

$(0,1)\in\mathcal T_1$ has infinite complement and is not a union of rays.
$(-1,1)\setminus K\in\mathcal T_2$ is not standard-open, since every interval around $0$ meets $K$.
$(0,1]\in\mathcal T_4$ is not $\mathcal T_2$-open: a basis element of $\mathcal T_2$ containing $1\in K$ is an interval $(c,d)$ with $d>1$, which is not contained in $(0,1]$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $\mathcal T_1$ contains $\mathcal T_3$ and $\mathcal T_5$; $\mathcal T_2$ contains $\mathcal T_1,\mathcal T_3,\mathcal T_5$; $\mathcal T_4$ contains $\mathcal T_1,\mathcal T_2,\mathcal T_3,\mathcal T_5$.
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $\mathcal T_3$ and $\mathcal T_5$ contain none of the others, and no further inclusion holds: $\mathcal T_2,\mathcal T_4\supseteq\mathcal T_1$ are not contained in $\mathcal T_3$ or $\mathcal T_5$, $\mathcal T_4\supseteq\mathcal T_2$ is not contained in $\mathcal T_1$, and $\mathcal T_4\not\subseteq\mathcal T_2$.

:::

:::

:::
