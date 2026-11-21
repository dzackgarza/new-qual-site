---
schema: qual/card@1
id: P-CASP20E
kind: problem
title: Biholomorphisms between $\DD\setminus\{0,1/2\}$ and $\DD\setminus\{0,-1/2\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Automorphisms
  - Biholomorphic Maps
relations: []
review: draft
---

::: {.problem}
Let $A_1 = \DD \setminus \left\{0, \frac{1}{2}\right\}$ and $A_2 = \DD \setminus \left\{0, -\frac{1}{2}\right\}$.
Find all bijective analytic maps from $A_1$ to $A_2$.
:::

::: {.solution}

The argument is the card's own, by removable singularities and the classification of the automorphisms of the disc; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $A_{1}=\DD\setminus\{0,\tfrac12\}$ and $A_{2}=\DD\setminus\{0,-\tfrac12\}$, and let $F:A_{1}\to A_{2}$ be a bijective analytic map.

::: pf

::: {.pf-step #extension}
$F$ extends to an automorphism $\widetilde F$ of $\DD$, and $F^{-1}$ extends to its inverse.

::: pf-proof
$F$ is bounded, since $F(A_{1})\subset A_{2}\subset\DD$, so its singularities at $0$ and $\frac12$ are removable (Riemann's removable singularity theorem) and $F$ extends to a holomorphic $\widetilde F:\DD\to\CC$; its image lies in $\DD$ because $F(A_{1})\subset\DD$ and $\widetilde F$ is continuous, $\DD$ being open and $A_{1}$ dense in $\DD$. Likewise $F^{-1}:A_{2}\to A_{1}$ is bounded and extends to a holomorphic $\widetilde G:\DD\to\DD$. The composites $\widetilde G\circ\widetilde F$ and $\widetilde F\circ\widetilde G$ are holomorphic on $\DD$ and equal the identity on the nonempty open set $A_{1}$, so by the identity theorem they are the identity on $\DD$. Hence $\widetilde F$ is a biholomorphic self-map of $\DD$, that is an automorphism, with inverse $\widetilde G$.
:::

:::

::: {.pf-step #permutation}
$\widetilde F$ maps $\{0,\tfrac12\}$ onto $\{0,-\tfrac12\}$.

::: pf-proof
$F$ maps $A_{1}$ bijectively onto $A_{2}$, so $\widetilde F$ maps $\DD\setminus\{0,\tfrac12\}$ onto $\DD\setminus\{0,-\tfrac12\}$ and therefore carries the complement $\{0,\tfrac12\}$ onto the complement $\{0,-\tfrac12\}$.
:::

:::

::: {.pf-step #two-maps}
$\widetilde F(z)=-z$ if $\widetilde F(0)=0$, and $\widetilde F(z)=\dfrac{z-1/2}{1-z/2}$ if $\widetilde F(\tfrac12)=0$.

::: pf-proof
Every automorphism of $\DD$ has the form $\widetilde F(z)=e^{i\theta}\dfrac{z-a}{1-\bar a z}$ with $a=\widetilde F^{-1}(0)\in\DD$ (Schwarz lemma, or the classification of disc automorphisms). If $\widetilde F(0)=0$ then $a=0$ and $\widetilde F(z)=e^{i\theta}z$ with $\abs{e^{i\theta}}=1$; step [](#permutation){.pf-ref} then forces $\widetilde F(\tfrac12)=e^{i\theta}/2=-\tfrac12$, so $e^{i\theta}=-1$ and $\widetilde F(z)=-z$. If $\widetilde F(\tfrac12)=0$ then $a=\tfrac12$ and $\widetilde F(z)=e^{i\theta}\dfrac{z-1/2}{1-z/2}$; step [](#permutation){.pf-ref} forces $\widetilde F(0)=e^{i\theta}\cdot(-\tfrac12)=-\tfrac12$, so $e^{i\theta}=1$ and $\widetilde F$ is the stated Möbius map.
:::

:::

::: {.pf-step #answer}
The bijective analytic maps $A_{1}\to A_{2}$ are exactly $z\mapsto-z$ and $z\mapsto\dfrac{z-1/2}{1-z/2}$.

::: pf-proof
Every such map is the restriction of one of the two maps of step [](#two-maps){.pf-ref}, by steps [](#extension){.pf-ref} and [](#permutation){.pf-ref}. Conversely both maps are Möbius transformations, hence biholomorphic on $\DD$; $-z$ carries $A_{1}$ onto $A_{2}$ since it exchanges $0$ and $-\tfrac12$ and fixes nothing else removed, and $\varphi(z)=(z-\tfrac12)/(1-z/2)$ is an automorphism of $\DD$ with $\varphi(\tfrac12)=0$ and $\varphi(0)=-\tfrac12$, so it carries $A_{1}=\DD\setminus\{0,\tfrac12\}$ bijectively onto $\DD\setminus\{- \tfrac12,0\}=A_{2}$. So both restrictions are bijective analytic maps $A_{1}\to A_{2}$ and there are no others.
:::

:::

:::
:::
