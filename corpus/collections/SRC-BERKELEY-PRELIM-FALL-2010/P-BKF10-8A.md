---
schema: qual/card@1
id: P-BKF10-8A
kind: problem
title: Positive semidefinite quadratic forms are sums of squares of linear forms
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8A of the retained Berkeley Fall 2010 preliminary-exam solution packet f10solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked reduction to the symmetric part, nonnegativity of the
    spectral eigenvalues, and the resulting explicit square decomposition.
---

::: {.problem}
Suppose
$$
f(x_1,\ldots,x_n)=\sum_{j,k}a_{jk}x_jx_k
$$
for real numbers $a_{jk}$.
If $f$ is nonnegative for all real arguments, show that $f$ can be written as a finite sum of squares of linear forms in $x_1,\ldots,x_n$.
:::

::: {.solution}
Let $A=(a_{jk})$ and regard $x=(x_1,\ldots,x_n)^T$ as a column vector,
so that
$$
f(x)=x^TAx.
$$

<1>1. Replacing $A$ by its symmetric part
$$
S\coloneqq\frac{A+A^T}{2}
$$
does not change $f$.

::: {.proof}
Write
$$
A=S+K,
\qquad
K\coloneqq\frac{A-A^T}{2}.
$$
Then $K^T=-K$. Since $x^TKx$ is a real scalar,
$$
x^TKx=(x^TKx)^T=x^TK^Tx=-x^TKx,
$$
so $x^TKx=0$. Hence
$$
x^TAx=x^TSx.
$$
Thus the same quadratic form is represented by the real symmetric matrix
$S$.
:::

<1>2. There exist an orthogonal matrix $Q$ and real numbers
$\lambda_1,\ldots,\lambda_n$ such that
$$
S=Q^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)Q.
$$

::: {.proof}
This is the real spectral theorem for symmetric matrices, applied to
$S=S^T$ from step <1>1.
:::

<1>3. Every $\lambda_i$ in step <1>2 is nonnegative.

::: {.proof}
Let $e_i$ be the $i$th standard basis vector and put $x=Q^Te_i$.
Then $Qx=e_i$, so by steps <1>1 and <1>2,
$$
0\le f(x)
=x^TSx
=e_i^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)e_i
=\lambda_i.
$$
:::

<1>4. The quadratic form $f$ is a sum of squares of linear forms.

::: {.proof}
Put
$$
y=Qx.
$$
Each coordinate $y_i$ is a real linear form in $x_1,\ldots,x_n$.
Using step <1>2,
$$
f(x)=x^TSx
=y^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)y
=\sum_{i=1}^n\lambda_i y_i^2.
$$
By step <1>3, each $\lambda_i\ge0$, so
$$
\boxed{
f(x)=\sum_{i=1}^n\left(\sqrt{\lambda_i}\,y_i\right)^2
}.
$$
Each $\sqrt{\lambda_i}\,y_i$ is a real linear form in the original
variables.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required finite sum-of-squares representation.
:::
:::
