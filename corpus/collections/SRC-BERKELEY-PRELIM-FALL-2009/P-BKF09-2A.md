---
schema: qual/card@1
id: P-BKF09-2A
kind: problem
title: No polynomial in the entries of a $2\times2$ matrix always gives an eigenvalue
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the 2x2 matrix with both rows and the field C against f09solutions.pdf page 1 problem 2A.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the one-matrix argument with $\sqrt z$, then the trace
    and determinant argument with the irreducibility of $ad-bc$ proved by counting the variables of a
    putative factorization. No retained solution set covers this exercise, so the argument is the card's
    own; the second argument's variable count was completed for this pass (the card's "exactly two terms"
    step omitted the disjointness count).
---

::: {.problem}
Prove that no polynomial $p(a, b, c, d)$ in four variables over $\CC$ has the property that when $p$ is evaluated on the entries of a $2 \times 2$ matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$, the result is an eigenvalue of $A$, for all $A$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. Two arguments are given: a one-matrix argument, and an argument through the trace and the determinant.

::: pf

::: {.pf-step #sqrts}
$p(0,z,1,0)^{2}=z$ for all $z\in\CC$, and no polynomial over $\CC$ has square $z$.

::: pf-proof
Take $A=\begin{bmatrix}0&z\\1&0\end{bmatrix}$. Its characteristic polynomial is $\lambda^{2}-(\operatorname{tr}A)\lambda+\det A=\lambda^{2}-0\cdot\lambda-z=\lambda^{2}-z$, whose roots are $\pm\sqrt z$; so an eigenvalue of $A$ is a square root of $z$. If $p$ always returned an eigenvalue, then $p(0,z,1,0)=\pm\sqrt z$ and squaring gives $p(0,z,1,0)^{2}=z$. But $p(0,z,1,0)$ is a polynomial in $z$ over $\CC$, and the degree of a square is twice the degree of the polynomial, hence even, while $\deg z=1$; so no polynomial over $\CC$ squares to $z$. This already contradicts the assumed property.
:::

:::

::: {.pf-step #trace-det}
If $p$ always evaluates to an eigenvalue, then $q=a+d-p$ evaluates to the other eigenvalue and $pq=ad-bc$ as polynomials in $a,b,c,d$.

::: pf-proof
The sum of the two eigenvalues of $A$ is $\operatorname{tr}A=a+d$, counted with multiplicity, so if $p(A)$ is one eigenvalue then $q(A)=a+d-p(A)$ is the other. The product of the two eigenvalues is $\det A=ad-bc$, so the product $pq$ takes the value $ad-bc$ at every matrix; two polynomials agreeing on all of $\CC^{4}$ are equal, so $pq=ad-bc$ identically.
:::

:::

::: {.pf-step #irreducible}
$ad-bc$ is irreducible in $\CC[a,b,c,d]$.

::: pf-proof
It is homogeneous of degree $2$, so a factorization is into a nonzero constant times a product $\lambda\mu$ of homogeneous linear forms. If a variable occurred in both $\lambda$ and $\mu$ with nonzero coefficients $\alpha,\beta$, then $\lambda\mu$ would contain $\alpha\beta$ times the square of that variable, and no other product of two linear forms contributing to $ad-bc$ can produce such a square term to cancel it; so no variable occurs in both. No variable divides $ad-bc$, so neither $\lambda$ nor $\mu$ is a single variable, hence each contains at least two of $a,b,c,d$. The variables used by $\lambda$ and by $\mu$ are disjoint subsets of a set with four elements, so each uses exactly two variables; then $\lambda\mu$ has the four terms obtained by multiplying them out, none cancelling, whereas $ad-bc$ has two terms. So no such factorization exists and $ad-bc$ is irreducible.
:::

:::

::: {.pf-step #constant}
Hence one of $p$, $q$ is constant, and a constant is not an eigenvalue of every $2\times2$ matrix.

::: pf-proof
From steps [](#trace-det){.pf-ref} and [](#irreducible){.pf-ref}, the irreducible polynomial $ad-bc$ divides the product $pq$, so it divides one factor; a factor of the same degree $2$ as $ad-bc$ is a nonzero constant multiple of it, and a factor of larger degree would leave a factor of degree $<1$, that is a constant. So one of $p$ and $q$ is constant. A constant $c$ fails to be an eigenvalue of every matrix: the matrix $(c+1)I$ has the single eigenvalue $c+1\ne c$.
:::

:::

::: {.pf-step}
No polynomial $p(a,b,c,d)$ evaluates to an eigenvalue of $\begin{bmatrix}a&b\\c&d\end{bmatrix}$ for every matrix.

::: pf-proof
Suppose such a $p$ exists. By step [](#sqrts){.pf-ref} we already have a contradiction; so suppose instead that no contradiction arises there. Then by step [](#constant){.pf-ref} one of $p$ and $q$ is constant. Both $p$ and $q$ evaluate to eigenvalues of every matrix, since $q$ evaluates to the other eigenvalue whenever $p$ does; but a constant evaluates to itself, and no constant is an eigenvalue of every $2\times2$ matrix. Contradiction. Hence no such polynomial exists, which is the assertion.
:::

:::

:::
:::
