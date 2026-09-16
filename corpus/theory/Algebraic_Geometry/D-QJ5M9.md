---
schema: qual/card@1
id: D-QJ5M9
kind: definition
title: Normal domains, and normality against regularity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Normal Varieties
  - Regular Local Rings
  - Normalization
relations:
- kind: uses
  target: D-0SYCY
review: draft
prompts:
- What is a normal domain?
- How is normality related to regularity?
- Why is normalization a resolution of singularities for curves?
- What is a normal scheme?
- What is the normalization of an integral scheme, and what universal property does it have?
---

::: {.definition title="Normal"}
An integral domain is \dfn{normal} if it is integrally closed in its fraction field.
A scheme $X$ is \dfn{normal} if every local ring $\OO_{X,p}$, for $p \in X$, is a normal domain.
:::

::: {.proposition}
A regular local ring is normal, and the converse fails in dimension $\geq 2$.
In dimension $1$ the two agree: a Noetherian local domain of dimension $1$ is normal exactly when it is a discrete valuation ring, that is, regular.
:::

::: {.definition title="Normalization"}
Let $X$ be an integral scheme.
A \dfn{normalization} of $X$ is a normal integral scheme $\widetilde{X}$ with a dominant morphism $\nu \colon \widetilde{X} \to X$ such that every dominant morphism $f \colon Y \to X$ from a normal integral scheme $Y$ factors uniquely as $f = \nu \circ \tilde{f}$ for a morphism $\tilde{f} \colon Y \to \widetilde{X}$.
:::

::: {.theorem title="Existence of the normalization"}
Every integral scheme $X$ has a normalization, unique up to unique isomorphism.
If $X = \Spec A$ is affine, $\widetilde{X} = \Spec \widetilde{A}$ for the integral closure $\widetilde{A}$ of $A$ in its fraction field, and in general $\widetilde{X}$ is obtained by gluing these over an affine cover.
If $X$ is a variety over a field $k$, then $\nu$ is finite and birational, and $\widetilde{X}$ is projective when $X$ is projective.
:::

::: {.proof}
1. For $X = \Spec A$, a dominant morphism $\Spec B \to \Spec A$ from a normal integral affine scheme is an injective ring map $A \to B$, which extends to fraction fields $K(A) \to K(B)$; the image of an element of $\widetilde{A}$ is integral over the image of $A$, hence lies in the integrally closed domain $B$, so $A \to B$ extends uniquely to $\widetilde{A} \to B$.
   For a general normal integral $Y$, apply this on an affine cover of $Y$ and glue by uniqueness.

2. Integral closure commutes with localization, $\widetilde{A_f} = \widetilde{A}_f$, so the affine normalizations glue over an affine cover of $X$, and the universal property holds by step 1 applied locally on $X$.

3. For $A$ a finitely generated $k$-domain, $\widetilde{A}$ is a finite $A$-module (finiteness of integral closure), so $\nu$ is finite; it is birational because $K(\widetilde{A}) = K(A)$.
:::

::: {.remark}
This is the whole answer to how the two notions relate, and the dimension-$1$ case is the one with a consequence: the normalization of a curve is normal, hence regular, hence smooth over a perfect field, so **normalization resolves singularities in dimension one**. That is why resolution is not an issue for curves and is a theorem for surfaces.

The standard normal-but-singular example is the quadric cone $V(xy - z^2) \subseteq \AA^3$, singular at the origin and normal, being regular in codimension one and Cohen--Macaulay — Serre's criterion $R_1 + S_2$.
The standard non-normal example is the cuspidal cubic $k[t^2,t^3] \subseteq k[t]$, whose normalization is $k[t]$.
:::
