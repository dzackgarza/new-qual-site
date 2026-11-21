---
schema: qual/card@1
id: P-APA23I
kind: problem
title: Trace of exterior powers of a normal operator and characteristic polynomial coefficients
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Multilinear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the exterior-power trace and characteristic-polynomial coefficient formulas.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight steps asserted their claim with no justification and each now carries one: the spectral theorem
    giving the orthonormal eigenbasis, the dimension $\binom{n}{d}$ of the exterior power with its basis of
    wedge products, the action of the induced map on decomposable wedges, the eigenvector conclusion, the
    trace as the sum of the diagonal entries read off as the elementary symmetric polynomial, the
    definition of the characteristic polynomial, its factorization through the eigenvalues with the
    coefficient $(-1)^d e_d$, and the substitution giving the alternating sum with its end cases. The
    closing step's proof now derives its two formulas from those steps rather than restating them, and the
    three container steps carry claims in place of labels, with the "*Proof:*" paragraphs removed and the
    "Goal" paragraph that restated the problem removed. Sources are cited by numbered statement: the
    spectral theorem for normal operators on a finite-dimensional complex inner product space, and the
    definition of the characteristic polynomial as $\det(tI - A)$. No page reference is written in the
    body of this card or in the event above. The statement is unchanged. The collection retains the UCSD
    applied algebra qualifying exam of Fall 2023 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let $H$ be an $n$-dimensional Hilbert space and $A \colon H \to H$ a normal linear transformation.

(a) Derive a formula for the trace of the degree $d$ exterior power $A^{\wedge d}$ as a function of the eigenvalues of $A$.

(b) Express the coefficients of the characteristic polynomial of $A$ in terms of traces of exterior powers of $A$.
:::

::: {.solution}

::: pf

