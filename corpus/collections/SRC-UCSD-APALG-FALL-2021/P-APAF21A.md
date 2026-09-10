---
schema: qual/card@1
id: P-APAF21A
kind: problem
title: Schur form; Hermitian quadratic forms determine a matrix; orthogonal projections are Hermitian
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: Official UCSD Fall 2021 PDF confirms part (c) omits the necessary projection hypothesis; repaired to assume A^2=A.
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: problem
Throughout, $M_n$ denotes the set of $n\times n$ matrices with complex components, $\mathbb{C}^n$ is the set of column vectors with $n$ complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A\in M_n$.

(b) Prove that for $A,B\in M_n$, if $x^HAx=x^HBx$ for all $x\in\mathbb{C}^n$, then $A=B$.
Give an example for which $x^TAx=x^TBx$ for all $x\in\mathbb{C}^n$ but $A\neq B$.

(c) Suppose $A$ is a projection, i.e. $A^2=A$. Prove that $A$ is an orthogonal projection if and only if $A$ is Hermitian, i.e., $A=A^H$.
:::

::: {.solution}
<1>1. **Schur decomposition theorem.** For every $A\in M_n(\mathbb C)$ there is a unitary matrix $U$ such that
\[
U^HAU=T
\]
is upper triangular. The diagonal entries of $T$ are the eigenvalues of $A$, counted with algebraic multiplicity.
::: {.proof}
This is the requested statement; no proof is required in part (a).
:::

<1>2. If $C\in M_n(\mathbb C)$ satisfies
\[
x^HCx=0
\qquad\text{for every }x\in\mathbb C^n,
\]
then $C=0$.
::: {.proof}
Let $e_1,\ldots,e_n$ be the standard basis. Taking $x=e_i$ gives
\[
C_{ii}=e_i^HC e_i=0
\]
for every $i$.
For $i\ne j$, take $x=e_i+e_j$. Then
\[
0=x^HCx=C_{ij}+C_{ji}.
\]
Now take $x=e_i+i e_j$. Since the diagonal entries vanish,
\[
0=x^HCx=iC_{ij}-iC_{ji}.
\]
Together with $C_{ij}+C_{ji}=0$, this gives
\[
C_{ij}=C_{ji}=0.
\]
Thus every entry of $C$ vanishes.
:::

<1>3. Hence, if
\[
x^HAx=x^HBx
\qquad\text{for every }x\in\mathbb C^n,
\]
then $A=B$.
::: {.proof}
Apply <1>2 to $C=A-B$. The hypothesis becomes
\[
x^H(A-B)x=0
\]
for every $x$, so $A-B=0$.
:::

<1>4. The analogous assertion with transpose in place of Hermitian transpose is false.
::: {.proof}
Take
\[
A=\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
B=0.
\]
Then $A\ne B$. For every $x=(x_1,x_2)^T\in\mathbb C^2$,
\[
x^TAx
=(x_1,x_2)
\begin{pmatrix}x_2\\-x_1\end{pmatrix}
=x_1x_2-x_2x_1=0
=x^TBx.
\]
Thus ordinary transpose quadratic forms do not determine an arbitrary complex matrix.
:::

<1>5. Suppose $A^2=A$. Then
\[
V=\operatorname{im}A\oplus\ker A,
\]
and $A$ is the projection onto $\operatorname{im}A$ along $\ker A$.
::: {.proof}
For every $x\in V$,
\[
x=Ax+(x-Ax).
\]
The first summand lies in $\operatorname{im}A$, while
\[
A(x-Ax)=Ax-A^2x=0,
\]
so the second lies in $\ker A$. If $u$ lies in both subspaces, then $u=Av$ for some $v$ and also $Au=0$; but idempotence gives
\[
u=Av=A^2v=A(Av)=Au=0.
\]
Thus the sum is direct, and $A$ acts as the identity on its image and as zero on its kernel.
:::

<1>6. If $A$ is an orthogonal projection, then $A=A^H$.
::: {.proof}
For an orthogonal projection,
\[
\operatorname{im}A\perp\ker A.
\]
By <1>5, write
\[
x=u+v,
\qquad
y=u'+v',
\]
with $u,u'\in\operatorname{im}A$ and $v,v'\in\ker A$. Then
\[
Ax=u,
\qquad
Ay=u'.
\]
Orthogonality gives
\[
\langle Ax,y\rangle
=\langle u,u'+v'\rangle
=\langle u,u'\rangle
=\langle u+v,u'\rangle
=\langle x,Ay\rangle.
\]
Therefore $A$ is self-adjoint, i.e. $A=A^H$.
:::

<1>7. Conversely, if $A^2=A$ and $A=A^H$, then $A$ is an orthogonal projection.
::: {.proof}
By <1>5, $A$ is a projection onto $\operatorname{im}A$ along $\ker A$. It remains to show these two subspaces are orthogonal.
Let $u\in\operatorname{im}A$ and $v\in\ker A$. Write $u=Ax$. Then
\[
\langle u,v\rangle
=\langle Ax,v\rangle
=\langle x,A^Hv\rangle
=\langle x,Av\rangle
=0.
\]
Hence
\[
\operatorname{im}A\perp\ker A,
\]
so the projection is orthogonal.
:::

<1>8. Thus, among projections $A^2=A$,
\[
\boxed{A\text{ is orthogonal}\iff A=A^H}.
\]
::: {.proof}
Combine <1>6 and <1>7.
:::
:::
