---
schema: qual/card@1
id: P-CASP23B
kind: problem
title: "Product of distances from a point on T to given points is at least one"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Polynomials
  - Unit Circle
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the one-line argument already on the card,
    correct as it stood. Added: the value |p(0)| = 1 from the moduli of the z_j; the existence
    of the maximum of |p| on the compact circle, which the prose used silently; and the final
    identification of the product of distances with |p(z_0)| at the maximiser. Not claimed: a
    retained solution set; the provenance names the examination paper.
---

::: {.problem}
Let $z_1, \ldots, z_n$ be points on $\circlegroup$.
Prove that there is $z_0 \in \circlegroup$ such that the product of the distances from $z_0$ to each of the given points is at least one.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2023 complex-analysis examination paper, which carries no solutions. The one-line argument below is the card's own and follows the card's previous prose.

Throughout $z_1,\dots,z_n$ lie on the unit circle $\circlegroup=\theset{\abs z=1}$ and $p(z)=\prod_{j=1}^n(z-z_j)$.

::: pf

::: {.pf-step #value-at-zero}
$\abs{p(0)}=1$.

::: pf-proof
$p(0)=\prod_j(0-z_j)$, so $\abs{p(0)}=\prod_j\abs{z_j}=\prod_j1=1$ because each $z_j$ has modulus $1$.

:::

:::

::: {.pf-step #maximum}
$\max_{\abs z=1}\abs{p(z)}\ge1$, and the maximum is attained on the circle.

::: pf-proof
$p$ is a polynomial, hence continuous on the compact circle, so its modulus attains a maximum there. The maximum modulus principle on the closed disk gives $\abs{p(0)}\le\max_{\abs z=1}\abs{p(z)}$, and $\abs{p(0)}=1$ by step [](#value-at-zero){.pf-ref}.

:::

:::

::: {.pf-step #conclusion}
There is $z_0\in\circlegroup$ with $\prod_{j=1}^n\abs{z_0-z_j}\ge1$.

::: pf-proof
Take $z_0$ a point of the circle where $\abs p$ attains its maximum. Then $\prod_j\abs{z_0-z_j}=\abs{p(z_0)}=\max_{\abs z=1}\abs p\ge1$ by step [](#maximum){.pf-ref}.

:::

:::

:::
:::
