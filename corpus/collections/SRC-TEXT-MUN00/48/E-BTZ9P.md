---
schema: qual/card@1
id: E-BTZ9P
kind: exercise
title: Pointwise limits of continuous functions are continuous somewhere uncountably
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

If $f_n$ is a sequence of continuous functions $f_n: \mathbb{R} \to \mathbb{R}$ such that $f_n(x) \to f(x)$ for each $x \in \mathbb{R}$, show that $f$ is continuous at uncountably many points of $\mathbb{R}$.
:::

::: {.solution}
<1>1. For each $n$, $F_n=\{x: \forall m,k\ge n, |f_m(x)-f_k(x)|\le1/n\}$ is closed and $\bigcup_nF_n=\R$.
Proof: Baire.

<1>2. By Baire, some $F_N$ contains interval $[a,b]$.
Proof: <1>1.

<1>3. On $[a,b]$, $f_n\to f$ uniformly, so $f$ continuous on $[a,b]$.
Proof: uniform limit of continuous.

<1>4. Hence $f$ continuous at uncountably many points (every point of $[a,b]$).
Proof: <1>3.

<1>5. Q.E.D.
Proof: <1>4.
:::
