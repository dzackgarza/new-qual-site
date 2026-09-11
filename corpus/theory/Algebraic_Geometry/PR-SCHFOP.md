---
schema: qual/card@1
id: PR-SCHFOP
kind: proposition
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

::: {.definition}
For $X \in \Sch\slice S$ and $T \in \Sch\slice S$, a **$T$-valued point** of $X$ is a morphism $T \to X$ over $S$.
The assignment $T \mapsto X(T) \da \Hom_S(T, X)$ is the **functor of points** of $X$, and $X \mapsto X(-)$ is fully faithful into $\Sets^{\Sch\slice S \op}$ by Yoneda.
:::

::: {.proposition}
- Morphisms $\Spec L \to X$, for $L$ a field, correspond to pairs: a point $x \in X$ and a field embedding $\kappa(x) \injects L$.
- Morphisms $\Spec k[\eps]/\eps^2 \to X$ for $X$ over $k$ correspond to pairs: a $k$-rational point $x$, and a tangent vector in $(\mfm_x/\mfm_x^2)\dual$.
:::

::: {.remark}
The functor of points is what makes the fibre product's universal property usable, and it is how you recover the naive picture: $X(k)$ for $k$ algebraically closed is the classical variety, and $X(\ZZ)$ or $X(\QQ)$ is what a number theorist means by the solutions.

The two computations above are the ones asked for, and they are the reason each test scheme is standard: a field detects a point together with how much of its residue field you can see, and the dual numbers detect a tangent vector.
Replacing $k[\eps]/\eps^2$ by $k[t]/t^n$ detects an $n$-th order arc, which is where jet schemes come from.

The usable slogan is that a scheme is determined by what maps into it, so constructing a scheme can be replaced by writing down a functor and proving it representable — this is how Hilbert and Picard schemes are defined.
:::
