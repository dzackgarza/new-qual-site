---
schema: qual/card@1
id: P-BERK84S-12
kind: problem
title: Orders of finite vector spaces, GLn, and SLn
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 12 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the ordered-basis count for GL_n and the determinant-fiber count for SL_n.
---

::: {.problem}
Let $\mathbf { F } _ { q }$ be a finite field with q elements and let V be an ndimensional vector space over $\mathbf { F } _ { q }$

1. Determine the number of elements in V .

2. Let $G L _ { n } ( \mathbf { F } _ { q } )$ denote the group of all $n \times n$ nonsingular matrices A over $\mathbf { F } _ { q }$ . Determine the order of $G L _ { n } ( \mathbf { F } _ { q } )$

3. Let $S L _ { n } ( \mathbf { F } _ { q } )$ denote the subgroup of $G L _ { n } ( \mathbf { F } _ { q } )$ consisting of matrices with determinant 1. Find the order of $S L _ { n } ( \mathbf { F } _ { q } )$
:::


::: {.solution}
<1>1. The vector space $V$ has $q^n$ elements.
::: {.proof}
Choose a basis $e_1,\ldots,e_n$ of $V$. Every vector has a unique expression
\[
v=a_1e_1+\cdots+a_ne_n,
\qquad a_i\in\mathbf F_q.
\]
There are $q$ choices for each of the $n$ coefficients, hence
\[
\boxed{|V|=q^n}.
\]
:::

<1>2. The order of $\mathrm{GL}_n(\mathbf F_q)$ is
\[
\boxed{
|\mathrm{GL}_n(\mathbf F_q)|
=\prod_{j=0}^{n-1}(q^n-q^j).
}
\]
::: {.proof}
An invertible $n\times n$ matrix is the same thing as an ordered basis of $\mathbf F_q^n$, with the columns of the matrix as the basis vectors.

The first column may be any nonzero vector, giving
\[
q^n-1
\]
choices. Once $j$ linearly independent columns have been chosen, their span has $q^j$ elements, so the next column may be any of the
\[
q^n-q^j
\]
vectors outside that span. Therefore
\[
|\mathrm{GL}_n(\mathbf F_q)|
=(q^n-1)(q^n-q)(q^n-q^2)\cdots(q^n-q^{n-1}).
\]
:::

<1>3. The order of $\mathrm{SL}_n(\mathbf F_q)$ is
\[
\boxed{
|\mathrm{SL}_n(\mathbf F_q)|
=\frac1{q-1}\prod_{j=0}^{n-1}(q^n-q^j).
}
\]
::: {.proof}
The determinant defines a group homomorphism
\[
\det:\mathrm{GL}_n(\mathbf F_q)\longrightarrow\mathbf F_q^\times.
\]
It is surjective: for each $a\in\mathbf F_q^\times$,
\[
\det\operatorname{diag}(a,1,\ldots,1)=a.
\]
Its kernel is exactly $\mathrm{SL}_n(\mathbf F_q)$. Since
\[
|\mathbf F_q^\times|=q-1,
\]
the first isomorphism theorem gives
\[
[\mathrm{GL}_n(\mathbf F_q):\mathrm{SL}_n(\mathbf F_q)]=q-1.
\]
Dividing the result of <1>2 by $q-1$ yields the displayed formula.
:::
:::
