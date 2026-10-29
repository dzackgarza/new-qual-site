---
schema: qual/card@1
id: P-GREPT-09
kind: problem
title: "Value of $\\cos(x^2)\\sin(x^2)$ at its first positive critical point"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 9 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $a$ be the smallest positive value of $x$ at which the function $f(x) = (\cos x^2)(\sin x^2)$ has a critical point. What is the value of $f(a)$?

(A) $\frac{\sqrt{2}}{4}$
(B) $\frac{1}{2}$
(C) $\frac{\sqrt{2}}{2}$
(D) $1$
(E) $\sqrt{2}$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The function can be written as
$$
f(x)=\frac12\sin(2x^2),
$$
and therefore
$$
f'(x)=2x\cos(2x^2).
$$


::: pf-proof

The identity $2\sin\theta\cos\theta=\sin(2\theta)$ with
$\theta=x^2$ gives the first formula. Differentiating by the chain rule gives
$$
f'(x)=\frac12\cos(2x^2)\cdot4x=2x\cos(2x^2).
$$

:::

:::

::: {.pf-step #s1-2}

The smallest positive critical point satisfies
$$
a^2=\frac\pi4.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, a positive critical point must satisfy
$\cos(2x^2)=0$. Thus
$$
2x^2=\frac\pi2+k\pi
$$
for an integer $k$ for which the right-hand side is positive. The smallest
positive value occurs for $k=0$, giving $2a^2=\pi/2$ and hence
$a^2=\pi/4$.

:::

:::

::: {.pf-step #s1-3}

At this point,
$$
f(a)=\boxed{\frac12},
$$
so the answer is (B).


::: pf-proof

Using step [](#s1-1){.pf-ref} and $2a^2=\pi/2$ from step [](#s1-2){.pf-ref},
$$
f(a)=\frac12\sin(2a^2)
=\frac12\sin\frac\pi2
=\frac12.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the requested value.

:::

:::

:::
