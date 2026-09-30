---
schema: qual/card@1
id: E-9MCHZ
kind: problem
title: Closures and separation under five topologies on the line
classification:
  areas:
  - topology
  topics:
  - Closure
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Consider the five topologies on $\mathbb{R}$ given in Exercise 7 of §13.

(a) Determine the closure of the set $K = \theset{1/n \mid n \in \mathbb{Z}_+}$ under each of these topologies.

(b) Which of these topologies satisfy the Hausdorff axiom?
the $T_1$ axiom?
:::

::: {.solution}
The five topologies of [[E-ALTNF]] are: $\mathcal T_1$ the standard topology; $\mathcal T_2$ the topology of $\mathbb R_K$, with basis the intervals $(a,b)$ and the sets $(a,b)-K$; $\mathcal T_3$ the finite complement topology; $\mathcal T_4$ the upper limit topology, with basis the intervals $(a,b]$; and $\mathcal T_5$ the topology with basis the rays $(-\infty,a)$.

::: pf

::: {.pf-step #s1}

In $\mathcal T_1$, $\overline K=\boxed{K\cup\{0\}}$.

::: pf-proof

Every interval about $0$ contains $1/n$ for large $n$, so $0\in\overline K$.
A point $x\notin K\cup\{0\}$ has an interval about it missing $K$: take $(-\infty,0)$ if $x<0$, $(1,\infty)$ if $x>1$, and $(\frac1{n+1},\frac1n)$ if $\frac1{n+1}<x<\frac1n$.

:::

:::

::: {.pf-step #s2}

In $\mathcal T_2$, $\overline K=\boxed{K}$.

::: pf-proof

The basic set $(-1,1)-K$ contains $0$ and misses $K$.
Every other point outside $K$ has a standard open interval missing $K$, by the proof of step [](#s1){.pf-ref}.
So $\mathbb R-K$ is open.

:::

:::

::: {.pf-step #s3}

In $\mathcal T_3$, $\overline K=\boxed{\mathbb R}$.

::: pf-proof

The closed sets are $\mathbb R$ and the finite sets, and $K$ is infinite.

:::

:::

::: {.pf-step #s4}

In $\mathcal T_4$, $\overline K=\boxed{K}$.

::: pf-proof

The basic set $(-1,0]$ contains $0$ and misses $K$.
For $x<0$, $x>1$, and $\frac1{n+1}<x<\frac1n$, the basic sets $(x-1,x]$, $(1,x]$, and $(\frac1{n+1},x]$ contain $x$ and miss $K$.
So $\mathbb R-K$ is open.

:::

:::

::: {.pf-step #s5}

In $\mathcal T_5$, $\overline K=\boxed{[0,\infty)}$.

::: pf-proof

A union of rays $(-\infty,a)$ is $\varnothing$, $\mathbb R$, or a ray $(-\infty,c)$, so the closed sets are $\varnothing$, $\mathbb R$, and the rays $[c,\infty)$.
A ray $[c,\infty)$ contains $K$ if and only if $c\le\frac1n$ for every $n$, that is, $c\le0$; the smallest is $[0,\infty)$.

:::

:::

::: {.pf-step #s6}

$\mathcal T_1$, $\mathcal T_2$, and $\mathcal T_4$ are Hausdorff, hence $T_1$.

::: pf-proof

$\mathcal T_1$ is the metric topology of $\mathbb R$, and $\mathcal T_2$ and $\mathcal T_4$ are finer than $\mathcal T_1$ by [[E-ALTNF]]; disjoint $\mathcal T_1$-open neighborhoods remain open in a finer topology.

:::

:::

::: {.pf-step #s7}

$\mathcal T_3$ is $T_1$ but not Hausdorff.

::: pf-proof

Singletons are finite, hence closed.
Two nonempty open sets have finite complements, so their intersection has finite complement in the infinite set $\mathbb R$ and is nonempty.

:::

:::

::: {.pf-step #s8}

$\mathcal T_5$ is neither $T_1$ nor Hausdorff.

::: pf-proof

By the description of closed sets in step [](#s5){.pf-ref}, the closure of $\{x\}$ is $[x,\infty)\ne\{x\}$.
A Hausdorff space is $T_1$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} answer (a), and steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} answer (b).

:::

:::

:::
