---
schema: qual/card@1
id: P-GRECH2-13
kind: problem
title: Slope of $xy(x+y)=x+y^4$ at $(1,1)$
classification:
  areas: [prelim]
  topics:
  - Implicit Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 13 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the slope of the tangent line to the curve $xy(x + y) = x + y^4$ at the point $(1, 1)$?

(A) $2$
(B) $1$
(C) $0$
(D) $-1$
(E) $-2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Along the curve, the derivative satisfies
$$
\frac{dy}{dx}
=\frac{1-2xy-y^2}{x^2+2xy-4y^3}.
$$


::: pf-proof

Expand the equation as
$$
x^2y+xy^2=x+y^4.
$$
Implicit differentiation gives
$$
2xy+x^2y'+y^2+2xyy'=1+4y^3y'.
$$
Collecting the $y'$ terms yields
$$
y'(x^2+2xy-4y^3)=1-2xy-y^2,
$$
which gives the displayed formula whenever the denominator is nonzero.

:::

:::

::: {.pf-step #s1-2}

At $(1,1)$, the slope is
$$
\boxed{2},
$$
so the answer is (A).


::: pf-proof

At $(1,1)$, the denominator in step [](#s1-1){.pf-ref} equals
$$
1+2-4=-1\ne0,
$$
and the numerator equals
$$
1-2-1=-2.
$$
Therefore
$$
y'(1)=\frac{-2}{-1}=2.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the tangent slope at the specified point and the corresponding choice.

:::

:::

:::
