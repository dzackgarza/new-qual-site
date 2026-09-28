---
schema: qual/card@1
id: D-QJ5M9
kind: definition
title: Normal domains and schemes, and their relation to regularity
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
If $X$ is a variety over a field $k$, then $\nu$ is finite and birational, and $\widetilde{X}$ is projective when $X$ is projective [@Har10a, Exercise II.3.8].
:::

::: {.remark}
The normalization of an integral curve is regular, hence smooth over a perfect field. Thus normalization resolves singularities of curves over perfect fields.

The quadric cone $V(xy - z^2) \subseteq \AA^3$ is normal and singular at the origin: it is regular in codimension one and Cohen--Macaulay, so it is normal by Serre's criterion $R_1 + S_2$.
The cuspidal cubic, with coordinate ring $k[t^2,t^3] \subseteq k[t]$, is not normal, and its normalization is $\Spec k[t]$.
:::
