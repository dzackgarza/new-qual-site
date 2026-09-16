---
schema: qual/card@1
id: T-LADICPROPER
kind: theorem
title: Proper pushforward preserves constructible $\ell$-adic sheaves
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

::: {.definition title="Constructible $\ell$-adic sheaf"}
Let $X$ be a scheme of finite type over a field and $\ell$ a prime invertible on $X$.
A \dfn{constructible $\ell$-adic sheaf} is a projective system $\mcf = (\mcf_n)_{n \geq 1}$ of constructible étale sheaves of $\ZZ/\ell^n$-modules with $\mcf_{n+1} \otimes_{\ZZ/\ell^{n+1}} \ZZ/\ell^n \cong \mcf_n$.
:::

::: {.theorem title="Finiteness of proper pushforward"}
Let $f \colon X \to Y$ be a morphism of schemes of finite type over a field, with $\ell$ invertible, and $\mcf$ a constructible $\ell$-adic sheaf on $X$.
Then $R^i f_! \mcf = (R^i f_! \mcf_n)_n$ is, up to Artin--Rees equivalence, a constructible $\ell$-adic sheaf on $Y$.
:::

::: {.proof}
1. *Finiteness in each level:* for a constructible sheaf of $\ZZ/\ell^n$-modules, $R^i f_! \mcf_n$ is constructible and vanishes for $i > 2 \dim X$, by proper base change and the finiteness theorem for proper morphisms.
2. *Compatibility of levels:* $f_!$ has finite cohomological dimension and commutes with derived tensor product with $\ZZ/\ell^n$, so $Rf_! \mcf_{n+1} \otimes^L \ZZ/\ell^n \simeq Rf_! \mcf_n$.
3. *Passage to the system:* the resulting long exact sequences relate $R^i f_! \mcf_{n+1} \otimes \ZZ/\ell^n$ to $R^i f_! \mcf_n$ up to $\operatorname{Tor}$ terms with uniformly bounded exponent, and these form an essentially zero system, so the $R^i f_! \mcf_n$ form an $\ell$-adic sheaf up to Artin--Rees equivalence.
:::

::: {.remark}
For $Y = \Spec \overline{\FF}_q$, this is the statement that $H^i_c(X_{\overline{\FF}_q}, \QQ_\ell) = \big(\varprojlim_n H^i_c(X, \ZZ/\ell^n)\big) \otimes \QQ_\ell$ is finite-dimensional, which is what the Grothendieck--Lefschetz trace formula needs.
:::
