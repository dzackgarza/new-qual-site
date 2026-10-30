---
schema: qual/card@1
id: P-APAS18B
kind: problem
title: Sum of $\abs{\lambda_i}^2$ bounded by sum of $\sigma_i^2$; equality and normality
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Normal Operators
relations: []
review: draft
---

::: {.problem}
Let $A\in\CC^{n\times n}$ be a matrix with eigenvalues $\lambda_1,\ldots,\lambda_n\in\CC$ and singular values $\sigma_1\geq\cdots\geq\sigma_n\geq 0$.
Show that
$$
\abs{\lambda_1}^2+\cdots+\abs{\lambda_n}^2\leq\sigma_1^2+\cdots+\sigma_n^2.
$$
If the above is an equality, is the matrix $A$ normal (i.e., $AA^*=A^*A$)? If yes, explain why; if no, give a counterexample.
:::

::: {.solution}

::: pf

::: {.pf-step #frobenius}

There is a unitary $U$ and an upper triangular $T=(t_{ij})$ with $A=UTU^*$, $t_{ii}=\lambda_i$, and
$$
\sum_{i=1}^n\sigma_i^2=\sum_{i=1}^n\abs{\lambda_i}^2+\sum_{i<j}\abs{t_{ij}}^2 .
$$

::: pf-proof

Schur decomposition gives $U$ and $T$, with the eigenvalues on the diagonal of $T$. The squared singular values are the eigenvalues of $A^*A$, so $\sum_i\sigma_i^2=\operatorname{tr}(A^*A)=\norm{A}_F^2$. The Frobenius norm is unitarily invariant, so $\norm{A}_F^2=\norm{T}_F^2$, which is the right side.

:::

:::

::: pf-step

$\sum_i\abs{\lambda_i}^2\le\sum_i\sigma_i^2$.

::: pf-proof

The sum $\sum_{i<j}\abs{t_{ij}}^2$ in step [](#frobenius){.pf-ref} is nonnegative.

:::

:::

::: pf-step

$\boxed{\text{Yes}}$: equality holds if and only if $A$ is normal.

::: pf-proof

By step [](#frobenius){.pf-ref}, equality holds if and only if every $t_{ij}$ with $i<j$ vanishes, that is, $T$ is diagonal. If $T$ is diagonal, then $A=UTU^*$ is unitarily diagonalizable and therefore normal. Conversely, if $A$ is normal, then the triangular matrix $T=U^*AU$ is normal, and comparing the $(1,1)$ entries of $T^*T$ and $TT^*$ gives $\abs{t_{11}}^2=\sum_j\abs{t_{1j}}^2$, so the rest of the first row vanishes; induction on the rows shows that $T$ is diagonal.

:::

:::

:::
:::
