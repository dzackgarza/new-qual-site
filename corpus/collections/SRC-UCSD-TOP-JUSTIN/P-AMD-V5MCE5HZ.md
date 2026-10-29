---
schema: qual/card@1
id: P-AMD-V5MCE5HZ
kind: problem
title: An injective map $S^m\to S^n$ homeomorphic on an open set onto an open set is a surjection of $S^n$
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source sheet printed "if f: S^m -> S^n and there is U ⊂ S^m with f|_U ≅ f(U), then m = n and f is surjective", false for the equatorial S^1 -> S^2; the statement now assumes f continuous and injective and U nonempty open with f(U) open and f|_U a homeomorphism onto f(U).'
---

::: {.problem}
Let $f: S^m \to S^n$ be continuous and injective, and suppose there is a nonempty open $U \subset S^m$ such that $f(U)$ is open in $S^n$ and $\restrictionof{f}{U} : U \to f(U)$ is a homeomorphism. Show that $m=n$ and $f$ is surjective.
:::

::: {.solution}

::: pf

::: {.pf-step #dim}

$m = n$.

::: pf-proof

Every point of $S^k$ has an open neighborhood homeomorphic to $\RR^k$. Shrinking $U$, we may take $U$ homeomorphic to a nonempty open subset of $\RR^m$ and $f(U)$ inside such a chart of $S^n$, so $f(U)$ is homeomorphic to a nonempty open subset of $\RR^n$. By invariance of dimension, a nonempty open subset of $\RR^m$ is homeomorphic to an open subset of $\RR^n$ only if $m = n$.

:::

:::

::: pf-step

$f$ is surjective.

::: pf-proof

By step [](#dim){.pf-ref}, $f : S^n \to S^n$ is a continuous injection. If $n = 0$, it is an injection of a two-point set into itself, hence a bijection. If $n \ge 1$, invariance of domain, applied in charts, makes $f$ an open map, so $f(S^n)$ is open. $f(S^n)$ is compact in the Hausdorff space $S^n$, hence closed. It is nonempty, and $S^n$ is connected, so $f(S^n) = S^n$.

:::

:::

:::

:::
