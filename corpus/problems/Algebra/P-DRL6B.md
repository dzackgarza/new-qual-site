---
schema: qual/card@1
id: P-DRL6B
kind: problem
title: Diagonalizable iff the space is a direct sum of eigenspaces
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $K$, and let $T: V \to V$ be a linear operator.
Show that $T$ is diagonalizable if and only if $V$ is the direct sum of its eigenspaces:
$$V = \bigoplus_{i=1}^k E_{\lambda_i}(T) = \bigoplus_{i=1}^k \ker(T - \lambda_i I)$$
where $\lambda_1, \dots, \lambda_k \in K$ are the distinct eigenvalues of $T$.
:::

::: {.solution}
For each eigenvalue $\lambda$ of $T$, write $E_\lambda=\ker(T-\lambda I)$.

::: pf

::: {.pf-step #direct}
The sum of the eigenspaces of $T$ is direct.

::: pf-proof
Suppose $v_1+\cdots+v_r=0$ with $v_i\in E_{\lambda_i}$ and the $\lambda_i$ distinct.
Applying $\prod_{j\ne i}(T-\lambda_jI)$ gives $\left(\prod_{j\ne i}(\lambda_i-\lambda_j)\right)v_i=0$, and the scalar is nonzero, so $v_i=0$.
:::

:::

::: {.pf-step #forward}
If $T$ is diagonalizable, then $V=\bigoplus_\lambda E_\lambda$.

::: pf-proof
$V$ has a basis of eigenvectors of $T$, and every basis vector lies in some $E_\lambda$, so the eigenspaces span $V$.
By step [](#direct){.pf-ref} the sum is direct.
:::

:::

::: pf-qed
Step [](#forward){.pf-ref} proves one implication.
Conversely, suppose $V=\bigoplus_\lambda E_\lambda$.
Choose a basis of each eigenspace and take their union.
Because the sum is direct and equals $V$, this union is a basis of $V$, and each of its vectors is an eigenvector of $T$.
The matrix of $T$ in this basis is diagonal, so $T$ is diagonalizable.
:::

:::

:::
