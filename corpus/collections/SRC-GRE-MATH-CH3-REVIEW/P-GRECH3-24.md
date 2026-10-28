---
schema: qual/card@1
id: P-GRECH3-24
kind: problem
title: Area of a vertical fence over a curve
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 24 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
A vertical fence is constructed whose base is the curve $y=x\sqrt{x}$, from $(0,0)$ to $(1,1)$, and whose height above each point $(x,y)$ along the curve is $x^3-y^2+27$. Find the area of this fence.

(A) $\frac{1}{9}(5\sqrt{5}-2)$
(B) $5\sqrt{13}-6$
(C) $9\sqrt{3}$
(D) $13\sqrt{13}-8$
(E) $27$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A parametrization of the base curve is
$$
x=t^2,\qquad y=t^3,\qquad 0\le t\le1,
$$
and along this curve the fence height is constantly $27$.


::: pf-proof

For $0\le t\le1$,
$$
y=t^3=(t^2)\sqrt{t^2}=x\sqrt{x},
$$
so the parametrization runs from $(0,0)$ to $(1,1)$ along the base curve. Along it,
$$
x^3-y^2+27
=(t^2)^3-(t^3)^2+27
=27.
$$

:::

:::

::: {.pf-step #s1-2}

The arc-length element of the base curve is
$$
ds=t\sqrt{4+9t^2}\,dt.
$$


::: pf-proof

From step [](#s1-1){.pf-ref},
$$
\frac{dx}{dt}=2t,\qquad
\frac{dy}{dt}=3t^2.
$$
Since $t\ge0$,
$$
ds
=\sqrt{\left(\frac{dx}{dt}\right)^2+
\left(\frac{dy}{dt}\right)^2}\,dt
=\sqrt{4t^2+9t^4}\,dt
=t\sqrt{4+9t^2}\,dt.
$$

:::

:::

::: {.pf-step #s1-3}

The fence area is
$$
\boxed{13\sqrt{13}-8},
$$
so the answer is (D).


::: pf-proof

The area of a vertical fence of height $H$ over a base curve $C$ is
$$
\int_C H\,ds.
$$
Using steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref},
$$
A
=27\int_0^1 t\sqrt{4+9t^2}\,dt.
$$
With $u=4+9t^2$, so $du=18t\,dt$,
$$
A
=\frac{27}{18}\int_4^{13}u^{1/2}\,du
=\frac32\cdot\frac23
\left[u^{3/2}\right]_4^{13}
=13^{3/2}-4^{3/2}
=13\sqrt{13}-8.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested area and corresponding choice.

:::

:::

:::
