---
schema: qual/card@1
id: PR-OOHUL
kind: proposition
title: Polar Cauchy--Riemann equations
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC\sm\ts{0}$ be open and let $f=u+iv$ be [[D-E7A5W|holomorphic]] on $\Omega$, with $u,v$ real-valued.
Writing $u$ and $v$ as functions of $(r,\theta)$ through $z=re^{i\theta}$, $r>0$,
$$
\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial\theta}\qquad\text{and}\qquad\frac{1}{r}\frac{\partial u}{\partial\theta}=-\frac{\partial v}{\partial r}.
$$
:::

::: {.proof}
With $x=r\cos\theta$ and $y=r\sin\theta$, the chain rule gives
$$
\begin{aligned}
u_r&=u_x\cos\theta+u_y\sin\theta, & u_\theta&=r(-u_x\sin\theta+u_y\cos\theta),\\
v_r&=v_x\cos\theta+v_y\sin\theta, & v_\theta&=r(-v_x\sin\theta+v_y\cos\theta).
\end{aligned}
$$
Substituting the Cauchy--Riemann equations $v_x=-u_y$ and $v_y=u_x$ gives
$$
v_\theta=r(u_y\sin\theta+u_x\cos\theta)=ru_r,\qquad v_r=-u_y\cos\theta+u_x\sin\theta=-\frac1r u_\theta.
$$
:::
