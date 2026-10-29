---
schema: qual/card@1
id: T-LADICPROPER
kind: theorem
title: Proper-support pushforward preserves constructible $\ell$-adic sheaves
slogan: 'Proper-support pushforward preserves constructible $\ell$-adic sheaves, so compact-support $\ell$-adic cohomology stays finite-dimensional.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Etale Cohomology
  - L-adic Sheaves
  - Constructible Sheaves
relations:
- kind: uses
  target: D-SHFCONSTR
- kind: uses
  target: T-BASECHANGE
review: draft
prompts:
- Why are higher direct images with proper support of $\ell$-adic sheaves again $\ell$-adic?
---

::: {.theorem title="Finiteness under proper-support pushforward"}
Let $f\colon X\to Y$ be a separated morphism of finite type between schemes of finite type over a field, let $\ell$ be invertible on $Y$, and let $\mcf$ be a constructible $\ell$-adic sheaf on $X$ in the sense of [[D-SHFCONSTR]].
Then each higher direct image with proper support
$$
R^if_!\mcf
$$
is a constructible $\ell$-adic sheaf on $Y$. If $f$ is proper, then $Rf_!=Rf_*$, so every $R^if_*\mcf$ is constructible $\ell$-adic.
:::

::: {.remark}
For $Y = \Spec \overline{\FF}_q$, constructibility gives finite-dimensional compactly supported cohomology
$$
H^i_c(X_{\overline{\FF}_q},\QQ_\ell).
$$
For a proper $X$, compactly supported and ordinary étale cohomology agree. These finite-dimensional $\QQ_\ell$-vector spaces are the cohomology groups appearing in the Grothendieck--Lefschetz trace formula.
:::
