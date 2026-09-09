---
schema: qual/card@1
id: P-HMX5O
kind: problem
title: Induced representations
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Give two definitions of "induced representation".
Why are they equivalent?
:::


::: {.solution}
Let $H\le G$ be a subgroup, let $k$ be a field, and let $V$ be a left $k[H]$-module.

<1>1. The tensor-product definition is
\[
\operatorname{Ind}_H^G V
=
k[G]\otimes_{k[H]}V,
\]
with $G$ acting by left multiplication on the $k[G]$ factor.
::: {.proof}
For $g\in G$ define
\[
g\cdot(x\otimes v)=(gx)\otimes v.
\]
This is well defined because left multiplication commutes with the balancing relation
\[
xh\otimes v=x\otimes hv.
\]
:::

<1>2. The function-model definition is
\[
\mathcal F
=
\{f:G\to V:f(gh)=h^{-1}f(g)\text{ for all }g\in G,h\in H\},
\]
with
\[
(g_0\cdot f)(g)=f(g_0^{-1}g).
\]
::: {.proof}
The covariance relation is preserved by left translation, so this is a $G$-representation.
:::

<1>3. Choose representatives $T\subseteq G$ for the left cosets $G/H$. Then both models are naturally isomorphic, as vector spaces, to
\[
\bigoplus_{t\in T} V.
\]
::: {.proof}
For the tensor model,
\[
k[G]=\bigoplus_{t\in T} t\,k[H]
\]
as a right $k[H]$-module, hence
\[
k[G]\otimes_{k[H]}V
\cong
\bigoplus_{t\in T}V.
\]

For the function model, the covariance relation determines $f$ uniquely from the values $f(t)$ on the representatives $t\in T$. Thus evaluation on $T$ gives the same direct-sum vector space.
:::

<1>4. The two identifications in <1>3 intertwine the $G$-actions.
::: {.proof}
For each $g\in G$ and $t\in T$, write uniquely
\[
gt=t'h
\qquad(t'\in T,\ h\in H).
\]
In the tensor model,
\[
g\cdot(t\otimes v)=t'h\otimes v=t'\otimes hv.
\]
In the function model, left translation produces exactly the same permutation of cosets together with the same $H$-action on the corresponding $V$-coordinate. Hence the two $G$-modules are isomorphic.
:::

Therefore the tensor-product and equivariant-function constructions are equivalent definitions of induction.
:::
