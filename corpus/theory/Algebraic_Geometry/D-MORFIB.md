---
schema: qual/card@1
id: D-MORFIB
kind: definition
title: The fibre of a morphism as a base change
classification:
  areas:
  - algebraic-geometry
  topics:
  - Fibres
  - Fibre Products
  - Residue Fields
relations:
- kind: related-to
  target: D-VKR54
review: draft
prompts:
- What is the fibre of a morphism of schemes?
- Why is the fibre taken over the residue field rather than the point?
- What is a geometric point, and a geometric fibre?
- What does it mean for a morphism to have geometrically connected, irreducible, reduced or integral fibres?
---

::: {.definition title="Fibre"}
For $f : X \to Y$ and $y \in Y$ with residue field $\kappa(y) = \OO_{Y,y}/\mfm_y$, the **fibre** is
\[
X_y \da \fiberprod{X}{Y}{\Spec \kappa(y)} .
\]
:::

::: {.definition title="Geometric points and fibres"}
A \dfn{geometric point} of a scheme $Y$ is a morphism $\bar{y} \colon \Spec \Omega \to Y$ with $\Omega$ an algebraically closed field.
The \dfn{geometric fibre} of $f \colon X \to Y$ over $\bar{y}$ is $X_{\bar{y}} = X \times_Y \Spec \Omega$.
For a property $P$ of schemes over a field such as connected, irreducible, reduced or integral, $f$ has \dfn{geometrically $P$ fibres} if every geometric fibre has $P$, and a $k$-scheme $X$ is \dfn{geometrically $P$} if $X \times_k \Spec \bar{k}$ has $P$.
:::

::: {.example}
$X = \Spec \QQ(i) \to \Spec \QQ$ has a one-point fibre, which is integral, but its geometric fibre $\Spec \QQ(i) \otimes_\QQ \overline{\QQ} \cong \Spec \overline{\QQ} \sqcup \Spec \overline{\QQ}$ is not connected.
Over $k = \FF_p(t)$, $\Spec k[x]/(x^p - t)$ is integral, and after base change to $\bar{k}$ it becomes $\Spec \bar{k}[x]/((x - t^{1/p})^p)$, which is not reduced.
:::

::: {.remark}
The definition is a base change and not a preimage, and that is the point: $f^{-1}(y)$ is only a set, while $X_y$ is a scheme over a field, so it has a dimension, a length, a genus, and a cohomology.
Taking $\kappa(y)$ rather than $\OO_{Y,y}$ is what makes it a scheme over a field; taking $\OO_{Y,y}$ instead gives the local picture of the family near $y$, which is the other useful base change.

The underlying space of $X_y$ is homeomorphic to $f^{-1}(y)$, so nothing is lost and the scheme structure is gained.
That structure is where the exam questions live: the fibres of $\Spec \ZZ[i] \to \Spec \ZZ$ are two points, one point, or a fat point according as $p$ splits, is inert, or ramifies, and the length of the fibre is $2$ in every case.
That constancy is flatness, and it is the model for every statement that a numerical invariant is constant in a flat family.
:::
