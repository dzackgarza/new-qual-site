---
schema: qual/card@1
id: P-APA23D
kind: problem
title: Rayleigh quotient bounds; $p$-norm of a diagonal matrix; $\|aa^H\|_2$ and a block companion
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
solved: false
---

::: problem
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $x^H$ denotes the Hermitian transpose of $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$. Prove that
\[
\lambda_n(A) \le \frac{x^H A x}{x^H x} \le \lambda_1(A)
\]
for all nonzero $x \in \mathbb{C}^n$.

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$. Prove that for all $1 \le p \le \infty$ the $p$-norm of $D$ is given by $\|D\|_p = \max_{1 \le i \le n} |d_i|$.

(c) Given $a \in \mathbb{C}^n$, find $\|A\|_2$ for the matrices
\[
A = aa^H
\quad\text{and}\quad
A = \begin{pmatrix} 0 & a^H \\ a & 0 \end{pmatrix}.
\]
(Show your work. Simply writing down the answer will not be sufficient.)
:::

