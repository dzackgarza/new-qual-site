---
schema: qual/card@1
id: P-WNOA2
kind: problem
title: Cauchy estimates for a holomorphic function of polynomial growth on a strip
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Suppose that $f$ is holomorphic on the strip $S = \{x+iy \mid x\in \mathbb{R},~ -1<y<1\}$ with $|f(z)| \leq A (1 + |z|)^\nu$ for $\nu \ge 0$ a fixed real number.
Show that for each integer $n\geq 0$ there exists an $A_n \geq 0$ such that $|f^{(n)}(x)| \leq A_n (1 + |x|)^\nu$ for all $x\in \mathbb{R}$.
:::

::: solution
Fix $n\ge0$. For each real $x$, the closed disk $\overline{D(x,1/2)}$ lies in the strip $S$. If $|\zeta-x|=1/2$, then
$$
1+|\zeta|\le 1+|x|+\frac12
\le \frac32(1+|x|).
$$
Therefore
$$
|f(\zeta)|
\le A\left(\frac32\right)^\nu(1+|x|)^\nu.
$$
Cauchy's estimate on the circle $|\zeta-x|=1/2$ gives
$$
|f^{(n)}(x)|
\le n!2^n A\left(\frac32\right)^\nu(1+|x|)^\nu.
$$
Thus one may take
$$
A_n=A\,n!\,2^n\left(\frac32\right)^\nu.
$$
:::
