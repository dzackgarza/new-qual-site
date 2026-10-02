---
schema: qual/card@1
id: T-SRFKOD
kind: definition
title: Kodaira dimension and the Enriques classification of surfaces
slogan: 'Kodaira dimension measures how much the pluricanonical system sees: nothing, a point, a curve, or the whole surface for $\kappa=-\infty,0,1,2$.'
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
The \dfn{Kodaira dimension} of a smooth projective variety $X$ is
$$
\kappa(X)
\coloneqq
\operatorname{trdeg}_k\!\left(\bigoplus_{m\geq0}H^0(X,\omega_X^{\otimes m})\right)-1
$$
when $H^0(X,\omega_X^{\otimes m})\ne0$ for some $m>0$, and $\kappa(X)\coloneqq-\infty$ otherwise.
It is a birational invariant, so for surfaces it is computed on a minimal model.
:::

::: {.theorem title="Zariski desingularization of surfaces"}
Let $Y$ be a projective surface over an algebraically closed field.
Then $Y$ admits a desingularization by a finite sequence that alternates normalizations and blowups of closed points.
The resulting smooth surface is projective.
:::

::: {.theorem title="Minimal resolution of normal surface singularities"}
Let $Y$ be a normal projective surface over an algebraically closed field.
There exists a unique minimal resolution $\varphi \colon X \to Y$ such that $X$ is smooth projective, $\varphi$ is an isomorphism over $\reg Y$, and every other desingularization $\varphi' \colon X' \to Y$ with the same two properties factors as $\varphi' = \varphi \circ \sigma$ where $\sigma \colon X' \to X$ is a composition of blowups of points over the exceptional locus of $\varphi$.
:::

::: {.theorem title="Enriques classification"}
A minimal smooth projective surface $X$ over $\CC$ falls into exactly one of:

- $\kappa(X)=-\infty$: $X$ is $\PP^2$ or a minimal ruled surface;

- $\kappa(X)=0$: $X$ is K3, Enriques, abelian, or bielliptic;

- $\kappa(X)=1$: $X$ is a properly elliptic surface;

- $\kappa(X)=2$: $X$ is of general type.

In particular $\kappa = -\infty$ are the rational and ruled surfaces, $\kappa = 0$ are the four classes above, $\kappa = 1$ are elliptic, and $\kappa = 2$ are general type.
:::

::: {.remark}
For a surface, $\kappa$ is the eventual dimension of the image of the pluricanonical maps: no pluricanonical sections for $-\infty$, and image dimension $0$, $1$, or $2$ for the remaining three cases.
For curves the same invariant gives the trichotomy $g=0$, $g=1$, $g \geq 2$, and the surface classification is its two-dimensional analogue.

The $\kappa = 0$ row is the one to be able to separate, by $(p_g, q)$: K3 has $(1,0)$ with $K \sim 0$ and simply connected; Enriques has $(0,0)$ with $2K \sim 0$, and is a free quotient of a K3 by an involution; abelian has $(1,2)$; bielliptic has $(0,1)$ and is a quotient of a product of elliptic curves.

Minimality is what makes the statement clean, and blowing up is exactly the operation that leaves $\kappa$ alone while changing $K^2$ — which is why the classification is stated for minimal models and read off as a birational statement.
:::

::: {.remark}
Over an algebraically closed field of characteristic $p > 0$ the classification of Bombieri and Mumford has the same four values of $\kappa$, but the $\kappa = 0$ and $\kappa = 1$ classes change: in characteristic $2$ and $3$ there are quasi-hyperelliptic surfaces and quasi-elliptic fibrations, and in characteristic $2$ there are non-classical Enriques surfaces with $h^1(\OO_X) = 1$.
The Enriques classification above also holds over an algebraically closed field of characteristic $0$.
:::
