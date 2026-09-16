---
schema: qual/card@1
id: P-TIE-F11-11
kind: problem
title: Fixed points of analytic self-maps of the disk
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 11.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the OCR misreading of |z| = 1? as |z| = 12 and labelled the bulleted parts (a)-(c), matching the source reference to (a), against Fall 2011, question 11, pages 5-6 of Questions_from_Tie.pdf.
---

::: {.problem}
Let $g$ be analytic for $\abs{z} \le 1$ and $\abs{g(z)} < 1$ for $\abs{z} = 1$.

(a) Show that $g$ has a unique fixed point in $\abs{z} < 1$.

(b) What happens if we replace $\abs{g(z)} < 1$ with $\abs{g(z)} \le 1$ for $\abs{z} = 1$? Give an example if (a) is not true or give an proof if (a) is still true.

(c) What happens if we simply assume that $f$ is analytic for $\abs{z} < 1$ and $\abs{f(z)} < 1$ for $\abs{z} < 1$? Suppose that $f(z) \not\equiv z$. Can $f$ have more than one fixed point in $\abs{z} < 1$?

Hint: The map $\psi_\alpha(z) = \frac{\alpha - z}{1 - \bar{\alpha} z}$ may be useful.
:::
