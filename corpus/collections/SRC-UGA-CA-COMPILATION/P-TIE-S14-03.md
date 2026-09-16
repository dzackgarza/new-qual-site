---
schema: qual/card@1
id: P-TIE-S14-03
kind: problem
title: $\int_{|z|=r}\frac{dz}{(z-a)(z-b)}$ for $|a|<r<|b|$ without Cauchy's theorem
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2014, question 3.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Separated part 3 of Spring 2014 question 1 from questions 2 and 3, which had been merged into this card, against page 7 of Questions_from_Tie.pdf; questions 2 and 3 are carried by their existing cards.
---

::: {.problem}
Solve the problem without using the Cauchy theorem.

Show that if $\abs{a} < r < \abs{b}$, then
$$
\int_\gamma \frac{dz}{(z-a)(z-b)}\,dz = \frac{2\pi i}{a-b}.
$$
Here $\gamma$ denotes the circle centered at the origin, of radius $r$, with the positive orientation.
:::

::: {.remark}
This is part 3 of question 1 of the Spring 2014 list in the source, whose opening instruction is to solve the problem without using Cauchy's theorem.
The source prints $dz$ twice in the integral.
:::
