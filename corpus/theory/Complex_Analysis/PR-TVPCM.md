---
schema: qual/card@1
id: PR-TVPCM
kind: proposition
title: Holomorphic at a point if and only if $\bar\partial f$ vanishes there
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $f=u+iv$ be defined on a neighborhood of $z_0\in\CC$, with $u,v$ real-valued and [[D-KLTBZ|real-differentiable]] at $z_0$.
Then $f$ is [[D-E7A5W|holomorphic]] at $z_0$ if and only if
$$
\delbar f(z_0)=\frac12(\del_x+i\del_y)f(z_0)=0.
$$
:::

::: {.proof}
At $z_0$,
$$
\begin{aligned}
2\delbar f&=(\del_x+i\del_y)(u+iv)\\
&=u_x+iv_x+iu_y-v_y\\
&=(u_x-v_y)+i(u_y+v_x).
\end{aligned}
$$
So $\delbar f(z_0)=0$ exactly when $u_x=v_y$ and $u_y=-v_x$ at $z_0$, the Cauchy--Riemann equations.
For $f$ real-differentiable at $z_0$, these hold if and only if the real derivative of $f$ at $z_0$ is multiplication by a complex number, that is, if and only if $f$ is complex differentiable at $z_0$.
:::
