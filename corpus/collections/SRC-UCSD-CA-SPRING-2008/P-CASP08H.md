---
schema: qual/card@1
id: P-CASP08H
kind: problem
title: Derivative bounds on the upper half-plane give continuation to $\operatorname{Im} z > -1$
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
  - Taylor Series
relations: []
review: draft
---

::: {.problem}
Let $f(z)$ be analytic in the upper half-plane $H := \{\operatorname{Im} z > 0\}$. Suppose that for every $p > 1$ and every $z = x + iy$ in $H$, there is $M > 0$ such that
$$
\abs{f^{(n)}(z)} \le \frac{n!\,M}{y^{n/p}}, \qquad \forall n \ge 0.
$$
Show that $f$ can be analytically continued to an analytic function in the half-plane $\{\operatorname{Im} z > -1\}$.

Hint: For each fixed $p$, show that there is $0 < c_p < 1$, with $\lim_{p \to \infty} c_p = 1$, such that $f$ can be analytically continued to the half-plane $\{\operatorname{Im} z > -c_p\}$.
:::

::: {.solution}
::: pf

::: {.pf-step #radius}
Fix $p>1$ and $z_0=x_0+iy_0\in H$. The Taylor series of $f$ at $z_0$ converges on $B(z_0,y_0^{1/p})$, and its sum agrees with $f$ on $B(z_0,y_0^{1/p})\cap H$.

::: pf-proof
The coefficients satisfy $\abs{f^{(n)}(z_0)/n!}\le M y_0^{-n/p}$, so the Cauchy–Hadamard formula gives radius of convergence at least $y_0^{1/p}$. The sum is analytic on $B(z_0,y_0^{1/p})$ and equals $f$ on $B(z_0,y_0)\subset H$. The set $B(z_0,y_0^{1/p})\cap H$ is convex, hence connected, so the identity theorem gives agreement on all of it.
:::

:::

::: {.pf-step #cp}
Let $y_p=p^{-p/(p-1)}$ and $c_p=y_p^{1/p}-y_p=(p-1)p^{-p/(p-1)}$. Then $0<c_p<1$ and $c_p\to1$ as $p\to\infty$.

::: pf-proof
The function $y\mapsto y^{1/p}-y$ on $(0,\infty)$ has derivative $\frac1p y^{1/p-1}-1$, which vanishes exactly at $y=y_p$, so $c_p$ is its maximum and $c_p>0$. Also $y_p^{1/p}=y_p\,p$, which gives the closed form. Since $p^{-p/(p-1)}=p^{-1}p^{-1/(p-1)}$ and $p^{1/(p-1)}>1$, $c_p<(p-1)/p<1$. Finally $p^{1/(p-1)}=e^{\log p/(p-1)}\to1$, so $c_p\to1$.
:::

:::

::: {.pf-step #strip}
For each $p>1$, $f$ extends to an analytic function $F_p$ on $H_p:=\{\operatorname{Im}z>-c_p\}$.

::: pf-proof
For $x\in\RR$ let $D_x=B(x+iy_p,\,y_p^{1/p})$. By step [](#radius){.pf-ref}, the Taylor series of $f$ at $x+iy_p$ defines an analytic $g_x$ on $D_x$ with $g_x=f$ on $D_x\cap H$. The union of the $D_x$ is the strip $\{y_p-y_p^{1/p}<\operatorname{Im}z<y_p+y_p^{1/p}\}$, whose lower edge is $\operatorname{Im}z=-c_p$ by step [](#cp){.pf-ref}. If $D_x\cap D_{x'}\neq\emptyset$, this intersection is convex and symmetric about the line $\operatorname{Im}z=y_p$, so it contains a point of $H$; there $g_x=f=g_{x'}$, and the identity theorem gives $g_x=g_{x'}$ on the connected set $D_x\cap D_{x'}$. Hence $f$ on $H$ and the $g_x$ on the $D_x$ define one analytic function $F_p$ on $H\cup\bigcup_xD_x=H_p$.
:::

:::

::: pf-qed
If $p<p'$ with $c_p\le c_{p'}$, then $F_p$ and $F_{p'}$ agree on $H$, hence on the connected set $H_p\cap H_{p'}$. So the $F_p$ glue to one analytic function on $\bigcup_pH_p$. By step [](#cp){.pf-ref}, $\sup_pc_p=1$ and each $c_p<1$, so $\bigcup_pH_p=\{\operatorname{Im}z>-1\}$.
:::

:::
:::
