---
schema: qual/card@1
id: P-CASP18A
kind: problem
title: 'An entire function with $\abs f\leq e^{\Re z}$ is identically zero or never zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Minimum Principle
relations: []
review: draft
---

::: {.problem}
Let $f$ be an analytic function on $\CC$ that satisfies the inequality $\abs{f(z)} \leq e^{\operatorname{Re} z}$ for all $z \in \CC$.
Prove that either $f(z) = 0$ for all $z \in \CC$ or $f(z) \neq 0$ for all $z \in \CC$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own application of Liouville's theorem follows, with the boundedness of $e^{-z}f(z)$ and the conclusion as separate steps.

::: pf

::: {.pf-step #entire-bounded}
$g(z)=e^{-z}f(z)$ is entire and satisfies $\abs{g(z)}\le1$ for all $z$.

::: pf-proof
$e^{-z}$ and $f$ are entire, so their product is entire. And $\abs{g(z)}=e^{-\operatorname{Re}z}\abs{f(z)}\le e^{-\operatorname{Re}z}e^{\operatorname{Re}z}=1$, using the hypothesis $\abs{f(z)}\le e^{\operatorname{Re}z}$ and $\abs{e^{-z}}=e^{-\operatorname{Re}z}$.
:::

:::

::: {.pf-step #constant}
$g$ is constant.

::: pf-proof
$g$ is entire and bounded, so Liouville's theorem gives $g\equiv c$ for some $c\in\CC$.
:::

:::

::: {.pf-step #form}
$f(z)=ce^{z}$ for all $z$.

::: pf-proof
From $g\equiv c$ and $g=e^{-z}f$ one gets $f(z)=e^{z}g(z)=ce^{z}$, and $e^{z}$ is never $0$.
:::

:::

::: {.pf-qed}
If $c=0$ then $f\equiv0$; if $c\ne0$ then $f(z)=ce^{z}\ne0$ for every $z$, since a product of nonzero complex numbers is nonzero. So $f$ is either identically zero or nowhere zero.
:::

:::

:::
