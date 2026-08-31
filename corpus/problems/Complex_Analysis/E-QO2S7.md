---
schema: qual/card@1
id: E-QO2S7
kind: exercise
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

::: {.proposition}
For $\Omega\subseteq\CC$, show that $A(\CC)\definedas \theset{f: \Omega \to \CC \st f\text{ is bounded}}$ is a Banach space.
:::

::: {.proof}
?

> Apply Morera's Theorem and Cauchy's Theorem
:::

::: {.solution}
**Goal:** For $\Omega \subseteq \CC$, show that the space of bounded holomorphic functions on $\Omega$, with the supremum norm, is a Banach space.

<1>1. The space $A(\Omega) = \{f: \Omega \to \CC \st f \text{ bounded and holomorphic}\}$ is a vector space with the sup norm $\norm{f}_\infty = \sup_{z \in \Omega}\abs{f(z)}$.
::: {.proof}
Pointwise addition and scalar multiplication preserve holomorphy (linearity of the derivative) and boundedness (triangle inequality); $\norm{\cdot}_\infty$ is a norm on bounded functions, so it restricts to a norm on $A(\Omega)$.
:::

<1>2. $A(\Omega)$ is complete: every Cauchy sequence has a pointwise limit.
::: {.proof}
Let $\{f_n\}$ be Cauchy in $A(\Omega)$.
:::
For each $z \in \Omega$, $\abs{f_n(z) - f_m(z)} \le \norm{f_n - f_m}_\infty \to 0$, so $\{f_n(z)\}$ is a Cauchy sequence in $\CC$; define $f(z) = \lim_n f_n(z)$.

<1>3. The limit $f$ is holomorphic.
::: {.proof}
Since $\{f_n\}$ converges uniformly on $\Omega$ to $f$ (Cauchy in sup norm implies uniform convergence), and each $f_n$ is holomorphic, Morera's theorem applies: for every closed curve $\gamma$, $\int_\gamma f = \lim_n \int_\gamma f_n = \lim_n 0 = 0$ (uniform convergence lets the limit pass through the integral; each integral vanishes by Cauchy's theorem).
:::
Hence $f$ is holomorphic.

<1>4. $f$ is bounded and $f_n \to f$ in $A(\Omega)$.
::: {.proof}
Since $\{f_n\}$ is Cauchy it is bounded in norm, say $\norm{f_n}_\infty \le M$; then $\abs{f(z)} = \lim \abs{f_n(z)} \le M$ for all $z$, so $f \in A(\Omega)$.
:::
And $\norm{f_n - f}_\infty \to 0$ by the uniform convergence from <1>3.

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>4 show $A(\Omega)$ is a complete normed space, i.e. a Banach space.
:::
:::
