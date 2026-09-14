---
schema: qual/card@1
id: P-CHAVAN-CA-1-1
kind: problem
title: Maximum modulus for polynomials via a unitary dilation
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1.1 in the deterministic MinerU Flash extraction; the standard-basis dimension is corrected to match the displayed (n+1)-by-(n+1) matrix.
---

::: {.problem}
Let
\[
p(z)=a_0+a_1z+\cdots+a_nz^n,
\qquad
s=\sqrt{1-|z|^2},
\qquad |z|\le1,
\]
and let $e_1,\ldots,e_{n+1}$ be the standard basis of $\mathbb C^{n+1}$.

1. Let $U$ be the $(n+1)\times(n+1)$ matrix whose columns, in order, are
   \[
   ze_1+se_2,\ e_3,\ldots,e_{n+1},\ se_1-\overline z e_2.
   \]
   Show that $U$ is unitary, hence its eigenvalues $\lambda_1,\ldots,\lambda_{n+1}$ have modulus $1$.
2. Show that $z^k=e_1^TU^ke_1$, and hence $p(z)=e_1^Tp(U)e_1$.
3. Deduce
   \[
   \max_{|z|\le1}|p(z)|\le\|p(U)\|.
   \]
4. If $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_{n+1})$, show
   \[
   \|p(U)\|=\|p(D)\|=\max_i|p(\lambda_i)|.
   \]

Conclude that
\[
\max_{|z|\le1}|p(z)|=\max_{|z|=1}|p(z)|.
\]
:::
