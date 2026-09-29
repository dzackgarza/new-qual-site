---
schema: qual/card@1
id: P-BKF90-5
kind: problem
title: A quotient of quadratic forms converges to an eigenvalue
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Expanded y in an orthonormal eigenbasis and showed the quotient converges
    to the largest eigenvalue whose eigenspace has a nonzero component of y.
---

::: {.problem}
Let $A$ be a real symmetric positive-definite $n\times n$ matrix and let $0\ne y\in\mathbb R^n$.
Prove that
\[
\lim_{m\to\infty}\frac{y^TA^{m+1}y}{y^TA^my}
\]
exists and is an eigenvalue of $A$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

There is an orthonormal basis $v_1,\ldots,v_n$ of eigenvectors of $A$ with positive eigenvalues $\lambda_1,\ldots,\lambda_n$.

::: pf-proof

Since $A$ is real symmetric, the spectral theorem gives an orthonormal eigenbasis. Since $A$ is positive definite, every eigenvalue is positive.

:::

:::

::: {.pf-step #s2}

Write
$$
y=\sum_{i=1}^n c_i v_i,
$$
and define
$$
\lambda_*\coloneqq\max\{\lambda_i:c_i\ne0\}.
$$
Then $\lambda_*$ is well-defined and is an eigenvalue of $A$.

::: pf-proof

Because $y\ne0$, at least one coefficient $c_i$ is nonzero. Hence the displayed set is a nonempty finite set of eigenvalues of $A$, so it has a maximum, and that maximum is itself an eigenvalue.

:::

:::

::: {.pf-step #s3}

For every nonnegative integer $m$,
$$
y^TA^my=\sum_{i=1}^n c_i^2\lambda_i^m>0.
$$

::: pf-proof

Using the orthonormal eigenbasis from step [](#s1){.pf-ref},
$$
A^my=\sum_{i=1}^n c_i\lambda_i^m v_i.
$$
Taking the inner product with $y$ gives the displayed sum. Every term is nonnegative, and at least one is positive because some $c_i\ne0$ and every $\lambda_i>0$.

:::

:::

::: {.pf-step #s4}

The quotient satisfies
$$
\frac{y^TA^{m+1}y}{y^TA^my}
=
\frac{\displaystyle\sum_{i=1}^n c_i^2\lambda_i(\lambda_i/\lambda_*)^m}
{\displaystyle\sum_{i=1}^n c_i^2(\lambda_i/\lambda_*)^m}.
$$

::: pf-proof

Apply step [](#s3){.pf-ref} with exponents $m$ and $m+1$, then divide numerator and denominator by the positive number $\lambda_*^m$.

:::

:::

::: {.pf-step #s5}

The quotient converges to $\lambda_*$.

::: pf-proof

If $c_i\ne0$, then $0<\lambda_i/\lambda_*\le1$ by definition of $\lambda_*$. Thus every term with $\lambda_i<\lambda_*$ tends to $0$ as $m\to\infty$, while every term with $\lambda_i=\lambda_*$ remains unchanged. Put
$$
S\coloneqq\sum_{\substack{i\\ \lambda_i=\lambda_*}}c_i^2.
$$
By definition of $\lambda_*$, one has $S>0$. Therefore step [](#s4){.pf-ref} gives
$$
\lim_{m\to\infty}\frac{y^TA^{m+1}y}{y^TA^my}
=
\frac{\lambda_*S}{S}
=
\lambda_*.
$$

:::

:::

::: {.pf-step #s6}

Hence
$$
\boxed{\lim_{m\to\infty}\frac{y^TA^{m+1}y}{y^TA^my}=\lambda_*},
$$
and this limit is an eigenvalue of $A$.

::: pf-proof

Step [](#s5){.pf-ref} gives the limit, and step [](#s2){.pf-ref} shows that $\lambda_*$ is an eigenvalue of $A$.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} is exactly the required conclusion.

:::

:::

:::
