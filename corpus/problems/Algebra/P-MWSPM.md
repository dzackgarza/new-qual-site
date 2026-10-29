---
schema: qual/card@1
id: P-MWSPM
kind: problem
title: Finitely generated flat modules over Noetherian local rings are free
classification:
  areas:
  - algebra
  topics:
  - Nakayama's Lemma
  - Free Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that a finitely generated module over a Noetherian local ring is flat iff it is free.
:::

::: {.solution}
Let $(R,\mathfrak m)$ be a Noetherian local ring with residue field $k=R/\mathfrak m$, and let $M$ be a finitely generated $R$-module.

::: pf

::: pf-step
If $M$ is free, then $M$ is flat.

::: pf-proof
Tensor product commutes with direct sums, and $R\otimes_R-$ is the identity functor, so $R^{(I)}\otimes_R-$ is exact.
:::

:::

::: {.pf-step #presentation}
There is an exact sequence $0\to K\to R^r\to M\to0$ such that $R^r\otimes_R k\to M\otimes_R k$ is an isomorphism.

::: pf-proof
Choose $m_1,\ldots,m_r\in M$ whose images form a basis of the $k$-vector space $M/\mathfrak mM$.
By Nakayama's lemma they generate $M$, so $e_i\mapsto m_i$ defines a surjection $R^r\to M$ with some kernel $K$, and after tensoring with $k$ it sends a basis of $k^r$ to a basis of $M/\mathfrak mM$.
:::

:::

::: pf-step
If $M$ is flat, then $M\cong R^r$ is free.

::: pf-proof
Since $M$ is flat, $\operatorname{Tor}_1^R(M,k)=0$, so tensoring the sequence of step [](#presentation){.pf-ref} with $k$ gives an exact sequence $0\to K/\mathfrak mK\to k^r\to M/\mathfrak mM\to0$.
The last map is an isomorphism by step [](#presentation){.pf-ref}, so $K/\mathfrak mK=0$.
Since $R$ is Noetherian, the submodule $K$ of $R^r$ is finitely generated, and Nakayama's lemma gives $K=0$.
:::

:::

:::

:::
