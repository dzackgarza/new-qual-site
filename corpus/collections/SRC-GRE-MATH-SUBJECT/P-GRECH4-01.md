---
schema: qual/card@1
id: P-GRECH4-01
kind: problem
title: Initial-value problem for $dy/dx=x^2/(x^2+1)$
classification:
  areas:
  - real-analysis
  topics:
  - Initial Value Problems
  - Separable Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 4 review Question 1 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Let $y = f(x)$ be the solution of the equation

$$
\frac{dy}{dx} = \frac{x^2}{x^2 + 1}
$$

such that $y = 0$ when $x = 0$. What is the value of $f(1)$?

(A) $1 - \log 2$
(B) $1 + \log 2$
(C) $1$
(D) $\log 2$
(E) $\frac{1}{4}(4 - \pi)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every solution of the differential equation has the form
$$
y=x-\arctan x+C.
$$


::: pf-proof

Rewrite the right-hand side as
$$
\frac{x^2}{x^2+1}
=1-\frac1{x^2+1}.
$$
Integrating gives
$$
y
=\int\left(1-\frac1{x^2+1}\right)\,dx
=x-\arctan x+C.
$$

:::

:::

::: {.pf-step #s1-2}

The initial condition forces $C=0$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
0=f(0)=0-\arctan0+C=C.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{f(1)=\frac14(4-\pi)},
$$
so the answer is (E).


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
f(1)
=1-\arctan1
=1-\frac{\pi}{4}
=\frac14(4-\pi).
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
