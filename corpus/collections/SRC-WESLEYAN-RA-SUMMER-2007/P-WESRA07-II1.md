---
schema: qual/card@1
id: P-WESRA07-II1
kind: problem
title: Continuity from below and failure of continuity from above without finiteness
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a measure space and let $A_1\subseteq A_2\subseteq\cdots$ be measurable.
Prove that
\[
\mu\!\left(\bigcup_{n=1}^\infty A_n\right)=\lim_{n\to\infty}\mu(A_n).
\]
Give an example showing that the corresponding statement for decreasing sequences is false in general.
:::

::: {.solution}
For $n\ge2$ set $B_n=A_n\setminus A_{n-1}$ and set $B_1=A_1$.
Then the $B_n$ are pairwise disjoint and
\[
A_n=\bigcup_{k=1}^n B_k,
\qquad
\bigcup_{n=1}^\infty A_n=\bigcup_{k=1}^\infty B_k.
\]
Hence countable additivity gives
\[
\mu(A_n)=\sum_{k=1}^n\mu(B_k)
\longrightarrow
\sum_{k=1}^\infty\mu(B_k)
=
\mu\!\left(\bigcup_{n=1}^\infty A_n\right).
\]

For the decreasing analogue, take Lebesgue measure on $\mathbb R$ and
\[
E_n=[n,\infty).
\]
Then $E_1\supseteq E_2\supseteq\cdots$ and
\[
\bigcap_{n=1}^\infty E_n=\varnothing,
\]
but
\[
\mu(E_n)=\infty
\quad\text{for every }n.
\]
Thus
\[
\lim_{n\to\infty}\mu(E_n)=\infty
\ne0
=
\mu\!\left(\bigcap_{n=1}^\infty E_n\right).
\]
The usual continuity-from-above theorem therefore requires a finiteness hypothesis such as $\mu(E_1)<\infty$.
:::
