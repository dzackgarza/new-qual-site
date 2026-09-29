---
schema: qual/card@1
id: E-AMD-R4LGOQ33
kind: problem
title: $p$-groups are solvable
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that every $p\dash$group is solvable.
:::

::: {.hint}
Induct on $\abs G$: $Z(G)$ is nontrivial and abelian, $G/Z(G)$ is a smaller $p$-group, and if $N\normal G$ with $N$ and $G/N$ solvable then $G$ is solvable.
:::

::: {.solution}

::: pf

::: pf-step
Argue by induction on $\abs G = p^n$.
:::

::: {.pf-step #base-case-order-le-p}
Base case: if $n \leq 1$ then $G$ is trivial or of prime order, hence abelian, hence solvable.
:::

::: {.pf-step #inductive-step}
Inductive step: let $n \geq 2$ and assume every $p$-group of order less than $p^n$ is solvable.

::: pf-proof

::: pf-step
The class equation $$\abs G = \abs{Z(G)} + \sum_i [G : C_G(x_i)]$$ over representatives of the conjugacy classes of size greater than $1$ has every index divisible by $p$, so $p$ divides $\abs{Z(G)}$ and $Z(G) \neq 1$.
:::

::: pf-step
$Z(G) \normal G$, and $Z(G)$ is abelian, hence solvable.
:::

::: pf-step
$\abs{G/Z(G)} = \abs G / \abs{Z(G)} < p^n$, and it is a power of $p$, so $G/Z(G)$ is solvable by the inductive hypothesis.
:::

::: {.pf-step #lifting-subnormal-series}
If $N \normal G$ with $N$ and $G/N$ solvable, then $G$ is solvable: lifting a subnormal series of $G/N$ with abelian quotients through $G \to G/N$ and appending a subnormal series of $N$ produces one for $G$.
:::

::: pf-step
Applying step [](#lifting-subnormal-series){.pf-ref} with $N = Z(G)$ makes $G$ solvable.
:::

:::

:::

::: pf-qed
Steps [](#base-case-order-le-p){.pf-ref} and [](#inductive-step){.pf-ref} complete the induction, so every $p$-group is solvable.
:::

:::

:::
