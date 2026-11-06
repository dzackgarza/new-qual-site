---
schema: qual/card@1
id: E-AMD-HO6G56UF
kind: problem
title: Commuting diagonalizable matrices are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
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
    standard linear algebra exercise, no repair needed), and the existing prose
    solution against a fresh re-derivation: A diagonalizable gives V as the
    direct sum of its eigenspaces (the sum is direct because eigenvectors for
    distinct eigenvalues are independent); AB = BA makes every A-eigenspace
    B-stable; the minimal polynomial of the restriction B|E_A(lambda) divides
    m_B, which splits with distinct roots because B is diagonalizable, and a
    divisor inherits that; so each eigenspace has a basis of B-eigenvectors, and
    the union of those bases is a basis of V of simultaneous eigenvectors. All
    correct. Also checked that no step silently assumes the field is algebraically
    closed: "splits over k" is carried in the hypothesis. No source solution is
    retained for this card, so no source comparison was made. What was not
    checked: any printed source.
---

::: {.exercise}
Show that if $A,B$ are diagonalizable and $[A, B] = 0$, then $A$ and $B$ are simultaneously diagonalizable.
:::

::: {.solution}
Let $V$ be a finite-dimensional vector space over a field $k$ and $A,B\in\operatorname{End}_k(V)$ with $AB=BA$; write $E_A(\lambda)=\ker(A-\lambda\Id)$ for the $\lambda$-eigenspace of $A$, and recall that an operator is diagonalizable exactly when its minimal polynomial splits over $k$ into distinct linear factors, equivalently when $V$ has a basis of eigenvectors.

::: pf

::: {.pf-step #decomposition}
$V=\bigoplus_{\lambda}E_A(\lambda)$, the sum over the eigenvalues of $A$ in $k$.

::: pf-proof
$A$ is diagonalizable, so $V$ has a basis $v_1,\ldots,v_n$ of eigenvectors; each $v_i$ lies in $E_A(\lambda_i)$ for its eigenvalue $\lambda_i$, so the $E_A(\lambda)$ span $V$. The sum is direct because eigenvectors for distinct eigenvalues are linearly independent: if $\sum_j w_j=0$ with $w_j\in E_A(\mu_j)$ for distinct $\mu_j$ and not all $w_j$ zero, applying $A$ repeatedly and taking a shortest nonempty such relation gives a contradiction with the distinctness of the $\mu_j$.
:::

:::

::: {.pf-step #stable}
$B\,E_A(\lambda)\subseteq E_A(\lambda)$ for every $\lambda$.

::: pf-proof
For $v\in E_A(\lambda)$ we have $A(Bv)=B(Av)=B(\lambda v)=\lambda\,Bv$ using $AB=BA$, so $Bv\in E_A(\lambda)$.
:::

:::

::: {.pf-step #restriction}
For every eigenvalue $\lambda$ of $A$, the restriction $B_\lambda=B|_{E_A(\lambda)}$ is diagonalizable.

::: pf-proof
Let $m_B$ be the minimal polynomial of $B$. Since $B$ is diagonalizable, $m_B$ splits over $k$ into distinct linear factors. Because $m_B(B)=0$ on all of $V$, it vanishes in particular on $E_A(\lambda)$, so the minimal polynomial of $B_\lambda$ divides $m_B$; a divisor of a polynomial that splits into distinct linear factors again splits into distinct linear factors, so the minimal polynomial of $B_\lambda$ splits over $k$ with distinct roots. That is exactly the criterion for $B_\lambda$ to be diagonalizable.
:::

:::

::: {.pf-step #basis}
Each $E_A(\lambda)$ has a basis consisting of eigenvectors of $B$.

::: pf-proof
By step [](#restriction){.pf-ref} the operator $B_\lambda$ is diagonalizable on the finite-dimensional space $E_A(\lambda)$ (finite-dimensional because it is a subspace of $V$), so $E_A(\lambda)$ has a basis of eigenvectors of $B_\lambda$, and such a vector is an eigenvector of $B$ because $B_\lambda$ is the restriction of $B$.
:::

:::

::: {.pf-step}
$V$ has a basis of vectors that are eigenvectors of both $A$ and $B$, so $A$ and $B$ are simultaneously diagonalizable.

::: pf-proof
Take the union, over the eigenvalues $\lambda$ of $A$, of the bases of step [](#basis){.pf-ref}. Each vector of that union lies in some $E_A(\lambda)$, hence is an eigenvector of $A$, and is an eigenvector of $B$ by construction. The union is a basis of $V$: the sum $V=\bigoplus_\lambda E_A(\lambda)$ is direct by step [](#decomposition){.pf-ref}, and a union of bases of the summands of a direct sum is a basis of the whole space. With respect to that basis both operators are represented by diagonal matrices.
:::

:::

:::
:::
