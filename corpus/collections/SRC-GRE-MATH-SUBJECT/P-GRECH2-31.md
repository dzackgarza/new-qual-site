---
schema: qual/card@1
id: P-GRECH2-31
kind: problem
title: Area bounded by $y=8x$, $y=x^3$ and $y=8$
classification:
  areas: [prelim]
  topics:
  - Area
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 31 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Calculate the area of the region in the first quadrant bounded by the graphs of $y = 8x$, $y = x^3$, and $y = 8$.

(A) $12$
(B) $8$
(C) $6$
(D) $\frac{16}{3}$
(E) $4$
:::

::: {.solution}

::: pf

::: pf-step

The relevant intersection points occur at $x=1$ and $x=2$.


::: pf-proof

The line $y=8x$ meets $y=8$ when $8x=8$, hence at $x=1$. The curve $y=x^3$ meets $y=8$ when $x^3=8$, hence at $x=2$. The graphs $y=8x$ and $y=x^3$ meet at $x=0$ and at $x=\sqrt8>2$, so the first-quadrant bounded region begins at the origin and uses the horizontal line as its upper boundary after $x=1$.

:::

:::

::: {.pf-step #s1-2}

The area is
$$
\int_0^1(8x-x^3)\,dx+\int_1^2(8-x^3)\,dx.
$$


::: pf-proof

For $0\le x\le1$, the upper boundary is $y=8x$ and the lower boundary is $y=x^3$. For $1\le x\le2$, the upper boundary is $y=8$ and the lower boundary remains $y=x^3$. Thus vertical slices give the displayed sum.

:::

:::

::: {.pf-step #s1-3}

The area equals
$$
\boxed{8},
$$
so the answer is (B).


::: pf-proof

Compute the two integrals from step [](#s1-2){.pf-ref}:
$$
\begin{aligned}
\int_0^1(8x-x^3)\,dx
&=\left[4x^2-\frac{x^4}{4}\right]_0^1
=\frac{15}{4},\\
\int_1^2(8-x^3)\,dx
&=\left[8x-\frac{x^4}{4}\right]_1^2
=\frac{17}{4}.
\end{aligned}
$$
Their sum is $32/4=8$.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested area and corresponding choice.

:::

:::

:::
