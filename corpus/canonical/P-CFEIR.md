---
schema: qual/card@1
id: P-CFEIR
kind: problem
title: Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$. Define $F$ by Show that
classification:
  areas:
  - real-analysis
  topics:
  - integrals
relations: []
review: draft
solved: true
---

::: problem
Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$.
Define $F$ by
$$
F(t):=\int_{-\infty}^{\infty} f(x) \cos (x t) d x
$$
Show that
$$
F'(t)=-\int_{-\infty}^{\infty} x f(x) \sin (x t) d x.
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $t \in \RR$, and consider the difference quotient for $h \neq 0$:
$$
\frac{F(t+h) - F(t)}{h} = \int_{-\infty}^\infty f(x) \frac{\cos(x(t+h)) - \cos(xt)}{h} \, dx.
$$

Define the integrand $g_h(x) = f(x) \frac{\cos(x(t+h)) - \cos(xt)}{h}$.

1. **Pointwise limit:** For each fixed $x \in \RR$, as $h \to 0$:
   $$
   \lim_{h \to 0} g_h(x) = f(x) \frac{d}{dt}[\cos(xt)] = -x f(x) \sin(xt).
   $$

2. **Dominating function:** By the Mean Value Theorem applied to $u \mapsto \cos(xu)$, there exists $c$ between $t$ and $t+h$ such that:
   $$
   \left| \frac{\cos(x(t+h)) - \cos(xt)}{h} \right| = |-x \sin(xc)| \leq |x|.
   $$
   Therefore, for all $h \neq 0$ and all $x \in \RR$:
   $$
   |g_h(x)| \leq |x f(x)|.
   $$
   Since $xf(x) \in L^1(\RR)$, the dominating function $g(x) = |xf(x)|$ is integrable on $\RR$.

3. **Application of Dominated Convergence Theorem:** By the Lebesgue Dominated Convergence Theorem:
   $$
   F'(t) = \lim_{h \to 0} \frac{F(t+h) - F(t)}{h} = \int_{-\infty}^\infty \lim_{h \to 0} g_h(x) \, dx = -\int_{-\infty}^\infty x f(x) \sin(xt) \, dx.
   $$
:::
