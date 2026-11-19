---
schema: qual/card@1
id: P-BKF09-2B
kind: problem
title: Real matrices with $P^TP=P$ are orthogonal projections $A(A^TA)^{-1}A^T$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the argument into numbered steps and supplied two things it used silently: that
    A^T A is invertible exactly when the columns of A are linearly independent, and that two
    orthogonal projections with the same image are equal (so identifying P as the orthogonal
    projection onto its own column space finishes the proof, given A chosen from that space).
    Also recorded the degenerate case P = 0, where the column space is trivial and the matrix A is
    allowed to have no columns, so that A^T A is the empty matrix and the displayed formula reads
    P = 0. Every macro used is one the preamble defines. No source text is retained for this
    examination, so nothing was checked against a printed page.

---

::: {.problem}
Let $P$ be a square matrix over $\RR$ such that $P^TP=P$.
Prove that there exists a matrix $A$ such that $A^TA$ is invertible and $P=A(A^TA)^{-1}A^T$.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $P$ be a real square matrix with $P^{T}P=P$. For a matrix $A$ write $C(A)$ for its column space, and call an $n\times n$ matrix $Q$ an orthogonal projection when $Q=Q^{T}=Q^{2}$; its image is then $C(Q)$ and $x-Qx\perp C(Q)$ for every $x$.

::: pf

::: {.pf-step #positive}
For a real matrix $A$, $A^{T}A$ is invertible if and only if the columns of $A$ are linearly independent.

::: pf-proof
$A^{T}Ax=0$ implies $\norm{Ax}^{2}=(Ax)^{T}(Ax)=x^{T}A^{T}Ax=0$, so $Ax=0$. Hence $\ker(A^{T}A)=\ker A$, and a square matrix is invertible exactly when its kernel is trivial; $\ker A=0$ is precisely linear independence of the columns.
:::

:::

::: {.pf-step #formula}
If the columns of $A$ are linearly independent, then $Q=A(A^{T}A)^{-1}A^{T}$ is the orthogonal projection onto $C(A)$.

::: pf-proof
$Q^{T}=A\bigl((A^{T}A)^{-1}\bigr)^{T}A^{T}=A(A^{T}A)^{-1}A^{T}=Q$ because $A^{T}A$ is symmetric, and $Q^{2}=A(A^{T}A)^{-1}A^{T}A(A^{T}A)^{-1}A^{T}=Q$. So $Q$ is an orthogonal projection. Its image lies in $C(A)$; and for $x\in C(A)$, say $x=Az$, we get $Qx=A(A^{T}A)^{-1}A^{T}Az=Az=x$, so the image is exactly $C(A)$. Being a projection onto $C(A)$ that is self-adjoint, it is the orthogonal projection onto $C(A)$: $x-Qx$ is orthogonal to every $Qy$, since $(x-Qx)^{T}Qy=x^{T}Qy-x^{T}Q^{T}Qy=x^{T}Qy-x^{T}Qy=0$.
:::

:::

::: {.pf-step #P-projection}
$P$ is the orthogonal projection onto its own column space.

::: pf-proof
For all $x,y$,
$$
(x-Px)^{T}Py=x^{T}Py-x^{T}P^{T}Py=x^{T}(P-P^{T}P)y=0
$$
because $P^{T}P=P$. So $x-Px$ is orthogonal to every element $Py$ of $C(P)$, which together with $Px\in C(P)$ says exactly that $P$ is the orthogonal projection onto $C(P)$.
:::

:::

::: {.pf-step #conclude}
Taking $A$ with columns a basis of $C(P)$ gives $P=A(A^{T}A)^{-1}A^{T}$.

::: pf-proof
Let $k=\dim C(P)$ and let $A$ be an $n\times k$ matrix whose columns are a basis of $C(P)$. The columns are linearly independent, so $A^{T}A$ is invertible by step [](#positive){.pf-ref}, and $A(A^{T}A)^{-1}A^{T}$ is the orthogonal projection onto $C(A)=C(P)$ by step [](#formula){.pf-ref}. By step [](#P-projection){.pf-ref} $P$ is also the orthogonal projection onto $C(P)$, and two orthogonal projections with the same image agree: each is determined by $x\mapsto$ the unique vector of that space with $x-(\cdot)$ orthogonal to it. Hence the two matrices are equal.
:::

:::

::: {.pf-step #degenerate}
When $P=0$ the identity holds with $A$ the $n\times 0$ matrix.

::: pf-proof
$P^{T}P=P$ holds for $P=0$, and $C(P)=\{0\}$ has dimension $0$, so the basis in step [](#conclude){.pf-ref} is empty and $A$ has no columns. Then $A^{T}A$ is the empty $0\times0$ matrix, which is invertible (its determinant is $1$ by the usual convention for the empty product), and $A(A^{T}A)^{-1}A^{T}$ is the $n\times n$ zero matrix, that is $P$. Readers who prefer no empty matrix may exclude $P=0$, which needs no argument.
:::

:::

:::

:::
