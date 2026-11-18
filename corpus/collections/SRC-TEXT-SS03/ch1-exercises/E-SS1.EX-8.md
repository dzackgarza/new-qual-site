---
schema: qual/card@1
id: E-SS1.EX-8
kind: problem
title: Chain rule for the Wirtinger derivatives $\partial_z$ and $\partial_{\bar z}$
classification:
  areas:
    - complex-analysis
  topics: [Cauchy-Riemann, Wirtinger Derivatives]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps. No retained set covers this exercise, so the argument is the
      card's own and the card says so. Checked against Stein and Shakarchi, Chapter 1 Exercise 8, and
      against their definitions of the Wirtinger derivatives as (1/2)(d/dx - i d/dy) and
      (1/2)(d/dx + i d/dy). Each step re-read: real differentiability writes dF = F_x dx + F_y dy;
      changing to dz and dzbar gives F_z dz + F_zbar dzbar; the chain rule for real-differentiable
      maps is d(g o f) = dg o df; collecting coefficients of the two differentials gives the two
      formulas, and linear independence of dz and dzbar over C makes the comparison legitimate. The
      card notes that no holomorphy is assumed and that the partials of g are taken at f(z), which is
      where the printed formula is easy to misread. Not claimed: anything about second derivatives.
---

::: {.exercise}
Suppose $U$ and $V$ are open sets in the complex plane. Prove that if $f : U \to V$ and $g : V \to \CC$ are two functions that are differentiable (in the real sense, that is, as functions of the two real variables $x$ and $y$), and $h = g \circ f$, then

$$
\frac{\partial h}{\partial z} = \frac{\partial g}{\partial z} \frac{\partial f}{\partial z} + \frac{\partial g}{\partial \overline{z}} \frac{\partial \overline{f}}{\partial z}
$$

and

$$
\frac{\partial h}{\partial \overline{z}} = \frac{\partial g}{\partial z} \frac{\partial f}{\partial \overline{z}} + \frac{\partial g}{\partial \overline{z}} \frac{\partial \overline{f}}{\partial \overline{z}}.
$$

This is the complex version of the chain rule.
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card, and none was located for this exercise among the retained sets. It is checked against Stein and Shakarchi, Complex Analysis (2003), Chapter 1 Exercise 8, where $\partial_z$ and $\partial_{\bar z}$ are $\frac12(\partial_x-i\partial_y)$ and $\frac12(\partial_x+i\partial_y)$.

::: pf

::: {.pf-step #wirtinger}
For a real-differentiable $F$, $dF=F_{z}\,dz+F_{\bar z}\,d\bar z$.

::: pf-proof
Real differentiability gives $dF=F_{x}\,dx+F_{y}\,dy$. With $z=x+iy$ one has $dz=dx+i\,dy$ and $d\bar z=dx-i\,dy$, so $dx=\frac12(dz+d\bar z)$ and $dy=\frac1{2i}(dz-d\bar z)$. Substituting,
$$
dF=\tfrac12(F_{x}-iF_{y})\,dz+\tfrac12(F_{x}+iF_{y})\,d\bar z=F_{z}\,dz+F_{\bar z}\,d\bar z ,
$$
which is the definition of the two Wirtinger derivatives.
:::

:::

::: {.pf-step #f}
$df=f_{z}\,dz+f_{\bar z}\,d\bar z$ and $d\bar f=(\bar f)_{z}\,dz+(\bar f)_{\bar z}\,d\bar z$.

::: pf-proof
Apply step [](#wirtinger){.pf-ref} to $F=f$ and to $F=\bar f$; both are real differentiable because $f$ is.
:::

:::

::: {.pf-step #chain}
$dh=g_{z}\,df+g_{\bar z}\,d\bar f$, where the partials of $g$ are evaluated at $w=f(z)$.

::: pf-proof
$g$ is real differentiable at $w=f(z)$, so its differential there is $dg=g_{z}\,dw+g_{\bar z}\,d\bar w$ by step [](#wirtinger){.pf-ref}; the chain rule for real-differentiable maps says $d(g\circ f)=dg\circ df$, and $df$ is the differential of $w=f(z)$.
:::

:::

::: {.pf-step #expand}
$dh=\bigl(g_{z}f_{z}+g_{\bar z}(\bar f)_{z}\bigr)dz+\bigl(g_{z}f_{\bar z}+g_{\bar z}(\bar f)_{\bar z}\bigr)d\bar z$.

::: pf-proof
Substitute step [](#f){.pf-ref} into step [](#chain){.pf-ref}:
$g_{z}(f_{z}dz+f_{\bar z}d\bar z)+g_{\bar z}\bigl((\bar f)_{z}dz+(\bar f)_{\bar z}d\bar z\bigr)$, and collect the coefficients of $dz$ and $d\bar z$.
:::

:::

::: {.pf-step #compare}
$h_{z}=g_{z}f_{z}+g_{\bar z}(\bar f)_{z}$ and $h_{\bar z}=g_{z}f_{\bar z}+g_{\bar z}(\bar f)_{\bar z}$.

::: pf-proof
Also $dh=h_{z}\,dz+h_{\bar z}\,d\bar z$ by step [](#wirtinger){.pf-ref} applied to the real-differentiable $h$. The differentials $dz,d\bar z$ are linearly independent over $\CC$ at each point, so the coefficients in the two expressions for $dh$ agree, which is the displayed pair of formulas.
:::

:::

::: {.pf-step}
The chain rules hold as stated.

::: pf-proof
Step [](#compare){.pf-ref} is exactly the exercise:
$$
\boxed{\partial_{z}(g\circ f)=(\partial_{w}g)(\partial_{z}f)+(\partial_{\bar w}g)(\partial_{z}\bar f),\quad
\partial_{\bar z}(g\circ f)=(\partial_{w}g)(\partial_{\bar z}f)+(\partial_{\bar w}g)(\partial_{\bar z}\bar f),}
$$
where the partials of $g$ are taken at $w=f(z)$. No holomorphy is assumed: the identities are the real chain rule written in the $z,\bar z$ coordinates, and the second formula is obtained exactly as the first.
:::

:::

:::
:::
