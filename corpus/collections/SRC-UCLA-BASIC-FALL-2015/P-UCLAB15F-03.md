---
schema: qual/card@1
id: P-UCLAB15F-03
kind: problem
title: Continuity of the pointwise limit of an alternating monotone series
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Basic Examination, Fall 2015, `assets/attachments/basic-15F.pdf`; the PDF is image-only and the preserved extraction supplies the statement text.
---

::: {.problem}
Let $\{f_n\}$ be continuous functions $f_n:[-1,1]\to[0,1]$ such that for each $x\in[-1,1]$:

1. the sequence $\{f_n(x)\}_{n=1}^{\infty}$ is non-increasing;
2. $\lim_{n\to\infty}f_n(x)=0$.

Define
\[
g_n(x):=\sum_{m=1}^n(-1)^m f_m(x).
\]
Prove that $g_n(x)$ converges to some $g(x)\in\mathbb R$ for every $x\in[-1,1]$ and that the resulting function $g:[-1,1]\to\mathbb R$ is continuous.
:::
