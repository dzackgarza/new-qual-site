---
schema: qual/card@1
id: P-APA17B
kind: problem
title: Simultaneous orthogonal diagonalization of commuting real symmetric matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Diagonalization
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 2 of the Qualifying Exam in Applied Algebra of May 30, 2017, printed p.
    2 of the nine-page paper retained at assets/attachments/APPLIED-ALGEBRA-EXAM.pdf, is the statement
    the card answers, and the paragraph at the head of the solution records that the paper prints no
    solutions, so the argument is the card's own. Checked: the statement against the paper's text layer
    at the page named; the spectral theorem, the invariance of the eigenspaces of A under B, and the
    spectral theorem on each; `qualc.authoring check` on the card, and `tmp/lam.sh` for the numbering
    and the QED. Not checked: no retained solution set exists for this paper to compare the argument
    with, and no other card of the collection in this pass.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same argument. Two things were repaired in passing: the
    solution wrote the restriction with a \restrict macro, which the corpus does not define, and it is
    now \restrictionof{B}{E_lambda}; and the step that the union of the per-eigenspace bases is an
    orthonormal basis, which the prose asserted in one sentence, now gives both halves --- orthonormality
    from the mutual orthogonality of distinct eigenspaces, and spanning from their direct sum. The final
    step computes the entries of Q^T A Q and Q^T B Q rather than asserting the diagonality. No published
    solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $A, B \in \RR^{n \times n}$ be two real symmetric matrices.
If $AB = BA$, show that there exists an orthogonal matrix $Q \in \RR^{n \times n}$ such that $Q^T AQ$ and $Q^T BQ$ are both diagonal.
:::

::: {.solution}

No published solution was located for this examination problem, which is Problem 2 printed on p. 2 of the retained paper `assets/attachments/APPLIED-ALGEBRA-EXAM.pdf` (the Qualifying Exam in Applied Algebra of May 30, 2017); the argument is the card's own, and it is the standard one: the spectral theorem for $A$, invariance of its eigenspaces under $B$ from the commutation, and the spectral theorem again on each eigenspace.

The statement was checked against the Spring 2017 applied-algebra examination collection holding this card. Throughout, $A,B\in\RR^{n\times n}$ are real symmetric, $\langle\cdot,\cdot\rangle$ is the Euclidean inner product on $\RR^{n}$, $A^{\mathsf{T}}=A$ and $B^{\mathsf{T}}=B$, and for an eigenvalue $\lambda$ of $A$ the eigenspace is $E_{\lambda}\coloneqq\ker(A-\lambda I)$.

::: pf

::: {.pf-step #spectral}

$\RR^{n}$ is the orthogonal direct sum of the eigenspaces of $A$.

::: pf-proof

$A$ is real symmetric, so it is orthogonally diagonalizable: the spectral theorem gives pairwise orthogonal eigenspaces whose direct sum is $\RR^{n}$, and the eigenvalues are real.

:::

:::

::: {.pf-step #invariant}

Each $E_{\lambda}$ is invariant under $B$.

::: pf-proof

Let $v\in E_{\lambda}$. Since $AB=BA$,
$$
A(Bv)=B(Av)=B(\lambda v)=\lambda\,Bv,
$$
so $Bv\in E_{\lambda}$: the image of the eigenspace lies in itself.

:::

:::

::: {.pf-step #restriction}

For each $\lambda$ the restriction $\restrictionof{B}{E_{\lambda}}\colon E_{\lambda}\to E_{\lambda}$ is symmetric with respect to the inner product restricted to $E_{\lambda}$.

::: pf-proof

For $u,v\in E_{\lambda}$ one has $\langle Bu,v\rangle=\langle u,Bv\rangle$, because $B$ is symmetric on $\RR^{n}$; and by step [](#invariant){.pf-ref} both $Bu$ and $Bv$ lie in $E_{\lambda}$, so this is an identity of the restricted inner product on $E_{\lambda}$.

:::

:::

::: {.pf-step #eigenbasis}

Each $E_{\lambda}$ has an orthonormal basis consisting of eigenvectors of $B$.

::: pf-proof

By steps [](#invariant){.pf-ref} and [](#restriction){.pf-ref} the restriction of $B$ is a symmetric endomorphism of the finite-dimensional inner product space $E_{\lambda}$, so the spectral theorem applies to it and gives an orthonormal basis of $E_{\lambda}$ made of its eigenvectors; those are eigenvectors of $B$ on $\RR^{n}$ as well.

:::

:::

::: {.pf-step #common-basis}

The union of these bases over the eigenvalues of $A$ is an orthonormal basis of $\RR^{n}$ of vectors that are eigenvectors of both $A$ and $B$.

::: pf-proof

Each basis vector lies in some $E_{\lambda}$, hence is an eigenvector of $A$, and is an eigenvector of $B$ by step [](#eigenbasis){.pf-ref}. The union is orthonormal because it is a union of orthonormal sets lying in mutually orthogonal subspaces (step [](#spectral){.pf-ref}), and it is a basis because those subspaces span $\RR^{n}$.

:::

:::

::: pf-step

The orthogonal matrix $Q$ whose columns are those vectors satisfies: $Q^{\mathsf{T}}AQ$ and $Q^{\mathsf{T}}BQ$ are both diagonal.

::: pf-proof

$Q$ is orthogonal because its columns form an orthonormal basis. For a diagonal entry, $(Q^{\mathsf{T}}AQ)_{ii}=q_{i}^{\mathsf{T}}Aq_{i}=\lambda_{i}$ where $q_{i}$ is the $i$-th column and $Aq_{i}=\lambda_{i}q_{i}$, and off the diagonal $(Q^{\mathsf{T}}AQ)_{ij}=q_{i}^{\mathsf{T}}Aq_{j}=\lambda_{j}q_{i}^{\mathsf{T}}q_{j}=0$ because the columns are orthonormal; so $Q^{\mathsf{T}}AQ$ is diagonal, and the same computation with $B$ and its eigenvalues gives $Q^{\mathsf{T}}BQ$ diagonal.

:::

:::

:::

:::
