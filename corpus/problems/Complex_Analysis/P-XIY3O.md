---
schema: qual/card@1
id: P-XIY3O
kind: problem
title: Green's theorem for rectangles, Cauchy's theorem, and Goursat's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Green's Theorem
  - Cauchy Integral Theorem
  - Cauchy-Riemann
  - Contour Integration
relations: []
review: draft
---

::: {.problem}
State and prove Green's Theorem for rectangles.
Use this to prove Cauchy's Theorem for functions that are analytic in a rectangle.
:::

::: {.problem title="Variant"}
Suppose $f\in C_\CC^1(\Omega)$ and $T\subset \Omega$ is a triangle with $T^\circ \subset \Omega$.

- Apply Green's theorem to show that $\int_T f(z) ~dz = 0$.
- Assume that $f'$ is continuous and prove Goursat's theorem.
:::

::: {.hint}
Green's theorem states
$$
\int_{T} F\, d x+G\, d y=\int_{T^\circ}\left(\frac{\partial G}{\partial x}-\frac{\partial F}{\partial y}\right) d x\, d y.
$$
:::

::: {.solution}
Let $R=[a,b]\times[c,d]$ with positively oriented boundary $\bd R$.
Green's theorem for rectangles: if $F,G$ are continuously differentiable on an open set containing $R$, then
$$
\int_{\bd R}F\dx+G\dy=\iint_R\qty{G_x-F_y}\dx\dy.
$$

::: pf

::: {.pf-step #green}
Green's theorem for rectangles holds.

::: pf-proof

::: {.pf-step #green-G}
$\int_{\bd R}G\dy=\iint_R G_x\dx\dy$.

::: pf-proof
On the horizontal sides $dy=0$; the right side is traversed upward and the left side downward. By Fubini's theorem and the fundamental theorem of calculus,
$$
\int_{\bd R}G\dy=\int_c^d\qty{G(b,y)-G(a,y)}\dy=\int_c^d\int_a^b G_x(x,y)\dx\dy.
$$
:::

:::

::: {.pf-step #green-F}
$\int_{\bd R}F\dx=-\iint_R F_y\dx\dy$.

::: pf-proof
On the vertical sides $dx=0$; the bottom side is traversed to the right and the top side to the left. Hence
$$
\int_{\bd R}F\dx=\int_a^b\qty{F(x,c)-F(x,d)}\dx=-\int_a^b\int_c^d F_y(x,y)\dy\dx.
$$
:::

:::

::: pf-qed
Add steps [](#green-G){.pf-ref} and [](#green-F){.pf-ref}.
:::

:::

:::

::: {.pf-step #cauchy-green}
If $f=u+iv$ is analytic with continuous derivative on an open set containing a region $D$ to which Green's theorem applies, then $\int_{\bd D}f(z)\dz=0$.

::: pf-proof
Since $\dz=\dx+i\dy$,
$$
\begin{aligned}
\int_{\bd D}f(z)\dz
&=\int_{\bd D}\qty{u\dx-v\dy}+i\int_{\bd D}\qty{v\dx+u\dy}\\
&=\iint_D\qty{-v_x-u_y}\dx\dy+i\iint_D\qty{u_x-v_y}\dx\dy=0,
\end{aligned}
$$
because the Cauchy--Riemann equations $u_x=v_y$, $u_y=-v_x$ make both integrands vanish.
The continuity of $f'$ makes $u,v$ continuously differentiable, as Green's theorem requires.
:::

:::

::: pf-step
Cauchy's theorem for a rectangle: if $f$ is analytic with continuous derivative on an open set containing $R$, then $\int_{\bd R}f(z)\dz=0$.

::: pf-proof
Apply step [](#cauchy-green){.pf-ref} with $D=R$, using step [](#green){.pf-ref}.
:::

:::

::: pf-step
Variant, first part: $\int_T f(z)\dz=0$.

::: pf-proof
The hypothesis $f\in C^1_\CC(\Omega)$ says that $f$ is holomorphic on $\Omega$ with continuous derivative. Apply step [](#cauchy-green){.pf-ref} with $D=T$, using Green's theorem for the triangle as stated in the hint.
:::

:::

::: pf-step
Variant, second part: Goursat's theorem, that $\int_T f(z)\dz=0$ for $f$ holomorphic on $\Omega$, holds when $f'$ is continuous.

::: pf-proof
Under this hypothesis $f\in C^1_\CC(\Omega)$, and the previous step applies.
:::

:::

:::

:::
