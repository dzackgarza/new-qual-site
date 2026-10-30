---
schema: qual/card@1
id: P-GRECH2-12
kind: problem
title: Tangent line at the inflection point of $y=x^3-3x^2+4x$
classification:
  areas: [prelim]
  topics:
  - Inflection Points
  - Tangent Lines
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 12 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the equation of the tangent line to the curve $y = x^3 - 3x^2 + 4x$ at the curve's inflection point?

(A) $y = 2x - 3$
(B) $y = x - 1$
(C) $y = x + 1$
(D) $y = 3x - 2$
(E) $x + y = 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The curve has its inflection point at $x=1$.


::: pf-proof

For
$$
y=x^3-3x^2+4x,
$$
the first two derivatives are
$$
y'=3x^2-6x+4,
\qquad
y''=6x-6.
$$
Thus $y''<0$ for $x<1$ and $y''>0$ for $x>1$. The concavity changes at $x=1$, so this is an inflection point.

:::

:::

::: {.pf-step #s1-2}

The inflection point is $(1,2)$ and the tangent slope there is $1$.


::: pf-proof

Evaluating the function and its first derivative at $1$ gives
$$
y(1)=1-3+4=2
$$
and
$$
y'(1)=3-6+4=1.
$$

:::

:::

::: {.pf-step #s1-3}

The tangent line is
$$
\boxed{y=x+1},
$$
so the answer is (C).


::: pf-proof

Using the point and slope from step [](#s1-2){.pf-ref}, the point-slope equation is
$$
y-2=1(x-1),
$$
which simplifies to $y=x+1$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested tangent line and corresponding choice.

:::

:::

:::
