---
schema: qual/card@1
id: P-ALGF20D
kind: problem
title: Jordan form of the all-ones matrix over an algebraically closed field
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Jordan Canonical Form
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 4 of the official UCSD Algebra Qualifying Exam, Fall 2020 source; the algebraically closed field hypothesis and all-ones matrix statement agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Corrected the prior unconditional diagonalizability claim; when char(F) divides n the matrix is nonzero square-zero of rank one, so its Jordan form has one size-two nilpotent block.
---

::: problem
Let $F$ be an algebraically closed field.
Let $A$ be the $n \times n$ matrix over $F$ such that every entry of $A$ is $1$.
Find the Jordan canonical form of $A$.
(The answer may depend on the properties of the field $F$).
:::

::: {.solution}
Let
\[
\mathbf 1=(1,\ldots,1)^t\in F^n.
\]

<1>1. For every $v=(v_1,\ldots,v_n)^t\in F^n$,
\[
Av=\left(\sum_{i=1}^n v_i\right)\mathbf 1,
\qquad
A^2=nA,
\]
where $n$ denotes the image of the integer $n$ in $F$.
::: {.proof}
Every row of $A$ consists entirely of $1$'s, so each coordinate of $Av$ equals $\sum_i v_i$. Applying this to $v=\mathbf1$ gives
\[
A\mathbf1=n\mathbf1,
\]
and therefore, for every $v$,
\[
A^2v=A\left(\left(\sum_i v_i\right)\mathbf1\right)
=n\left(\sum_i v_i\right)\mathbf1
=nAv.
\]
:::

<1>2. The matrix $A$ has rank $1$, and
\[
\ker A=\left\{v\in F^n:\sum_{i=1}^n v_i=0\right\}
\]
has dimension $n-1$.
::: {.proof}
Every column of $A$ equals the nonzero vector $\mathbf1$, so $\operatorname{im}A=F\mathbf1$ and $\operatorname{rank}A=1$. The kernel description follows from <1>1, and rank-nullity gives its dimension.
:::

<1>3. If $n\ne0$ in $F$, then $A$ is diagonalizable with Jordan form
\[
\operatorname{diag}(n,0,\ldots,0).
\]
::: {.proof}
By <1>1,
\[
A\mathbf1=n\mathbf1,
\]
so $F\mathbf1$ is an eigenspace for the eigenvalue $n$. By <1>2, $\ker A$ is the eigenspace for $0$ and has dimension $n-1$.

Because $n\ne0$, the vector $\mathbf1$ does not lie in $\ker A$: its coordinate sum is $n$. Hence
\[
F^n=F\mathbf1\oplus\ker A.
\]
Thus there is a basis consisting of one eigenvector with eigenvalue $n$ and $n-1$ eigenvectors with eigenvalue $0$, giving the displayed diagonal Jordan form.
:::

<1>4. If $n=0$ in $F$, then $A$ is nonzero, has square zero, and its Jordan form is
\[
J_2(0)\oplus J_1(0)^{\oplus(n-2)}.
\]
::: {.proof}
The condition $n=0$ in $F$ means $\operatorname{char}F$ divides the positive integer $n$, so necessarily $n\ge2$. By <1>1,
\[
A^2=0,
\]
while <1>2 gives $\operatorname{rank}A=1$, so $A\ne0$.

Since $A^2=0$, every nilpotent Jordan block has size at most $2$. If there are $r$ blocks of size $2$, then the rank of the Jordan form is exactly $r$, because each $J_2(0)$ has rank $1$ and each $J_1(0)$ has rank $0$. Since $\operatorname{rank}A=1$, there is exactly one size-$2$ block. The remaining $n-2$ dimensions are size-$1$ zero blocks, yielding
\[
J_2(0)\oplus J_1(0)^{\oplus(n-2)}.
\]
:::

Therefore the Jordan form is diagonal with entries $n,0,\ldots,0$ when $\operatorname{char}F\nmid n$, and is one $2\times2$ nilpotent block plus $n-2$ zero blocks when $\operatorname{char}F\mid n$.
:::
