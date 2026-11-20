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
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Nine of the card's fourteen steps, every leaf of the four parts, asserted their claim with
    no proof body; each now carries a `pf-proof`, and the `**Goal.**` paragraph that restated
    the plan is replaced by a sentence naming the three ingredients. No claim was changed.
    Checked: that each of the two integrals defining $F$ converges absolutely, that the
    difference quotient is an integral of $g_h$ and that $g_h$ is integrable, the pointwise
    limit, and the mean value bound $\abs{g_h(x)}\le\abs{xf(x)}$, which is what makes the
    dominated convergence theorem applicable; the argument is the standard one and no step
    uses more than $f,xf\in L^1$. Not checked: the qualifying examination the problem comes
    from is not in the checkout, so the statement stands as the card has it; no published
    solution was consulted.
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

The derivative is taken under the integral sign: the difference quotient is an integral of $g_h$, the $g_h$ converge pointwise to $-x f(x)\sin(xt)$, and the mean value theorem bounds them all by the integrable function $\abs{x f(x)}$.

::: pf

::: pf-step

Difference quotient representation:

::: pf-proof

Step 1.1 fixes the data and step 1.2 writes the quotient as one integral, which is what the dominated convergence theorem is applied to.

::: pf-step

Fix $t \in \RR$ and let $h \in \RR \setminus \{0\}$.

::: pf-proof

These are the point at which $F$ is differentiated and the increment of the quotient; $h\ne0$ is required for the quotient to be defined, and the limit below is taken over $h\to0$ through nonzero values, so fixing an arbitrary such pair loses nothing.

:::

:::

::: pf-step

Form the difference quotient of $F$:
$$\frac{F(t + h) - F(t)}{h} = \frac{1}{h} \left( \int_{-\infty}^\infty f(x) \cos(x(t + h)) \, dx - \int_{-\infty}^\infty f(x) \cos(xt) \, dx \right) = \int_{-\infty}^\infty g_h(x) \, dx,$$
where
$$g_h(x) = f(x) \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right).$$

::: pf-proof

Both integrals defining $F(t+h)$ and $F(t)$ exist, since $\abs{f(x)\cos(xs)}\le\abs{f(x)}$ and $f\in L^1$. The integral is additive and homogeneous, so the difference of the two integrals is the integral of the difference, and dividing by the constant $h\ne0$ divides the integral. The resulting integrand is $g_h$, which is integrable because $\abs{g_h(x)}\le2\abs{f(x)}/\abs{h}$ and $f\in L^1$.

:::

:::

:::

:::

::: pf-step

Pointwise limit of $g_h(x)$ as $h \to 0$:

::: pf-proof

Step 2.1 differentiates $t\mapsto\cos(xt)$ and step 2.2 multiplies by $f(x)$, giving the pointwise limit that the theorem needs.

::: pf-step

For each fixed $x \in \RR$, the function $u(t) = \cos(xt)$ is differentiable with derivative $u'(t) = -x \sin(xt)$.

::: pf-proof

$u$ is the composition of $\cos$, whose derivative is $-\sin$, with the linear map $t\mapsto xt$, whose derivative is the constant $x$; by the chain rule $u'(t)=-x\sin(xt)$ for every $t$.

:::

:::

::: pf-step

Thus, by definition of the derivative:
$$\lim_{h \to 0} g_h(x) = f(x) \lim_{h \to 0} \left( \frac{\cos(x(t + h)) - \cos(xt)}{h} \right) = -x f(x) \sin(xt) \quad \text{for all } x \in \RR.$$

::: pf-proof

The bracket is the difference quotient of $u$ at $t$, which tends to $u'(t)=-x\sin(xt)$ by step 2.1 and the definition of the derivative. Multiplication by the constant $f(x)$ is continuous, so the limit of $g_h(x)=f(x)$ times the bracket is $f(x)u'(t)$.

:::

:::

:::

:::

::: pf-step

