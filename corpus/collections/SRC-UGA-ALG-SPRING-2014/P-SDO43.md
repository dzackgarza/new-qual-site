---
schema: qual/card@1
id: P-SDO43
kind: problem
title: Surjective $R$-linear endomorphisms of $R^n$ are injective, but injective ones
  need not be surjective
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Rank and Nullity
  - Modules
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $R$ be a commutative ring with identity and let $n$ be a positive integer.

a. Prove that every surjective $R\dash$linear endomorphism $T: R^n \to R^n$ is injective.

b. Show that an injective $R\dash$linear endomorphism of $R^n$ need not be surjective.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every surjective $R$-linear endomorphism $T:R^n\to R^n$ is injective.


::: pf-proof

Let $A\in M_n(R)$ represent $T$. For each standard basis vector $e_i$, surjectivity supplies a vector $v_i$ such that $Av_i=e_i$. Form the matrix $B$ with columns $v_i$. Then $AB=I_n$. Taking determinants in the commutative ring $R$ gives $\det(A)\det(B)=1$, so $\det(A)$ is a unit. The adjugate identity $A\operatorname{adj}(A)=\det(A)I_n$ then supplies an inverse $\det(A)^{-1}\operatorname{adj}(A)$ for $A$. Thus $T$ is an isomorphism, in particular injective.

:::

:::

::: {.pf-step #s1-2}

An injective endomorphism of a finite-rank free module need not be surjective.


::: pf-proof

Take $R=\ZZ$ and $n=1$. Multiplication by $2$ defines an injective endomorphism $T:\ZZ\to\ZZ$ because $2m=0$ implies $m=0$. It is not surjective because $1\notin 2\ZZ$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} establish parts (a) and (b), respectively.

:::

:::

:::
