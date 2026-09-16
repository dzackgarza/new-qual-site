---
schema: qual/card@1
id: D-SHFSIX
kind: definition
title: The six operations on sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Six Functor Formalism
  - Derived Categories
  - Verdier Duality
relations:
- kind: uses
  target: D-COHDER
review: draft
prompts:
- What is the six functor formalism?
- What is the extension by zero sheaf, and what are its stalks?
- What is the exceptional inverse image?
---

::: {.definition title="Extension by zero"}
Let $j \colon U \hookrightarrow X$ be the inclusion of an open subset and $\mathcal{F}$ a sheaf of abelian groups on $U$.
The \dfn{extension by zero} $j_! \mathcal{F}$ is the sheafification of the presheaf $V \mapsto \mathcal{F}(V)$ if $V \subseteq U$, and $V \mapsto 0$ otherwise.
Its stalks are $(j_! \mathcal{F})_x = \mathcal{F}_x$ for $x \in U$ and $0$ for $x \notin U$; $j_!$ is exact and left adjoint to $j^{-1}$.
:::

::: {.definition title="Six operations"}
For a continuous map $f \colon X \to Y$ of locally compact Hausdorff spaces, the \dfn{six operations} on bounded-below derived categories of sheaves of abelian groups are
\[
f^{-1} \dashv Rf_*, \qquad Rf_! \dashv f^!, \qquad \otimes^L \dashv R\mathcal{H}om .
\]
Here $f_!$ is direct image with proper supports: $(f_! \mathcal{F})(V)$ consists of the sections $s \in \mathcal{F}(f^{-1}V)$ whose support is proper over $V$.
The \dfn{exceptional inverse image} $f^!$ is the right adjoint of $Rf_!$; it exists on derived categories when $f_!$ has finite cohomological dimension, and is not the derived functor of a functor on sheaves.
:::

::: {.proposition}
1. For $f$ proper, $Rf_! = Rf_*$; for $j$ an open inclusion, $j^! = j^{-1}$.
2. Base change: for a Cartesian square with $g \colon Y' \to Y$ and $f' \colon X' \to Y'$, $g^{-1} Rf_! \cong Rf'_! g'^{-1}$.
3. Projection formula: $Rf_!(\mathcal{F} \otimes^L f^{-1} \mathcal{G}) \cong Rf_! \mathcal{F} \otimes^L \mathcal{G}$.
4. Verdier duality: for $a \colon X \to \mathrm{pt}$, the \dfn{dualizing complex} is $\omega_X = a^! \ZZ$, and for a topological manifold of dimension $n$ it is the orientation sheaf placed in degree $-n$.
   For a closed inclusion $i \colon Z \hookrightarrow X$, $i^! \mathcal{F}$ is the derived functor of sections of $\mathcal{F}$ supported in $Z$, restricted to $Z$.
:::

::: {.remark}
The same formalism holds for constructible sheaves on complex algebraic varieties and for $\ell$-adic sheaves on schemes of finite type over a field, where it is the framework for Poincaré duality and the Lefschetz trace formula.
:::
