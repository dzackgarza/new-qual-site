---
schema: qual/card@1
id: P-5SR2D
kind: problem
title: Analyticity of $z\mapsto\overline{f(\overline{z})}$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Reflection
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Prove that if $z\mapsto f(z)$ is analytic, then $z \mapsto \overline{f(\bar z)}$ is analytic.
:::

::: {.solution title="Cauchy-Riemann"}
Let $f$ be analytic on an open set $\Omega$, and let $\Omega^* \coloneqq \theset{\bar z \suchthat z\in\Omega}$.
Define $g(z) \coloneqq \overline{f(\bar z)}$ on $\Omega^*$.
Write $f = u + iv$ and $g = a + ib$, so that $a(x,y) = u(x,-y)$ and $b(x,y) = -v(x,-y)$.

::: pf

::: {.pf-step #partials}
$a_x = u_x$, $a_y = -u_y$, $b_x = -v_x$ and $b_y = v_y$, where the partial derivatives of $u$ and $v$ are evaluated at $(x,-y)$.

::: pf-proof
This is the chain rule applied to $(x,y)\mapsto(x,-y)$.
In particular $a$ and $b$ are real-differentiable, since $u$ and $v$ are.
:::

:::

::: pf-step
$g$ is analytic on $\Omega^*$.

::: pf-proof
By step [](#partials){.pf-ref} and the Cauchy--Riemann equations $u_x = v_y$, $u_y = -v_x$ for $f$,
$$
a_x = u_x = v_y = b_y, \qquad a_y = -u_y = v_x = -b_x.
$$
So $g$ is real-differentiable and satisfies the Cauchy--Riemann equations, hence is holomorphic.
:::

:::

:::

:::

::: {.solution title="Direct definition"}
Let $f$ be analytic on an open set $\Omega$ and $g(z) \coloneqq \overline{f(\bar z)}$ for $\bar z\in\Omega$.

::: pf

::: pf-step
$g$ is complex differentiable at each $z$ with $\bar z\in\Omega$, and $g'(z) = \overline{f'(\bar z)}$.

::: pf-proof
For $h\neq0$ small,
$$
\frac{g(z+h) - g(z)}{h} = \overline{\left(\frac{f(\bar z + \bar h) - f(\bar z)}{\bar h}\right)}.
$$
As $h\to0$, $\bar h\to0$, so the quotient inside the conjugation tends to $f'(\bar z)$.
Since conjugation is continuous, the left side tends to $\overline{f'(\bar z)}$.
:::

:::

:::

:::

::: {.solution title="Power series"}
Let $f$ be analytic on an open set $\Omega$ and $g(z) \coloneqq \overline{f(\bar z)}$ for $\bar z\in\Omega$.

::: pf

::: pf-step
Near each point $z_0$ with $\bar z_0\in\Omega$, $g$ is given by a convergent power series in $z - z_0$.

::: pf-proof
Since $f$ is analytic at $\bar z_0$, $f(w) = \sum_{k\ge0} c_k (w-\bar z_0)^k$ for $\abs{w - \bar z_0}<r$, for some $r>0$.
For $\abs{z-z_0}<r$, put $w = \bar z$; then $\abs{w-\bar z_0} = \abs{z - z_0}$ and
$$
g(z) = \overline{\sum_{k\ge0} c_k \overline{(z-z_0)}^{\,k}} = \sum_{k\ge0} \bar c_k (z-z_0)^k,
$$
using that conjugation is continuous and additive.
:::

:::

:::

:::
