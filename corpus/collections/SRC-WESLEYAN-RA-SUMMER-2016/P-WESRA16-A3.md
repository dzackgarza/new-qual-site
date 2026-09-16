---
schema: qual/card@1
id: P-WESRA16-A3
kind: problem
title: 'Integration against a nonnegative measurable density and continuity from below'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group A, problem A3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash severely garbles the opening sentence of part (a), but the displayed definition of $\mu$, the words “is a countably-additive measure,” and part (b) determine the mathematical task.
---

::: {.problem}
Let $f:\mathbb R^d\to[0,\infty)$ be measurable and define
\[
\mu(A)=\int_{\mathbb R^d}f\,\mathbf1_A.
\]

(a) Prove that $\mu$ is a countably additive measure on the Lebesgue measurable sets.

(b) If $M_0\subseteq M_1\subseteq\cdots$ are measurable and $M=\bigcup_nM_n$, prove that
\[
\lim_{n\to\infty}\int_{\mathbb R^d}f\mathbf1_{M_n}
\]
exists, identifying the limit.
:::