::: {.pf-step #spectral-basis}
$H$ has an orthonormal basis of eigenvectors of $A$, and $\bigwedge^d H$ has the corresponding basis of wedge products, on which $A^{\wedge d}$ acts diagonally.

::: pf-proof

::: pf-step
By the Spectral Theorem for normal operators on a finite-dimensional complex Hilbert space $H$, there exists an orthonormal basis $\{v_1, v_2, \dots, v_n\}$ of $H$ consisting of eigenvectors of $A$:
$$A v_j = \lambda_j v_j \quad \text{for } j = 1, \dots, n.$$

::: pf-proof
A normal operator on a finite-dimensional complex Hilbert space is unitarily diagonalizable: the spectral theorem gives an orthonormal basis of eigenvectors, which is the displayed statement with $\lambda_j$ the eigenvalue attached to $v_j$.
:::

:::

::: pf-step
The $d$-th exterior power $\bigwedge^d H$ has dimension $\binom{n}{d}$, with an orthonormal basis given by the wedge products
$$\{v_I = v_{i_1} \wedge v_{i_2} \wedge \cdots \wedge v_{i_d} : 1 \le i_1 < i_2 < \cdots < i_d \le n\}.$$

::: pf-proof
The $d$-th exterior power of an $n$-dimensional space has dimension $\binom{n}{d}$, since a basis is given by the wedge products of $d$ elements of a basis in increasing index order; the $v_I$ listed are $\binom{n}{d}$ in number, and they are orthonormal because the $v_j$ are orthonormal and the wedge of an orthonormal set has norm one.
:::

:::

::: pf-step
By definition of the induced linear transformation $A^{\wedge d}: \bigwedge^d H \to \bigwedge^d H$:
$$A^{\wedge d}(v_{i_1} \wedge \cdots \wedge v_{i_d}) = (A v_{i_1}) \wedge \cdots \wedge (A v_{i_d}) = (\lambda_{i_1} v_{i_1}) \wedge \cdots \wedge (\lambda_{i_d} v_{i_d}) = \left(\prod_{k=1}^d \lambda_{i_k}\right) v_{i_1} \wedge \cdots \wedge v_{i_d}.$$

::: pf-proof
The induced map on the exterior power is defined on decomposable wedges by applying the operator to each factor; an eigenvector of $A$ is carried to a scalar multiple of itself, and the multivariable wedge is multilinear, so the scalar factors come out and multiply.
:::

:::

::: pf-step
Thus every basis vector $v_I$ is an eigenvector of $A^{\wedge d}$ with eigenvalue $\prod_{k=1}^d \lambda_{i_k}$.

::: pf-proof
A basis vector $v_I$ is carried by $A^{\wedge d}$ to the scalar $\prod_{k=1}^{d}\lambda_{i_k}$ times itself, which is exactly the statement that it is an eigenvector with that eigenvalue; the basis consists of such vectors, so the operator is diagonal in that basis.
:::

:::

:::

:::

::: {.pf-step #trace-formula-for-wedge-power}
$\operatorname{tr}(A^{\wedge d}) = e_d(\lambda_1, \dots, \lambda_n)$.

::: pf-proof

::: pf-step
The trace of an operator is the sum of its eigenvalues (the diagonal entries with respect to any orthonormal basis):
$$\operatorname{tr}\left(A^{\wedge d}\right) = \sum_{1 \le i_1 < i_2 < \cdots < i_d \le n} \lambda_{i_1} \lambda_{i_2} \cdots \lambda_{i_d} = e_d(\lambda_1, \dots, \lambda_n),$$
where $e_d(\lambda_1, \dots, \lambda_n)$ is the $d$-th elementary symmetric polynomial in the eigenvalues of $A$.

::: pf-proof
The trace is the sum of the diagonal entries in any basis, and in a basis of eigenvectors the diagonal entries are the eigenvalues listed; the eigenvalues of $A^{\wedge d}$ are the products $\prod_k \lambda_{i_k}$ over the increasing index tuples, one for each basis vector, and the sum of those products over all such tuples is the definition of the $d$-th elementary symmetric polynomial in the eigenvalues.
:::

:::

:::

:::

::: {.pf-step #char-poly}
$p_A(t) = \sum_{d=0}^{n} (-1)^d \operatorname{tr}(A^{\wedge d})\, t^{n-d}$.

::: pf-proof

::: pf-step
The characteristic polynomial of $A$ is defined by $p_A(t) = \det(tI - A)$.

::: pf-proof
The characteristic polynomial is defined as the determinant of $tI - A$, a monic polynomial of degree $n$ in $t$.
:::

:::

::: pf-step
Factoring $p_A(t)$ through its eigenvalues:
$$p_A(t) = \prod_{j=1}^n (t - \lambda_j) = \sum_{d=0}^n (-1)^d e_d(\lambda_1, \dots, \lambda_n) t^{n-d}.$$

::: pf-proof
Over $\CC$ the characteristic polynomial factors into linear factors $t - \lambda_j$, one for each eigenvalue counted with multiplicity, because the eigenvalues are the roots of $p_A$; expanding the product and collecting the coefficient of $t^{n-d}$ gives $(-1)^d$ times the sum of all products of $d$ distinct eigenvalues, which is $(-1)^d e_d$.
:::

:::

::: pf-step
Substituting $e_d(\lambda_1, \dots, \lambda_n) = \operatorname{tr}(A^{\wedge d})$ from step [](#trace-formula-for-wedge-power){.pf-ref} yields:
$$p_A(t) = \sum_{d=0}^n (-1)^d \operatorname{tr}\left(A^{\wedge d}\right) t^{n-d} = t^n - \operatorname{tr}(A) t^{n-1} + \operatorname{tr}\left(A^{\wedge 2}\right) t^{n-2} - \cdots + (-1)^n \operatorname{tr}\left(A^{\wedge n}\right),$$
with the standard convention $\operatorname{tr}(A^{\wedge 0}) = 1$ and $\operatorname{tr}(A^{\wedge n}) = \det(A)$.

::: pf-proof
Substituting the identity $\operatorname{tr}(A^{\wedge d}) = e_d(\lambda_1,\dots,\lambda_n)$ established in the trace formula into the expansion of $p_A$ gives the displayed alternating sum; the two end terms are $e_0 = 1$, since the empty product is $1$, and $e_n = \prod_j \lambda_j = \det(A)$, which is the product of the eigenvalues counted with multiplicity.
:::

:::

:::

:::

::: pf-step
$\operatorname{tr}(A^{\wedge d})$ is the $d$-th elementary symmetric polynomial in the eigenvalues, and the coefficient of $t^{n-d}$ in $\det(tI - A)$ is $(-1)^d \operatorname{tr}(A^{\wedge d})$.

::: pf-proof

The first identity is step [](#trace-formula-for-wedge-power){.pf-ref}, obtained by summing the diagonal entries of $A^{\wedge d}$ in the eigenbasis of step [](#spectral-basis){.pf-ref}; the second is step [](#char-poly){.pf-ref}, whose alternating sum has $(-1)^d e_d$ as the coefficient of $t^{n-d}$, and substituting the first identity into it replaces $e_d$ by the trace. The two end cases follow from $e_0 = 1$ and $e_n = \det(A)$.
:::

:::

:::

:::
