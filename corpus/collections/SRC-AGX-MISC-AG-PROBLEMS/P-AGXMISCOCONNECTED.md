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

::: {.solution}
The source leaves the hypotheses implicit.
Assume that $X$ and $Y$ are integral Noetherian schemes and that $\pi$ is proper and dominant, so $K(Y) \subseteq K(X)$.
Say that $Y$ is integrally closed in $K(X)$ if for every affine open $V \subseteq Y$ the ring $\OO_Y(V)$ is integrally closed in $K(X)$.
The forward implication holds under these assumptions; the reverse implication needs $X$ normal, and the remark gives a counterexample without it.

<1>1. For every affine open $V \subseteq Y$, $B \coloneqq \pi_* \OO_X(V) = \OO_X(\pi^{-1} V)$ is a subring of $K(X)$ containing $A \coloneqq \OO_Y(V)$ and finite over $A$.

::: {.proof}
$X$ is integral, so $\OO_X(\pi^{-1} V)$ embeds in $K(X)$, and $\pi^\sharp$ is injective because $\pi$ is dominant.
$\pi$ is proper, so $\pi_* \OO_X$ is a coherent $\OO_Y$-module, and $B$ is a finitely generated $A$-module.
:::

<1>2. If $Y$ is integrally closed in $K(X)$, then $\OO_Y \to \pi_* \OO_X$ is an isomorphism.

::: {.proof}
By step <1>1 every element of $B$ is integral over $A$, since $B$ is a finite $A$-module, and lies in $K(X)$.
So $B \subseteq A$ when $A$ is integrally closed in $K(X)$, and $A \subseteq B$ always; hence $A = B$ for every affine $V$.
:::

<1>3. If $X$ is normal and $\OO_Y \to \pi_* \OO_X$ is an isomorphism, then $Y$ is integrally closed in $K(X)$.

::: {.proof}
Let $t \in K(X)$ be integral over $A = \OO_Y(V)$.
Then $t$ is integral over $\OO_{X,x}$ for every $x \in \pi^{-1} V$, and $\OO_{X,x}$ is integrally closed in $K(X)$ because $X$ is normal, so $t \in \bigcap_{x \in \pi^{-1} V} \OO_{X,x} = \OO_X(\pi^{-1} V) = B$.
By hypothesis $B = A$, so $t \in A$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give the two implications under the stated hypotheses.
:::
:::

::: {.remark}
Normality of $X$ is needed for the implication in step <1>3.
Let $Y$ be the cuspidal cubic $V(y^2 - x^3)$ and $\pi = \mathrm{id}_Y$.
Then $\OO_Y \to \pi_* \OO_X$ is an isomorphism, but $t = y/x \in K(Y)$ satisfies $t^2 = x$, so it is integral over $\OO_Y$ and does not lie in $\OO_Y$.
:::
