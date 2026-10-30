---
schema: qual/card@1
id: P-5YLZS
kind: problem
title: $F'(t)=-\int_{-\infty}^{\infty} xf(x)\sin(xt)\,dx$ for $F(t)=\int_{-\infty}^{\infty}
  f(x)\cos(xt)\,dx$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
  - Integrals
relations: []
review: draft
---

::: {.problem}
Suppose $f(x)$ and $x f(x)$ are integrable on $\RR$ ($f, xf \in L^1(\RR)$). Define $F: \RR \to \RR$ by
$$
F(t) = \int_{-\infty}^{\infty} f(x) \cos(x t) \, dx.
$$
Show that $F$ is differentiable on $\RR$ and that
$$
F'(t) = -\int_{-\infty}^{\infty} x f(x) \sin(x t) \, dx.
$$
:::

::: {.solution}
**Goal:** Prove that differentiation under the integral sign is valid for $F(t)$ using the difference quotient and the Dominated Convergence Theorem.

::: pf

::: pf-step
Difference quotient representation:

::: pf-proof

::: pf-step
Fix $t \in \RR$ and let $h \in \RR \setminus \{0\}$.

:::

::: pf-step
Form the difference quotient of $F$:
$$\frac{F(t + h) - F(t)}{h} = \frac{1}{h} \left( \int_{-\infty}^\infty f(x) \cos(x(t + h)) \, dx - \int_{-\infty}^\infty f(x) \cos(xt) \, dx \right) = \int_{-\infty}^\infty g_h(x) \, dx,$$
where
$$g_h(x) = f(x) \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right).$$

:::

:::

:::

::: pf-step
Pointwise limit of $g_h(x)$ as $h \to 0$:

::: pf-proof

::: pf-step
For each fixed $x \in \RR$, the function $u(t) = \cos(xt)$ is differentiable with derivative $u'(t) = -x \sin(xt)$.

:::

::: pf-step
Thus, by definition of the derivative:
$$\lim_{h \to 0} g_h(x) = f(x) \lim_{h \to 0} \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right) = -x f(x) \sin(xt) \quad \text{for all } x \in \RR.$$

:::

:::

:::

::: pf-step
Dominated bound:

::: pf-proof

::: pf-step
For each $x \in \RR$ and $h \ne 0$, apply the Mean Value Theorem to $t \mapsto \cos(xt)$ on the interval between $t$ and $t + h$.

:::

::: pf-step
There exists $\xi_h$ strictly between $t$ and $t + h$ such that
$$\frac{\cos(x(t + h)) - \cos(xt)}{h} = -x \sin(x \xi_h).$$

:::

::: pf-step
Take absolute values:
$$\abs{g_h(x)} = \abs{f(x)} \cdot \abs{{-x \sin(x \xi_h)}} = \abs{x f(x)} \abs{\sin(x \xi_h)} \le \abs{x f(x)} \cdot 1 = \abs{x f(x)}.$$

:::

::: pf-step
By hypothesis, $g(x) = \abs{x f(x)} \in L^1(\RR)$ is an integrable function that dominates $\abs{g_h(x)}$ for all $h \ne 0$.

:::

:::

:::

::: pf-step
Evaluation of $F'(t)$ by Dominated Convergence:

::: pf-proof

::: pf-step
By the Dominated Convergence Theorem:
$$F'(t) = \lim_{h \to 0} \frac{F(t + h) - F(t)}{h} = \lim_{h \to 0} \int_{-\infty}^\infty g_h(x) \, dx = \int_{-\infty}^\infty \lim_{h \to 0} g_h(x) \, dx = -\int_{-\infty}^\infty x f(x) \sin(xt) \, dx.$$

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$F'(t) = -\int_{-\infty}^{\infty} x f(x) \sin(xt) \, dx$.
:::

:::

:::

:::
