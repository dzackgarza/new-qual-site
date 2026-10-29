---
schema: qual/card@1
id: P-KPLQU
kind: problem
title: Green's theorem for rectangles and Cauchy's theorem on a rectangle
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
State and prove Green's Theorem for rectangles.
Use this to prove Cauchy's Theorem for functions that are analytic in a rectangle.
:::

::: {.solution}
Let $R=[a,b]\times[c,d]$, and let $\partial R$ be its positively oriented boundary.

::: pf

::: {.pf-step #green}
If $P,Q$ have continuous first partial derivatives on a neighbourhood of $R$, then
$$
\boxed{\int_{\partial R}P\,dx+Q\,dy =\iint_R(Q_x-P_y)\,dA.}
$$

::: pf-proof
On the horizontal sides $dy = 0$, the bottom side runs from $a$ to $b$ and the top side from $b$ to $a$; by the fundamental theorem of calculus in $y$,
$$
\int_a^b P(x,c)\,dx-\int_a^b P(x,d)\,dx =-\int_a^b\int_c^d P_y(x,y)\,dy\,dx.
$$
On the vertical sides $dx = 0$, and in the same way
$$
\int_c^d Q(b,y)\,dy-\int_c^d Q(a,y)\,dy =\int_c^d\int_a^b Q_x(x,y)\,dx\,dy.
$$
Add the two and apply Fubini's theorem to the continuous integrands.
:::

:::

::: pf-step
If $f=u+iv$ is analytic on a neighbourhood of $R$, then $\boxed{\int_{\partial R}f(z)\,dz=0}$.

::: pf-proof
An analytic $f$ has a continuous derivative, so $u$ and $v$ have continuous first partial derivatives satisfying $u_x = v_y$ and $u_y = -v_x$.
Since $f(z)\,dz=(u\,dx-v\,dy)+i(v\,dx+u\,dy)$, step [](#green){.pf-ref} gives
$$
\int_{\partial R}f(z)\,dz = \iint_R(-v_x-u_y)\,dA + i\iint_R(u_x-v_y)\,dA = 0.
$$
:::

:::

:::
:::
