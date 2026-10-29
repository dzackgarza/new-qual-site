---
schema: qual/card@1
id: PR-SCHFOP
kind: definition
title: The functor of points, and what small test schemes detect
classification:
  areas:
  - algebraic-geometry
  topics:
  - Functor Of Points
  - Residue Fields
  - Tangent Spaces
relations:
- kind: uses
  target: D-SCHFPR
- kind: related-to
  target: FE-O12TX
review: draft
prompts:
- What is a $T$-valued point of a scheme?
- Characterise morphisms $\Spec L \to X$ for $L$ a field.
- Characterise morphisms $\Spec k[\eps]/\eps^2 \to X$.
---

Fields detect points with residue-field embeddings; dual numbers detect tangent vectors.

::: {.definition}
For $X \in \Sch\slice S$ and $T \in \Sch\slice S$, a \dfn{$T$-valued point} of $X$ is a morphism $T \to X$ over $S$.
The assignment
$$
T\longmapsto X(T)\coloneqq\Hom_S(T,X)
$$
is the \dfn{functor of points} of $X$.
Yoneda gives a fully faithful embedding
$$
\Sch\slice S\longrightarrow\operatorname{Fun}\bigl((\Sch\slice S)^{\mathrm{op}},\Sets\bigr),
\qquad
X\longmapsto X(-).
$$
:::

::: {.proposition}
- For any scheme $X$ and field $L$, morphisms $\Spec L \to X$ correspond to pairs consisting of a point $x \in X$ and a field embedding $\kappa(x) \hookrightarrow L$.

- If $X$ is a $k$-scheme, then $k$-morphisms $\Spec k[\eps]/(\eps^2) \to X$ correspond to pairs consisting of a $k$-rational point $x\in X(k)$ and a tangent vector
  $$
  v\in T_xX\cong\Hom_k(\mfm_x/\mfm_x^2,k).
  $$
:::

::: {.remark}
If $X$ is a variety over an algebraically closed field $k$, the set $X(k)$ identifies with the closed points of $X$.

These two computations explain the standard test schemes: a field detects a point together with a residue-field embedding, while the dual numbers detect a tangent vector.
Replacing the dual numbers by $k[t]/(t^{n+1})$ gives an $n$-jet.
The jet functor of a $k$-scheme $X$ sends a $k$-scheme $T$ to
$$
\Hom_k\bigl(T\times_k\Spec k[t]/(t^{n+1}),X\bigr).
$$

Since Yoneda is fully faithful, a scheme is determined up to unique isomorphism by its functor of points.
Moduli constructions therefore begin by specifying a functor and asking whether it is representable by a scheme or by a broader geometric object.
:::
