---
schema: qual/card@1
id: D-VARSEVBRAUER
kind: definition
title: Severi--Brauer varieties, and the Brauer class of a twisted projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Severi-Brauer Varieties
  - Brauer Group
  - Conics
relations:
- kind: related-to
  target: PR-VGA2L
review: draft
prompts:
- What is a Severi--Brauer variety?
---

::: {.definition title="Severi--Brauer variety"}
Let $k$ be a field with separable closure $k^s$.
A \dfn{Severi--Brauer variety} of dimension $n$ over $k$ is a variety $X$ over $k$ with $X_{k^s} \cong \PP^n_{k^s}$.
:::

::: {.theorem}
1. Isomorphism classes of Severi--Brauer varieties of dimension $n$ over $k$ are in bijection with $H^1(\Gal(k^s/k), \PGL_{n+1}(k^s))$, hence with isomorphism classes of central simple $k$-algebras of degree $n+1$; each has a class in $\operatorname{Br}(k)$.

2. (Châtelet) $X \cong \PP^n_k$ if and only if $X(k) \neq \emptyset$, if and only if its Brauer class is trivial.
:::

::: {.example}
The Severi--Brauer varieties of dimension $1$ are the smooth conics.
The conic $x^2 + y^2 + z^2 = 0$ over $\RR$ has no real point, so it is not $\PP^1_\RR$; it corresponds to the Hamilton quaternions.
If $k$ is finite, or is the function field of a curve over an algebraically closed field, then $\operatorname{Br}(k) = 0$ (Wedderburn, Tsen), so every Severi--Brauer variety over $k$ is a projective space.
:::
