---
schema: qual/card@1
id: PR-SCHFIB
kind: proposition
title: The scheme-theoretic fibre of a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibre Products
  - Fibres
  - Residue Fields
relations:
- kind: uses
  target: D-SCHFPR
review: draft
prompts:
- What is the fibre of a morphism of schemes over a point?
- Why is the scheme-theoretic fibre better than the set-theoretic preimage?
---

::: {.definition}
For $f: X \to Y$ and $y \in Y$ with residue field $\kappa(y) \da \OO_{Y,y}/\mfm_y$, the \dfn{fibre} is
\[
X_y \da \fiberprod{X}{Y}{\Spec \kappa(y)} .
\]
Its underlying space is $f\inv(y)$, but it carries a scheme structure over the field $\kappa(y)$.
:::

::: {.example}
For $\AA^1\slice k \to \AA^1\slice k$, $t \mapsto t^2$, the fibre over a nonzero $a$ is $\Spec k[t]/(t^2 - a)$, which is two reduced points when $a$ is a square in $k$ and one point with residue field $k(\sqrt a)$ otherwise.
The fibre over $0$ is $\Spec k[t]/(t^2)$, one point of length $2$.
For $\Spec \ZZ[i] \to \Spec \ZZ$ the fibre over $(p)$ is $\Spec \FF_p[x]/(x^2+1)$: two points, one point, or a double point according to $p \bmod 4$.
:::

::: {.remark}
The fibre is the reason the fibre product is worth constructing, so lead with it.
The set-theoretic preimage loses the two things that make fibres behave: the multiplicity at a branch point, and the residue field extension at a point that splits only after base change.
Both are visible in the examples, and in each the fibre has $k$-dimension $2$ for every base point — this is the constancy that a naive count of preimages fails to see.

The follow-up is flatness: a morphism is flat exactly when the fibres vary in the way these examples suggest, and "flat is the right notion of a continuously varying family" is the sentence being fished for.
:::
