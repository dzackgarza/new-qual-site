---
schema: qual/card@1
id: P-ALGS07E
kind: problem
title: "An algebraic extension of a perfect field is perfect"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Recall that a "perfect" field of characteristic $p$ is one for which the Frobenius map $\operatorname{Fr}: x \mapsto x^p$ is onto.

Let $F$ be a perfect field, and $E/F$ an algebraic extension.
Show that $E$ is perfect.
:::

::: {.solution}
**Goal.** Show an algebraic extension $E$ of a perfect field $F$ is perfect.

<1>1. It suffices to show the Frobenius $\operatorname{Fr}: E \to E$, $x \mapsto x^p$, is surjective.
::: {.proof}
a field of characteristic $p$ is perfect iff Frobenius is onto (by definition).
:::

<1>2. Frobenius is injective on any field.
::: {.proof}
$x^p = y^p$ implies $(x - y)^p = x^p - y^p = 0$ (freshman's dream in characteristic $p$), so $x = y$.
:::

<1>3. For any $\alpha \in E$, there is $\beta \in E$ with $\beta^p = \alpha$.
<2>1. $\alpha$ is algebraic over $F$, so $F(\alpha)/F$ is finite.
::: {.proof}
$\alpha$ is algebraic by hypothesis.
:::
<2>2. Frobenius $F(\alpha) \to F(\alpha)$ is an injective $F$-linear map of a finite-dimensional $F$-vector space, hence surjective.
::: {.proof}
an injective linear map between finite-dimensional spaces of the same dimension is an isomorphism.
:::
<2>3. Hence there is $\beta \in F(\alpha) \subseteq E$ with $\beta^p = \alpha$.
::: {.proof}
surjectivity of Frobenius on $F(\alpha)$.
:::

<1>4. Frobenius is surjective on $E$.
::: {.proof}
<1>3 holds for every $\alpha \in E$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4 shows $E$ is perfect.
:::
:::
