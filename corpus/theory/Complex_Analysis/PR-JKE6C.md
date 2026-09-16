---
schema: qual/card@1
id: PR-JKE6C
kind: proposition
title: Cauchy--Riemann implies holomorphic
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
Let $\Omega\subseteq\CC$ be open and let $f = u+iv\colon\Omega\to\CC$, where $u,v\colon\Omega\to\RR$ are continuously differentiable as functions of $(x,y)$, $z=x+iy$.
If $u_x=v_y$ and $u_y=-v_x$ on $\Omega$, then $f$ is [[D-E7A5W|holomorphic]] on $\Omega$ and
$$
f'(z) = \del f(z) = u_x(z) + iv_x(z).
$$
:::

::: {.proof}
Fix $z\in\Omega$ and write $h=h_1+ih_2$.
Since $u$ and $v$ are continuously differentiable, they are real differentiable at $z$, so
$$
f(z+h)-f(z)=u_xh_1+u_yh_2+i\qty{v_xh_1+v_yh_2}+o(\abs{h}),
$$
with the partial derivatives evaluated at $z$.
Substituting $u_y=-v_x$ and $v_y=u_x$ gives $u_xh_1-v_xh_2+i\qty{v_xh_1+u_xh_2}=(u_x+iv_x)(h_1+ih_2)$, so $\frac{f(z+h)-f(z)}{h}\to u_x+iv_x$ as $h\to0$.
Finally, $\del f=\frac12\qty{f_x-if_y}=\frac12\qty{u_x+v_y+i(v_x-u_y)}=u_x+iv_x$ by the same equations.
:::
