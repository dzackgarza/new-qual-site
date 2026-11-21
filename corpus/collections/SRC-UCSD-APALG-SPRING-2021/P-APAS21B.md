---
schema: qual/card@1
id: P-APAS21B
kind: problem
title: Rayleigh min-characterization of $\lambda_n$; $p$-norm of a diagonal matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, which is
    correct as it stood. Added: the spectral theorem as the named input (A = A^H makes A
    normal, and the eigenvalues are real, which is what lets the Rayleigh quotient be called a
    convex combination of them); the weights written out with the normalizing sum; and the
    finite-p case checked term by term including the hypothesis d_j = M. Since the executant
    ordered the eigenvalues decreasingly and the statement concerns lambda_n, the two steps are
    labelled part-a and part-b and the second covers p = infinity separately. Not claimed: a
    retained solution set; the provenance names the examination paper.
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex components, and $x^H$ denotes the Hermitian transpose of a vector or matrix $x$.

(a) Consider any Hermitian $A \in M_n$ with eigenvalues ordered so that $\lambda_n(A) \le \cdots \le \lambda_2(A) \le \lambda_1(A)$.
Prove that
$$
\lambda_n = \min_{x \ne 0} \frac{x^H A x}{x^H x}.
$$

(b) Suppose that $D \in M_n$ with $D = \operatorname{diag}(d_1, d_2, \dots, d_n)$.
Prove that for all $1 \le p \le \infty$ the $p$-norm of $D$ is given by $\norm{D}_p = \max_{1 \le i \le n} \abs{d_i}$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/202-Qual-SP21.pdf`, the examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $A\in M_n$ is Hermitian with eigenvalues ordered $\lambda_n\le\cdots\le\lambda_1$, $D=\operatorname{diag}(d_1,\dots,d_n)$, and $\norm{\cdot}_p$ is the operator norm induced by the vector $p$-norm, for $1\le p\le\infty$.

::: pf

::: {.pf-step #spectral}
There is an orthonormal basis $u_1,\dots,u_n$ of $\CC^n$ with $Au_i=\lambda_iu_i$ and $\lambda_i\in\RR$.

::: pf-proof
This is the spectral theorem for Hermitian matrices: $A=A^H$, so $A$ is normal and unitarily diagonalizable, and the eigenvalues of a Hermitian matrix are real.

:::

:::

::: {.pf-step #rayleigh}
For $x\ne0$, $\dfrac{x^HAx}{x^Hx}\ge\lambda_n$, with equality for any nonzero $x$ in the $\lambda_n$-eigenspace.

::: pf-proof
Write $x=\sum_ic_iu_i$ with $c_i\in\CC$, not all zero. Then $x^Hx=\sum_i\abs{c_i}^2$ and $x^HAx=\sum_i\lambda_i\abs{c_i}^2$, since the basis is orthonormal; hence
$$
\frac{x^HAx}{x^Hx}=\frac{\sum_i\lambda_i\abs{c_i}^2}{\sum_i\abs{c_i}^2},
$$
a convex combination of the real numbers $\lambda_i$ with weights $\abs{c_i}^2/\sum_j\abs{c_j}^2$, which are nonnegative and sum to $1$. Such a combination lies between $\min_i\lambda_i=\lambda_n$ and $\max_i\lambda_i$. For $x=u_n$ the combination is $\lambda_n$ itself.

:::

:::

::: {.pf-step #part-a}
$\lambda_n=\min_{x\ne0}\dfrac{x^HAx}{x^Hx}$.

::: pf-proof
Step [](#rayleigh){.pf-ref} gives the inequality in one direction for every $x\ne0$ and equality at $x=u_n$, so the minimum exists and equals $\lambda_n$.

:::

:::

::: {.pf-step #finite-p}
For $1\le p<\infty$, $\norm{D}_p=M\coloneqq\max_i\abs{d_i}$.

::: pf-proof
For any $x$, $\norm{Dx}_p^p=\sum_i\abs{d_ix_i}^p\le M^p\sum_i\abs{x_i}^p=M^p\norm{x}_p^p$, so $\norm{D}_p\le M$. If $j$ is an index with $\abs{d_j}=M$ then $\norm{De_j}_p=\abs{d_j}=M=\norm{e_j}_pM$, so the supremum is attained and $\norm{D}_p=M$.

:::

:::

::: {.pf-step #infinite-p}
For $p=\infty$, $\norm{D}_\infty=M$.

::: pf-proof
$\norm{Dx}_\infty=\max_i\abs{d_ix_i}\le M\max_i\abs{x_i}=M\norm{x}_\infty$, so $\norm{D}_\infty\le M$; and at $x=e_j$ with $\abs{d_j}=M$ one has $\norm{De_j}_\infty=M$.

:::

:::

::: {.pf-step #part-b}
$\norm{D}_p=\max_{1\le i\le n}\abs{d_i}$ for every $1\le p\le\infty$.

::: pf-proof
Steps [](#finite-p){.pf-ref} and [](#infinite-p){.pf-ref} cover all $p$ in the stated range.

:::

:::

:::
:::
