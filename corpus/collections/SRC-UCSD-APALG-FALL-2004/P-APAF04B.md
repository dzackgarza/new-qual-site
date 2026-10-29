---
schema: qual/card@1
id: P-APAF04B
kind: problem
title: Real linear independence over $\CC$; real eigenvalues of real matrices
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

::: {.problem}
(a) Show that $a_1,\ldots,a_n\in\RR^m$ are linearly independent over $\CC$ iff they are linearly independent over $\RR$.

(b) Show that if $A\in M_n(\RR)$, then an eigenvalue $\lambda$ of $A$ is real iff it has a real corresponding eigenvector.

(Notation: $M_n(\RR)$ denotes the set of $n\times n$ real matrices.)
:::

::: {.solution}

::: pf

::: pf-step

The vectors $a_1,\ldots,a_n\in\RR^m$ are linearly independent over $\CC$ if and only if they are linearly independent over $\RR$.

::: pf-proof

If they are linearly independent over $\CC$, then they are automatically linearly independent over the subfield $\RR$.

Conversely, suppose they are linearly independent over $\RR$ and
$$
\sum_{j=1}^n z_j a_j=0
$$
with $z_j\in\CC$. Write
$$
z_j=x_j+iy_j,
\qquad x_j,y_j\in\RR.
$$
Because every $a_j$ has real coordinates,
$$
0=\sum_j(x_j+iy_j)a_j
=\sum_jx_ja_j+i\sum_jy_ja_j
$$
implies
$$
\sum_jx_ja_j=0,
\qquad
\sum_jy_ja_j=0
$$
in $\RR^m$. Real linear independence gives $x_j=y_j=0$ for every $j$, hence $z_j=0$ for every $j$. Thus the vectors are linearly independent over $\CC$.

:::

:::

::: {.pf-step #s2}

Let $A\in M_n(\RR)$ and let $0\ne v\in\RR^n$ satisfy
$$
Av=\lambda v
$$
for some $\lambda\in\CC$. Then $\lambda\in\RR$.

::: pf-proof

Since $A$ and $v$ are real, $Av\in\RR^n$. Choose an index $j$ with $v_j\ne0$. The $j$-th coordinate of the eigenvalue equation gives
$$
(Av)_j=\lambda v_j.
$$
Both $(Av)_j$ and $v_j$ are real and $v_j\ne0$, so
$$
\lambda=\frac{(Av)_j}{v_j}\in\RR.
$$

:::

:::

::: {.pf-step #s3}

Conversely, if $\lambda\in\RR$ is an eigenvalue of $A$, then $A$ has a nonzero real eigenvector for $\lambda$.

::: pf-proof

Choose a nonzero complex eigenvector
$$
z=x+iy\in\CC^n,
\qquad x,y\in\RR^n,
$$
with
$$
Az=\lambda z.
$$
Since $A$ and $\lambda$ are real,
$$
Ax+iAy=\lambda x+i\lambda y.
$$
Equality of real and imaginary parts gives
$$
Ax=\lambda x,
\qquad
Ay=\lambda y.
$$
Because $z\ne0$, at least one of $x,y$ is nonzero. That nonzero vector lies in $\RR^n$ and is an eigenvector of $A$ for $\lambda$.

:::

:::

::: pf-step

Therefore an eigenvalue of a real matrix is real if and only if it has a real corresponding eigenvector.

::: pf-proof

The two implications are steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
