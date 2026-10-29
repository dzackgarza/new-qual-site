---
schema: qual/card@1
id: P-CALCPT3-08
kind: problem
title: "Possible domain of the continuous function $\\sqrt{\\tan^2x-1}$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 8 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
Suppose that the function $f$ is defined on an interval by the formula $f(x)=\sqrt{\tan^2x-1}$.
If $f$ is continuous, which of the following intervals could be its domain?

(A) $\left(\frac{3\pi}{4},\pi\right)$
(B) $\left(\frac{\pi}{4},\frac{\pi}{2}\right)$
(C) $\left(\frac{\pi}{4},\frac{3\pi}{4}\right)$
(D) $\left(-\frac{\pi}{4},0\right)$
(E) $\left(-\frac{3\pi}{4},-\frac{\pi}{4}\right)$
:::

::: {.solution}
The formula defines a real number at $x$ exactly when $\tan x$ is defined and $\tan^2x\ge 1$, that is, when $\cos x\ne 0$ and $\abs{\tan x}\ge 1$.
An interval can be the domain only if every point of it satisfies both conditions.

::: pf

::: {.pf-step #reject-poles}
Choices (C) and (E) are impossible.

::: pf-proof
The interval $\left(\frac{\pi}{4},\frac{3\pi}{4}\right)$ contains $\frac{\pi}{2}$ and the interval $\left(-\frac{3\pi}{4},-\frac{\pi}{4}\right)$ contains $-\frac{\pi}{2}$.
At both points $\cos x=0$, so $\tan x$ and hence $f(x)$ is undefined.
:::

:::

::: {.pf-step #reject-small}
Choices (A) and (D) are impossible.

::: pf-proof
On $\left(\frac{3\pi}{4},\pi\right)$ the tangent increases from $-1$ to $0$, and on $\left(-\frac{\pi}{4},0\right)$ it increases from $-1$ to $0$.
On both intervals $0\le\tan^2x<1$ at every point, so $\tan^2x-1<0$ and the square root is not real.
:::

:::

::: pf-step
The domain could be $\boxed{\left(\frac{\pi}{4},\frac{\pi}{2}\right)}$, choice (B).

::: pf-proof
On $\left(\frac{\pi}{4},\frac{\pi}{2}\right)$ the cosine does not vanish and $\tan x>1$, so $\tan^2x-1>0$.
There $f$ is the composition of the continuous functions $\tan$, $t\mapsto t^2-1$ and $\sqrt{\cdot}$ on $[0,\infty)$, hence continuous.
Steps [](#reject-poles){.pf-ref} and [](#reject-small){.pf-ref} exclude every other choice.
:::

:::

:::

:::
