---
schema: qual/card@1
id: P-FO6H7
kind: problem
title: Commuting diagonalizable operators are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, whose three ingredients
    (the eigenspace decomposition of A, the B-invariance of the eigenspaces, and
    diagonalizability of the restriction via the minimal polynomial) are correct and were kept.
    Added: the reason the union of the chosen bases is a basis of V, which the card had
    asserted; and the statement that a divisor of a product of distinct linear factors is again
    such a product. Nothing weakened.
---

::: {.problem}
Let $F$ be a field and $V$ a finite dimensional $F\dash$vector space, and let $A, B: V\to V$ be commuting $F\dash$linear maps.
Suppose there is a basis $\mcb_1$ with respect to which $A$ is diagonalizable and a basis $\mcb_2$ with respect to which $B$ is diagonalizable.

Prove that there is a basis $\mcb_3$ with respect to which $A$ and $B$ are both diagonalizable.
:::

::: {.solution}
Throughout $V$ is a finite-dimensional $F$-vector space, $A, B \in \End_{F}(V)$ satisfy $AB = BA$, and $E_{\lambda}(A) \coloneqq \ker(A - \lambda I)$ is the eigenspace of $A$ for $\lambda \in F$.

::: pf

::: {.pf-step #eigenspace-sum}
$V = \bigoplus_{\lambda \in F} E_{\lambda}(A)$, the sum over the distinct eigenvalues of $A$.

::: pf-proof
$A$ is diagonalizable, so $V$ has a basis of eigenvectors of $A$; each basis vector lies in its own eigenspace, so the eigenspaces span $V$. Eigenspaces for distinct eigenvalues are independent, so the sum is direct.

:::

:::

::: {.pf-step #invariant}
Each $E_{\lambda}(A)$ is $B$-invariant.

::: pf-proof
For $v \in E_{\lambda}(A)$ the commutation gives $A(Bv) = B(Av) = B(\lambda v) = \lambda Bv$, so $Bv \in E_{\lambda}(A)$.

:::

:::

::: {.pf-step #restriction}
For each $\lambda$ the restriction $\restrictionof{B}{E_{\lambda}(A)}$ is diagonalizable.

::: pf-proof
$B$ is diagonalizable, so its minimal polynomial $m_{B}$ is a product of distinct linear factors. The minimal polynomial of the restriction divides $m_{B}$, because $m_{B}(B) = 0$ restricts to $0$; a divisor of a product of distinct linear factors is again such a product. A linear map on a finite-dimensional space whose minimal polynomial is a product of distinct linear factors is diagonalizable, so the restriction is.

:::

:::

::: {.pf-step #bases}
For each $\lambda$ there is a basis $\mcb_{\lambda}$ of $E_{\lambda}(A)$ consisting of eigenvectors of $B$, and $\mcb_{3} \coloneqq \bigcup_{\lambda} \mcb_{\lambda}$ is a basis of $V$.

::: pf-proof
Each $\mcb_{\lambda}$ exists by step [](#restriction){.pf-ref}. The union is independent and spans because the sum of the eigenspaces is direct and equals $V$, which is step [](#eigenspace-sum){.pf-ref}.

:::

:::

::: pf-step
With respect to $\mcb_{3}$ both $A$ and $B$ are diagonal.

::: pf-proof
Every vector of $\mcb_{3}$ lies in some $\mcb_{\lambda}$: it is an eigenvector of $B$ by construction, and an eigenvector of $A$ because it lies in the eigenspace $E_{\lambda}(A)$. A basis of simultaneous eigenvectors puts both matrices in diagonal form.

:::

:::

:::
:::
