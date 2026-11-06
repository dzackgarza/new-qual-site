---
schema: qual/card@1
id: E-AMD-FAT34AQV
kind: problem
title: Diagonalizable versus distinct eigenvalues
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    yes/no question, answered no, no repair needed), and the existing prose
    solution against a fresh re-derivation: the identity matrix is already
    diagonal, hence diagonalizable; det((x-1)Id_n) = (x-1)^n, so 1 is the only
    eigenvalue with multiplicity n and for n >= 2 the eigenvalues are not distinct.
    Correct. The prose also asserted the converse (n distinct eigenvalues implies
    diagonalizable) with the reason compressed into a clause; that direction is now
    a step with the linear independence argument for eigenvectors of distinct
    eigenvalues, since the card's question is only complete when the direction that
    does hold is distinguished from the one that fails. No source solution is
    retained for this card, so no source comparison was made. What was not checked:
    any printed source.

---

::: {.exercise}
Does diagonalizable imply distinct eigenvalues?
:::

::: {.solution}
Fix a field $k$ and $n\geq1$; $\Id_n$ is the $n\times n$ identity matrix, and a matrix is diagonalizable when it is similar to a diagonal matrix, equivalently when $k^n$ has a basis of eigenvectors.

::: pf

::: {.pf-step #diagonalizable}
$\Id_n$ is diagonalizable.

::: pf-proof
$\Id_n$ is itself a diagonal matrix — its off-diagonal entries are all $0$ — so it is similar to a diagonal matrix by the identity similarity. Equivalently, the standard basis of $k^n$ consists of eigenvectors of $\Id_n$ with eigenvalue $1$.
:::

:::

::: {.pf-step #charpoly}
The characteristic polynomial of $\Id_n$ is $(x-1)^n$, so $1$ is its only eigenvalue, with algebraic multiplicity $n$.

::: pf-proof
$\chi(x)=\det(x\Id_n-\Id_n)=\det((x-1)\Id_n)=(x-1)^n$, using that the determinant of a scalar multiple $\lambda\Id_n$ of the identity is $\lambda^n$. The eigenvalues are the roots of $\chi$ in $k$, and $(x-1)^n$ vanishes exactly at $x=1$; the multiplicity of that root is $n$.
:::

:::

::: {.pf-step #answer}
For $n\geq2$, diagonalizable does not imply distinct eigenvalues; the identity matrix is a counterexample.

::: pf-proof
$\Id_n$ is diagonalizable by step [](#diagonalizable){.pf-ref}, and by step [](#charpoly){.pf-ref} its set of eigenvalues is $\{1\}$, a single element. For $n\geq2$ the matrix has $n$ eigenvalues counted with multiplicity, so its eigenvalues are not pairwise distinct while it is diagonalizable. Hence the implication fails.
:::

:::

::: {.pf-step #converse}
Conversely, if an $n\times n$ matrix over $k$ has $n$ distinct eigenvalues in $k$, then it is diagonalizable.

::: pf-proof
Choose an eigenvector $v_i$ for each eigenvalue $\lambda_i$, $1\leq i\leq n$. Eigenvectors belonging to distinct eigenvalues are linearly independent: if $\sum_i c_iv_i=0$ is a shortest nontrivial relation, applying $A-\lambda_j\Id$ for one $j$ with $c_j\neq0$ and using the distinctness kills the $j$th term while leaving the others nonzero multiples, giving a shorter relation, a contradiction. So $v_1,\ldots,v_n$ are $n$ linearly independent vectors in an $n$-dimensional space, hence a basis of eigenvectors, and the matrix is diagonalizable.
:::

:::

:::
:::
