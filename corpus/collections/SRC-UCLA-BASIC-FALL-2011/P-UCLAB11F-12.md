---
schema: qual/card@1
id: P-UCLAB11F-12
kind: problem
title: Least-squares minimizers differ by a kernel vector
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 12. Let $A$ be an $m\times n$ real matrix and let $b\in\mathbb R^m$.
Suppose $Ax$ and $Ay$ both have minimal distance to $b$ among all vectors in $\operatorname{image}(A)$.
Prove that
\[
x-y\in\ker A.
\]
:::

Let
\[
M=\operatorname{image}(A)\subseteq\mathbb R^m.
\]

::: pf

::: pf-step

The nearest point in the subspace $M$ to $b$ is unique.


::: pf-proof

Suppose
\[
u,v\in M
\]
both minimize the Euclidean distance to $b$, and let
\[
d=\|b-u\|=\|b-v\|.
\]
Since $M$ is a subspace,
\[
\frac{u+v}{2}\in M.
\]
Using the parallelogram identity with
\[
p=b-u,
\qquad
q=b-v,
\]
one obtains
\[
\left\|b-\frac{u+v}{2}\right\|^2
=
\frac12\|b-u\|^2
+
\frac12\|b-v\|^2
-
\frac14\|u-v\|^2.
\]
Thus
\[
\left\|b-\frac{u+v}{2}\right\|^2
=
d^2-\frac14\|u-v\|^2.
\]
If $u\ne v$, the right side is strictly smaller than $d^2$, contradicting minimality of $d$. Hence
\[
u=v.
\]

:::

:::

::: pf-step

Under the hypotheses of the problem,
\[
Ax=Ay.
\]


::: pf-proof

The vectors $Ax$ and $Ay$ both belong to
\[
M=\operatorname{image}(A)
\]
and both have minimal distance to $b$. By uniqueness from step <1>1, they are equal.

:::

:::

::: pf-step

One has
\[
A(x-y)=0.
\]


::: pf-proof

By linearity of $A$ and step <1>2,
\[
A(x-y)
=
Ax-Ay
=0.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{x-y\in\ker A}.
\]


::: pf-proof

Step <1>3 is exactly the defining condition for membership in the kernel of $A$.

:::

:::

::: pf-qed

Step <1>4 is the required conclusion.

:::

:::
