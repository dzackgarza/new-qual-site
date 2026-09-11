---
schema: qual/card@1
id: T-SRFKOD
kind: theorem
title: Kodaira dimension and the Enriques classification of surfaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Kodaira Dimension
  - Classification of Surfaces
  - Minimal Models
relations:
- kind: uses
  target: D-SRFRULED
- kind: uses
  target: T-SRFCAST
review: draft
prompts:
- Discuss the classification of surfaces.
- What is the Kodaira dimension?
- Which surfaces have Kodaira dimension zero?
---

::: {.definition}
The **Kodaira dimension** of a smooth projective variety $X$ is
\[
\kappa(X) = \operatorname{trdeg}_k \bigoplus_{n \geq 0} H^0(X, \OO_X(nK_X)) - 1 ,
\]
set to $-\infty$ when every plurigenus vanishes.
It is a birational invariant, so for surfaces it is computed on a minimal model.
:::

::: {.theorem title="Enriques classification"}
A minimal smooth projective surface falls into exactly one of:

- $\kappa = -\infty$: rational and ruled surfaces;

- $\kappa = 0$: K3, Enriques, abelian, and bielliptic surfaces;

- $\kappa = 1$: properly elliptic surfaces, those with an elliptic fibration;

- $\kappa = 2$: surfaces of general type.
:::

::: {.remark}
The organising idea is that $\kappa$ measures how much of the surface the pluricanonical systems can see: nothing at $-\infty$, a point at $0$, a curve at $1$, the whole surface at $2$.
For curves the same invariant gives the trichotomy $g=0$, $g=1$, $g \geq 2$, and the surface classification is its two-dimensional analogue.

The $\kappa = 0$ row is the one to be able to separate, by $(p_g, q)$: K3 has $(1,0)$ with $K \sim 0$ and simply connected; Enriques has $(0,0)$ with $2K \sim 0$, and is a free quotient of a K3 by an involution; abelian has $(1,2)$; bielliptic has $(0,1)$ and is a quotient of a product of elliptic curves.

Minimality is what makes the statement clean, and blowing up is exactly the operation that leaves $\kappa$ alone while changing $K^2$ — which is why the classification is stated for minimal models and read off as a birational statement.
:::
