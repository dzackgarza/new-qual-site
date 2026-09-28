---
schema: qual/card@1
id: P-TIE-F11-20
kind: problem
title: Uniform continuity of $z^2$ on disks but not on $\mathbb{C}$
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 20.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Split off the Laplace-equation problem that the source prints under Fall 2011, question 20, page 6 of Questions_from_Tie.pdf, leaving the uniform-continuity problem and a remark.
---

::: {.problem}
Show that $f(z) = z^2$ is uniformly continuous in any open disk $\abs{z} < R$, where $R > 0$ is fixed, but it is not uniformly continuous on $\mathbb{C}$.
:::

::: {.remark}
Under this number the source also prints, as parts (1) and (2), the Cauchy problem for the Laplace equation with $u(x,y) = \frac{e^{ny} - e^{-ny}}{2n^2}\sin nx$ on the unit disk, which is question 19 of the Fall 2009 list.
It is a separate problem, carried by its own card.
:::
