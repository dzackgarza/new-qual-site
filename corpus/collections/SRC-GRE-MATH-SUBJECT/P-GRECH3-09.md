---
schema: qual/card@1
id: P-GRECH3-09
kind: problem
title: Surface of revolution about the $x$-axis
classification:
  areas:
  - real-analysis
  topics:
  - Surfaces of Revolution
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 9 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
If the curve $z=f(x)$ in the $xz$-plane is revolved around the $x$-axis, which of the following is an equation that describes the resulting surface?

(A) $y^2+z^2=\abs{f(x)}$
(B) $z^2=f(x^2+y^2)$
(C) $y^2=f(x^2+z^2)$
(D) $x^2+z^2=[f(x)]^2$
(E) $y^2+z^2=[f(x)]^2$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For each fixed $x$, revolving the point $(x,0,f(x))$ about the $x$-axis produces the circle
$$
y^2+z^2=[f(x)]^2.
$$


::: pf-proof

Rotation about the $x$-axis leaves the $x$-coordinate fixed and preserves the distance to the $x$-axis. The point $(x,0,f(x))$ has distance
$$
\sqrt{0^2+[f(x)]^2}=\abs{f(x)}
$$
from the $x$-axis. Hence its orbit under rotation is exactly the circle in the plane with that fixed $x$-coordinate and radius $\abs{f(x)}$, whose equation is
$$
y^2+z^2=\abs{f(x)}^2=[f(x)]^2.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore the surface of revolution is described by
$$
\boxed{y^2+z^2=[f(x)]^2},
$$
so the answer is (E).


::: pf-proof

The original curve consists of the points $(x,0,f(x))$ as $x$ varies. By step [](#s1-1){.pf-ref}, the rotation orbit of each such point is exactly the circle cut out by the displayed equation at that value of $x$. Taking these circles over all $x$ on the curve gives precisely the stated surface.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested equation and corresponding choice.

:::

:::

:::
