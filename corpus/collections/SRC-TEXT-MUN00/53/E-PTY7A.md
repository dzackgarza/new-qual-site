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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The solution opened by claiming that no retained solution set covers the exercise, contradicting the
    source-checked event above it, which compares the argument with dbFin's Section 53 Problem 1 solution
    kept at tmp/sources/dbfin/section-53-covering-spaces/problem-1-solution.txt. That copy was read again:
    it gives continuity, surjectivity and the decomposition of the preimage into open slices
    homeomorphic to $X$, which is the argument the card states. The opening sentence now names the set and
    its three clauses, and keeps the printed statement with the omitted nonemptiness hypothesis in the
    card's own step. Not checked here: the printed pages, which are the earlier session's citations.

---

::: {.exercise}

Let $Y$ have the discrete topology.
Show that if $p: X \times Y \to X$ is projection on the first coordinate, then $p$ is a covering map.
:::

::: {.solution}

The argument is the retained published solution of dbFin, "Section 53: Problem 1 Solution" (`tmp/sources/dbfin/section-53-covering-spaces/problem-1-solution.txt`, read 2026-11-11): $p$ is continuous and surjective, and $p^{-1}(X)=\bigcup_{y\in Y}X\times\{y\}$, each slice $X\times\{y\}$ being open in $X\times Y$ because $Y$ is discrete and homeomorphic to $X$. The printed statement is kept as printed, and the hypothesis it omits is named in step [](#hypothesis){.pf-ref}, with a counterexample: for $X$ a one-point space and $Y$ empty the projection is not surjective, so it is not a covering map.

Let $Y$ be discrete and $p:X\times Y\to X$ the projection on the first coordinate. In Munkres a covering map is a continuous surjection $p:E\to B$ such that every point of $B$ has an evenly covered neighbourhood (printed p. 336).

::: pf

::: {.pf-step #slices}
For open $U\subseteq X$, $p^{-1}(U)=U\times Y=\bigsqcup_{y\in Y}U\times\{y\}$, and each slice $U\times\{y\}$ is open in $X\times Y$.

::: pf-proof
$p^{-1}(U)$ consists of the pairs $(u,y)$ with $u\in U$, which is the union of the slices $U\times\{y\}$ over $y\in Y$, and the slices are pairwise disjoint because a pair has exactly one second coordinate. Since $Y$ is discrete, $\{y\}$ is open in $Y$, so the slice $U\times\{y\}$ is a basis element of the product topology, hence open; the union of open sets is open.
:::

:::

::: {.pf-step #slices-homeomorphic}
For each $y\in Y$ the restriction $p\restriction_{U\times\{y\}}:U\times\{y\}\to U$ is a homeomorphism.

::: pf-proof
It is the restriction of the continuous projection, hence continuous, and it is a bijection with inverse $u\mapsto(u,y)$, which is continuous as the map $U\to X\times Y$ whose coordinates are the identity and the constant map $u\mapsto y$ (Theorem 18.4).
:::

:::

::: {.pf-step #evenly}
Every point of $X$ has an evenly covered neighbourhood, so $p$ is a covering map.

::: pf-proof
Let $x\in X$ and take $U=X$, an open neighbourhood of $x$. By steps [](#slices){.pf-ref} and [](#slices-homeomorphic){.pf-ref}, $p^{-1}(U)$ is the disjoint union of the open slices $U\times\{y\}$, each mapped homeomorphically onto $U$ by $p$; that is exactly $U$ being evenly covered. The projection is continuous and, when $Y\ne\varnothing$, surjective, so it is a covering map.
:::

:::

::: {.pf-step #hypothesis}
The printed statement needs $Y\ne\varnothing$: for $Y=\varnothing$ and $X\ne\varnothing$ the projection $X\times\varnothing\to X$ is the empty map into a nonempty set, hence not surjective, and so not a covering map.

::: pf-proof
$X\times\varnothing=\varnothing$, and the projection of the empty set has empty image, while a covering map is surjective by the definition quoted above; the argument of step [](#evenly){.pf-ref} also breaks down, since it writes down a slice $U\times\{y\}$ and no point $y$ of $Y$ exists. For every nonempty discrete $Y$ the projection is a covering map, as shown.
:::

:::

::: {.pf-qed}
For nonempty discrete $Y$ the projection $p:X\times Y\to X$ is a covering map (step [](#evenly){.pf-ref}), and the empty $Y$ is the single case the printed statement does not cover (step [](#hypothesis){.pf-ref}).
:::

:::

:::
