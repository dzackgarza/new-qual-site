---
schema: qual/card@1
id: P-Y4TND
kind: problem
title: $\int_{-\infty}^{\infty}\frac{e^{ax}}{1+e^x}\,dx=\frac{\pi}{\sin\pi a}$ for $0<a<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
Show that for $0<a<1$,
\[
\int_{-\infty}^{\infty}{e^{ax}\over1+e^x}\,dx
={\pi\over\sin\pi a}.
\]
:::

::: {.solution}
With $t=e^x$,
\[
\int_{-\infty}^{\infty}{e^{ax}\over1+e^x}\,dx
=\int_0^\infty {t^{a-1}\over1+t}\,dt.
\]
For $0<a<1$, Euler's beta integral gives
\[
\int_0^\infty {t^{a-1}\over1+t}\,dt
=B(a,1-a)=\Gamma(a)\Gamma(1-a)
={\pi\over\sin\pi a},
\]
by Euler's reflection formula.
:::