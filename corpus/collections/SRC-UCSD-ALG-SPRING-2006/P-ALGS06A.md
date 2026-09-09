---
schema: qual/card@1
id: P-ALGS06A
kind: problem
title: "Left and right eigenvectors of a matrix for distinct eigenvalues"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
(a) Consider $\lambda_i, \lambda_j \in \operatorname{eig}(A)$ such that $\lambda_i \neq \lambda_j$.
Let $(x_i, y_i)$ and $(x_j, y_j)$ denote the right and left eigenvectors of $A$ associated with $\lambda_i$ and $\lambda_j$.
Show that $y_i^* x_j = 0$.

(b) Let $x$ denote an eigenvector of $A$ associated with an eigenvalue $\lambda$.
Prove that if $\lambda$ has a left-eigenvector $y$ such that $y^* x = 0$, then the algebraic multiplicity $\operatorname{am}(\lambda) > 1$.
:::

::: {.solution}
<1>1. If $Ax_j=\lambda_jx_j$ and $y_i^*A=\lambda_i y_i^*$, then
\[
\lambda_i y_i^*x_j=y_i^*Ax_j=\lambda_j y_i^*x_j.
\]
Since $\lambda_i\ne\lambda_j$, one has $y_i^*x_j=0$.
::: {.proof}
Subtracting the two expressions gives
\[
(\lambda_i-\lambda_j)y_i^*x_j=0.
\]
The scalar $\lambda_i-\lambda_j$ is nonzero.
:::

<1>2. For part (b), suppose toward a contradiction that $\lambda$ has algebraic multiplicity $1$.
Then $\ker(A-\lambda I)=\langle x\rangle$, and $x\notin\operatorname{im}(A-\lambda I)$.
::: {.proof}
Algebraic multiplicity $1$ implies geometric multiplicity $1$.
If $x=(A-\lambda I)z$, then $(A-\lambda I)^2z=0$ but $(A-\lambda I)z=x\ne0$, giving a Jordan chain of length at least $2$, impossible when the algebraic multiplicity is $1$.
:::

<1>3. A left eigenvector $y$ for $\lambda$ satisfies $y^*(A-\lambda I)=0$, so
\[
\operatorname{im}(A-\lambda I)\subseteq\ker(y^*).
\]
Under the assumption of <1>2, both spaces have dimension $n-1$, hence they are equal.
::: {.proof}
Rank-nullity gives $\dim\operatorname{im}(A-\lambda I)=n-1$, while $y\ne0$ gives $\dim\ker(y^*)=n-1$.
:::

<1>4. If $y^*x=0$, then $x\in\ker(y^*)=\operatorname{im}(A-\lambda I)$, contradicting <1>2. Therefore the algebraic multiplicity of $\lambda$ is greater than $1$.
::: {.proof}
This is the contradiction obtained from <1>2 and <1>3.
:::
:::
