---
schema: qual/card@1
id: P-BKF07-2B
kind: problem
title: Diagonalizability of consecutive powers of a matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the invariant eigenspace decomposition of A^m, the
    square-free minimal-polynomial argument on nonzero eigenspaces, and the
    nilpotent zero-eigenspace case against the vendored solution.
---

::: {.problem}
Let \(A\) be an \(n\times n\) complex matrix.
Suppose \(m\ge1\) and \(A^m\) is diagonalizable.
Prove that \(A^{m+1}\) is diagonalizable.
:::

::: {.solution}
Let $V\coloneqq\CC^n$. For each eigenvalue $\lambda$ of $A^m$, set
$$
E_\lambda\coloneqq\ker(A^m-\lambda I).
$$

<1>1. The space $V$ decomposes as
$$
V=\bigoplus_\lambda E_\lambda,
$$
and every $E_\lambda$ is invariant under $A$.

::: {.proof}
The direct-sum decomposition follows from the diagonalizability of
$A^m$. Since $A$ commutes with $A^m$, if $v\in E_\lambda$, then
$$
A^m(Av)=A(A^m v)=A(\lambda v)=\lambda Av.
$$
Thus $Av\in E_\lambda$, so each $E_\lambda$ is $A$-invariant.
:::

<1>2. On $E_0$, the operator $A^{m+1}$ is zero and hence diagonalizable.

::: {.proof}
If $v\in E_0$, then $A^m v=0$, so
$$
A^{m+1}v=A(A^m v)=0.
$$
Thus the restriction of $A^{m+1}$ to $E_0$ is the zero operator.
:::

<1>3. If $\lambda\ne0$, then the restriction
$B\coloneqq A|_{E_\lambda}$ is diagonalizable.

::: {.proof}
For every $v\in E_\lambda$,
$$
B^m v=A^m v=\lambda v,
$$
so $B$ is annihilated by
$$
p(x)=x^m-\lambda.
$$
Because $\lambda\ne0$ and the ground field is $\CC$, the polynomial
$p$ has no repeated root: a common root of $p$ and
$p'(x)=mx^{m-1}$ would have to be both nonzero and zero. Hence the
minimal polynomial of $B$ divides a polynomial with distinct linear
factors. Therefore $B$ is diagonalizable.
:::

<1>4. For every eigenvalue $\lambda$ of $A^m$, the restriction of
$A^{m+1}$ to $E_\lambda$ is diagonalizable.

::: {.proof}
For $\lambda=0$, this is step <1>2. If $\lambda\ne0$, step <1>3
shows that $B=A|_{E_\lambda}$ is diagonalizable. Therefore its power
$$
B^{m+1}=A^{m+1}|_{E_\lambda}
$$
is diagonalizable as well.
:::

<1>5. The matrix $A^{m+1}$ is diagonalizable.

::: {.proof}
By step <1>1, $V$ is the direct sum of the $A$-invariant spaces
$E_\lambda$. Step <1>4 gives a basis of each $E_\lambda$ consisting
of eigenvectors of $A^{m+1}$. The union of these bases is therefore an
eigenbasis of $V$ for $A^{m+1}$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
