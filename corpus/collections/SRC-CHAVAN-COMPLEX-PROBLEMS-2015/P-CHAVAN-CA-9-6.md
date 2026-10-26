---
schema: qual/card@1
id: P-CHAVAN-CA-9-6
kind: problem
title: The complex general linear group is path-connected
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Show that $\operatorname{GL}_n(\mathbb C)$ is path-connected.
:::

::: pf

::: pf-step

Under the coordinate identification
$$
M_n(\CC)\cong\CC^{n^2},
$$
the determinant is a polynomial function in $n^2$ complex variables.


::: pf-proof

For $A=(a_{ij})$, the Leibniz formula
$$
\det A
=
\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)
\prod_{i=1}^n a_{i,\sigma(i)}
$$
is a polynomial in the matrix entries.

:::

:::

::: pf-step

The singular matrices form the zero set of this polynomial, and therefore
$$
\operatorname{GL}_n(\CC)
=
\CC^{n^2}\setminus Z(\det).
$$


::: pf-proof

A complex matrix is invertible if and only if its determinant is nonzero.

:::

:::

::: pf-step

The space $\operatorname{GL}_n(\CC)$ is path-connected.


::: pf-proof

Theorem 9.5 in the source states that the complement of the zero set of any
complex polynomial in $N$ variables is path-connected. Apply it with
$N=n^2$ and the determinant polynomial from step <1>1, then use the
identification in step <1>2.

:::

:::

::: pf-qed

Step <1>3 is the required conclusion.

:::

:::
