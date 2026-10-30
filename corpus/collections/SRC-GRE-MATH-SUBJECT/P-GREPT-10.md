---
schema: qual/card@1
id: P-GREPT-10
kind: problem
title: "Integral curve of $y'=2x/(y^2-1)$ through $(2,3)$"
classification:
  areas: [prelim]
  topics:
  - Separable Equations
  - Initial Value Problems
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

::: pf

::: {.pf-step #s1-1}

Every integral curve satisfies
$$
\frac13y^3-y=x^2+C
$$
for some constant $C$.


::: pf-proof

Rearranging the differential equation gives
$$
(y^2-1)\,dy=2x\,dx.
$$
Integrating both sides yields
$$
\frac13y^3-y=x^2+C.
$$

:::

:::

::: {.pf-step #s1-2}

The curve through $(2,3)$ has $C=2$.


::: pf-proof

Substituting $(x,y)=(2,3)$ into step [](#s1-1){.pf-ref} gives
$$
\frac13(27)-3=4+C,
$$
so $6=4+C$ and hence $C=2$.

:::

:::

::: {.pf-step #s1-3}

Therefore the required integral curve is
$$
\boxed{x^2+2=\frac13y^3-y},
$$
so the answer is (D).


::: pf-proof

Substituting the value of $C$ from step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref} and rearranging
gives the displayed equation.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the integral curve passing through the prescribed point.

:::

:::

:::
