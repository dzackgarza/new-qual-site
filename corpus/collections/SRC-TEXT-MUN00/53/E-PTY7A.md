---
schema: qual/card@1
id: E-PTY7A
kind: problem
title: Projection from a product with a discrete space is a covering map
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-corrected
  by: gpt-6.1-sol
  date: 2026-10-31
  note: 'The projection is a covering map only if the discrete factor is nonempty when X is nonempty; a covering map is surjective.'
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 53: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-1-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-53-covering-spaces/problem-1-solution.txt), and against Munkres, Topology (2000), Section 53
    Exercise 1, printed p. 341, with the definition of a covering map on printed p. 336. dbFin's is the same three lines. What was corrected: the stored statement had added the hypothesis that $Y$ is nonempty. The book prints "Let $Y$ have the discrete topology", and the exercise needs $Y$ nonempty, because a covering map is by definition a continuous surjection (printed p. 336) and the projection $X\times\varnothing\to X$ has empty domain; the printed wording is restored and the solution now names that hypothesis and the counterexample without it.
---

::: {.exercise}

Let $Y$ have the discrete topology.
Show that if $p: X \times Y \to X$ is projection on the first coordinate, then $p$ is a covering map.
:::

::: {.solution}
Fix $x\in X$ and let $U$ be any open neighborhood of $x$ (for example $U=X$). Since $Y$ is discrete, every singleton $\{y\}$ is open, and
$$
p^{-1}(U)=U\times Y=\bigsqcup_{y\in Y}(U\times\{y\}).
$$
Each $U\times\{y\}$ is open in $X\times Y$, and the restriction
$$
p\restrict_{U\times\{y\}}:U\times\{y\}\longrightarrow U
$$
is a homeomorphism with inverse $u\mapsto(u,y)$. Thus every open $U$ is evenly covered; in particular $p:X\times Y\to X$ is a covering map.

The printed statement carries no hypothesis on $Y$, and it needs one: a covering map is by definition a continuous surjection (printed p. 336), and for $Y=\varnothing$ with $X\neq\varnothing$ the projection $X\times\varnothing\to X$ has empty domain and is not surjective, while the argument above uses a point $y$ of $Y$ to write down the slice $U\times\{y\}$. For every nonempty discrete $Y$ the projection is a covering map, with $U=X$ evenly covered and the slices $X\times\{y\}$.
:::
