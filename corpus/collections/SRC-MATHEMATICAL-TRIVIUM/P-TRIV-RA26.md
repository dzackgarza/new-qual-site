---
schema: qual/card@1
id: P-TRIV-RA26
kind: problem
title: $\int_0^1\frac{dx}{(ax+b(1-x))^2}=\frac1{ab}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned Real Analysis Problem 26 against page 10 of the source PDF and added an erratum remark for the missing hypothesis ab > 0.
---

::: {.problem}
Show that $\displaystyle\int_0^1 \frac{dx}{(ax + b(1-x))^2} = \frac{1}{ab}$, $a, b \in \mathbb{R}$.
:::

::: {.remark}
Erratum: as stated, with arbitrary $a, b \in \mathbb{R}$, the identity is false.
For $a = 1$, $b = -1$ the integrand is $\frac{1}{(2x-1)^2}$, which is not integrable near $x = \frac{1}{2}$, so the integral diverges, while $\frac{1}{ab} = -1$.
More generally, if $ab < 0$ then $ax + b(1-x)$ vanishes at $x = \frac{b}{b-a} \in (0,1)$ and the integral diverges, and if $ab = 0$ the right-hand side is undefined.
The identity holds under the corrected hypothesis $ab > 0$, that is, $a$ and $b$ nonzero of the same sign.
:::
