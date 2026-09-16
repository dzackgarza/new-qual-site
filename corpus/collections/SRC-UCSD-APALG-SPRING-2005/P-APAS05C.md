---
schema: qual/card@1
id: P-APAS05C
kind: problem
title: Eigenpair of algebraic and geometric multiplicity one yields a complementary block form
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: problem
Assume that $(\lambda, x)$ is an eigenpair of $A \in \mathbb{C}^{n\times n}$ such that $am(\lambda) = gm(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::

::: {.solution}
Let
\[
N:=A-\lambda I.
\]
Since $gm(\lambda)=1$,
\[
\ker N=\mathbb Cx.
\]

<1>1. The subspace
\[
W:=\operatorname{im}N
\]
has dimension $n-1$ and is $A$-invariant.
::: {.proof}
By rank-nullity,
\[
\dim W=\operatorname{rank}N=n-\dim\ker N=n-1.
\]
Moreover $A$ commutes with $N=A-\lambda I$, so if $w=Nz\in W$, then
\[
Aw=ANz=NAz\in W.
\]
Thus $W$ is $A$-invariant.
:::

<1>2. One has
\[
\mathbb Cx\cap W=\{0\}.
\]
::: {.proof}
Suppose instead that $0\ne cx\in W$. Since $c\ne0$, this implies $x\in W$, so there exists $z\in\mathbb C^n$ with
\[
Nz=x,
\qquad\text{i.e.}\qquad
(A-\lambda I)z=x.
\]
Then $x$ and $z$ are linearly independent, because if $z=\alpha x$, then
\[
Nz=\alpha Nx=0,
\]
contrary to $Nz=x\ne0$.
The subspace $U=\operatorname{span}\{x,z\}$ is $A$-invariant, since
\[
Ax=\lambda x,
\qquad
Az=x+\lambda z.
\]
With respect to the basis $(x,z)$ of $U$, the restriction $A|_U$ has matrix
\[
\begin{pmatrix}
\lambda&1\\
0&\lambda
\end{pmatrix}.
\]
Hence the characteristic polynomial of $A|_U$ is $(t-\lambda)^2$. Extending $(x,z)$ to a basis adapted to the invariant subspace $U$ makes the matrix of $A$ block upper triangular, so $(t-\lambda)^2$ divides the characteristic polynomial of $A$. This contradicts $am(\lambda)=1$.
Therefore $\mathbb Cx\cap W=0$.
:::

<1>3. Therefore
\[
\mathbb C^n=\mathbb Cx\oplus W.
\]
Choose a basis $x_2,\ldots,x_n$ of $W$ and set
\[
X=(x_2\ \cdots\ x_n),
\qquad
P=(x\quad X).
\]
Then $P$ is nonsingular.
::: {.proof}
By <1>1 and <1>2,
\[
\dim(\mathbb Cx+W)=1+(n-1)=n,
\]
so the sum is direct and equals all of $\mathbb C^n$. Hence the columns of $P$ form a basis, so $P$ is invertible.
:::

<1>4. Relative to the basis given by the columns of $P$,
\[
P^{-1}AP=
\begin{pmatrix}
\lambda&0\\
0&M
\end{pmatrix}
\]
for some $(n-1)\times(n-1)$ matrix $M$.
::: {.proof}
The line $\mathbb Cx$ is $A$-invariant and $Ax=\lambda x$. By <1>1, the complementary subspace $W$ is also $A$-invariant. Therefore the matrix of $A$ with respect to the direct-sum basis
\[
\mathbb C^n=\mathbb Cx\oplus W
\]
has no off-diagonal blocks. Its first block is $[\lambda]$, and the second block is the matrix $M$ of $A|_W$ in the basis $x_2,\ldots,x_n$.
:::

<1>5. Writing
\[
P^{-1}=
\begin{pmatrix}
y^*\\
Y^*
\end{pmatrix},
\]
we obtain exactly
\[
\boxed{
\begin{pmatrix}y^*\\Y^*\end{pmatrix}
A(x\quad X)
=
\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}.}
\]
::: {.proof}
This is simply the identity from <1>4 after writing the first row of $P^{-1}$ as $y^*$ and the remaining $n-1$ rows as $Y^*$.
:::
:::
