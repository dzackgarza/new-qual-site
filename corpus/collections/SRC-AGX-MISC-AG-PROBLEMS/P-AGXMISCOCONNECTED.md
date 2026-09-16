---
schema: qual/card@1
id: P-AGXMISCOCONNECTED
kind: problem
title: $\OO_Y \to \pi_* \OO_X$ is an isomorphism exactly when $Y$ is integrally closed in $K(X)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Proper Morphisms
  - Integral Closure
  - Stein Factorisation
relations:
- kind: related-to
  target: T-MORSTEIN
review: draft
---

::: {.problem}
Show that given $\pi: X \rightarrow Y$, $Y$ is integrally closed in $K(X)$ over $K(Y)$ if and only if $\OO_{Y} \rightarrow \pi_{*} \OO_{X}$ is an isomorphism (i.e., $\pi$ is $\OO$-connected).
:::

::: {.remark}
The statement leaves its hypotheses implicit; it is meant for integral Noetherian schemes $X$ and $Y$ with $\pi$ proper and dominant, so that $K(Y) \subseteq K(X)$, and with $Y$ integrally closed in $K(X)$ meaning that $\OO_Y(V)$ is integrally closed in $K(X)$ for every affine open $V \subseteq Y$.
The implication from $\OO_Y \cong \pi_* \OO_X$ to integral closedness needs $X$ normal.
Let $Y$ be the cuspidal cubic $V(y^2 - x^3)$ and $\pi = \id_Y$.
Then $\OO_Y \to \pi_* \OO_X$ is an isomorphism, but $t = y/x \in K(Y)$ satisfies $t^2 = x$, so it is integral over $\OO_Y$ and does not lie in $\OO_Y$.
:::
