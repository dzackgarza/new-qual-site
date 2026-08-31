---
schema: qual/card@1
id: P-ALGF22F
kind: problem
title: "Coefficients of monic polynomials with product in the integral closure must lie in it"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $A$ be a subring of an integral domain $B$ and let $C$ be the integral closure of $A$ inside $B$.
Let $f$ and $g$ be monic polynomials with coefficients in $B$ such that all of the coefficients of $fg$ lie in $C$.
Prove that the coefficients of $f$ and $g$ belong to $C$.
:::

::: {.solution}
<1>1. Let $f(x) = \prod_i (x - \alpha_i)$ and $g(x) = \prod_j (x - \beta_j)$ over an algebraic closure of the fraction field of $B$.
::: {.proof}
factor the monic polynomials.
:::

<1>2. The roots of $fg$ are the $\alpha_i$ and $\beta_j$, and the coefficients of $fg$ are the elementary symmetric functions of these roots.
::: {.proof}
Vieta's formulas.
:::

<1>3. Since the coefficients of $fg$ lie in $C$, each root of $fg$ is integral over $C$ (hence over $A$).
::: {.proof}
a root of a monic polynomial with coefficients in $C$ is integral over $C$; since $C$ is integral over $A$, it is integral over $A$.
:::

<1>4. Hence each $\alpha_i$ and each $\beta_j$ is integral over $A$.
::: {.proof}
<1>2 and <1>3 (the roots of $fg$ are exactly the $\alpha_i$ and $\beta_j$).
:::

<1>5. The coefficients of $f$ are elementary symmetric functions of the $\alpha_i$, hence are integral over $A$ (a sum of products of integral elements is integral).
::: {.proof}
the integral elements form a ring.
:::

<1>6. The coefficients of $f$ lie in $B$ (by hypothesis) and are integral over $A$, so they lie in $C$ (the integral closure of $A$ in $B$).
::: {.proof}
definition of $C$.
:::

<1>7. Similarly, the coefficients of $g$ lie in $C$.
::: {.proof}
the same argument with the $\beta_j$.
:::

<1>8. Q.E.D.
::: {.proof}
<1>6 and <1>7.
:::
:::
