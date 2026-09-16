---
schema: qual/card@1
id: P-WKGRZ
kind: problem
title: A $p$-group acting on a set of cardinality not divisible by $p$ has a fixed
  point
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Group Actions
  - Orbit-Stabilizer
relations: []
review: draft
---

::: {.problem}
Let a finite $p$-group $G$ act on a finite set $X$ with $p\nmid |X|$. Prove that the action has a fixed point.
:::

::: {.solution}
Decompose $X$ into $G$-orbits. By orbit--stabilizer, every orbit has cardinality
\[
|G:G_x|,
\]
which is a power of $p$.

An orbit has size $1$ exactly when its point is fixed by all of $G$. Every nontrivial orbit therefore has cardinality divisible by $p$.

Let $X^G$ denote the set of fixed points. Summing orbit sizes gives
\[
|X|\equiv |X^G|\pmod p.
\]
Since $p\nmid |X|$, we have
\[
|X^G|\not\equiv0\pmod p.
\]
In particular $X^G\ne\varnothing$, so the action has a fixed point.
:::
