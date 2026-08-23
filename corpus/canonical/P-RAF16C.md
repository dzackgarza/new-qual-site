---
schema: qual/card@1
id: P-RAF16C
kind: problem
title: "Evaluation of integral via Fubini-Tonelli"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Use the fact that
$$
\frac{1}{x} = \int_0^\infty e^{-xt}\,dt \quad (x > 0)
$$
and the Fubini-Tonelli Theorem to evaluate the integral
$$
\int_0^\infty e^{-\alpha x} \frac{\sin(\beta x)}{x}\,dx,
$$
where $\alpha$ and $\beta$ are positive numbers. Be sure to verify the assumption in the Fubini-Tonelli Theorem.

You may find the following formula useful:
$$
\int e^{ax}\sin bx\,dx = \frac{e^{ax}}{a^2 + b^2}(a\sin bx - b\cos bx) + C.
$$
:::
