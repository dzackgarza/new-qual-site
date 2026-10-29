---
schema: qual/card@1
id: P-GRECH4-07
kind: problem
title: Value of a first-order linear ODE solution
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
  note: Re-transcribed from Chapter 4 review Question 7 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR) and checked against the source scans in assets/attachments/gre-math-ch4-review/, replacing the earlier chapter-4.pdf transcription.
---

::: {.problem}
Let $y = f(x)$ be the solution of the equation

$$
\frac{dy}{dx} + \frac{y}{x} = \sin x
$$

such that $f(\pi) = 1$. What is the value of $f(\frac{1}{2}\pi)$?

(A) $\frac{2}{\pi} - 1$
(B) $\frac{2}{\pi}$
(C) $\frac{2}{\pi} + 1$
(D) $\frac{\pi}{2}$
(E) $\frac{\pi}{2} + 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

On the positive $x$-axis, multiplication by the integrating factor $x$ gives
$$
(xy)'=x\sin x.
$$


::: pf-proof

The differential equation is
$$
y'+\frac1x y=\sin x.
$$
Multiplying by $x$ gives
$$
xy'+y=x\sin x.
$$
The left-hand side is $(xy)'$ by the product rule.

:::

:::

::: {.pf-step #s1-2}

The general solution on this interval is
$$
y=-\cos x+\frac{\sin x+C}{x}.
$$


::: pf-proof

Integrating step [](#s1-1){.pf-ref} gives
$$
xy=\int x\sin x\,dx
=-x\cos x+\sin x+C,
$$
where integration by parts was used. Division by $x>0$ gives the displayed formula.

:::

:::

::: {.pf-step #s1-3}

The condition $f(\pi)=1$ forces $C=0$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
1=f(\pi)
=-\cos\pi+\frac{\sin\pi+C}{\pi}
=1+\frac{C}{\pi}.
$$
Hence $C=0$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{f\left(\frac{\pi}{2}\right)=\frac{2}{\pi}},
$$
so the answer is (B).


::: pf-proof

Using step [](#s1-3){.pf-ref} in step [](#s1-2){.pf-ref},
$$
f\left(\frac{\pi}{2}\right)
=-\cos\frac{\pi}{2}
+\frac{\sin(\pi/2)}{\pi/2}
=\frac{2}{\pi}.
$$

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested value and corresponding choice.

:::

:::

:::
