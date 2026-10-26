---
schema: qual/card@1
id: P-UCLAB07F-06
kind: problem
title: Dimension formulas involving a linear map and its adjoint
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $T:V\to W$ be a linear transformation between finite-dimensional vector spaces.
Compute, with proof, \[\dim(\operatorname{Null}T)+\dim(\operatorname{Range}T)\] and \[\dim(\operatorname{Null}T^*)+\dim(\operatorname{Range}T)\] in terms of $\dim V$ and $\dim W$, where $T^*$ is the adjoint of $T$.
:::

The use of the adjoint implicitly equips $V$ and $W$ with inner products.

::: pf

::: pf-step

One has
\[
\boxed{
\dim(\operatorname{Null}T)
+
\dim(\operatorname{Range}T)
=
\dim V
}.
\]


::: pf-proof

This is the rank-nullity theorem for the linear map
\[
T:V\to W.
\]

:::

:::

::: pf-step

The orthogonal complement of $\operatorname{Range}T$ is
\[
(\operatorname{Range}T)^\perp
=
\operatorname{Null}T^*.
\]


::: pf-proof

Let $w\in W$. Then
\[
w\in(\operatorname{Range}T)^\perp
\]
if and only if
\[
\langle Tv,w\rangle_W=0
\]
for every $v\in V$. By the defining property of the adjoint,
\[
\langle Tv,w\rangle_W
=
\langle v,T^*w\rangle_V.
\]
Thus the displayed vanishing holds for all $v\in V$ if and only if
\[
T^*w=0.
\]
Hence the two subspaces are equal.

:::

:::

::: pf-step

One has
\[
\dim(\operatorname{Null}T^*)
=
\dim W-\dim(\operatorname{Range}T).
\]


::: pf-proof

By step <1>2,
\[
\operatorname{Null}T^*
=
(\operatorname{Range}T)^\perp.
\]
For every subspace $Y$ of a finite-dimensional inner-product space,
\[
\dim Y+\dim Y^\perp=\dim W.
\]
Apply this to
\[
Y=\operatorname{Range}T.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\dim(\operatorname{Null}T^*)
+
\dim(\operatorname{Range}T)
=
\dim W
}.
\]


::: pf-proof

Add $\dim(\operatorname{Range}T)$ to both sides of the equality in step <1>3.

:::

:::

::: pf-qed

Step <1>1 gives the first requested quantity, and step <1>4 gives the second.

:::

:::
