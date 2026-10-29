---
schema: qual/card@1
id: P-AMH-ALG-SG16-18
kind: problem
title: An ideal in the ring of upper triangular $2\times 2$ real matrices
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
Let
$$
R=\left\{\begin{pmatrix}a&b\\0&c\end{pmatrix}:a,b,c\in\RR\right\}.
$$
You may assume that $R$ is a ring under the operations of matrix addition and matrix multiplication. Prove that the set
$$
I=\left\{\begin{pmatrix}a&b\\0&0\end{pmatrix}:a,b\in\RR\right\}
$$
is an ideal of $R$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}
The set $I$ is nonempty.

::: pf-proof
The zero matrix has the required form:
$$
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}\in I.
$$
:::

:::

::: {.pf-step #s1-2}
The set $I$ is closed under subtraction.

::: pf-proof
Let
$$
A=
\begin{pmatrix}
a&b\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
x&y\\
0&0
\end{pmatrix}
$$
belong to $I$.  Then
$$
A-B=
\begin{pmatrix}
a-x&b-y\\
0&0
\end{pmatrix},
$$
which again has the defining form of an element of $I$.
:::

:::

::: {.pf-step #s1-3}
The set $I$ is closed under left multiplication by arbitrary elements
of $R$.

::: pf-proof
Let
$$
R_0=
\begin{pmatrix}
r&s\\
0&t
\end{pmatrix}\in R,
\qquad
A=
\begin{pmatrix}
a&b\\
0&0
\end{pmatrix}\in I.
$$
Then
$$
R_0A=
\begin{pmatrix}
ra&rb\\
0&0
\end{pmatrix}\in I.
$$
:::

:::

::: {.pf-step #s1-4}
The set $I$ is closed under right multiplication by arbitrary elements
of $R$.

::: pf-proof
With $R_0$ and $A$ as in step [](#s1-3){.pf-ref},
$$
AR_0=
\begin{pmatrix}
ar&as+bt\\
0&0
\end{pmatrix}\in I.
$$
Thus multiplication on the right also preserves $I$.
:::

:::

::: pf-step
Therefore $I$ is a two-sided ideal of $R$.

::: pf-proof
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that $I$ is an additive subgroup of the additive group
of $R$, using the subtraction criterion.  Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} show absorption
under multiplication by arbitrary elements of $R$ on both sides.  These are
exactly the two-sided ideal axioms.
:::

:::

:::

:::
