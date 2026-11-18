---
schema: qual/card@1
id: P-BKF04-4A
kind: problem
title: $A$ is diagonalizable iff every nilpotent $f(A)$ is zero
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: invariance under conjugation, the diagonal case, and
    the converse through the squarefree minimal polynomial, with Cayley--Hamilton used where it enters. No
    retained solution set covers this exercise (the collection retains the examination, not solutions), so
    the argument is the card's own; it was re-read for this pass and each use of the hypothesis is now its
    own step.
---

::: {.problem}
Let $A$ be an $n\times n$ matrix with complex entries. Prove that $A$ is diagonalizable if and only if the following is true: Whenever $f$ is a polynomial with complex coefficients such that $f(A)$ is nilpotent, we have $f(A)=0$. (A matrix $A$ is nilpotent if $A^m=0$ for some $m\geq1$.)
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. A matrix with complex entries is diagonalizable exactly when its minimal polynomial has distinct roots, which is the criterion used at the end.

::: pf

::: {.pf-step #conjugation}
Conjugation preserves both diagonalizability and the stated property; so does replacing $A$ by a conjugate.

::: pf-proof
If $A$ is diagonalizable, so is $CAC^{-1}$ for invertible $C$, since a diagonalizing basis is carried to a diagonalizing basis. For the property, $f(CAC^{-1})=Cf(A)C^{-1}$ for every polynomial $f$, so $f(CAC^{-1})$ is nilpotent exactly when $f(A)$ is, and $f(CAC^{-1})=0$ exactly when $f(A)=0$. So the two conditions hold for $A$ exactly when they hold for a conjugate of $A$, and $A$ may be taken diagonal for the forward direction.
:::

:::

::: {.pf-step #forward}
If $A$ is diagonalizable, then $f(A)$ nilpotent implies $f(A)=0$.

::: pf-proof
By step [](#conjugation){.pf-ref} take $A$ diagonal, with diagonal entries $\lambda_{1},\dots,\lambda_{n}$. Then $f(A)$ is diagonal with entries $f(\lambda_{1}),\dots,f(\lambda_{n})$, so $f(A)^{m}$ is diagonal with entries $f(\lambda_{i})^{m}$. If $f(A)$ is nilpotent then $f(\lambda_{i})^{m}=0$ for some $m$ and every $i$, so $f(\lambda_{i})=0$ and $f(A)=0$.
:::

:::

::: {.pf-step #cayley-hamilton}
For $f(x)=\prod_{\lambda}(x-\lambda)$, the product over the distinct eigenvalues of $A$, one has $f(A)^{k}=0$ for some $k$.

::: pf-proof
Write $c(x)=\prod_{\lambda}(x-\lambda)^{m_{\lambda}}$ for the characteristic polynomial of $A$, where $m_{\lambda}$ is the multiplicity of the eigenvalue $\lambda$. Taking $k\ge m_{\lambda}$ for all $\lambda$, the polynomial $c$ divides $f^{k}$, say $f^{k}=c\,g$. By the Cayley--Hamilton theorem $c(A)=0$, so $f(A)^{k}=c(A)g(A)=0$.
:::

:::

::: {.pf-step}
Conversely, if $f(A)$ nilpotent implies $f(A)=0$ for every polynomial $f$, then $A$ is diagonalizable.

::: pf-proof
Let $f$ be the product of $x-\lambda$ over the distinct eigenvalues of $A$. By step [](#cayley-hamilton){.pf-ref} the matrix $f(A)$ is nilpotent, so by hypothesis $f(A)=0$: the polynomial $f$ annihilates $A$. Hence the minimal polynomial of $A$ divides $f$, so every root of the minimal polynomial is a root of $f$ and occurs in it to the first power; the minimal polynomial has distinct roots. By the criterion stated at the outset, $A$ is diagonalizable. Together with step [](#forward){.pf-ref} this proves the equivalence.
:::

:::

:::
:::
