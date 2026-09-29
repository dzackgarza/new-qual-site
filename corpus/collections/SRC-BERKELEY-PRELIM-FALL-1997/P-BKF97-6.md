---
schema: qual/card@1
id: P-BKF97-6
kind: problem
title: Distinct real exponentials are linearly independent
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 in the deterministic MinerU Flash extraction assets/attachments/Fall97_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Differentiated a putative linear relation through order n-1 at zero;
    the coefficient vector lies in the kernel of a Vandermonde matrix with
    nonzero determinant.
---

::: {.problem}
Let $\alpha_1,\ldots,\alpha_n$ be distinct real numbers.
Show that the functions
\[
e^{\alpha_1t},\ldots,e^{\alpha_nt}
\]
are linearly independent over $\mathbb R$.
:::

::: {.solution}

::: pf

::: {.pf-step #linear-relation-assumption}
Suppose real coefficients $c_1,\ldots,c_n$ satisfy
$$
\sum_{j=1}^n c_je^{\alpha_jt}=0
$$
for every real $t$.

::: pf-proof
This is the general form of a real linear relation among the given
functions. It remains to show that every coefficient is zero.
:::

:::

::: {.pf-step #moment-relations}
For each integer
$$
k=0,\ldots,n-1,
$$
one has
$$
\sum_{j=1}^n c_j\alpha_j^k=0.
$$

::: pf-proof
Differentiate the identity from step [](#linear-relation-assumption){.pf-ref} exactly $k$ times:
$$
\sum_{j=1}^n
c_j\alpha_j^k e^{\alpha_jt}
=0.
$$
Evaluating at $t=0$ gives the displayed relation.
:::

:::

::: {.pf-step #vandermonde-system}
The relations from step [](#moment-relations){.pf-ref} form the matrix equation
$$
\begin{pmatrix}
1&1&\cdots&1\\
\alpha_1&\alpha_2&\cdots&\alpha_n\\
\alpha_1^2&\alpha_2^2&\cdots&\alpha_n^2\\
\vdots&\vdots&&\vdots\\
\alpha_1^{n-1}&\alpha_2^{n-1}&\cdots&\alpha_n^{n-1}
\end{pmatrix}
\begin{pmatrix}
c_1\\
c_2\\
\vdots\\
c_n
\end{pmatrix}
=0.
$$

::: pf-proof
The row indexed by $k$ is exactly the equation in step [](#moment-relations){.pf-ref}.
:::

:::

::: {.pf-step #vandermonde-invertible}
The matrix in step [](#vandermonde-system){.pf-ref} is invertible.

::: pf-proof
It is a Vandermonde matrix. Its determinant is
$$
\prod_{1\leq i<j\leq n}
(\alpha_j-\alpha_i).
$$
The numbers $\alpha_1,\ldots,\alpha_n$ are distinct, so every factor is
nonzero. Hence the determinant is nonzero.
:::

:::

::: {.pf-step #coefficients-zero}
One has
$$
c_1=\cdots=c_n=0.
$$

::: pf-proof
Step [](#vandermonde-system){.pf-ref} places the coefficient vector in the kernel of the invertible
matrix from step [](#vandermonde-invertible){.pf-ref}. That kernel is trivial.
:::

:::

::: {.pf-step #functions-linearly-independent}
The functions
$$
e^{\alpha_1t},\ldots,e^{\alpha_nt}
$$
are linearly independent over $\RR$.

::: pf-proof
Step [](#coefficients-zero){.pf-ref} shows that the only real linear relation among them is the
trivial relation.
:::

:::

::: pf-qed
Step [](#functions-linearly-independent){.pf-ref} is the required conclusion.
:::

:::

:::
