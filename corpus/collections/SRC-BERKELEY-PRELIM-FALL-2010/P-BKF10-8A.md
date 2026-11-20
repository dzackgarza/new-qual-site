---
schema: qual/card@1
id: P-BKF10-8A
kind: problem
title: Positive semidefinite quadratic forms are sums of squares of linear forms
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Provenance recorded: Problem 8A, printed pp. 3--4 of the packet is the source of the argument, and the paragraph at the head
    of the solution says what the card adds. Checked: the packet read in its text layer at the page
    named and the card's steps compared with its sentences, `qualc.authoring check` on the card, and
    `tmp/lam.sh` for the numbering and the QED. Not checked: no other card of the collection in this
    pass.
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

The argument is Problem 8A of the retained Berkeley preliminary-exam solution packet, `assets/attachments/f10solutions.pdf`, transcribed: assume the matrix symmetric; induct on $n$; if $a_{11}=0$ then every other entry of the first row and column vanishes, since $f$ would otherwise take negative values, so $a_{11}>0$; then completing the square in $x_1$ kills the rest of the first row and column and leaves a non-negative form in $n-1$ variables, which is a sum of squares by induction. What the card adds is the symplectisation to $S=(A+A^T)/2$ and the step structure, not the argument.
Let $A=(a_{jk})$ and regard $x=(x_1,\ldots,x_n)^T$ as a column vector,
so that
$$
f(x)=x^TAx.
$$

::: pf

::: {.pf-step #s1}

Replacing $A$ by its symmetric part
$$
S\coloneqq\frac{A+A^T}{2}
$$
does not change $f$.

::: pf-proof

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

:::

::: {.pf-step #s2}

There exist an orthogonal matrix $Q$ and real numbers
$\lambda_1,\ldots,\lambda_n$ such that
$$
S=Q^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)Q.
$$

::: pf-proof

This is the real spectral theorem for symmetric matrices, applied to
$S=S^T$ from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s3}

Every $\lambda_i$ in step [](#s2){.pf-ref} is nonnegative.

::: pf-proof

Let $e_i$ be the $i$th standard basis vector and put $x=Q^Te_i$.
Then $Qx=e_i$, so by steps [](#s1){.pf-ref} and [](#s2){.pf-ref},
$$
0\le f(x)
=x^TSx
=e_i^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)e_i
=\lambda_i.
$$

:::

:::

::: {.pf-step #s4}

The quadratic form $f$ is a sum of squares of linear forms.

::: pf-proof

Put
$$
y=Qx.
$$
Each coordinate $y_i$ is a real linear form in $x_1,\ldots,x_n$.
Using step [](#s2){.pf-ref},
$$
f(x)=x^TSx
=y^T\operatorname{diag}(\lambda_1,\ldots,\lambda_n)y
=\sum_{i=1}^n\lambda_i y_i^2.
$$
By step [](#s3){.pf-ref}, each $\lambda_i\ge0$, so
$$
\boxed{
f(x)=\sum_{i=1}^n\left(\sqrt{\lambda_i}\,y_i\right)^2
}.
$$
Each $\sqrt{\lambda_i}\,y_i$ is a real linear form in the original
variables.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required finite sum-of-squares representation.

:::

:::

:::
