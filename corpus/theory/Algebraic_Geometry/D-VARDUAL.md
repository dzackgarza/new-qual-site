---
schema: qual/card@1
id: D-VARDUAL
kind: definition
title: The dual variety of a projective variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dual Varieties
  - Tangent Spaces
  - Projective Varieties
relations:
- kind: uses
  target: D-0SYCY
review: draft
prompts:
- What is a dual variety?
---

::: {.definition title="Dual variety"}
Let $X \subseteq \PP^n$ be an irreducible projective variety, and let $(\PP^n)^\dual$ be the projective space of hyperplanes in $\PP^n$.
A hyperplane $H$ is \dfn{tangent} to $X$ at a smooth point $p$ when $H$ contains the projective tangent space $\mathbb{T}_p X$.
The \dfn{dual variety} $X^\dual \subseteq (\PP^n)^\dual$ is the closure of the set of hyperplanes tangent to $X$ at some smooth point.
:::

::: {.proposition}
The incidence correspondence
\[
\Phi = \overline{\ts{ (p, H) \st p \in X_{\mathrm{sm}},\ \mathbb{T}_p X \subseteq H }} \subseteq X \times (\PP^n)^\dual
\]
is irreducible of dimension $n-1$, since over each smooth point $p$ the fibre is a projective space of dimension $n - 1 - \dim X$.
So $X^\dual$, the image of $\Phi$ under the second projection, is irreducible of dimension at most $n-1$.
Over a field of characteristic zero, $(X^\dual)^\dual = X$.
:::

::: {.example}
If $X \subseteq \PP^2$ is a smooth conic $x^\top A x = 0$ with $A$ symmetric and invertible, the tangent line at $p$ has coordinates $Ap$, and $X^\dual$ is the conic $\xi^\top A^{-1} \xi = 0$.
A linear subspace $\PP^k \subseteq \PP^n$ has dual variety the linear subspace of hyperplanes containing it, of dimension $n-k-1$, so a dual variety need not be a hypersurface.
:::
