---
schema: qual/card@1
id: P-TRIV-DE23
kind: problem
title: Integral solution of the modified Bessel equation of order zero
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 23, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Verify that $\int _ { 1 } ^ { \infty } \mathrm { d } t \frac { e ^ { - x t } } { \sqrt { t ^ { 2 } - 1 } }$ is a solution to the differential equation $y ^ { \prime \prime } { + } \frac { 1 } { x } y ^ { \prime } { - } y =$ 0.
:::

::: {.solution}

For $x>0$, set
$$
y(x)=\int_1^\infty\frac{e^{-xt}}{\sqrt{t^2-1}}\,dt.
$$

::: pf

::: {.pf-step #s1-1}

Differentiation under the integral sign gives
$$
y'(x)=-\int_1^\infty\frac{t e^{-xt}}{\sqrt{t^2-1}}\,dt,
\qquad
y''(x)=\int_1^\infty\frac{t^2 e^{-xt}}{\sqrt{t^2-1}}\,dt.
$$


::: pf-proof

For $x$ in any compact subinterval of $(0,\infty)$, the integrands obtained after one or two $x$-derivatives are bounded at infinity by a polynomial in $t$ times $e^{-ct}$ for some $c>0$, and near $t=1$ by a constant multiple of $(t-1)^{-1/2}$. These bounds are integrable, so differentiation under the integral sign is justified by dominated convergence.

:::

:::

::: {.pf-step #s1-2}

One has
$$
y''(x)-y(x)
=\int_1^\infty e^{-xt}\sqrt{t^2-1}\,dt.
$$


::: pf-proof

Subtract the defining integral for $y$ from the expression for $y''$ in step [](#s1-1){.pf-ref}:
$$
y''-y
=\int_1^\infty
\frac{(t^2-1)e^{-xt}}{\sqrt{t^2-1}}\,dt,
$$
which simplifies to the displayed integral.

:::

:::

::: {.pf-step #s1-3}

Integration by parts gives
$$
\int_1^\infty e^{-xt}\sqrt{t^2-1}\,dt
=-\frac1x y'(x).
$$


::: pf-proof

Since
$$
\frac d{dt}\sqrt{t^2-1}=\frac{t}{\sqrt{t^2-1}},
$$
integration by parts with $u=\sqrt{t^2-1}$ and $dv=e^{-xt}dt$ yields
$$
\int_1^\infty e^{-xt}\sqrt{t^2-1}\,dt
=\left[-\frac1x e^{-xt}\sqrt{t^2-1}\right]_1^\infty
+\frac1x\int_1^\infty\frac{t e^{-xt}}{\sqrt{t^2-1}}\,dt.
$$
The boundary term vanishes at both endpoints, and step [](#s1-1){.pf-ref} identifies the remaining integral as $-y'(x)$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{y''+\frac1x y'-y=0}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} to obtain $y''-y=-y'/x$, and rearrange.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} verifies the required differential equation for every $x>0$.

:::

:::

:::
