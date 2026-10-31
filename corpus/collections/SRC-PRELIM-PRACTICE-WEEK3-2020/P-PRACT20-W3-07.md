---
schema: qual/card@1
id: P-PRACT20-W3-07
kind: problem
title: Taylor series of the sine integral $\int_0^x\frac{\sin t}{t}\,dt$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
  - Integrals
relations: []
review: draft
---

::: {.problem}
Find the Taylor Series for $\displaystyle f(x) = \int_{0}^{x} \frac{\sin(t)}{t}\, dt$ about $x = 0$.
:::

::: {.solution}
Start with the Taylor series for $\sin t$, divide by $t$, and integrate term by term, which is valid because the series converges on all of $\RR$:

$$
\sin t=\sum_{n=0}^{\infty}\frac{(-1)^nt^{2n+1}}{(2n+1)!}\quad\Longrightarrow\quad\frac{\sin t}{t}=\sum_{n=0}^{\infty}\frac{(-1)^nt^{2n}}{(2n+1)!}\quad\Longrightarrow\quad f(x)=\sum_{n=0}^{\infty}\frac{(-1)^nx^{2n+1}}{(2n+1)!\,(2n+1)}.
$$
:::
