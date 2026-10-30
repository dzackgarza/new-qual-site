---
schema: qual/card@1
id: P-GRECH2-20
kind: problem
title: Largest rectangle inscribed in a semicircle
classification:
  areas: [prelim]
  topics:
  - Optimization
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 20 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the maximum area of a rectangle inscribed in a semicircle of radius $a$?

(A) $\frac{\sqrt{2}}{2}a^2$
(B) $\frac{\sqrt{3}}{2}a^2$
(C) $a^2$
(D) $\frac{\pi}{2\sqrt{2}}a^2$
(E) $a^2\sqrt{2}$
:::

::: {.solution}

Let $x$ be the half-width and $y$ the height of an inscribed rectangle. Then the upper-right vertex $(x,y)$ lies on the semicircle, so
$$
x^2+y^2=a^2,
$$
and the rectangle has area $A=2xy$.

::: pf

::: {.pf-step #s1-1}

Every such rectangle satisfies $A\le a^2$.


::: pf-proof

Since
$$
(x-y)^2\ge0,
$$
one has
$$
2xy\le x^2+y^2.
$$
Using $x^2+y^2=a^2$ gives
$$
A=2xy\le a^2.
$$

:::

:::

::: {.pf-step #s1-2}

The upper bound in step [](#s1-1){.pf-ref} is attained.


::: pf-proof

Take
$$
x=y=\frac{a}{\sqrt2}.
$$
Then
$$
x^2+y^2=\frac{a^2}{2}+\frac{a^2}{2}=a^2,
$$
so this rectangle is inscribed in the semicircle, and its area is
$$
2xy=2\left(\frac{a}{\sqrt2}\right)^2=a^2.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the maximum area is
$$
\boxed{a^2},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-1){.pf-ref} gives $a^2$ as an upper bound, and step [](#s1-2){.pf-ref} exhibits an inscribed rectangle attaining it.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested maximum and corresponding choice.

:::

:::

:::
