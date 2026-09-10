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

::: problem
Let $R$ be a commutative ring with identity and let $n$ be a positive integer.

a. Prove that every surjective $R\dash$linear endomorphism $T: R^n \to R^n$ is injective.

b. Show that an injective $R\dash$linear endomorphism of $R^n$ need not be surjective.
:::

::: solution
For (a), let $A\in M_n(R)$ be the matrix of $T$ in the standard basis. Because $T$ is surjective, for each standard basis vector $e_i$ choose $v_i\in R^n$ with $T(v_i)=e_i$. Let $B$ be the matrix whose $i$th column is $v_i$. Then
\[
AB=I.
\]
Taking determinants in the commutative ring $R$ gives
\[
\det(A)\det(B)=1,
\]
so $\det(A)$ is a unit. The adjugate identity
\[
A\operatorname{adj}(A)=\det(A)I
\]
therefore shows that
\[
A^{-1}=\det(A)^{-1}\operatorname{adj}(A).
\]
Thus $T$ is invertible, in particular injective.

For (b), take $R=\mathbb Z$, $n=1$, and
\[
T:\mathbb Z\to\mathbb Z,
\qquad
T(m)=2m.
\]
This map is injective, but it is not surjective because $1$ is not in its image.
:::
