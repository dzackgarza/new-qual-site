---
schema: qual/card@1
id: P-GREPT-10
kind: problem
title: "Integral curve of $y'=2x/(y^2-1)$ through $(2,3)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 10 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Find the equation of the integral curve that passes through the point $(2, 3)$ of the differential equation

$$y' = \frac{2x}{y^2 - 1}$$

(A) $x^2 - 2 = \frac{1}{3}y^3 + y$
(B) $x^2 - 1 = \frac{1}{3}y^3 - 2y$
(C) $x^2 + 1 = \frac{1}{3}y^3 + y$
(D) $x^2 + 2 = \frac{1}{3}y^3 - y$
(E) $2(x^2 - 1) = \frac{1}{3}y^3 - y$
:::

::: {.solution}
<1>1. Every integral curve satisfies
$$
\frac13y^3-y=x^2+C
$$
for some constant $C$.

::: {.proof}
Rearranging the differential equation gives
$$
(y^2-1)\,dy=2x\,dx.
$$
Integrating both sides yields
$$
\frac13y^3-y=x^2+C.
$$
:::

<1>2. The curve through $(2,3)$ has $C=2$.

::: {.proof}
Substituting $(x,y)=(2,3)$ into step <1>1 gives
$$
\frac13(27)-3=4+C,
$$
so $6=4+C$ and hence $C=2$.
:::

<1>3. Therefore the required integral curve is
$$
\boxed{x^2+2=\frac13y^3-y},
$$
so the answer is (D).

::: {.proof}
Substituting the value of $C$ from step <1>2 into step <1>1 and rearranging
gives the displayed equation.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the integral curve passing through the prescribed point.
:::
:::
