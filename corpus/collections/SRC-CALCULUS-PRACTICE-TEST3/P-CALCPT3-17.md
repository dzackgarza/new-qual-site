---
schema: qual/card@1
id: P-CALCPT3-17
kind: problem
title: "Evaluate $1-\\sin^2(\\arccos(\\pi/12))$"
classification:
  areas: [prelim]
  topics: [Trigonometry]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 17 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree. The source writes Arccos for the principal inverse cosine."
---

::: {.problem}
$$1-\sin^2\left(\arccos\frac{\pi}{12}\right)=$$

(A) $\sqrt{\dfrac{1-\cos\frac{\pi}{24}}{2}}$
(B) $\sqrt{\dfrac{1-\cos\frac{\pi}{6}}{2}}$
(C) $\sqrt{\dfrac{1+\cos\frac{\pi}{24}}{2}}$
(D) $\frac{\pi}{6}$
(E) $\frac{\pi^2}{144}$
:::

::: {.solution}
Write $\theta=\arccos\frac{\pi}{12}$.

::: pf

::: {.pf-step #defined}
$\theta$ is defined and $\cos\theta=\frac{\pi}{12}$.

::: pf-proof
Since $0<\pi<12$, the number $\frac{\pi}{12}$ lies in $[-1,1]$, the domain of $\arccos$, and $\cos(\arccos t)=t$ for every $t\in[-1,1]$.
:::

:::

::: pf-step
The expression equals $\boxed{\frac{\pi^2}{144}}$, choice (E).

::: pf-proof
By the identity $\sin^2\theta+\cos^2\theta=1$ and step [](#defined){.pf-ref}, $1-\sin^2\theta=\cos^2\theta=\left(\frac{\pi}{12}\right)^2=\frac{\pi^2}{144}$.
:::

:::

:::

:::
