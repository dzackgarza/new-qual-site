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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 1.1 of the official UCSD Algebra Qualifying Examination, Fall 2006; the statement and displayed block decomposition agree with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Repaired the prior dimensionally impossible identification of ker(A-lambda I)^* with ker(y^*). The proof now derives Ran(A-lambda I)=ker(y^*) from inclusion and equal dimension, then uses algebraic multiplicity one to show y^*x is nonzero.
---

::: {.problem}
Assume that $(\lambda, x)$ is an eigenpair of $A \in M_n$ such that $\operatorname{am}(\lambda) = \operatorname{gm}(\lambda) = 1$.
Prove that there exists a nonsingular matrix $(x \quad X)$ with inverse $(y \quad Y)^*$ such that
\[
\begin{pmatrix} y^* \\ Y^* \end{pmatrix} A (x \quad X) = \begin{pmatrix} \lambda & 0 \\ 0 & M \end{pmatrix}.
\]
:::

::: {.solution}
Set
\[
N:=A-\lambda I.
\]
Since $\operatorname{gm}(\lambda)=1$, we have
\[
\ker N=\operatorname{span}\{x\},
\qquad
\operatorname{rank}N=n-1.
\]

<1>1. There is a left eigenvector $y\neq0$ for $\lambda$, and it satisfies $y^*x\neq0$.
::: {.proof}
Because
\[
\operatorname{rank}N^*=\operatorname{rank}N=n-1,
\]
the nullspace of $N^*$ is one-dimensional.
Choose
\[
0\neq y\in\ker N^*.
\]
Then
\[
y^*N=0,
\]
so $y$ is a left eigenvector for $\lambda$.

For every $v$,
\[
y^*(Nv)=0,
\]
hence
\[
\operatorname{Ran}N\subseteq\ker y^*.
\]
Both spaces have dimension $n-1$, so
\[
\operatorname{Ran}N=\ker y^*.
\]

Suppose, toward a contradiction, that $y^*x=0$.
Then
\[
x\in\ker y^*=\operatorname{Ran}N,
\]
so there exists $z$ with
\[
Nz=x.
\]
Since $x\neq0$ and $Nx=0$, the vectors $x,z$ are linearly independent and
\[
N^2z=0.
\]
Thus the generalized eigenspace
\[
\ker N^2
\]
has dimension at least $2$.
The algebraic multiplicity of $\lambda$ is at least the dimension of every generalized-eigenspace stage, in particular
\[
\operatorname{am}(\lambda)\ge \dim\ker N^2\ge2,
\]
contrary to $\operatorname{am}(\lambda)=1$.
Therefore
\[
y^*x\neq0.
\]
Rescale $y$ so that
\[
y^*x=1.
\]
:::

<1>2. Choose the remaining columns $X$ so that $(x\ \ X)$ is nonsingular and its first dual row is $y^*$.
::: {.proof}
Since
\[
\dim\ker y^*=n-1
\]
and $x\notin\ker y^*$, choose columns $x_2,\ldots,x_n$ forming a basis of $\ker y^*$ and set
\[
X=(x_2\ \cdots\ x_n).
\]
Then
\[
P:=(x\ \ X)
\]
is nonsingular.
Moreover,
\[
y^*P=(1\ \ 0\ \cdots\ 0).
\]
Hence the first row of $P^{-1}$ is $y^*$.
Write the remaining rows as $Y^*$, so
\[
P^{-1}=
\begin{pmatrix}
y^*\\
Y^*
\end{pmatrix}.
\]
Consequently
\[
y^*X=0,
\qquad
Y^*x=0.
\]
:::

<1>3. In this basis, $A$ has the required block-diagonal form.
::: {.proof}
Since $Ax=\lambda x$,
\[
y^*Ax=\lambda y^*x=\lambda
\]
and
\[
Y^*Ax=\lambda Y^*x=0.
\]
Also $y^*A=\lambda y^*$ because $y^*(A-\lambda I)=0$, hence
\[
y^*AX=\lambda y^*X=0.
\]
Therefore
\[
P^{-1}AP
=
\begin{pmatrix}
y^*Ax & y^*AX\\
Y^*Ax & Y^*AX
\end{pmatrix}
=
\begin{pmatrix}
\lambda & 0\\
0 & M
\end{pmatrix},
\]
where
\[
M:=Y^*AX.
\]
This is exactly the required decomposition.
:::
:::
