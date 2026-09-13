---
schema: qual/card@1
id: FE-MORNOTFLAT
kind: example
title: The blowup and the normalisation of a node are not flat
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flatness
  - Blowups
  - Counterexamples
relations:
- kind: uses
  target: D-MORFLAT
review: draft
prompts:
- Give an example of a non-flat morphism.
- Why is a normalisation not flat?
---

::: {.example title="The blowup"}
Let $\pi : \Bl_0 \AA^2 \to \AA^2$.
Every fibre over $p \neq 0$ is a single point, and $\pi^{-1}(0) \cong \PP^1$.
Flatness over a reduced connected base forces the fibres to be equidimensional, so $\pi$ is not flat.
:::

::: {.example title="Normalisation of a node"}
Let $X$ be a nodal cubic with node $q$ and let $f : \tilde X \to X$ be its normalisation.
If $f$ were flat then $f_* \OO_{\tilde X}$ would be a flat coherent sheaf, hence locally free, and of rank $1$ hence invertible.
But $q$ has two preimages, so $(f_* \OO_{\tilde X})_q$ needs two generators over $\OO_{X,q}$, and an invertible sheaf needs one.
:::

::: {.remark}
The two examples are the two ways flatness fails, and they are worth separating.
The blowup fails because the fibre dimension jumps; the normalisation fails because the fibre *length* jumps, from $1$ to $2$, while the dimension is constant at $0$.
So "equidimensional fibres" is necessary and not sufficient, and the invariant that flatness really keeps constant is the Hilbert polynomial.

No nontrivial normalisation is flat, for the same rank argument, and a ramified map of curves in the sense of a map that is not finite locally free is not either.
The contrast to draw is with a ramified map of *smooth* curves, which is finite flat of constant degree: there the ramification shows up in the fibre being a fat point, not in the degree dropping.
:::
