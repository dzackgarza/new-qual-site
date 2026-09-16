---
schema: qual/card@1
id: T-COHSVAN
kind: theorem
title: Serre vanishing for large twists
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Vanishing Theorems
  - Twisting Sheaves
relations:
- kind: uses
  target: T-COHFIN
review: draft
prompts:
- State Serre vanishing.
- What does "$n \gg 0$" depend on?
- How is ampleness characterised cohomologically?
---

::: {.theorem}
Let $A$ be Noetherian, $X$ projective over $A$ with $\OO_X(1)$ very ample, and $\mcf \in \Coh(X)$.
Then there is $n_0$ such that
\[
H^i(X, \mcf(n)) = 0 \quad \text{for all } i > 0 \text{ and all } n \geq n_0 .
\]
[@Har10a]
:::

::: {.remark}
Twisting enough kills everything above degree zero, and $\mcf(n)$ becomes globally generated as well.
The threshold $n_0$ depends on $\mcf$, not only on $X$: this is the hypothesis examiners probe, since no single $n$ works for all coherent sheaves at once.

Two uses are constant.
The Hilbert polynomial $\chi(\mcf(n))$ equals $h^0(\mcf(n))$ for $n \gg 0$, which is what identifies the Euler characteristic with the classical Hilbert function of a graded module.
And the converse direction is a criterion: an invertible $\mcl$ on a proper $A\dash$scheme is ample exactly when every coherent $\mcf$ has $H^{i>0}(\mcf \tensor \mcl^{\tensor n}) = 0$ for $n \gg 0$.
That is the statement to quote when asked for a cohomological characterisation of ampleness, and it is the one that makes ampleness checkable without producing an embedding.
:::
