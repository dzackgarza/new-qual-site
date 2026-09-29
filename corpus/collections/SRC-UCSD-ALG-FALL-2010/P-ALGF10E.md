---
schema: qual/card@1
id: P-ALGF10E
kind: problem
title: "Intermediate extensions of abelian Galois extensions are Galois"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Let $E$ be a finite-dimensional Galois extension of a field $F$ and let $G = \operatorname{Gal}(E/F)$.
Suppose that $G$ is an abelian group.
Prove that if $K$ is any field between $E$ and $F$, then $K$ is a Galois extension of $F$.
What is the Galois group of $K$ over $F$?
:::

::: {.solution}

::: pf

::: pf-step
By the fundamental theorem of Galois theory, $K$ corresponds to a subgroup $H = \operatorname{Gal}(E/K) \le G$.

::: pf-proof
Galois correspondence.
:::

:::

::: {.pf-step #subgroups-normal}
Since $G$ is abelian, every subgroup $H \le G$ is normal.

::: pf-proof
abelian groups have all subgroups normal.
:::

:::

::: {.pf-step #k-galois}
Hence $K/F$ is Galois (a subgroup $H$ corresponds to a Galois intermediate field iff $H$ is normal in $G$).

::: pf-proof
step [](#subgroups-normal){.pf-ref} and the fundamental theorem.
:::

:::

::: {.pf-step #galois-group-quotient}
The Galois group of $K$ over $F$ is $\operatorname{Gal}(K/F) \cong G/H$.

::: pf-proof
fundamental theorem of Galois theory.
:::

:::

::: pf-qed
step [](#k-galois){.pf-ref} and step [](#galois-group-quotient){.pf-ref}.
:::

:::
:::
