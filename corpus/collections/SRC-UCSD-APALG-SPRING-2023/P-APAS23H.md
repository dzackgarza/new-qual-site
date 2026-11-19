---
schema: qual/card@1
id: P-APAS23H
kind: problem
title: 'Invariant inner products for the unipotent $\ZZ$-representation on $\CC^2$'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Part B, Problem 4 of the Spring 2023 Applied Algebra Qualifying Exam, printed
    p. 4 of the Part B paper retained at assets/attachments/Applied_Algebra_Part_B_SP23.pdf, is the
    statement the card answers, and the head of the solution names it. Checked: the statement against
    the paper's text layer at the page named; the negative answer, from the unipotence of $\rho(1)$,
    which would have to be diagonalizable under a $G$-invariant inner product; `qualc.authoring check`
    on the card, and `tmp/lam.sh` for the numbering and the QED. Not checked: no retained solution set
    exists for this paper to compare the argument with, and no other card of the collection in this
    pass.
---

::: {.problem}
Let $G = \ZZ$ be the group of integers under addition.
The group homomorphism $\rho \colon G \to \mathrm{GL}_2(\CC)$ given by
$$
\rho(n) = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}
$$
gives $\CC^2$ the structure of a $G$-module.
Does $\CC^2$ admit a $G$-invariant inner product?
:::

::: {.solution}

The problem is Part B, Problem 4 of the Spring 2023 Applied Algebra Qualifying Exam, printed p. 4 of the Part B paper retained at `assets/attachments/Applied_Algebra_Part_B_SP23.pdf`. The paper prints no solutions, so nothing below is transcribed: the argument is the card's own.

No.

If such a $G$-invariant inner product existed, then the operator representing the generator $1\in\ZZ$,
$$
T=\rho(1)=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$
would preserve that inner product. Thus $T$ would be unitary with respect to that positive-definite Hermitian form.

Every unitary operator on a finite-dimensional complex inner-product space is diagonalizable: after choosing an orthonormal basis, its matrix is unitary and hence normal, so the spectral theorem applies.

But $T$ is a nontrivial Jordan block. Its only eigenvalue is $1$, and
$$
T-I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0,
\qquad
(T-I)^2=0.
$$
Therefore its minimal polynomial is $(t-1)^2$, so $T$ is not diagonalizable. This contradiction shows that no $G$-invariant inner product exists.

Hence
$$
\boxed{\CC^2\text{ admits no }\ZZ\text{-invariant inner product for this representation}.}
$$
:::
