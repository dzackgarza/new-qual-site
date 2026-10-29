---
schema: qual/card@1
id: P-CALCPT3-18
kind: problem
title: "Derivative of $\\sum_{n\\ge0}(-1)^nx^{2n}$ on $(0,1)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 18 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree. Choice (E) reads (1-2x)^2 in the denominator in both the extraction and the page render."
---

::: {.problem}
If $f(x)=\sum_{n=0}^{\infty}(-1)^nx^{2n}$ for all $x\in(0,1)$, then $f'(x)=$

(A) $\sin x$
(B) $\cos x$
(C) $\frac{1}{1+x^2}$
(D) $\frac{-2x}{(1+x^2)^2}$
(E) $\frac{2x}{(1-2x)^2}$
:::

::: {.solution}

::: pf

::: {.pf-step #closed-form}
$f(x)=\frac{1}{1+x^2}$ for $x\in(0,1)$.

::: pf-proof
The series is geometric with ratio $-x^2$, and $\abs{-x^2}<1$ for $x\in(0,1)$, so it converges to $\frac{1}{1-(-x^2)}=\frac{1}{1+x^2}$.
:::

:::

::: pf-step
$f'(x)=\boxed{\frac{-2x}{(1+x^2)^2}}$, choice (D).

::: pf-proof
Differentiate the closed form of step [](#closed-form){.pf-ref} with the chain rule: $\frac{d}{dx}(1+x^2)^{-1}=-(1+x^2)^{-2}\cdot 2x$.
:::

:::

:::

:::
