---
schema: qual/card@1
id: P-GREPT-23
kind: problem
title: "Slope of $y=x^\\pi-\\pi^x$ at $(\\pi,0)$"
classification:
  areas: [prelim]
  topics:
  - Differentiation
  - Tangent Lines
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 23 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The extraction prints the second term as pi^s; the book's Chapter 10 solution differentiates pi^x."
---

::: {.problem}
Determine the slope of the curve $y = x^{\pi} - \pi^{x}$ at the point $(\pi, 0)$.

(A) $\pi^{\pi}(1 - \log \pi)$
(B) $\pi^{\pi}(1 + \log \pi)$
(C) $\pi^{\pi}$
(D) $1$
(E) $0$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The derivative of the curve is
$$
y'=\pi x^{\pi-1}-\pi^x\log\pi.
$$


::: pf-proof

Since $\pi$ is constant,
$$
\frac{d}{dx}x^\pi=\pi x^{\pi-1}.
$$
Also $\pi^x=e^{x\log\pi}$, so
$$
\frac{d}{dx}\pi^x=\pi^x\log\pi.
$$
Subtracting gives the displayed derivative.

:::

:::

::: {.pf-step #s1-2}

At $x=\pi$, the slope is
$$
y'(\pi)=\pi^\pi(1-\log\pi).
$$


::: pf-proof

Substituting $x=\pi$ into step [](#s1-1){.pf-ref} gives
$$
y'(\pi)
=\pi\pi^{\pi-1}-\pi^\pi\log\pi
=\pi^\pi-\pi^\pi\log\pi
=\pi^\pi(1-\log\pi).
$$

:::

:::

::: {.pf-step #s1-3}

Therefore the requested slope is
$$
\boxed{\pi^\pi(1-\log\pi)},
$$
so the answer is (A).


::: pf-proof

Step [](#s1-2){.pf-ref} evaluates the derivative at the specified point.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the required slope.

:::

:::

:::
