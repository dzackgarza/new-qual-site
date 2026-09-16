---
schema: qual/card@1
id: D-MODAMPLE
kind: definition
title: Ample and very ample invertible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ampleness
  - Line Bundles
  - Projective Morphisms
relations:
- kind: uses
  target: D-MODGG
- kind: uses
  target: D-MODPULL
review: draft
prompts:
- Define ample and very ample.
- What is the relation between the two?
- Why is a proper scheme with a very ample sheaf projective?
---

::: {.definition title="Ample, very ample"}
$\mcl \in \Pic(X)$ is \dfn{very ample} over $Y$ if there is an immersion $\iota: X \to \PP^n_Y$ with $\iota^*\OO(1) \cong \mcl$.
$\mcl$ is **ample** if for every coherent $\mcf$ there is $N_0$ with $\mcf \tensor \mcl^{\tensor n}$ globally generated for all $n \geq N_0$.
:::

::: {.theorem}
For $X$ of finite type over a Noetherian ring $A$: $\mcl$ is ample if and only if $\mcl^{\tensor m}$ is very ample over $\Spec A$ for some $m > 0$.
:::

::: {.remark}
Very ampleness is a statement about one sheaf and an embedding; ampleness is a statement about all coherent sheaves and is stable under taking powers.
The theorem says they differ only by that instability, which is why ampleness is the notion that behaves well in families and very ampleness is the notion you verify.

The immediate consequence to have ready is that a proper $X$ over $Y$ carrying a very ample sheaf is projective: the immersion $\iota$ has closed image by properness, so it is a closed immersion.
Conversely a projective $X$ has $\iota^*\OO(1)$ very ample by definition, so over a Noetherian base "projective" is "proper plus a very ample sheaf", which is the form the question is usually asked in.
Ampleness is also where the numerical criteria live: on a curve $\mcl$ is ample exactly when $\deg \mcl > 0$.
:::
