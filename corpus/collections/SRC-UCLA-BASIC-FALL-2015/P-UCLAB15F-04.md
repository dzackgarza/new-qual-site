---
schema: qual/card@1
id: P-UCLAB15F-04
kind: problem
title: Limit of a recursively defined Volterra sequence
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
Define $f_n:[0,\infty)\to\mathbb R$ recursively by $f_1(x)=0$ and
\[
f_{n+1}(x)=e^{-2x}+\int_0^x f_n(t)e^{-2t}\,dt,
\qquad n\ge1.
\]
Show that
\[
f(x):=\lim_{n\to\infty}f_n(x)
\]
exists for all $x\ge0$ and identify $f$ explicitly.
:::
