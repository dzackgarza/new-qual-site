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

::: pf

::: {.pf-step #V-decomposes-invariant}
The space $V$ decomposes as
$$
V=\bigoplus_\lambda E_\lambda,
$$
and every $E_\lambda$ is invariant under $A$.

::: pf-proof
The direct-sum decomposition follows from the diagonalizability of
$A^m$. Since $A$ commutes with $A^m$, if $v\in E_\lambda$, then
$$
A^m(Av)=A(A^m v)=A(\lambda v)=\lambda Av.
$$
Thus $Av\in E_\lambda$, so each $E_\lambda$ is $A$-invariant.
:::

:::

::: {.pf-step #E0-diagonalizable}
On $E_0$, the operator $A^{m+1}$ is zero and hence diagonalizable.

::: pf-proof
If $v\in E_0$, then $A^m v=0$, so
$$
A^{m+1}v=A(A^m v)=0.
$$
Thus the restriction of $A^{m+1}$ to $E_0$ is the zero operator.
:::

:::

::: {.pf-step #B-diagonalizable-nonzero}
If $\lambda\ne0$, then the restriction
$B\coloneqq A|_{E_\lambda}$ is diagonalizable.

::: pf-proof
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

:::

::: {.pf-step #restriction-diagonalizable}
For every eigenvalue $\lambda$ of $A^m$, the restriction of
$A^{m+1}$ to $E_\lambda$ is diagonalizable.

::: pf-proof
For $\lambda=0$, this is step [](#E0-diagonalizable){.pf-ref}. If $\lambda\ne0$, step [](#B-diagonalizable-nonzero){.pf-ref}
shows that $B=A|_{E_\lambda}$ is diagonalizable. Therefore its power
$$
B^{m+1}=A^{m+1}|_{E_\lambda}
$$
is diagonalizable as well.
:::

:::

::: {.pf-step #A-m1-diagonalizable}
The matrix $A^{m+1}$ is diagonalizable.

::: pf-proof
By step [](#V-decomposes-invariant){.pf-ref}, $V$ is the direct sum of the $A$-invariant spaces
$E_\lambda$. Step [](#restriction-diagonalizable){.pf-ref} gives a basis of each $E_\lambda$ consisting
of eigenvectors of $A^{m+1}$. The union of these bases is therefore an
eigenbasis of $V$ for $A^{m+1}$.
:::

:::

::: pf-qed
Step [](#A-m1-diagonalizable){.pf-ref} is the required conclusion.
:::

:::

:::
