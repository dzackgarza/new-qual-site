---
schema: qual/card@1
id: P-UCLAB11S-05
kind: problem
title: Solvability via the orthogonal complement of the transpose kernel
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $A$ be an $n\times n$ real matrix and let $b\in\mathbb R^n$.
Prove that $Ax=b$ has a solution if and only if
\[
b\in(\ker A^T)^\perp.
\]
:::

::: pf

::: pf-step

One always has
\[
\operatorname{im}A
\subseteq
(\ker A^T)^\perp.
\]


::: pf-proof

Let
\[
y\in\operatorname{im}A.
\]
Then
\[
y=Ax
\]
for some $x\in\mathbb R^n$.
If
\[
z\in\ker A^T,
\]
then
\[
A^Tz=0.
\]
Therefore
\[
\langle y,z\rangle
=
\langle Ax,z\rangle
=
\langle x,A^Tz\rangle
=0.
\]
Thus $y$ is orthogonal to every vector in $\ker A^T$.
Hence
\[
y\in(\ker A^T)^\perp.
\]

:::

:::

::: pf-step

The two spaces in step <1>1 have the same dimension.


::: pf-proof

By rank-nullity applied to
\[
A^T:\mathbb R^n\to\mathbb R^n,
\]
one has
\[
\dim\ker A^T
+
\operatorname{rank}A^T
=
n.
\]
Since
\[
\operatorname{rank}A^T
=
\operatorname{rank}A,
\]
it follows that
\[
\dim(\ker A^T)^\perp
=
n-\dim\ker A^T
=
\operatorname{rank}A
=
\dim\operatorname{im}A.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\operatorname{im}A
=
(\ker A^T)^\perp.
}
\]


::: pf-proof

Step <1>1 gives an inclusion between finite-dimensional subspaces, and step <1>2 shows that they have equal dimension.
Hence they are equal.

:::

:::

::: pf-step

The equation
\[
Ax=b
\]
has a solution if and only if
\[
b\in\operatorname{im}A.
\]


::: pf-proof

By definition, $b$ lies in the image of $A$ exactly when there exists an $x$ such that
\[
Ax=b.
\]

:::

:::

::: pf-step

Consequently,
\[
\boxed{
Ax=b\text{ is solvable}
\iff
b\in(\ker A^T)^\perp.
}
\]


::: pf-proof

Combine steps <1>3 and <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required equivalence.

:::

:::
