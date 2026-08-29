---
schema: qual/card@1
id: P-ALGF06A
kind: problem
title: "Eigenpair of algebraic and geometric multiplicity one yields a complementary block form"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Assume that $(\lambda, x)$ is an eigenpair of $A \in M_n$ such that $\operatorname{am}(\lambda) = \operatorname{gm}(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::

::: solution
Let
\[
N:=A-\lambda I.
\]
Since $\operatorname{gm}(\lambda)=1$, $\dim\ker N=1$ and therefore $\operatorname{rank}N=n-1$.
Let $x$ be a nonzero vector with $Nx=0$.
Also choose $y\neq0$ in the left eigenspace of $\lambda$, so $y^*N=0$.

We first show $y^*x\neq0$.
Because $\ker N$ has dimension $1$ and $N$ has rank $n-1$, we have
\[
\ker N^*=\ker y^*=\operatorname{Ran}N.
\]
If $y^*x=0$, then $x\in\ker y^*=\operatorname{Ran}N$, so $x=Nz$ for some $z$.
Then $Nx=0$ implies $N^2z=0$ and $z\notin\ker N$, which would force a Jordan chain of length at least $2$ for $\lambda$ and hence $\operatorname{am}(\lambda)\ge2$, a contradiction.
So $y^*x\neq0$.
Scale $y$ so that $y^*x=1$.

Let
\[
X:=[x_2,\dots,x_n]
\]
be any matrix whose columns form a basis of $\ker y^*$ (so $\dim\ker y^*=n-1$, $x\notin\ker y^*$, and $(x\ \ X)$ is invertible).
Take the unique block-row matrix $(y^*\ \ Y^*)$ satisfying
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix}(x\ \ X)=I.
\]
Then by construction $Y^*x=0$, $Y^*X=I$, and $y^*X=0$.

Compute:
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix}A(x\ \ X)
=
\begin{pmatrix}
y^*Ax & y^*AX\\
Y^*Ax & Y^*AX
\end{pmatrix}.
\]
Since $y^*N=0$ and $Nx=0$, we have $y^*Ax=\lambda$ and $y^*AX=\lambda y^*X=0$.
Also $Ax=\lambda x$ and $Y^*x=0$ imply $Y^*Ax=0$.
Set $M:=Y^*AX$.

Therefore
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix}A(x\ \ X)=\begin{pmatrix}\lambda&0\\0&M\end{pmatrix}.
\]
:::
