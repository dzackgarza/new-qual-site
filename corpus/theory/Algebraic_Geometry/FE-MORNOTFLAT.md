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
The morphism $\pi$ is projective.
If it were flat, the Hilbert polynomial of its fibres with respect to a relatively ample line bundle would be locally constant on the connected base $\AA^2$; in particular the fibre dimension would be constant.
Since the general fibre is zero-dimensional and the exceptional fibre is one-dimensional, $\pi$ is not flat.
:::

::: {.example title="Normalisation of a node"}
Let $X$ be a nodal cubic with node $q$ and let $f : \tilde X \to X$ be its normalisation.
If $f$ were flat then $f_* \OO_{\tilde X}$ would be a flat coherent sheaf, hence locally free, and of rank $1$ hence invertible.
But $q$ has two preimages, so $(f_* \OO_{\tilde X})_q$ needs two generators over $\OO_{X,q}$, and an invertible sheaf needs one.
:::

::: {.remark}
The two examples exhibit different failures of flatness.
The blowup fails because the fibre dimension jumps; the normalisation fails because the fibre *length* jumps, from $1$ to $2$, while the dimension is constant at $0$.
For projective flat families over a connected Noetherian base, the Hilbert polynomial is constant; equal fibre dimension alone is not sufficient for flatness.

No nontrivial normalisation is flat, for the same rank argument; more generally, a finite morphism $f$ to a Noetherian scheme is flat exactly when $f_*\OO$ is locally free.
By contrast, a nonconstant morphism of smooth projective curves is finite flat of constant degree; ramification then appears through nonreduced fibre structure rather than a drop in degree.
:::
