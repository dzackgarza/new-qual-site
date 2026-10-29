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
Let $A$ be an $n\times n$ real matrix and let $b\in\RR^n$.
Prove that $Ax=b$ has a solution if and only if
\[
b\in(\ker A^T)^\perp.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

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
for some $x\in\RR^n$.
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

::: {.pf-step #s1-2}

The two spaces in step [](#s1-1){.pf-ref} have the same dimension.


::: pf-proof

By rank-nullity applied to
\[
A^T:\RR^n\to\RR^n,
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

::: {.pf-step #s1-3}

Therefore
\[
\boxed{
\operatorname{im}A
=
(\ker A^T)^\perp.
}
\]


::: pf-proof

Step [](#s1-1){.pf-ref} gives an inclusion between finite-dimensional subspaces, and step [](#s1-2){.pf-ref} shows that they have equal dimension.
Hence they are equal.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

Consequently,
\[
\boxed{
Ax=b\text{ is solvable}
\iff
b\in(\ker A^T)^\perp.
}
\]


::: pf-proof

Combine steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required equivalence.

:::

:::

:::
