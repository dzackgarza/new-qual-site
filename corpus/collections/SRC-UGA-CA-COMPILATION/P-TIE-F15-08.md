---
schema: qual/card@1
id: P-TIE-F15-08
kind: problem
title: Taylor coefficient ratios detect a pole on the unit circle
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2015, question 8.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the source wording of Fall 2015, question 8, page 10 of Questions_from_Tie.pdf, and moved the note on the expression the source omits for c_n into a remark.
---

::: {.problem}
Suppose that $f$ is holomorphic in an open set containing the closed unit disc, except for a pole at $z_0$ on the unit circle. Let denote the the power series in the open disc. Show that (1) $c_n \ne 0$ for all large enough $n$'s, and (2) $\lim_{n\to\infty} \frac{c_n}{c_{n+1}} = z_0$.
:::

::: {.remark}
The source omits the defining expression between "Let" and "denote", so the coefficients $c_n$ are never introduced.
From the conclusions, the missing text defines $c_n$ as the coefficients of the power series expansion of $f$ in the open unit disc, $f(z) = \sum_{n=0}^\infty c_n z^n$ for $\abs{z} < 1$; the source does not supply this wording.
:::
