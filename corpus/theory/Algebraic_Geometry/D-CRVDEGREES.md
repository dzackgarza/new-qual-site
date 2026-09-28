---
schema: qual/card@1
id: D-CRVDEGREES
kind: definition
title: Degrees of points, finite morphisms, line bundles and coherent sheaves on curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Curves
  - Euler Characteristic
relations:
- kind: related-to
  target: PR-Y5S7V
- kind: related-to
  target: D-VARDEG
- kind: uses
  target: D-COHEULER
review: draft
prompts:
- What is the degree of a closed point?
- What is the degree of a morphism at a point?
- How is the degree of a line bundle or a coherent sheaf on a projective curve defined, and how does it behave under pullback?
---

Let $k$ be a field.

::: {.definition title="Degree of a closed point"}
Let $X$ be a scheme locally of finite type over $k$ and $p \in X$ a closed point.
The \dfn{degree} of $p$ is $\deg p = [\kappa(p) : k]$, which is finite by the Nullstellensatz.
:::

::: {.definition title="Degree of a finite morphism"}
Let $\pi \colon X \to Y$ be a finite morphism and $y \in Y$.
The \dfn{degree of $\pi$ at $y$} is $\dim_{\kappa(y)} (\pi_* \OO_X \otimes_{\OO_Y} \kappa(y))$.
Since $\pi$ is affine, $\pi^{-1}(y) = \Spec (\pi_* \OO_X \otimes \kappa(y))$, so this is the dimension of the ring of functions on the fibre.
If $X$ is a curve without embedded points, $Y$ is a regular curve and $\pi$ is finite and surjective, then $\pi_* \OO_X$ is locally free of finite rank, and its rank, the degree at every point, is the \dfn{degree} $\deg \pi$.
:::

::: {.definition title="Degree of a line bundle and of a coherent sheaf"}
Let $C$ be a projective curve over $k$.
The \dfn{degree} of an invertible sheaf $\mathcal{L}$ on $C$ is $\deg_C \mathcal{L} = \chi(C, \mathcal{L}) - \chi(C, \OO_C)$.
If $C$ is integral, the \dfn{degree} of a coherent sheaf $\mathcal{F}$ on $C$ is $\deg \mathcal{F} = \chi(C, \mathcal{F}) - (\operatorname{rank} \mathcal{F}) \chi(C, \OO_C)$, where $\operatorname{rank} \mathcal{F}$ is the dimension of the stalk of $\mathcal{F}$ at the generic point over the function field.
For rank $1$ locally free $\mathcal{F}$ the two definitions agree.
:::

::: {.proposition}
Let $C$ be a regular projective integral curve over $k$.

1. For a divisor $D = \sum_i n_i p_i$, $\deg \OO_C(D) = \deg D = \sum_i n_i \deg p_i$ ([[PR-Y5S7V]]); so if $s$ is a nonzero rational section of $\mathcal{L}$, then $\deg \mathcal{L} = \deg \div s$.

2. For a locally free sheaf $\mathcal{E}$ of rank $r$ and an invertible sheaf $\mathcal{L}$, $\chi(\mathcal{E} \otimes \mathcal{L}) = \chi(\mathcal{E}) + r \deg \mathcal{L}$.

3. If $\pi \colon C' \to C$ is a finite surjective morphism from a projective integral curve, then $\deg_{C'} \pi^* \mathcal{L} = (\deg \pi)(\deg_C \mathcal{L})$ [@Har10a, Proposition II.6.9].
:::

