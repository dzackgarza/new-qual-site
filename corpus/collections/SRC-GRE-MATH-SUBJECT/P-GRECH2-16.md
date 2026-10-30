---
schema: qual/card@1
id: P-GRECH2-16
kind: problem
title: Linear approximation of the change in $1/\sqrt{x^3+1}$
classification:
  areas: [prelim]
  topics:
  - Linear Approximation
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 16 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
Let $y = \frac{1}{\sqrt{x^3 + 1}}$. If $x$ increases from 2 to 2.09, which of the following most closely approximates the change in $y$?

(A) $0.08$
(B) $0.04$
(C) $-0.02$
(D) $-0.06$
(E) $-0.09$
:::

::: {.solution}

Let
$$
f(x)=(x^3+1)^{-1/2}.
$$

::: pf

::: {.pf-step #s1-1}

The derivative at $x=2$ is
$$
f'(2)=-\frac29.
$$


::: pf-proof

The chain rule gives
$$
f'(x)
=-\frac12(x^3+1)^{-3/2}(3x^2)
=-\frac32x^2(x^3+1)^{-3/2}.
$$
Hence
$$
f'(2)
=-6\cdot9^{-3/2}
=-6\cdot\frac1{27}
=-\frac29.
$$

:::

:::

::: {.pf-step #s1-2}

The linear approximation to the change in $y$ is
$$
\boxed{-0.02},
$$
so the answer is (C).


::: pf-proof

Here
$$
\Delta x=2.09-2=0.09=\frac9{100}.
$$
The differential approximation gives
$$
\Delta y\approx f'(2)\Delta x
=-\frac29\cdot\frac9{100}
=-\frac1{50}
=-0.02.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the requested approximation and corresponding choice.

:::

:::

:::
