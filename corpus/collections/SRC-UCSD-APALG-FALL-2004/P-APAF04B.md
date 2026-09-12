---
schema: qual/card@1
id: P-APAF04B
kind: problem
title: Real linear independence over $\mathbb{C}$; real eigenvalues of real matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
(a) Show that $a_1,\ldots,a_n\in\mathbb{R}^m$ are linearly independent over $\mathbb{C}$ iff they are linearly independent over $\mathbb{R}$.

(b) Show that if $A\in M_n(\mathbb{R})$, then an eigenvalue $\lambda$ of $A$ is real iff it has a real corresponding eigenvector.

(Notation: $M_n(\mathbb{R})$ denotes the set of $n\times n$ real matrices.)
:::

::: {.solution}
<1>1. The vectors $a_1,\ldots,a_n\in\mathbb R^m$ are linearly independent over $\mathbb C$ if and only if they are linearly independent over $\mathbb R$.
::: {.proof}
If they are linearly independent over $\mathbb C$, then they are automatically linearly independent over the subfield $\mathbb R$.

Conversely, suppose they are linearly independent over $\mathbb R$ and
\[
\sum_{j=1}^n z_j a_j=0
\]
with $z_j\in\mathbb C$. Write
\[
z_j=x_j+iy_j,
\qquad x_j,y_j\in\mathbb R.
\]
Because every $a_j$ has real coordinates,
\[
0=\sum_j(x_j+iy_j)a_j
=\sum_jx_ja_j+i\sum_jy_ja_j
\]
implies
\[
\sum_jx_ja_j=0,
\qquad
\sum_jy_ja_j=0
\]
in $\mathbb R^m$. Real linear independence gives $x_j=y_j=0$ for every $j$, hence $z_j=0$ for every $j$. Thus the vectors are linearly independent over $\mathbb C$.
:::

<1>2. Let $A\in M_n(\mathbb R)$ and let $0\ne v\in\mathbb R^n$ satisfy
\[
Av=\lambda v
\]
for some $\lambda\in\mathbb C$. Then $\lambda\in\mathbb R$.
::: {.proof}
Since $A$ and $v$ are real, $Av\in\mathbb R^n$. Choose an index $j$ with $v_j\ne0$. The $j$-th coordinate of the eigenvalue equation gives
\[
(Av)_j=\lambda v_j.
\]
Both $(Av)_j$ and $v_j$ are real and $v_j\ne0$, so
\[
\lambda=\frac{(Av)_j}{v_j}\in\mathbb R.
\]
:::

<1>3. Conversely, if $\lambda\in\mathbb R$ is an eigenvalue of $A$, then $A$ has a nonzero real eigenvector for $\lambda$.
::: {.proof}
Choose a nonzero complex eigenvector
\[
z=x+iy\in\mathbb C^n,
\qquad x,y\in\mathbb R^n,
\]
with
\[
Az=\lambda z.
\]
Since $A$ and $\lambda$ are real,
\[
Ax+iAy=\lambda x+i\lambda y.
\]
Equality of real and imaginary parts gives
\[
Ax=\lambda x,
\qquad
Ay=\lambda y.
\]
Because $z\ne0$, at least one of $x,y$ is nonzero. That nonzero vector lies in $\mathbb R^n$ and is an eigenvector of $A$ for $\lambda$.
:::

<1>4. Therefore an eigenvalue of a real matrix is real if and only if it has a real corresponding eigenvector.
::: {.proof}
The two implications are <1>2 and <1>3.
:::
:::
