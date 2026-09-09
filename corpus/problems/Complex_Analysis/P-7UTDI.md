---
schema: qual/card@1
id: P-7UTDI
kind: problem
title: Constancy of holomorphic functions of constant modulus, real part, argument,
  or conjugate
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Open Mapping Theorem
  - Maximum Modulus Principle
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
Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if it satisfies any of the following conditions:

a. $|f(z)|$ is constant.
b. $\Re(f(z))$ is constant.
c. $\arg(f(z))$ is constant.
d. $\overline{f(z)}$ is analytic.
:::

::: solution
Write $f=u+iv$ on the connected domain.

<1>1. If $|f|$ is constant, then either $f\equiv0$, or $f$ is nonzero and its image lies in a circle. A nonconstant holomorphic map is open, but a circle has empty interior. Hence $f$ is constant.

<1>2. If $\Re f=u$ is constant, then $u_x=u_y=0$. By the Cauchy--Riemann equations,
\[
v_y=u_x=0,\qquad v_x=-u_y=0,
\]
so $v$ is constant and therefore $f$ is constant.

<1>3. If $\arg f\equiv\theta_0$, then $f$ never vanishes and
\[
e^{-i\theta_0}f
\]
is real-valued. It is holomorphic, so by part (2) it is constant. Hence $f$ is constant.

<1>4. If $\overline f=u-iv$ is also holomorphic, then applying the Cauchy--Riemann equations to both $u+iv$ and $u-iv$ gives
\[
u_x=v_y=-v_y,
\qquad
u_y=-v_x=v_x.
\]
Thus $u_x=u_y=v_x=v_y=0$, so $f$ is constant.
:::
