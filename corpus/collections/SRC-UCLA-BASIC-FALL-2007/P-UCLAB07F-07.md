---
schema: qual/card@1
id: P-UCLAB07F-07
kind: problem
title: Derivative of a matrix inverse
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Let $A(x)$ be a differentiable matrix-valued function on $\mathbb R$, with $A(x)$ invertible for every $x$.
Starting from entrywise differentiation, show that $A^{-1}(x)$ is differentiable and \[(A^{-1})'(x)=-A^{-1}(x)A'(x)A^{-1}(x).\]
:::

::: {.solution}
Write
\[
A(x)=(a_{ij}(x)).
\]

<1>1. Every entry of $\operatorname{adj}(A(x))$ is differentiable.

::: {.proof}
Each entry of the adjugate matrix is, up to sign, the determinant of an $(n-1)\times(n-1)$ minor of $A(x)$. Expanding that determinant expresses it as a polynomial in the entries $a_{ij}(x)$. Since each $a_{ij}$ is differentiable, every such polynomial is differentiable.
:::

<1>2. The scalar function
\[
x\longmapsto\det A(x)
\]
is differentiable and never vanishes.

::: {.proof}
The determinant is a polynomial in the entries of $A(x)$, hence differentiable by entrywise differentiability. Since $A(x)$ is invertible for every $x$,
\[
\det A(x)\ne0
\]
for every $x$.
:::

<1>3. The matrix-valued function $A^{-1}(x)$ is differentiable entrywise.

::: {.proof}
By the adjugate formula,
\[
A^{-1}(x)
=
\frac{\operatorname{adj}(A(x))}{\det A(x)}.
\]
By steps <1>1--<1>2, each numerator entry is differentiable and the denominator is a differentiable scalar function that never vanishes. Therefore every entry of $A^{-1}(x)$ is differentiable.
:::

<1>4. Differentiating
\[
A(x)A^{-1}(x)=I
\]
entrywise gives
\[
A'(x)A^{-1}(x)+A(x)(A^{-1})'(x)=0.
\]

::: {.proof}
The $(i,j)$ entry of the product $A(x)A^{-1}(x)$ is
\[
\sum_{k=1}^n a_{ik}(x)b_{kj}(x),
\]
where
\[
A^{-1}(x)=(b_{ij}(x)).
\]
By step <1>3, all $b_{ij}$ are differentiable. Applying the ordinary product rule term by term yields
\[
\frac{d}{dx}\bigl(A(x)A^{-1}(x)\bigr)
=
A'(x)A^{-1}(x)+A(x)(A^{-1})'(x).
\]
The derivative of the constant matrix $I$ is zero.
:::

<1>5. One has
\[
\boxed{
(A^{-1})'(x)
=
-A^{-1}(x)A'(x)A^{-1}(x)
}.
\]

::: {.proof}
Multiply the identity in step <1>4 on the left by $A^{-1}(x)$:
\[
A^{-1}A'A^{-1}+(A^{-1})'=0.
\]
Rearranging gives the displayed formula.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>3 proves differentiability of the inverse matrix, and step <1>5 gives its derivative.
:::
:::
