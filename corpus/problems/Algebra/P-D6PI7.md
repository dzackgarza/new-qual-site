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
---

::: {.problem}
Let $A$ be an $n\times n$ matrix over a field $F$. Show that if $A$ is diagonalizable over $F$, its minimal polynomial is squarefree.
:::

::: {.solution}
Suppose $A$ is diagonalizable over $F$. Then for some $P\in\GL_n(F)$,
$$
P^{-1}AP=\diag(\lambda_1,\dots,\lambda_n).
$$
Let $\mu_1,\dots,\mu_r$ be the distinct eigenvalues of $A$ and put
$$
q(x)=\prod_{j=1}^r(x-\mu_j).
$$
Then $q$ is squarefree and
$$
q(A)=P\,\diag(q(\lambda_1),\dots,q(\lambda_n))P^{-1}=0.
$$
Hence the minimal polynomial $m_A$ divides $q$.

Conversely, if $\mu_j$ is an eigenvalue with eigenvector $v\ne0$, then
$$
0=m_A(A)v=m_A(\mu_j)v,
$$
so $m_A(\mu_j)=0$. Thus every factor $(x-\mu_j)$ divides $m_A$. Since these factors are pairwise coprime,
$$
q\mid m_A.
$$
Therefore $m_A=q$, a product of distinct linear factors. In particular, $m_A$ is squarefree.
:::
