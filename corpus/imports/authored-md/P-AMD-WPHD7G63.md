---
schema: qual/card@1
id: P-AMD-WPHD7G63
kind: problem
title: "Suppose $f(x)$ and $xf(x)$ are integrable on $\\RR$. Define $F$ by $F(t):=\\int_{-\\infty}^{\\infty} f(x) \\cos (x t) d x$ Show that $F^{\\prime}(t)=-\\int_{-\\infty}^{\\infty} x f(x) \\sin (x t) d x$"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - integrals
relations: []
review: draft
solved: true
---

::: {.problem}
Suppose $f(x)$ and $xf(x)$ are integrable on $\RR$.
Define $F$ by
$$
F(t):=\int_{-\infty}^{\infty} f(x) \cos (x t) d x
$$
Show that
$$
F^{\prime}(t)=-\int_{-\infty}^{\infty} x f(x) \sin (x t) d x.
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Suppose $f, x f(x) \in L^1(\RR)$. Define $F(t) = \int_{-\infty}^\infty f(x)\cos(xt)\,dx$. Prove that $F$ is differentiable on $\RR$ with derivative $F'(t) = -\int_{-\infty}^\infty x f(x)\sin(xt)\,dx$.

<1>1. **Differentiability of the integrand and the difference quotient.**
  <2>1. Fix $t \in \RR$. For any sequence $\{h_n\}_{n=1}^\infty \subset \RR \setminus \{0\}$ with $h_n \to 0$ as $n \to \infty$, define for each $n \in \NN$:
    $$
    g_n(x) = f(x) \frac{\cos(x(t+h_n)) - \cos(xt)}{h_n}.
    $$
  <2>2. For every $x \in \RR$, $\lim_{n\to\infty} g_n(x) = -x f(x)\sin(xt)$.
    Proof: By the definition of the derivative of $t \mapsto \cos(xt)$,
    $$
    \lim_{n\to\infty} \frac{\cos(x(t+h_n)) - \cos(xt)}{h_n} = \frac{d}{dt}\cos(xt) = -x\sin(xt).
    $$
    Multiplying by $f(x)$ gives the pointwise limit $g(x) \definedas -x f(x)\sin(xt)$.

<1>2. **Domination by an $L^1(\RR)$ function.**
  <2>1. For all $x, t, h \in \RR$ with $h \neq 0$, $\left| \frac{\cos(x(t+h)) - \cos(xt)}{h} \right| \leq |x|$.
    Proof: By the Mean Value Theorem applied to $\phi(u) = \cos(xu)$, there exists some $\xi$ strictly between $t$ and $t+h$ such that:
    $$
    \frac{\cos(x(t+h)) - \cos(xt)}{h} = \phi'(\xi) = -x \sin(x\xi).
    $$
    Since $|\sin(x\xi)| \leq 1$ for all $\xi \in \RR$, we have $|\phi'(\xi)| = |-x\sin(x\xi)| \leq |x|$.
  <2>2. For all $n \in \NN$ and all $x \in \RR$, $|g_n(x)| \leq |x f(x)|$.
    Proof: By <1>1 (<2>1) and <2>1:
    $$
    |g_n(x)| = |f(x)| \left| \frac{\cos(x(t+h_n)) - \cos(xt)}{h_n} \right| \leq |f(x)| \cdot |x| = |x f(x)|.
    $$
  <2>3. The dominating function $G(x) \definedas |x f(x)|$ is in $L^1(\RR)$.
    Proof: By hypothesis, $xf(x)$ is integrable on $\RR$, so $\int_{-\infty}^\infty |x f(x)|\,dx < \infty$.

<1>3. **Application of the Dominated Convergence Theorem.**
  <2>1. $\lim_{n\to\infty} \int_{-\infty}^\infty g_n(x)\,dx = \int_{-\infty}^\infty g(x)\,dx = -\int_{-\infty}^\infty x f(x)\sin(xt)\,dx$.
    Proof: The sequence of measurable functions $\{g_n\}$ satisfies:
    1. $g_n(x) \to g(x) = -x f(x)\sin(xt)$ pointwise for all $x \in \RR$ (by <1>1);
    2. $|g_n(x)| \leq G(x)$ for all $n$ and all $x \in \RR$, with $G \in L^1(\RR)$ (by <1>2).
    By Lebesgue's Dominated Convergence Theorem, $\lim_{n\to\infty} \int_{-\infty}^\infty g_n(x)\,dx = \int_{-\infty}^\infty \lim_{n\to\infty} g_n(x)\,dx = \int_{-\infty}^\infty -x f(x)\sin(xt)\,dx$.
  <2>2. $\lim_{n\to\infty} \frac{F(t+h_n) - F(t)}{h_n} = -\int_{-\infty}^\infty x f(x)\sin(xt)\,dx$.
    Proof: By linearity of the integral:
    $$
    \frac{F(t+h_n) - F(t)}{h_n} = \int_{-\infty}^\infty f(x) \frac{\cos(x(t+h_n)) - \cos(xt)}{h_n}\,dx = \int_{-\infty}^\infty g_n(x)\,dx.
    $$
    Taking the limit as $n \to \infty$ and applying <2>1 yields the result.
  <2>3. Since the sequence $\{h_n\}$ with $h_n \to 0$ was arbitrary, the two-sided limit exists and equals the derivative:
    $$
    F'(t) = \lim_{h\to 0} \frac{F(t+h) - F(t)}{h} = -\int_{-\infty}^\infty x f(x)\sin(xt)\,dx.
    $$

<1>4. **Conclusion.**
  $F$ is differentiable on $\RR$ and $F'(t) = -\int_{-\infty}^\infty x f(x)\sin(xt)\,dx$. Q.E.D.
:::
