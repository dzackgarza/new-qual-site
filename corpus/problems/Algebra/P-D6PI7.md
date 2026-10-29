---
schema: qual/card@1
id: P-D6PI7
kind: problem
title: Diagonalizable matrices have squarefree minimal polynomials
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Minimal and Characteristic Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source reads "- Show that if a matrix is diagonalizable, its minimal polynomial is squarefree." with no matrix or field declared; the statement declares an n x n matrix A over a field F.'
- event: solution-written
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Converted the prose solution to a STYLE-08 structured proof.
---

::: {.problem}
Let $A$ be an $n\times n$ matrix over a field $F$. Show that if $A$ is diagonalizable over $F$, its minimal polynomial is squarefree.
:::

::: {.solution}
Suppose $A$ is diagonalizable over $F$, so that $P^{-1}AP=\diag(\lambda_1,\ldots,\lambda_n)$ for some $P\in\GL_n(F)$.
Let $\mu_1,\ldots,\mu_r$ be the distinct eigenvalues of $A$, put $q(x)=\prod_{j=1}^r(x-\mu_j)$, and let $m_A$ be the minimal polynomial of $A$.

::: pf

::: {.pf-step #divides}
$m_A\mid q$.

::: pf-proof
Each $\lambda_i$ is one of the $\mu_j$, so $q(\lambda_i)=0$ and
$$
q(A)=P\,\diag(q(\lambda_1),\ldots,q(\lambda_n))P^{-1}=0.
$$
The minimal polynomial divides every polynomial that annihilates $A$.
:::

:::

::: {.pf-step #divided}
$q\mid m_A$.

::: pf-proof
If $v\ne0$ is an eigenvector for $\mu_j$, then $0=m_A(A)v=m_A(\mu_j)v$, so $m_A(\mu_j)=0$ and $(x-\mu_j)\mid m_A$.
The factors $x-\mu_j$ are pairwise coprime, so their product $q$ divides $m_A$.
:::

:::

::: pf-qed
Both polynomials are monic, so steps [](#divides){.pf-ref} and [](#divided){.pf-ref} give $m_A=q$, a product of distinct linear factors.
Hence $m_A$ is squarefree.
:::

:::

:::
