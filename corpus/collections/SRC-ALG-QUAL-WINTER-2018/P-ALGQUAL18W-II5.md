---
schema: qual/card@1
id: P-ALGQUAL18W-II5
kind: problem
title: Trace of the induced endomorphism on the symmetric square
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 5 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md; Flash mangles the symmetric-square notation in the problem line, while its worked solution repeatedly identifies the induced map as $S^2f$.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Independently proved the identity from matrix coefficients on the standard
    basis of the symmetric square, without extending the field or dividing by
    2, so the argument works in every characteristic. Direct pdftotext review
    of the source PDF confirms its trace sum is over i<=j; the retained Flash
    extraction drops the equality sign there.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $F$, and let $f:V\to V$ be linear.
Let $S^2f$ denote the induced endomorphism of the symmetric square $S^2V$.
Prove that
\[
2\operatorname{tr}(S^2f)
=
\operatorname{tr}(f)^2+\operatorname{tr}(f^2).
\]
:::

::: {.solution}
Let
$$
n=\dim_F V
$$
and choose a basis $v_1,\ldots,v_n$ of $V$. Write
$$
f(v_j)=\sum_{i=1}^n a_{ij}v_i.
$$

<1>1. The vectors
$$
v_i v_j,
\qquad
1\leq i\leq j\leq n,
$$
form a basis of $S^2V$.

::: {.proof}
The symmetric square is the degree-two part of the symmetric algebra on $V$.
Relative to the chosen basis of $V$, its degree-two monomials are exactly the
displayed vectors.
:::

<1>2. In the basis from step <1>1,
$$
\trace(S^2f)
=
\sum_{i=1}^n a_{ii}^2
+
\sum_{1\leq i<j\leq n}
\left(a_{ii}a_{jj}+a_{ij}a_{ji}\right).
$$

::: {.proof}
For a diagonal basis vector,
$$
(S^2f)(v_i^2)=f(v_i)^2,
$$
whose coefficient of $v_i^2$ is $a_{ii}^2$.

If $i<j$, then
$$
(S^2f)(v_i v_j)
=
f(v_i)f(v_j).
$$
The terms contributing to the coefficient of $v_i v_j$ are obtained by
choosing $v_i$ from $f(v_i)$ and $v_j$ from $f(v_j)$, or $v_j$ from
$f(v_i)$ and $v_i$ from $f(v_j)$. Their total coefficient is
$$
a_{ii}a_{jj}+a_{ji}a_{ij}.
$$
Summing these diagonal coefficients over the basis from step <1>1 gives the
displayed trace formula.
:::

<1>3. The square of the trace of $f$ is
$$
\trace(f)^2
=
\sum_{i=1}^n a_{ii}^2
+
2\sum_{1\leq i<j\leq n}a_{ii}a_{jj}.
$$

::: {.proof}
Since
$$
\trace(f)=\sum_{i=1}^n a_{ii},
$$
expanding its square gives the formula.
:::

<1>4. The trace of $f^2$ is
$$
\trace(f^2)
=
\sum_{i=1}^n a_{ii}^2
+
2\sum_{1\leq i<j\leq n}a_{ij}a_{ji}.
$$

::: {.proof}
If $A=(a_{ij})$ is the matrix of $f$, then
$$
\trace(f^2)
=
\sum_{i=1}^n(A^2)_{ii}
=
\sum_{i,j=1}^n a_{ij}a_{ji}.
$$
The terms with $i=j$ give $\sum_i a_{ii}^2$. For each pair $i<j$, the two
off-diagonal terms are
$$
a_{ij}a_{ji}
\qquad\text{and}\qquad
a_{ji}a_{ij},
$$
whose sum is $2a_{ij}a_{ji}$.
:::

<1>5. The required identity holds:
$$
\boxed{
2\trace(S^2f)
=
\trace(f)^2+\trace(f^2)
}.
$$

::: {.proof}
Doubling the formula in step <1>2 gives
$$
2\trace(S^2f)
=
2\sum_i a_{ii}^2
+
2\sum_{i<j}a_{ii}a_{jj}
+
2\sum_{i<j}a_{ij}a_{ji}.
$$
Adding the formulas from steps <1>3 and <1>4 gives exactly the same
expression.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is precisely the claimed trace identity.
:::
:::
