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

::: problem
Suppose $f(x)$ and $x f(x)$ are integrable on $\mathbb{R}$ ($f, xf \in L^1(\mathbb{R})$). Define $F: \mathbb{R} \to \mathbb{R}$ by
$$
F(t) = \int_{-\infty}^{\infty} f(x) \cos(x t) \, dx.
$$
Show that $F$ is differentiable on $\mathbb{R}$ and that
$$
F'(t) = -\int_{-\infty}^{\infty} x f(x) \sin(x t) \, dx.
$$
:::

::: solution
**Goal:** Prove that differentiation under the integral sign is valid for $F(t)$ using the difference quotient and the Dominated Convergence Theorem.

<1>1. Difference quotient representation:
::: {.proof}
    <2>1. Fix $t \in \mathbb{R}$ and let $h \in \mathbb{R} \setminus \{0\}$.
    <2>2. Form the difference quotient of $F$:
    $$\frac{F(t + h) - F(t)}{h} = \frac{1}{h} \left( \int_{-\infty}^\infty f(x) \cos(x(t + h)) \, dx - \int_{-\infty}^\infty f(x) \cos(xt) \, dx \right) = \int_{-\infty}^\infty g_h(x) \, dx,$$
    where
    $$g_h(x) = f(x) \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right).$$

:::

<1>2. Pointwise limit of $g_h(x)$ as $h \to 0$:
::: {.proof}
    <2>1. For each fixed $x \in \mathbb{R}$, the function $u(t) = \cos(xt)$ is differentiable with derivative $u'(t) = -x \sin(xt)$.
    <2>2. Thus, by definition of the derivative:
    $$\lim_{h \to 0} g_h(x) = f(x) \lim_{h \to 0} \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right) = -x f(x) \sin(xt) \quad \text{for all } x \in \mathbb{R}.$$

:::

<1>3. Dominated bound:
::: {.proof}
    <2>1. For each $x \in \mathbb{R}$ and $h \ne 0$, apply the Mean Value Theorem to $t \mapsto \cos(xt)$ on the interval between $t$ and $t + h$.
    <2>2. There exists $\xi_h$ strictly between $t$ and $t + h$ such that
    $$\frac{\cos(x(t + h)) - \cos(xt)}{h} = -x \sin(x \xi_h).$$
    <2>3. Take absolute values:
    $$|g_h(x)| = |f(x)| \cdot |{-x \sin(x \xi_h)}| = |x f(x)| |\sin(x \xi_h)| \le |x f(x)| \cdot 1 = |x f(x)|.$$
    <2>4. By hypothesis, $g(x) = |x f(x)| \in L^1(\mathbb{R})$ is an integrable function that dominates $|g_h(x)|$ for all $h \ne 0$.

:::

<1>4. Evaluation of $F'(t)$ by Dominated Convergence:
::: {.proof}
    <2>1. By the Dominated Convergence Theorem:
    $$F'(t) = \lim_{h \to 0} \frac{F(t + h) - F(t)}{h} = \lim_{h \to 0} \int_{-\infty}^\infty g_h(x) \, dx = \int_{-\infty}^\infty \lim_{h \to 0} g_h(x) \, dx = -\int_{-\infty}^\infty x f(x) \sin(xt) \, dx.$$

:::

<1>5. Conclusion:
::: {.proof}
    $F'(t) = -\int_{-\infty}^{\infty} x f(x) \sin(xt) \, dx$.
:::
:::
