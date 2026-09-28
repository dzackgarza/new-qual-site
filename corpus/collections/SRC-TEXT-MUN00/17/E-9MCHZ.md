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

(a) Determine the closure of the set $K = \ts{1/n \mid n \in \mathbb{Z}_+}$ under each of these topologies.

(b) Which of these topologies satisfy the Hausdorff axiom?
the $T_1$ axiom?
:::

::: {.solution}
The five topologies of [[E-ALTNF]] are: $\mathcal T_1$ the standard topology; $\mathcal T_2$ the topology of $\mathbb R_K$, with basis the intervals $(a,b)$ and the sets $(a,b)-K$; $\mathcal T_3$ the finite complement topology; $\mathcal T_4$ the upper limit topology, with basis the intervals $(a,b]$; and $\mathcal T_5$ the topology with basis the rays $(-\infty,a)$.

<1>1. In $\mathcal T_1$, $\overline K=\boxed{K\cup\{0\}}$.

::: {.proof}
Every interval about $0$ contains $1/n$ for large $n$, so $0\in\overline K$.
A point $x\notin K\cup\{0\}$ has an interval about it missing $K$: take $(-\infty,0)$ if $x<0$, $(1,\infty)$ if $x>1$, and $(\frac1{n+1},\frac1n)$ if $\frac1{n+1}<x<\frac1n$.
:::

<1>2. In $\mathcal T_2$, $\overline K=\boxed{K}$.

::: {.proof}
The basic set $(-1,1)-K$ contains $0$ and misses $K$.
Every other point outside $K$ has a standard open interval missing $K$, by the proof of step <1>1.
So $\mathbb R-K$ is open.
:::

<1>3. In $\mathcal T_3$, $\overline K=\boxed{\mathbb R}$.

::: {.proof}
The closed sets are $\mathbb R$ and the finite sets, and $K$ is infinite.
:::

<1>4. In $\mathcal T_4$, $\overline K=\boxed{K}$.

::: {.proof}
The basic set $(-1,0]$ contains $0$ and misses $K$.
For $x<0$, $x>1$, and $\frac1{n+1}<x<\frac1n$, the basic sets $(x-1,x]$, $(1,x]$, and $(\frac1{n+1},x]$ contain $x$ and miss $K$.
So $\mathbb R-K$ is open.
:::

<1>5. In $\mathcal T_5$, $\overline K=\boxed{[0,\infty)}$.

::: {.proof}
A union of rays $(-\infty,a)$ is $\varnothing$, $\mathbb R$, or a ray $(-\infty,c)$, so the closed sets are $\varnothing$, $\mathbb R$, and the rays $[c,\infty)$.
A ray $[c,\infty)$ contains $K$ if and only if $c\le\frac1n$ for every $n$, that is, $c\le0$; the smallest is $[0,\infty)$.
:::

<1>6. $\mathcal T_1$, $\mathcal T_2$, and $\mathcal T_4$ are Hausdorff, hence $T_1$.

::: {.proof}
$\mathcal T_1$ is the metric topology of $\mathbb R$, and $\mathcal T_2$ and $\mathcal T_4$ are finer than $\mathcal T_1$ by [[E-ALTNF]]; disjoint $\mathcal T_1$-open neighborhoods remain open in a finer topology.
:::

<1>7. $\mathcal T_3$ is $T_1$ but not Hausdorff.

::: {.proof}
Singletons are finite, hence closed.
Two nonempty open sets have finite complements, so their intersection has finite complement in the infinite set $\mathbb R$ and is nonempty.
:::

<1>8. $\mathcal T_5$ is neither $T_1$ nor Hausdorff.

::: {.proof}
By the description of closed sets in step <1>5, the closure of $\{x\}$ is $[x,\infty)\ne\{x\}$.
A Hausdorff space is $T_1$.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1 through <1>5 answer (a), and steps <1>6 through <1>8 answer (b).
:::
:::
