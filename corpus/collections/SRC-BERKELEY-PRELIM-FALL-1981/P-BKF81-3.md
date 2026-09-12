---
schema: qual/card@1
id: P-BKF81-3
kind: problem
title: A $p$-subgroup action has a fixed point
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Decomposed the n points into G-orbits, whose sizes are powers of p, and used p∤n to force an orbit of size one."
---

::: problem
Let $S_n$ act on $n$ objects and let $G\le S_n$ have order $p^k$, where the prime $p$ does not divide $n$. Show that $G$ has a fixed point.
:::

::: solution
Let $X$ be the set of the $n$ objects on which $S_n$, and hence $G$, acts.
Decompose $X$ into $G$-orbits:
$$
X=\mathcal O_1\sqcup\cdots\sqcup\mathcal O_r.
$$

<1>1. Every orbit has cardinality a power of $p$.
::: proof
For $x\in X$, the orbit-stabilizer theorem gives
$$
|Gx|=[G:G_x].
$$
Since
$$
|G|=p^k,
$$
the index of every subgroup of $G$ is a power of $p$. Thus each orbit size is
$$
|Gx|=p^j
$$
for some $0\le j\le k$.
:::

<1>2. At least one orbit has size one.
::: proof
Suppose no point were fixed by all of $G$. Then no orbit would have size
$1$, so every orbit size would be divisible by $p$. Therefore
$$
n=|X|=\sum_{i=1}^r|\mathcal O_i|
$$
would be divisible by $p$. This contradicts the hypothesis
$$
p\nmid n.
$$
Hence some orbit has size $1$. Its unique point is fixed by every element of
$G$.
:::
:::
