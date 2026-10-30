---
schema: qual/card@1
id: T-MORSMREG
kind: theorem
title: Smoothness and regularity over a field
slogan: 'Smoothness is geometric regularity: over a perfect field, finite-type schemes are smooth exactly when they are regular.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Smooth Morphisms
  - Regularity
  - Singularities
relations:
- kind: uses
  target: D-MORSM
- kind: related-to
  target: PR-MORJAC
review: draft
prompts:
- How is smoothness related to regularity?
- Is a regular scheme smooth?
- State the Jacobian criterion and the criterion for smoothness over a field by differentials.
---

::: {.theorem}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$.
If $X \to \Spec k$ is smooth of relative dimension $n$ then $X$ is regular of dimension $n$.
The converse holds when $k$ is perfect, in particular when $k = \kbar$, and fails otherwise.
:::

::: {.theorem title="Smoothness over a field"}
Let $k$ be a field and $X$ a scheme locally of finite type over $k$, of pure dimension $n$. The following are equivalent.

1. $X$ is smooth over $k$.

2. $\Omega_{X/k}$ is locally free of rank $n$.

3. $X_{\bar{k}} = X \times_k \Spec \bar{k}$ is regular.

If $k$ is perfect, these are also equivalent to: $X$ is regular.

[@Har77, Theorem II.8.15, Theorem III.10.2]
:::

::: {.remark}
Smoothness is a property of a morphism, while regularity is a property of local rings.
For a finite-type scheme over a field, smoothness is geometric regularity: it is equivalent to regularity after extension to an algebraic closure. Over a perfect field, regularity is already geometric, so regular and smooth coincide.

For an affine presentation by generators of the scheme-theoretic defining ideal, [[PR-MORJAC]] computes the tangent-space dimension from the Jacobian matrix and gives the corresponding smoothness criterion over an algebraically closed field.

Over an imperfect field the converse fails: for $k=\FF_p(t)$, $X=\Spec k[x]/(x^p-t)$ is the spectrum of a field and hence regular, while $X_{\bar k}=\Spec \bar k[x]/(x-t^{1/p})^p$ is nonreduced, so $X$ is not smooth over $k$.

A smooth morphism has geometrically regular fibres. Regularity of the total space is a separate question: if the base is regular then a smooth total space is regular, while an open immersion from the regular locus of a singular scheme is smooth with regular source even though the ambient base is singular.
:::
