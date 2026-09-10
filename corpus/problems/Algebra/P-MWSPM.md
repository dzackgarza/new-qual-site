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

::: problem
Show that a finitely generated module over a Noetherian local ring is flat iff it is free.
:::

::: {.solution}
Let $(R,\mathfrak m)$ be a Noetherian local ring and let $M$ be finitely generated.

Free modules are flat. Conversely, suppose $M$ is flat. Choose $m_1,\dots,m_r\in M$ whose images form a basis of the $R/\mathfrak m$-vector space $M/\mathfrak mM$. Nakayama's lemma says they generate $M$, so there is an exact sequence
\[
0\to K\to R^r\to M\to0.
\]
Because $M$ is flat, tensoring with $k=R/\mathfrak m$ preserves exactness on the left. Hence
\[
0\to K/\mathfrak mK\to k^r\to M/\mathfrak mM\to0.
\]
The last map is an isomorphism by construction, so $K/\mathfrak mK=0$. Since $R$ is Noetherian, $K\subset R^r$ is finitely generated; Nakayama therefore gives $K=0$. Thus $M\cong R^r$ is free.
:::
