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
<1>1. Suppose real coefficients $c_1,\ldots,c_n$ satisfy
$$
\sum_{j=1}^n c_je^{\alpha_jt}=0
$$
for every real $t$.

::: {.proof}
This is the general form of a real linear relation among the given
functions. It remains to show that every coefficient is zero.
:::

<1>2. For each integer
$$
k=0,\ldots,n-1,
$$
one has
$$
\sum_{j=1}^n c_j\alpha_j^k=0.
$$

::: {.proof}
Differentiate the identity from step <1>1 exactly $k$ times:
$$
\sum_{j=1}^n
c_j\alpha_j^k e^{\alpha_jt}
=0.
$$
Evaluating at $t=0$ gives the displayed relation.
:::

<1>3. The relations from step <1>2 form the matrix equation
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

::: {.proof}
The row indexed by $k$ is exactly the equation in step <1>2.
:::

<1>4. The matrix in step <1>3 is invertible.

::: {.proof}
It is a Vandermonde matrix. Its determinant is
$$
\prod_{1\leq i<j\leq n}
(\alpha_j-\alpha_i).
$$
The numbers $\alpha_1,\ldots,\alpha_n$ are distinct, so every factor is
nonzero. Hence the determinant is nonzero.
:::

<1>5. One has
$$
c_1=\cdots=c_n=0.
$$

::: {.proof}
Step <1>3 places the coefficient vector in the kernel of the invertible
matrix from step <1>4. That kernel is trivial.
:::

<1>6. The functions
$$
e^{\alpha_1t},\ldots,e^{\alpha_nt}
$$
are linearly independent over $\RR$.

::: {.proof}
Step <1>5 shows that the only real linear relation among them is the
trivial relation.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
