---
schema: qual/card@1
id: P-P9FXD
kind: problem
title: A $p$-group acting on a finite set of order not divisible by $p$ has a fixed
  point
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Group Actions
  - Fixed Points
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared the finite-set and prime-power hypotheses and the global fixed-point conclusion with page 4 of the original scan, Groups 3."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $p$ be prime, $G$ be a group of order $p^n > 1$, and $X$ be a finite $G$-set whose size is not divisible by $p$.
Prove that $G$ has a fixed point in $X$: i.e., an $x \in X$ such that $gx = x$ for all $g \in G$.
:::

::: solution
<1>1. Every orbit has cardinality a power of $p$, and a singleton orbit
is exactly a point fixed by all of $G$.

::: proof
For $x\in X$, let $G_x=\{g\in G:gx=x\}$ be its stabilizer.
The map $G/G_x\to Gx$ sending $gG_x$ to $gx$ is a bijection:
two representatives give the same point exactly when they lie in the
same left coset. Hence
$$
|Gx|=[G:G_x]=\frac{p^n}{|G_x|},
$$
which is a power of $p$. The orbit is a singleton precisely when
$gx=x$ for every $g\in G$. Every other orbit has size divisible by $p$.
:::

<1>2. The global fixed-point set $X^G$ is nonempty.

::: proof
The orbits partition the finite set $X$. The singleton orbits contribute
exactly $|X^G|$, and all other contributions are divisible by $p$.
Therefore
$$
|X|\equiv |X^G|\pmod p.
$$
The left side is nonzero modulo $p$ by hypothesis, so $|X^G|$ cannot
be zero. Any $x\in X^G$ is fixed by every element of $G$, as required.
:::
:::
