---
schema: qual/card@1
id: P-MMAQ-5WDF4PWP7U
kind: problem
title: "Let $f, g \\in L^1([0, 1])$ and for all $x\\in [0, 1]$ define $F(x):=\\int_{0}^{x} f(y) d y \\quad \\text { and } \\quad G(x):=\\int_{0}^{x} g(y) d y$"
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - fubini-tonelli
  - l1
relations: []
review: draft
solved: true
---

::: problem
Let $f, g \in L^1([0, 1])$ and for all $x\in [0, 1]$ define
$$
F(x):=\int_{0}^{x} f(y) d y \quad \text { and } \quad G(x):=\int_{0}^{x} g(y) d y.
$$

Prove that
$$
\int_{0}^{1} F(x) g(x) d x=F(1) G(1)-\int_{0}^{1} f(x) G(x) d x
$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $f, g \in L^1([0, 1])$ and $F(x) = \int_0^x f(y)\,dy$, $G(x) = \int_0^x g(y)\,dy$. Prove integration by parts via Fubini-Tonelli:
$$
\int_0^1 F(x) g(x)\,dx = F(1) G(1) - \int_0^1 f(x) G(x)\,dx.
$$

<1>1. **Express the left-hand side integral as an iterated integral.**
  <2>1. Substitute the definition of $F(x)$:
    $$
    \int_0^1 F(x) g(x)\,dx = \int_0^1 \left( \int_0^x f(y)\,dy \right) g(x)\,dx = \int_0^1 \left( \int_0^1 f(y) g(x) \chi_{\{0 \leq y \leq x \leq 1\}}(y, x)\,dy \right) dx.
    $$
    Proof: The region of integration in the $(y, x)$-plane is the triangle $\Delta \definedas \{(y, x) \in [0, 1]^2 : 0 \leq y \leq x \leq 1\}$.
  <2>2. The integrand $H(y, x) \definedas f(y) g(x) \chi_\Delta(y, x)$ is measurable on $[0, 1]^2$.
    Proof: $f(y)$ and $g(x)$ are measurable on $[0, 1]$, so their product $(y, x) \mapsto f(y)g(x)$ is product-measurable on $[0, 1]^2$. The set $\Delta = \{(y, x) : x - y \geq 0\} \cap [0, 1]^2$ is closed, hence Borel measurable in $[0, 1]^2$. Thus their product is measurable.

<1>2. **Verify integrability on $[0, 1]^2$ to apply Fubini's Theorem.**
  <2>1. By Tonelli's Theorem for non-negative measurable functions:
    $$
    \int_{[0, 1]^2} |H(y, x)|\,d(y, x) = \int_0^1 \int_0^1 |f(y)| |g(x)| \chi_\Delta(y, x)\,dy\,dx \leq \int_0^1 \int_0^1 |f(y)| |g(x)|\,dy\,dx
    $$
    $$
    = \left(\int_0^1 |f(y)|\,dy\right) \left(\int_0^1 |g(x)|\,dx\right) = \|f\|_1 \|g\|_1 < \infty.
    $$
    Proof: Since $f, g \in L^1([0, 1])$, the product of their norms is finite.
  <2>2. $H(y, x) \in L^1([0, 1]^2)$.
    Proof: The integral of $|H|$ is finite by <2>1.

<1>3. **Interchange order of integration using Fubini's Theorem.**
  <2>1. By Fubini's Theorem:
    $$
    \int_0^1 F(x) g(x)\,dx = \iint_\Delta f(y) g(x)\,d(y, x) = \int_0^1 f(y) \left( \int_y^1 g(x)\,dx \right) dy.
    $$
    Proof: The vertical cross-sections of $\Delta$ are $y \in [0, x]$ for fixed $x \in [0, 1]$, and the horizontal cross-sections are $x \in [y, 1]$ for fixed $y \in [0, 1]$.
  <2>2. $\int_y^1 g(x)\,dx = G(1) - G(y)$.
    Proof: By definition $G(1) = \int_0^1 g(x)\,dx$ and $G(y) = \int_0^y g(x)\,dx$, so $\int_y^1 g(x)\,dx = \int_0^1 g(x)\,dx - \int_0^y g(x)\,dx = G(1) - G(y)$.
  <2>3. Substitute into the reversed iterated integral:
    $$
    \int_0^1 F(x) g(x)\,dx = \int_0^1 f(y) [G(1) - G(y)]\,dy = G(1) \int_0^1 f(y)\,dy - \int_0^1 f(y) G(y)\,dy.
    $$
    Proof: By linearity of the integral.
  <2>4. Since $\int_0^1 f(y)\,dy = F(1)$, we obtain:
    $$
    \int_0^1 F(x) g(x)\,dx = F(1) G(1) - \int_0^1 f(y) G(y)\,dy = F(1) G(1) - \int_0^1 f(x) G(x)\,dx.
    $$

<1>4. **Conclusion.**
  The integration by parts formula is proved rigorously. Q.E.D.
:::
