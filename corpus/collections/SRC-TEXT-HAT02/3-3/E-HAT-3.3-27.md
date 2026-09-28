---
schema: qual/card@1
id: E-HAT-3.3-27
kind: problem
title: "Normal form for skew-symmetric forms over $\\mathbb{Z}$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 27; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that after a suitable change of basis, a skew-symmetric nonsingular bilinear form over $\mathbb{Z}$ can be represented by a matrix consisting of $2 \times 2$ blocks $\bigl(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\bigr)$ along the diagonal and zeros elsewhere.
:::

::: {.solution}
Let $L$ be a free abelian group of finite rank with a skew-symmetric nonsingular bilinear form
\[
B:L\times L\to\mathbb Z.
\]
Nonsingularity over $\mathbb Z$ means the adjoint map $L\to L^*$ is an isomorphism.

Choose a primitive element $e\in L$. Since the functional $B(e,-)$ is primitive in $L^*$, there exists $f\in L$ with
\[
B(e,f)=1.
\]
Then the restriction of $B$ to $P=\mathbb Ze\oplus\mathbb Zf$ has matrix
\[
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
For any $x\in L$, set
\[
x'=x-B(x,f)e+B(x,e)f.
\]
A direct calculation gives
\[
B(x',e)=B(x',f)=0.
\]
Thus
\[
L=P\oplus P^\perp.
\]
The restriction of $B$ to $P^\perp$ is again integral, skew-symmetric, and nonsingular. Induction on the rank therefore splits $L$ as an orthogonal direct sum of such rank-two planes.

Replacing $f$ by $-f$ in each plane changes the displayed block to
\[
\boxed{\begin{pmatrix}0&-1\\1&0\end{pmatrix}},
\]
so after a suitable integral change of basis the matrix is a block diagonal sum of these standard symplectic blocks.
:::
