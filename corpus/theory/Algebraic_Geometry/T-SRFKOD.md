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

::: {.theorem title="Zariski desingularization of surfaces"}
Every projective surface $Y$ admits a desingularization by a finite sequence that alternates normalizations and blowups of maximal ideals.
The resulting smooth surface is projective.
:::

::: {.theorem title="Minimal resolution of normal surface singularities"}
Let $Y$ be a normal projective surface.
There exists a unique minimal resolution $\varphi \colon X \to Y$ such that $X$ is smooth projective, $\varphi$ is an isomorphism over $\reg Y$, and every other desingularization $\varphi' \colon X' \to Y$ with the same two properties factors as $\varphi' = \varphi \circ \sigma$ where $\sigma \colon X' \to X$ is a composition of blowups of points over the exceptional locus of $\varphi$.
:::

::: {.theorem title="Enriques classification"}
A minimal smooth projective surface $X$ falls into exactly one of:

- $\kappa(X) = -\infty$ iff $|12K_X| = \varnothing$ iff $X$ is $\PP^2$ or a minimal ruled surface;

- $\kappa(X) = 0$ iff $|12K_X| = \{0\}$ iff $X$ is K3, Enriques, abelian, or bielliptic;

- $\kappa(X) = 1$ iff $X$ is a properly elliptic surface;

- $\kappa(X) = 2$ iff $X$ is of general type.

In particular $\kappa = -\infty$ are the rational and ruled surfaces, $\kappa = 0$ are the four classes above, $\kappa = 1$ are elliptic, and $\kappa = 2$ are general type.
:::

::: {.remark}
The organising idea is that $\kappa$ measures how much of the surface the pluricanonical systems can see: nothing at $-\infty$, a point at $0$, a curve at $1$, the whole surface at $2$.
For curves the same invariant gives the trichotomy $g=0$, $g=1$, $g \geq 2$, and the surface classification is its two-dimensional analogue.

The $\kappa = 0$ row is the one to be able to separate, by $(p_g, q)$: K3 has $(1,0)$ with $K \sim 0$ and simply connected; Enriques has $(0,0)$ with $2K \sim 0$, and is a free quotient of a K3 by an involution; abelian has $(1,2)$; bielliptic has $(0,1)$ and is a quotient of a product of elliptic curves.

Minimality is what makes the statement clean, and blowing up is exactly the operation that leaves $\kappa$ alone while changing $K^2$ — which is why the classification is stated for minimal models and read off as a birational statement.
:::
