---
schema: qual/card@1
id: P-S06EZ
kind: problem
title: Complex solutions of $e^z=2i$
classification:
  areas:
  - prelim
  topics:
  - Complex Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Find all complex numbers $z = x + iy$, $(x, y \in \mathbb{R})$, such that $e^z = 2i$.
:::


::: {.solution}
<1>1. Write $z=x+iy$ with $x,y\in\mathbb R$. Then
\[
e^z=e^x(\cos y+i\sin y).
\]
:::

<1>2. If $e^z=2i$, then $e^x=2$.
::: {.proof}
Taking absolute values gives
\[
e^x=|e^z|=|2i|=2.
\]
Hence $x=\ln2$.
:::

<1>3. The argument condition is
\[
y=\frac\pi2+2\pi k,
\qquad k\in\mathbb Z.
\]
::: {.proof}
After <1>2, the equation becomes
\[
\cos y+i\sin y=i.
\]
Thus $\cos y=0$ and $\sin y=1$, which occurs exactly when $y=\pi/2+2\pi k$.
:::

<1>4. Therefore all solutions are
\[
\boxed{z=\ln2+i\left(\frac\pi2+2\pi k\right),\qquad k\in\mathbb Z.}
\]
::: {.proof}
Every such $z$ satisfies
\[
e^z=2e^{i(\pi/2+2\pi k)}=2i,
\]
and <1>2--<1>3 show that no other solutions are possible.
:::
