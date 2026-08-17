---
schema: qual/card@1
id: P-LW3KB
kind: problem
title: "Let $V$ be a vector space over a field $F$ and $V\\dual$ its dual."
classification:
  areas:
  - algebra
  topics:
  - bilinear-forms
  - dual-spaces
  - vector-spaces
relations: []
review: draft
solved: false
---

::: problem
Let $V$ be a vector space over a field $F$ and $V\dual$ its dual.
A *symmetric bilinear form* $(\wait, \wait)$ on $V$ is a map $V\cross V\to F$ satisfying
\[
(av_1 + b v_2, w) = a(v_1, w) + b(v_2, w) \qtext{and} (v_1, v_2) = (v_2, v_1)
\]
for all $a, b\in F$ and $v_1, v_2 \in V$.
The form is *nondegenerate* if the only element $w\in V$ satisfying $(v, w) = 0$ for all $v\in V$ is $w=0$.

Suppose $(\wait, \wait)$ is a nondegenerate symmetric bilinear form on $V$.
If $W$ is a subspace of $V$, define
\[
W^{\perp} \definedas \theset{v\in V \suchthat (v, w) = 0 \text{ for all } w\in W}
.\]

a.
Show that if $X, Y$ are subspaces of $V$ with $Y\subset X$, then $X^{\perp} \subseteq Y^{\perp}$.

b.
Define an injective linear map 
\[
\psi: Y^{\perp}/X^{\perp} \injects (X/Y)\dual
\]
which is an isomorphism if $V$ is finite dimensional.
:::
