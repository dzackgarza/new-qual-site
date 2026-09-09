---
schema: qual/card@1
id: P-ALGS06F
kind: problem
title: "Projective, flat, and injective module constructions via tensor and Hom"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $R$ be a commutative ring and let $M$ and $N$ be $R$-modules.
Prove the following.

(a) If $M$ and $N$ are projective $R$-modules, then $M \otimes_R N$ is a projective $R$-module.

(b) If $M$ and $N$ are flat $R$-modules, then $M \otimes_R N$ is a flat $R$-module.

(c) If $M$ is a flat $R$-module and $N$ is an injective $R$-module, then $\operatorname{Hom}_R(M, N)$ is an injective $R$-module.

(d) Let $p$ be a prime number and let $\mathbb{Z}_{(p)}$ denote the localization of $\mathbb{Z}$ with respect to its prime ideal $p\mathbb{Z}$.
Show that $\operatorname{Hom}_\mathbb{Z}(\mathbb{Z}_{(p)}, \mathbb{Q}/\mathbb{Z})$ is an injective $\mathbb{Z}$-module.
:::

::: {.solution}
<1>1. If $M$ and $N$ are projective, then $M\otimes_R N$ is projective.
::: {.proof}
Choose free modules $F,G$ and modules $M',N'$ with
\[
F\cong M\oplus M',\qquad G\cong N\oplus N'.
\]
Then
\[
F\otimes_R G
\cong (M\otimes_RN)\oplus(M\otimes_RN')\oplus(M'\otimes_RN)\oplus(M'\otimes_RN').
\]
The tensor product of free modules is free: if $F\cong R^{(I)}$ and $G\cong R^{(J)}$, then
\[
F\otimes_RG\cong R^{(I\times J)}.
\]
Thus $M\otimes_RN$ is a direct summand of a free module, hence projective.
:::

<1>2. If $M$ and $N$ are flat, then $M\otimes_RN$ is flat.
::: {.proof}
For every $R$-module $X$ there is a natural isomorphism
\[
X\otimes_R(M\otimes_RN)\cong (X\otimes_RM)\otimes_RN.
\]
The functor $-\otimes_RM$ is exact because $M$ is flat, and $-\otimes_RN$ is exact because $N$ is flat. Their composition is exact, so $-\otimes_R(M\otimes_RN)$ is exact. Hence $M\otimes_RN$ is flat.
:::

<1>3. If $M$ is flat and $N$ is injective, then $\operatorname{Hom}_R(M,N)$ is injective.
::: {.proof}
For every $R$-module $X$, tensor--Hom adjunction gives a natural isomorphism
\[
\operatorname{Hom}_R\!\left(X,\operatorname{Hom}_R(M,N)\right)
\cong
\operatorname{Hom}_R(X\otimes_RM,N).
\]
The functor $-\otimes_RM$ is exact because $M$ is flat. The contravariant functor $\operatorname{Hom}_R(-,N)$ is exact because $N$ is injective. Therefore
\[
X\longmapsto \operatorname{Hom}_R\!\left(X,\operatorname{Hom}_R(M,N)\right)
\]
is exact, which is exactly the injectivity criterion for $\operatorname{Hom}_R(M,N)$.
:::

<1>4. The $\mathbb Z$-module $\mathbb Z_{(p)}$ is flat, and $\mathbb Q/\mathbb Z$ is injective.
::: {.proof}
Every localization of a commutative ring is flat over the original ring, so $\mathbb Z_{(p)}$ is flat over $\mathbb Z$.
The abelian group $\mathbb Q/\mathbb Z$ is divisible: for every nonzero integer $n$, multiplication by $n$ is surjective. Over the PID $\mathbb Z$, divisible modules are injective by Baer's criterion.
:::

<1>5. Therefore
\[
\operatorname{Hom}_\mathbb Z(\mathbb Z_{(p)},\mathbb Q/\mathbb Z)
\]
is an injective $\mathbb Z$-module.
::: {.proof}
Apply <1>3 with $R=\mathbb Z$, $M=\mathbb Z_{(p)}$, and $N=\mathbb Q/\mathbb Z$, using <1>4.
:::
:::
