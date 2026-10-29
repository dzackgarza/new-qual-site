---
schema: qual/card@1
id: P-CALCPT3-25
kind: problem
title: "Regularity of a function with $f(x)-f(y)\\le K|x-y|$ on $[0,1]$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 25 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree where the extraction is legible."
---

::: {.problem}
Let $f$ be a real-valued function with domain $[0,1]$.
If there is some $K>0$ such that $f(x)-f(y)\le K|x-y|$ for all $x$ and $y$ in $[0,1]$, which of the following must be true?

(A) $f$ is discontinuous at each point of $(0,1)$.
(B) $f$ is not continuous on $(0,1)$, but is discontinuous at only countably many points of $(0,1)$.
(C) $f$ is continuous on $(0,1)$, but is differentiable at only countably many points of $(0,1)$.
(D) $f$ is continuous on $(0,1)$, but may not be differentiable on $(0,1)$.
(E) $f$ is differentiable on $(0,1)$.
:::

::: {.solution}

::: pf

::: {.pf-step #lipschitz}
$\abs{f(x)-f(y)}\le K\abs{x-y}$ for all $x,y\in[0,1]$.

::: pf-proof
The hypothesis with $x$ and $y$ exchanged gives $f(y)-f(x)\le K\abs{y-x}=K\abs{x-y}$.
Together with $f(x)-f(y)\le K\abs{x-y}$ this bounds $\abs{f(x)-f(y)}$.
:::

:::

::: {.pf-step #continuous}
$f$ is continuous on $[0,1]$, and in particular on $(0,1)$; so (A) and (B) are false.

::: pf-proof
Given $\varepsilon>0$, take $\delta=\varepsilon/K$.
By step [](#lipschitz){.pf-ref}, $\abs{x-y}<\delta$ implies $\abs{f(x)-f(y)}<\varepsilon$.
:::

:::

::: {.pf-step #examples}
(C) and (E) need not hold.

::: pf-proof
The function $f(x)=x$ satisfies the hypothesis with $K=1$ and is differentiable at every point of $(0,1)$, which is uncountably many points, so (C) fails for it.
The function $f(x)=\abs{x-\frac12}$ satisfies the hypothesis with $K=1$, by the reverse triangle inequality, and is not differentiable at $\frac12$, since its one-sided derivatives there are $-1$ and $1$; so (E) fails for it.
:::

:::

::: pf-step
The statement that must be true is $\boxed{\text{(D)}}$.

::: pf-proof
Step [](#continuous){.pf-ref} gives continuity on $(0,1)$, and the second example of step [](#examples){.pf-ref} shows that differentiability on $(0,1)$ may fail.
The same two steps rule out (A), (B), (C), and (E).
:::

:::

:::

:::
