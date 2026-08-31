---
schema: qual/card@1
id: P-2HIC2
kind: problem
title: $\int_0^1 Fg=F(1)G(1)-\int_0^1 fG$ for $F(x)=\int_0^x f$ and $G(x)=\int_0^x
  g$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $f, g \in L^1([0, 1])$, and for all $x \in [0, 1]$ define
$$
F(x) = \int_0^x f(y) \, dy \quad \text{and} \quad G(x) = \int_0^x g(y) \, dy.
$$

Prove that
$$
\int_0^1 F(x) g(x) \, dx = F(1) G(1) - \int_0^1 f(x) G(x) \, dx.
$$
:::

::: solution
**Goal:** Prove the integration by parts formula for absolutely continuous functions using Tonelli's and Fubini's Theorems on the triangular domain $0 \le y \le x \le 1$.

<1>1. Absolute integrability on the product space:
::: {.proof}
    <2>1. Define the indicator function of the triangle $T = \{(x, y) \in [0, 1]^2 \mid 0 \le y \le x \le 1\}$:
    $$\chi_T(x, y) = \begin{cases} 1 & \text{if } 0 \le y \le x \le 1, \\ 0 & \text{otherwise}. \end{cases}$$
    <2>2. The function $(x, y) \mapsto |f(y)| |g(x)| \chi_T(x, y)$ is non-negative and Lebesgue measurable on $[0, 1]^2$.
    <2>3. By Tonelli's Theorem:
    $$\int_0^1 \int_0^1 |f(y)| |g(x)| \chi_T(x, y) \, dy \, dx = \int_0^1 |g(x)| \left( \int_0^x |f(y)| \, dy \right) dx \le \int_0^1 |g(x)| \|f\|_{L^1} \, dx = \|f\|_{L^1} \|g\|_{L^1}.$$
    <2>4. Since $f, g \in L^1([0, 1])$, $\|f\|_{L^1} \|g\|_{L^1} < \infty$.
    <2>5. Thus $(x, y) \mapsto f(y) g(x) \chi_T(x, y) \in L^1([0, 1]^2)$.

:::

<1>2. Express the left-hand integral as a double integral:
::: {.proof}
    <2>1. By definition of $F(x)$, for each $x \in [0, 1]$:
    $$F(x) g(x) = \left( \int_0^x f(y) \, dy \right) g(x) = \int_0^1 f(y) g(x) \chi_T(x, y) \, dy.$$
    <2>2. Integrating over $x \in [0, 1]$:
    $$\int_0^1 F(x) g(x) \, dx = \int_0^1 \left( \int_0^1 f(y) g(x) \chi_T(x, y) \, dy \right) dx.$$

:::

<1>3. Interchange order of integration via Fubini's Theorem:
::: {.proof}
    <2>1. By <1>1, Fubini's Theorem applies to the product $f(y) g(x) \chi_T(x, y)$.
    <2>2. Reversing the order of integration:
    $$\int_0^1 \left( \int_0^1 f(y) g(x) \chi_T(x, y) \, dy \right) dx = \int_0^1 \left( \int_0^1 f(y) g(x) \chi_T(x, y) \, dx \right) dy.$$
    <2>3. Because $\chi_T(x, y) = 1$ if and only if $y \le x \le 1$:
    $$\int_0^1 f(y) g(x) \chi_T(x, y) \, dx = f(y) \int_y^1 g(x) \, dx.$$
    <2>4. Thus:
    $$\int_0^1 F(x) g(x) \, dx = \int_0^1 f(y) \left( \int_y^1 g(x) \, dx \right) dy.$$

:::

<1>4. Evaluate the inner integral and conclude:
::: {.proof}
    <2>1. By additivity of the Lebesgue integral:
    $$\int_y^1 g(x) \, dx = \int_0^1 g(x) \, dx - \int_0^y g(x) \, dx = G(1) - G(y).$$
    <2>2. Substitute into the integral from <1>3:
    $$\int_0^1 F(x) g(x) \, dx = \int_0^1 f(y) (G(1) - G(y)) \, dy = G(1) \int_0^1 f(y) \, dy - \int_0^1 f(y) G(y) \, dy.$$
    <2>3. Since $\int_0^1 f(y) \, dy = F(1)$, relabeling the dummy variable $y$ as $x$ gives:
    $$\int_0^1 F(x) g(x) \, dx = F(1) G(1) - \int_0^1 f(x) G(x) \, dx.$$

:::

<1>5. Conclusion:
::: {.proof}
    The integration by parts identity holds for all $f, g \in L^1([0, 1])$ by Fubini–Tonelli.
:::
:::
