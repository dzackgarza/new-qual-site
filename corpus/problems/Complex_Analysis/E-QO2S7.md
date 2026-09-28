---
schema: qual/card@1
id: E-QO2S7
kind: problem
title: Bounded Complex Analytic Functions form a Banach Space
classification:
  areas:
  - complex-analysis
  topics:
  - Function Spaces
  - Uniform Convergence
  - Morera
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
For an open set $\Omega\subseteq\CC$, show that $A(\Omega)\definedas \theset{f: \Omega \to \CC \st f\text{ is holomorphic and bounded}}$, with the supremum norm, is a Banach space.
:::

::: {.hint}
Apply Morera's theorem and Cauchy's theorem.
:::

::: {.solution}
Write $A(\Omega) \coloneqq \{f: \Omega \to \CC \st f \text{ bounded and holomorphic}\}$ and $\norm{f}_\infty \coloneqq \sup_{z \in \Omega}\abs{f(z)}$, and let $\{f_n\}$ be a Cauchy sequence in $A(\Omega)$.

<1>1. $A(\Omega)$ is a vector space and $\norm{\cdot}_\infty$ is a norm on it.

::: {.proof}
Pointwise addition and scalar multiplication preserve holomorphy (linearity of the derivative) and boundedness (triangle inequality); $\norm{\cdot}_\infty$ is a norm on bounded functions, so it restricts to a norm on $A(\Omega)$.
:::

<1>2. There is a function $f\colon\Omega\to\CC$ with $f_n\to f$ uniformly on $\Omega$.

::: {.proof}
For each $z \in \Omega$, $\abs{f_n(z) - f_m(z)} \le \norm{f_n - f_m}_\infty \to 0$, so $\{f_n(z)\}$ is a Cauchy sequence in $\CC$; define $f(z) \coloneqq \lim_n f_n(z)$.
Letting $m\to\infty$ in $\abs{f_n(z) - f_m(z)} \le \sup_{k\geq n}\norm{f_n - f_k}_\infty$ gives $\sup_{z\in\Omega}\abs{f_n(z) - f(z)} \le \sup_{k\geq n}\norm{f_n - f_k}_\infty$, which tends to $0$ because $\{f_n\}$ is Cauchy.
:::

<1>3. $f$ is holomorphic.

::: {.proof}
By step <1>2, $f$ is a uniform limit of continuous functions, so $f$ is continuous on $\Omega$, and for every closed triangle $T\subseteq\Omega$, $\int_{\partial T} f = \lim_n \int_{\partial T} f_n = \lim_n 0 = 0$ (uniform convergence lets the limit pass through the integral; each integral vanishes by Goursat's theorem).
Hence $f$ is holomorphic by Morera's theorem [[T-LHSMY]].
:::

<1>4. $f\in A(\Omega)$ and $\norm{f_n - f}_\infty \to 0$.

::: {.proof}
Since $\{f_n\}$ is Cauchy it is bounded in norm, say $\norm{f_n}_\infty \le M$; then $\abs{f(z)} = \lim \abs{f_n(z)} \le M$ for all $z$, so $f$ is bounded, and $f$ is holomorphic by step <1>3, so $f \in A(\Omega)$.
By step <1>2, $\norm{f_n - f}_\infty \to 0$.
:::

<1>5. Q.E.D.

::: {.proof}
By step <1>1, $A(\Omega)$ is a normed space, and by step <1>4 every Cauchy sequence in it converges in $A(\Omega)$, so $A(\Omega)$ is a Banach space.
:::
:::
