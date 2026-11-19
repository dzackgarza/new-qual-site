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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained book `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf`: the statement is question 1 of the Chapter 4
    Review Questions, printed on PDF p. 188, and its printed words are the card's. The chapter,
    the question number and the page are now named in the solution's opening sentence. Not checked
    in this pass: the argument, which the edit does not touch.
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
This is question 1 of the Chapter 4 Review Questions of *Cracking the GRE Mathematics Subject Test*, retained in this repository as `assets/attachments/Cracking_the_GRE_Mathematics_Subject.pdf`, on PDF p. 188; the statement below is its wording.

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
