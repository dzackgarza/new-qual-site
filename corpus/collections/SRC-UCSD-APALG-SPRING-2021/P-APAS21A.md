---
schema: qual/card@1
id: P-APAS21A
kind: problem
title: Schur form; deflating a simple eigenpair and the angle between $x$ and $y$
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) State, but do not prove, the Schur decomposition theorem for a matrix $A \in M_n$.

(b) Let $(\lambda, x)$ be a simple eigenpair of $A \in M_n$ with $x^H x = 1$.
Prove that there exists a nonsingular matrix $\begin{pmatrix} x & X \end{pmatrix}$ with inverse $\begin{pmatrix} y & Y \end{pmatrix}^H$ such that
$$
\begin{pmatrix} y^H \\ Y^H \end{pmatrix}
A
\begin{pmatrix} x & X \end{pmatrix}
=
\begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
$$

(c) Hence prove that the angle $\theta$ between $x$ and $y$ satisfies $\sec \theta = \norm{y}_2$.
:::

::: {.solution}

The argument is the card's own; part (a) is quoted as the exercise instructs, and the proof of (b) isolates the two facts it needs — that a simple eigenvalue has no Jordan chain of length two, and that $\operatorname{im}(A-\lambda I)$ is $A$-invariant.

::: pf

::: {.pf-step #a}
(a) Schur decomposition: for every $A\in M_{n}$ there is a unitary $Q$ with $Q^{H}AQ=T$ upper triangular, and the diagonal entries of $T$ are the eigenvalues of $A$ counted with algebraic multiplicity.

::: pf-proof
The exercise asks for the statement and not a proof, so it is quoted; the proof is the induction on $n$ recorded on [[P-APAS13A]]. The diagonal entries of an upper triangular matrix are its eigenvalues, and $Q^{H}AQ$ is similar to $A$, so they are the eigenvalues of $A$ with multiplicity.
:::

:::

::: {.pf-step #kernel-image}
(b) With $N=A-\lambda I$ and $(\lambda,x)$ a simple eigenpair, $\ker N=\CC x$ and $\ker N\cap\operatorname{im}N=\{0\}$.

::: pf-proof
The geometric multiplicity $\dim\ker N$ is at least $1$ (as $x\ne0$ is an eigenvector) and at most the algebraic multiplicity of $\lambda$, which is $1$ because the eigenpair is simple; so $\ker N=\CC x$. If $0\ne v=Nw\in\ker N$, then $N^{2}w=Nv=0$ while $Nw=v\ne0$, so $w\notin\ker N$ and $w,Nw$ are linearly independent vectors spanning a $2$-dimensional $N$-invariant space on which $N$ is nilpotent; that gives a Jordan chain of length $2$ for $\lambda$, hence algebraic multiplicity at least $2$, contradicting simplicity. So no such $v$ exists.
:::

:::

::: {.pf-step #split}
(b) $\CC^{n}=\ker N\oplus\operatorname{im}N=\CC x\oplus\operatorname{im}(A-\lambda I)$, and $\operatorname{im}N$ is $A$-invariant.

::: pf-proof
$\dim\ker N+\dim\operatorname{im}N=n$ by rank-nullity, and the two subspaces meet only in $0$ by step [](#kernel-image){.pf-ref}, so their sum is direct and equals $\CC^{n}$. If $v=Nu$ then $Av=ANu=NAu$, because $A$ commutes with $N=A-\lambda I$, and $NAu\in\operatorname{im}N$; so $A$ carries $\operatorname{im}N$ into itself.
:::

:::

::: {.pf-step #block}
(b) Taking the columns of $X$ to be a basis of $\operatorname{im}N$, the matrix $S=(x\ X)$ is nonsingular and $S^{-1}AS=\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}$ for some $M\in M_{n-1}$.

::: pf-proof
$x$ spans $\ker N$, so $\{x\}$ together with a basis of $\operatorname{im}N$ is a basis of $\CC^{n}$ by step [](#split){.pf-ref}; hence $S$ is nonsingular. Its first column is $S e_{1}=x$, and $ASe_{1}=Ax=\lambda x$, so the first column of $S^{-1}AS$ is $(\lambda,0,\ldots,0)^{T}$. Its remaining columns are $S^{-1}AX_{j}$ where $X_{j}$ is a column of $X$; since $AX_{j}\in\operatorname{im}N$, which is spanned by the columns of $X$, the first coordinate of that vector vanishes and the rest form an $(n-1)\times(n-1)$ matrix $M$. So the block form holds with a zero block in the $(2,1)$ position.
:::

:::

::: {.pf-step #left-eigenvector}
(b) With $S^{-1}=\begin{pmatrix}y^{H}\\ Y^{H}\end{pmatrix}$, one has $y^{H}x=1$, and $y$ is a left eigenvector of $A$ for $\lambda$; hence $\begin{pmatrix}y^{H}\\ Y^{H}\end{pmatrix}A(x\ X)=\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}$.

::: pf-proof
$S^{-1}S=I$ gives $y^{H}x=1$ and $y^{H}X=0$. The columns of $X$ span $\operatorname{im}N=\operatorname{im}(A-\lambda I)$, so $y^{H}X=0$ says that the linear functional $y^{H}$ vanishes on the image of $A-\lambda I$, that is $y^{H}(A-\lambda I)=0$, or $y^{H}A=\lambda y^{H}$. Multiplying the block form of step [](#block){.pf-ref} on the left by $S^{-1}$ and using $S=(x\ X)$ gives the displayed identity: the first block column is $y^{H}Ax=\lambda y^{H}x=\lambda$ and $Y^{H}Ax=\lambda Y^{H}x$, and $Y^{H}x=0$ because $Y^{H}$ is the remaining block of $S^{-1}$ and $S^{-1}S=I$; the second block column is $y^{H}AX=0$, from $y^{H}(A-\lambda I)=0$, and $Y^{H}AX=M$.
:::

:::

::: {.pf-step #angle}
(c) $\sec\theta=\norm{y}_{2}$ for the angle $\theta$ between $x$ and $y$.

::: pf-proof
For complex vectors the angle is defined by $\cos\theta=\dfrac{\abs{y^{H}x}}{\norm{y}_{2}\norm{x}_{2}}$, taking the acute angle. Here $y^{H}x=1$ and $\norm{x}_{2}=1$ by hypothesis, so $\cos\theta=1/\norm{y}_{2}$ and therefore
$$
\boxed{\sec\theta=\norm{y}_{2}}.
$$
In particular $\norm{y}_{2}\ge1$, as $\cos\theta\le1$ requires, which is also Cauchy--Schwarz applied to $y^{H}x=1$.
:::

:::

:::
:::
