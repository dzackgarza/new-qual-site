---
schema: qual/card@1
id: P-GRECH3-15
kind: problem
title: Approximate change in cylinder volume
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
  note: "Checked against Chapter 3 review Question 15 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree. The chapter-3.pdf extraction dropped the square in choice (E); the book extraction has it."
---

::: {.problem}
A right circular cylinder has base radius $r=100$ cm and height $h=100$ cm. Which of the following best describes how the volume of the cylinder will change if $r$ increases to $101$ cm and $h$ decreases to $99$ cm?

(A) Volume will decrease by approximately $3\pi(100)^2$ cubic cm
(B) Volume will decrease by approximately $\pi(100)^2$ cubic cm
(C) Volume will increase by approximately $\pi(100)^2$ cubic cm
(D) Volume will increase by approximately $2\pi(100)^2$ cubic cm
(E) Volume will increase by approximately $3\pi(100)^2$ cubic cm
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For a cylinder with volume $V(r,h)=\pi r^2h$, the first-order change is
$$
\Delta V\approx 2\pi rh\,\Delta r+\pi r^2\,\Delta h.
$$


::: pf-proof

The partial derivatives are
$$
\frac{\partial V}{\partial r}=2\pi rh,
\qquad
\frac{\partial V}{\partial h}=\pi r^2.
$$
Therefore the linear approximation at $(r,h)$ gives
$$
\Delta V
\approx
\frac{\partial V}{\partial r}\Delta r
+\frac{\partial V}{\partial h}\Delta h,
$$
which is the displayed formula.

:::

:::

::: {.pf-step #s1-2}

At $(r,h)=(100,100)$ with $\Delta r=1$ and $\Delta h=-1$,
$$
\Delta V\approx \pi(100)^2.
$$


::: pf-proof

Substituting the stated changes into step [](#s1-1){.pf-ref} gives
$$
\Delta V
\approx
2\pi(100)(100)(1)
+\pi(100)^2(-1)
=\pi(100)^2.
$$

:::

:::

::: {.pf-step #s1-3}

The volume therefore increases by approximately
$$
\boxed{\pi(100)^2\text{ cubic cm}},
$$
so the answer is (C).


::: pf-proof

The approximation in step [](#s1-2){.pf-ref} is positive, so it represents an increase, with magnitude $\pi(100)^2$ cubic cm.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested approximate change and corresponding choice.

:::

:::

:::
