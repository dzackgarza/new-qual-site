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

\[
\frac{dy}{dx} + \frac{y}{x} = \sin x
\]

such that $f(\pi) = 1$. What is the value of $f(\frac{1}{2}\pi)$?

(A) $\frac{2}{\pi} - 1$
(B) $\frac{2}{\pi}$
(C) $\frac{2}{\pi} + 1$
(D) $\frac{\pi}{2}$
(E) $\frac{\pi}{2} + 1$
:::

::: {.solution}
<1>1. On the positive $x$-axis, multiplication by the integrating factor $x$ gives
$$
(xy)'=x\sin x.
$$

::: {.proof}
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

<1>2. The general solution on this interval is
$$
y=-\cos x+\frac{\sin x+C}{x}.
$$

::: {.proof}
Integrating step <1>1 gives
$$
xy=\int x\sin x\,dx
=-x\cos x+\sin x+C,
$$
where integration by parts was used. Division by $x>0$ gives the displayed formula.
:::

<1>3. The condition $f(\pi)=1$ forces $C=0$.

::: {.proof}
By step <1>2,
$$
1=f(\pi)
=-\cos\pi+\frac{\sin\pi+C}{\pi}
=1+\frac{C}{\pi}.
$$
Hence $C=0$.
:::

<1>4. Therefore
$$
\boxed{f\left(\frac{\pi}{2}\right)=\frac{2}{\pi}},
$$
so the answer is (B).

::: {.proof}
Using step <1>3 in step <1>2,
$$
f\left(\frac{\pi}{2}\right)
=-\cos\frac{\pi}{2}
+\frac{\sin(\pi/2)}{\pi/2}
=\frac{2}{\pi}.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested value and corresponding choice.
:::
:::
