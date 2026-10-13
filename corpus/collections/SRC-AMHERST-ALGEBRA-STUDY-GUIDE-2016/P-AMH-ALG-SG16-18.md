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
(January 2012) Let
\[
R=\left\{\begin{pmatrix}a&b\\0&c\end{pmatrix}:a,b,c\in\mathbb{R}\right\}.
\]
You may assume that $R$ is a ring under the operations of matrix addition and matrix multiplication. Prove that the set
\[
I=\left\{\begin{pmatrix}a&b\\0&0\end{pmatrix}:a,b\in\mathbb{R}\right\}
\]
is an ideal of $R$.
:::

::: {.solution}
<1>1. The set $I$ is nonempty.

::: {.proof}
The zero matrix has the required form:
$$
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}\in I.
$$
:::

<1>2. The set $I$ is closed under subtraction.

::: {.proof}
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

<1>3. The set $I$ is closed under left multiplication by arbitrary elements
of $R$.

::: {.proof}
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

<1>4. The set $I$ is closed under right multiplication by arbitrary elements
of $R$.

::: {.proof}
With $R_0$ and $A$ as in step <1>3,
$$
AR_0=
\begin{pmatrix}
ar&as+bt\\
0&0
\end{pmatrix}\in I.
$$
Thus multiplication on the right also preserves $I$.
:::

<1>5. Therefore $I$ is a two-sided ideal of $R$.

::: {.proof}
Steps <1>1 and <1>2 show that $I$ is an additive subgroup of the additive group
of $R$, using the subtraction criterion.  Steps <1>3 and <1>4 show absorption
under multiplication by arbitrary elements of $R$ on both sides.  These are
exactly the two-sided ideal axioms.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
