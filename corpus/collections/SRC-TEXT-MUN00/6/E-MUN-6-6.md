---
schema: qual/card@1
id: E-MUN-6-6
kind: problem
title: Bijection between $\mathcal{P}(A)$ and $X^n$
classification:
  areas:
  - topology
  topics:
  - Finite Sets
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

(a) Let $A = \{1, \ldots, n\}$ . Show there is a bijection of $\mathcal{P}(A)$ with the cartesian product $X^n$, where $X$ is the two-element set $X = \{0, 1\}$ .

(b) Show that if $A$ is finite, then $\mathcal{P}(A)$ is finite.
:::

::: {.solution}

(a) For $S\subseteq A$, let $\chi_S(i)=1$ if $i\in S$, and let
$\chi_S(i)=0$ otherwise. The map
$$
S\longmapsto(\chi_S(1),\ldots,\chi_S(n))
$$
from $\mathcal P(A)$ to $\{0,1\}^n$ is bijective. Its inverse sends a
binary $n$-tuple $(x_1,\ldots,x_n)$ to $\{i\in A:x_i=1\}$.

(b) Any finite set $A$ has a bijection with $\{1,\ldots,n\}$ for some
$n\ge0$. This induces a bijection of their power sets. By part (a),
$\mathcal P(A)$ has $2^n$ elements, so it is finite. For $n=0$, the
power set of the empty set is $\{\varnothing\}$, in agreement with
$2^0=1$.
:::
