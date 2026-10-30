---
schema: qual/card@1
id: P-GRECH1-09
kind: problem
title: Area after scaling an ellipse
classification:
  areas:
  - algebra
  topics:
  - Conic Sections
  - Area
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Re-transcribed from Chapter 1 review Question 9 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), replacing the earlier chapter-1.pdf transcription.
---

::: {.problem}
Let $C$ be the curve in the $xy$-plane described by the equation $x^2 + 4y^2 = 16$. If every point $(x, y)$ on $C$ is replaced by the point $(\frac{1}{2}x, y)$, what is the area enclosed by the resulting curve?

(A) $8$
(B) $4\pi$
(C) $16$
(D) $8\pi$
(E) $16\pi$
:::

::: {.solution}

Let $(x',y')=(x/2,y)$ denote the image of a point $(x,y)$ on $C$.

::: pf

::: {.pf-step #s1-1}

The resulting curve has equation
$$
(x')^2+(y')^2=4.
$$


::: pf-proof

Since $x=2x'$ and $y=y'$, substituting into $x^2+4y^2=16$ gives
$$
4(x')^2+4(y')^2=16,
$$
which is equivalent to the displayed equation.

:::

:::

::: {.pf-step #s1-2}

The enclosed area is
$$
\boxed{4\pi},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref}, the image curve is the circle of radius $2$ centered at the origin. Its enclosed area is therefore
$$
\pi(2)^2=4\pi.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested area and corresponding choice.

:::

:::

:::