Dominated bound:

::: pf-proof

Steps 3.1--3.4 produce a single integrable function bounding every $g_h$: the mean value theorem turns the difference quotient into a derivative at an intermediate point, and $\abs{\sin}\le1$ removes it.

::: pf-step

For each $x \in \RR$ and $h \ne 0$, apply the Mean Value Theorem to $t \mapsto \cos(xt)$ on the interval between $t$ and $t + h$.

::: pf-proof

For fixed $x$ the function $u(t)=\cos(xt)$ is differentiable, hence continuous, on all of $\RR$; the mean value theorem applies to $u$ on the closed interval with endpoints $t$ and $t+h$ (which is $[t+h,t]$ when $h<0$).

:::

:::

::: pf-step

There exists $\xi_h$ strictly between $t$ and $t + h$ such that
$$\frac{\cos(x(t + h)) - \cos(xt)}{h} = -x \sin(x \xi_h).$$

::: pf-proof

The mean value theorem gives $u(t+h)-u(t)=h\,u'(\xi_h)$ for some $\xi_h$ strictly between the endpoints, and $u'(\xi_h)=-x\sin(x\xi_h)$ by step 2.1; dividing by $h\ne0$ gives the displayed identity.

:::

:::

::: pf-step

Take absolute values:
$$\abs{g_h(x)} = \abs{f(x)} \cdot \abs{{-x \sin(x \xi_h)}} = \abs{x f(x)} \abs{\sin(x \xi_h)} \le \abs{x f(x)} \cdot 1 = \abs{x f(x)}.$$

::: pf-proof

By step 3.2, $g_h(x)=f(x)(-x\sin(x\xi_h))$, so $\abs{g_h(x)}=\abs{f(x)}\abs{x}\abs{\sin(x\xi_h)}=\abs{xf(x)}\abs{\sin(x\xi_h)}$; and $\abs{\sin y}\le1$ for every real $y$.

:::

:::

::: pf-step

By hypothesis, $g(x) = \abs{x f(x)} \in L^1(\RR)$ is an integrable function that dominates $\abs{g_h(x)}$ for all $h \ne 0$.

::: pf-proof

The hypothesis is that $xf\in L^1(\RR)$, that is $\int_\RR\abs{xf(x)}\,dx<\infty$; step 3.3 gives $\abs{g_h(x)}\le\abs{xf(x)}$ at every $x$ and for every $h\ne0$, so $g=\abs{xf}$ is an integrable dominating function.

:::

:::

:::

:::

::: pf-step

Evaluation of $F'(t)$ by Dominated Convergence:

::: pf-proof

Step 4.1 assembles the three parts: the quotient is the integral of $g_h$, the $g_h$ converge pointwise, and they are dominated; the conclusion then is the definition of $F'(t)$.

::: pf-step

By the Dominated Convergence Theorem:
$$F'(t) = \lim_{h \to 0} \frac{F(t + h) - F(t)}{h} = \lim_{h \to 0} \int_{-\infty}^\infty g_h(x) \, dx = \int_{-\infty}^\infty \lim_{h \to 0} g_h(x) \, dx = -\int_{-\infty}^\infty x f(x) \sin(xt) \, dx.$$

::: pf-proof

The first equality is the definition of $F'(t)$ and shows the limit exists once the others are justified. The second is step 1.2. The third is the dominated convergence theorem: $g_h\to-xf(x)\sin(xt)$ pointwise by step 2.2 and $\abs{g_h}\le\abs{xf}\in L^1$ by step 3.4. The last equality substitutes the limit.

:::

:::

:::

:::

::: pf-step

Conclusion:

::: pf-proof

The identity $F'(t)=-\int_\RR xf(x)\sin(xt)\,dx$ of step 4.1 holds at the arbitrary point $t\in\RR$ fixed in step 1.1, so $F$ is differentiable on $\RR$ with that derivative, which is the assertion of the problem.

:::

:::

:::
:::