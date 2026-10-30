---
schema: qual/card@1
id: P-GRECH2-29
kind: problem
title: Area under $y=x\arctan x$ on $[0,1]$
classification:
  areas: [prelim]
  topics:
  - Integration by Parts
  - Area
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 29 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
What is the area of the region in the first quadrant bounded by the curve $y = x \arctan x$ and the line $x = 1$?

(A) $\frac{\pi-4}{4}$
(B) $\frac{\pi-2}{4}$
(C) $\frac{\pi}{4}$
(D) $\frac{\pi+2}{4}$
(E) $\frac{\pi+4}{4}$
:::

::: {.solution}

::: pf

::: pf-step

The required area is
$$
\int_0^1 x\arctan x\,dx.
$$


::: pf-proof

For $0\le x\le1$, both $x$ and $\arctan x$ are nonnegative, so the graph lies above the $x$-axis. It meets the axis at $x=0$, and the vertical boundary is $x=1$, hence the first-quadrant area is the displayed integral.

:::

:::

::: {.pf-step #s1-2}

An antiderivative of $x\arctan x$ is
$$
\frac12(x^2+1)\arctan x-\frac{x}{2}.
$$


::: pf-proof

Integrate by parts with
$$
u=\arctan x,
\qquad
dv=x\,dx.
$$
Then
$$
du=\frac{dx}{1+x^2},
\qquad
v=\frac{x^2}{2},
$$
so
$$
\begin{aligned}
\int x\arctan x\,dx
&=\frac{x^2}{2}\arctan x-\frac12\int\frac{x^2}{1+x^2}\,dx\\
&=\frac{x^2}{2}\arctan x-\frac12\int\left(1-\frac1{1+x^2}\right)dx\\
&=\frac12(x^2+1)\arctan x-\frac{x}{2}+C.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

The area is
$$
\boxed{\frac{\pi-2}{4}},
$$
so the answer is (B).


::: pf-proof

Using step [](#s1-2){.pf-ref},
$$
\begin{aligned}
\int_0^1 x\arctan x\,dx
&=\left[\frac12(x^2+1)\arctan x-\frac{x}{2}\right]_0^1\\
&=\frac\pi4-\frac12\\
&=\frac{\pi-2}{4}.
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested area and corresponding choice.

:::

:::

:::
