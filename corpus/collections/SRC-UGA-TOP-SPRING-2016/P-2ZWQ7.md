---
schema: qual/card@1
id: P-2ZWQ7
kind: problem
title: A nonnegative matrix has a real eigenvalue, via Brouwer
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Spring 2016 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the zero-column case separately, then verified that normalization of Ax defines a continuous self-map of the simplex and that a Brouwer fixed point is an eigenvector.
---

::: problem
Use the Brouwer fixed point theorem to show that an $n \times n$ matrix with nonnegative entries has a real eigenvalue.
:::

::: {.solution}
Let $A=(a_{ij})$ be an $n\times n$ real matrix with $a_{ij}\ge0$.

<1>1. If $A$ has a zero column, then $0$ is a real eigenvalue of $A$.
::: {.proof}
If the $j$th column is zero, then
\[
Ae_j=0,
\]
where $e_j\ne0$ is the $j$th standard basis vector.
Thus $e_j$ is an eigenvector with eigenvalue $0$.
:::

<1>2. Assume from now on that no column of $A$ is zero, and let
\[
\Delta^{n-1}
=\left\{x=(x_1,\dots,x_n)\in\RR^n:\ x_i\ge0,\ \sum_{i=1}^n x_i=1\right\}.
\]
For every $x\in\Delta^{n-1}$, the vector $Ax$ is nonzero and has nonnegative coordinates.
::: {.proof}
Choose $j$ with $x_j>0$, which exists because the coordinates of $x$ sum to $1$.
The $j$th column $Ae_j$ is nonzero and has nonnegative coordinates by hypothesis.
Since
\[
Ax=\sum_{k=1}^n x_kAe_k
\]
is a nonnegative linear combination of the columns and contains the nonzero summand $x_jAe_j$, at least one coordinate of $Ax$ is strictly positive.
Hence $Ax\ne0$.
:::

<1>3. Define
\[
F:\Delta^{n-1}\longrightarrow\Delta^{n-1},
\qquad
F(x)=\frac{Ax}{\sum_{i=1}^n(Ax)_i}.
\]
Then $F$ is a continuous self-map of the simplex.
::: {.proof}
By <1>2, $Ax$ has nonnegative coordinates and is nonzero, so
\[
s(x):=\sum_{i=1}^n(Ax)_i>0.
\]
Therefore $F(x)$ has nonnegative coordinates and coordinate sum $1$, hence belongs to $\Delta^{n-1}$.
Both $x\mapsto Ax$ and $s$ are continuous, and $s$ never vanishes on the simplex, so $F$ is continuous.
:::

<1>4. The matrix $A$ has a positive real eigenvalue.
::: {.proof}
The simplex $\Delta^{n-1}$ is compact and convex, so Brouwer's fixed point theorem applied to <1>3 gives some $x\in\Delta^{n-1}$ with
\[
F(x)=x.
\]
Thus
\[
Ax=s(x)x.
\]
By <1>2, $s(x)>0$, and $x\ne0$ because its coordinates sum to $1$.
Therefore $x$ is an eigenvector of $A$ with real eigenvalue
\[
\lambda=s(x)>0.
\]
Together with <1>1, this proves that every nonnegative real matrix has a real eigenvalue.
:::
:::
