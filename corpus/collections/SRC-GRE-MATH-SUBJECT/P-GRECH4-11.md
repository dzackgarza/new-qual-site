---
schema: qual/card@1
id: P-GRECH4-11
kind: problem
title: Implicit curve from its slope
classification:
  areas:
  - real-analysis
  topics:
  - Separable Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 11 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
At every point $(x, y)$ on a curve in the $xy$-plane, the slope is equal to:

$$
\frac{1 - 2xy}{x^2 + 3y^2 + 1}
$$

What is the equation of this curve, given that it passes through the point $(1, 1)$?

(A) $\frac{1}{3}x^3 + 3xy^2 + x + y - xy^2 = \frac{13}{3}$
(B) $xy^2 + y^3 + x - y = 2$
(C) $\frac{1}{3}x^3 + 3xy^2 - x + y + xy^2 = \frac{13}{3}$
(D) $x^2y + y^3 - x + y = 2$
(E) $x^2y^2 + xy^3 + x - y = 1$
:::

::: {.solution}

::: pf

::: pf-step

The slope equation is equivalent to the exact differential equation
$$
(2xy-1)\,dx+(x^2+3y^2+1)\,dy=0.
$$


::: pf-proof

The given slope is
$$
\frac{dy}{dx}
=\frac{1-2xy}{x^2+3y^2+1}.
$$
Multiplying through by the denominator and moving all terms to the left gives the displayed differential form. Its coefficients
$$
M=2xy-1,
\qquad
N=x^2+3y^2+1
$$
satisfy
$$
M_y=2x=N_x,
$$
so the equation is exact.

:::

:::

::: {.pf-step #s1-2}

A potential for this differential form is
$$
F(x,y)=x^2y-x+y^3+y.
$$


::: pf-proof

Integrating $M=2xy-1$ with respect to $x$ gives
$$
F=x^2y-x+h(y).
$$
Then
$$
F_y=x^2+h'(y)
$$
must equal
$$
N=x^2+3y^2+1.
$$
Thus $h'(y)=3y^2+1$, so one may take $h(y)=y^3+y$.

:::

:::

::: {.pf-step #s1-3}

The curve through $(1,1)$ is
$$
\boxed{x^2y+y^3-x+y=2},
$$
so the answer is (D).


::: pf-proof

Integral curves of the exact equation satisfy $F(x,y)=C$. At $(1,1)$,
$$
C
=F(1,1)
=1-1+1+1
=2.
$$
Substituting this value into the potential from step [](#s1-2){.pf-ref} gives the displayed curve.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required curve and corresponding choice.

:::

:::

:::
