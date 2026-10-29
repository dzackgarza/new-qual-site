---
schema: qual/card@1
id: T-MORZMT
kind: theorem
title: Zariski's main theorem
slogan: 'Quasi-finite morphisms are finite up to deleting points; birational projective maps to normal targets must contract positive-dimensional fibres unless they are isomorphisms.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Zariski's Main Theorem
  - Quasi-finite Morphisms
  - Normality
relations:
- kind: uses
  target: D-MORQF
- kind: uses
  target: PR-MORFINCHAR
review: draft
prompts:
- State Zariski's main theorem.
- What does Zariski's main theorem say about birational morphisms to a normal variety?
---

::: {.theorem title="Grothendieck's form"}
A separated quasi-finite morphism $f : X \to Y$ of Noetherian schemes factors as
$$
X \injects \overline{X} \to Y
$$
with the first an open immersion and the second finite.
:::

::: {.theorem title="Zariski's form"}
Let $f : X \to Y$ be a birational projective morphism of Noetherian integral schemes with $Y$ **normal**. Then $f_* \OO_X = \OO_Y$ and every fibre of $f$ is connected.
In particular a birational projective morphism to a normal $Y$ that is quasi-finite is an isomorphism.
Since each fibre is connected, $\dim f^{-1}(y) > 0$ unless $f^{-1}(y)$ is a single point.
:::

::: {.theorem title="Purity of the exceptional locus"}
Let $f : X \to Y$ be as above, with $X$ and $Y$ normal projective varieties over $\CC$.
The exceptional locus
$$
E = E(f) \coloneqq \bigcup_{\dim f^{-1}(y) > 0} f^{-1}(y)
$$
is Zariski-closed in $X$.
If $y_{0} \in f(E)$ is a smooth point of $Y$, then $E$ has codimension $1$ in $X$ near the points of the fibre $f^{-1}(y_{0})$.
In particular if $Y$ is smooth then $E$ is pure of codimension $1$ in $X$.
:::

::: {.remark}
The first form is the structural statement: a separated quasi-finite morphism is an open subscheme of a finite one. The projection $V(xy-1)\to\AA^1$, $(x,y)\mapsto x$, is the model: it is quasi-finite and not finite, and it is the open immersion of $\AA^1\sm\theset{0}$ into the finite morphism $\id_{\AA^1}$.
Read alongside "finite equals proper plus quasi-finite", it says a quasi-finite morphism fails to be finite only by missing points of a finite one.

The second form is the one used in birational geometry, and normality is where all the weight sits.
Without it the theorem fails: the normalisation of a nodal cubic is a birational projective quasi-finite morphism that is not an isomorphism, and the two preimages of the node are exactly the disconnected fibre that normality would forbid.
So the theorem is the precise sense in which a normal variety cannot be improved by a birational morphism without contracting something positive-dimensional.
:::
