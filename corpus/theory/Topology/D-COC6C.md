---
schema: qual/card@1
id: D-COC6C
kind: definition
title: Coproduct
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $\mathcal C$ be a category and $(X_\alpha)_{\alpha\in A}$ a family of objects of $\mathcal C$.
A \dfn{coproduct} of $(X_\alpha)_{\alpha\in A}$ is an object $\coprod_{\alpha\in A} X_\alpha$ together with morphisms $\iota_\beta\colon X_\beta\to\coprod_{\alpha\in A} X_\alpha$ for $\beta\in A$ such that for every object $Y$ and every family of morphisms $f_\beta\colon X_\beta\to Y$ there is a unique morphism $f\colon\coprod_{\alpha\in A} X_\alpha\to Y$ with $f\circ\iota_\beta = f_\beta$ for every $\beta\in A$.
:::

::: {.remark}
The coproduct in $\mathcal C$ is the product in the opposite category $\mathcal C^{\mathrm{op}}$.
By the uniqueness in the definition, two coproducts of the same family are isomorphic by a unique isomorphism compatible with the morphisms $\iota_\beta$.
:::

::: {.example}
In $\Top$ the coproduct is the disjoint union $\coprod_\alpha X_\alpha$, a subset $U$ being open if $U\cap X_\alpha$ is open in $X_\alpha$ for every $\alpha$.
In the category of based spaces it is the [[D-IGUUS|wedge sum]] $\bigvee_\alpha X_\alpha$.
In $\Ab$ it is the [[D-TZSG2|direct sum]] $\bigoplus_\alpha X_\alpha$, and in $\Grp$ it is the [[D-JDDCP|free product]] $\ast_\alpha X_\alpha$.
:::

::: {.concept}
See [@Hat02].
:::
