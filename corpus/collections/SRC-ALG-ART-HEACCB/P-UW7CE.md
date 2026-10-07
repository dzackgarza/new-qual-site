---
schema: qual/card@1
id: P-UW7CE
kind: problem
title: A complex matrix with $A^2=A$ is similar to a diagonal matrix
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Let $A\in M_n(\CC)$ with $A^2 = A$.
Show that $A$ is similar to a diagonal matrix, and exhibit an explicit diagonal matrix similar to $A$.
:::

::: {.solution}
<1>1. The vector space decomposes as
\[
\CC^n=\operatorname{im}A\oplus\ker A.
\]
::: {.proof}
For every vector $v$,
\[
v=Av+(v-Av).
\]
The first term lies in $\operatorname{im}A$, while
\[
A(v-Av)=Av-A^2v=0,
\]
so the second lies in $\ker A$. If $w\in\operatorname{im}A\cap\ker A$, write $w=Au$; then
\[
w=Au=A^2u=Aw=0,
\]
so the sum is direct.
:::

<1>2. The map $A$ acts as the identity on $\operatorname{im}A$ and as zero on $\ker A$.
::: {.proof}
If $w=Av\in\operatorname{im}A$, then
\[
Aw=A^2v=Av=w.
\]
If $w\in\ker A$, then $Aw=0$ by definition.
:::

<1>3. Let $r=\operatorname{rank}A$. Choose a basis $u_1,\dots,u_r$ of $\operatorname{im}A$ and a basis $v_1,\dots,v_{n-r}$ of $\ker A$. Their union is a basis of $\CC^n$.
::: {.proof}
This follows from the direct-sum decomposition in step <1>1. The dimensions are $r$ and $n-r$ by rank-nullity.
:::

<1>4. In the basis from <1>3, the matrix of $A$ is
\[
\operatorname{diag}(I_r,0_{n-r}).
\]
Hence
\[
\boxed{A\sim\operatorname{diag}(\underbrace{1,\dots,1}_{r},\underbrace{0,\dots,0}_{n-r})}.
\]
::: {.proof}
By step <1>2, each $u_i$ is an eigenvector with eigenvalue $1$ and each $v_j$ is an eigenvector with eigenvalue $0$.
:::

<1>5. Equivalently, the minimal polynomial of $A$ divides $x(x-1)$, which has distinct roots, so $A$ is diagonalizable.
::: {.proof}
The equation $A^2=A$ gives $A(A-I)=0$, hence $m_A(x)\mid x(x-1)$. A matrix whose minimal polynomial splits into distinct linear factors is diagonalizable, consistent with the explicit basis above.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>4 gives the requested explicit diagonal matrix similar to $A$; step <1>5 gives the equivalent minimal-polynomial criterion.
:::
:::
