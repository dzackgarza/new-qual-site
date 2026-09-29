---
schema: qual/card@1
id: P-MMAQ-RFQAUA7NB7
kind: problem
title: Bounded variation, Brouwer on $[0,1]$, uniform limits of uniformly continuous
  functions, and the mean value theorem in $\RR^n$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Continuity
  - Mean Value Theorem
  - Variation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Prove or disprove each of the following statements.

(a) If $f$ is of bounded variation on $[0,1]$, then it is continuous on $[0,1]$.

(b) If $f : [0, 1] \to [0, 1]$ is a continuous function, then there exists $x_0 \in [0, 1]$ such that $f(x_0) = x_0$.

(c) Let $\{f_n\}$ be a sequence of uniformly continuous functions on an interval $I$.
If $\{f_n\}$ converges uniformly to a function $f$ on $I$, then $f$ is also uniformly continuous on $I$.

(d) If $f$ is differentiable on a connected set $E \subset \mathbb{R}^n$, then for any $x, y \in E$, there exists $z \in E$ such that $f(x) - f(y) = \nabla f(z)(x - y)$.
:::

::: {.solution}

::: pf

::: {.pf-step #a-is-false}
Statement (a) is false.

::: pf-proof

::: pf-step
Let $f(x) = 0$ on $[0, 1/2]$ and $f(x) = 1$ on $(1/2, 1]$.
:::

::: pf-step
$f$ has bounded variation on $[0,1]$.

::: pf-proof
For any partition $0 = x_0 < \dots < x_k = 1$, all increments $\abs{f(x_j) - f(x_{j-1})}$ vanish except the single one crossing $1/2$, which is $\leq 1$; hence the total variation is $\leq 1$.
:::

:::

::: pf-step
$f$ is not continuous at $1/2$.

::: pf-proof
$\lim_{x \to 1/2^+} f(x) = 1 \neq 0 = f(1/2)$.
:::

:::

:::

::: pf-qed
This disproves (a).
:::

:::

::: {.pf-step #b-is-true}
Statement (b) is true.

::: pf-proof

::: pf-step
Define $g(x) \definedas f(x) - x$ on $[0,1]$; then $g$ is continuous, $g(0) = f(0) \geq 0$, and $g(1) = f(1) - 1 \leq 0$.

::: pf-proof
$f: [0,1] \to [0,1]$, so $f(0) \in [0,1]$ and $f(1) \in [0,1]$; continuity of $g$ follows from continuity of $f$.
:::

:::

::: pf-step
By the intermediate value theorem, there is $x_0 \in [0,1]$ with $g(x_0) = 0$, i.e. $f(x_0) = x_0$.

::: pf-proof
IVT applied to $g$: $0$ lies between $g(0) \geq 0$ and $g(1) \leq 0$.
:::

:::

:::

::: pf-qed
This proves (b).
:::

:::

::: {.pf-step #c-is-true}
Statement (c) is true.

::: pf-proof

::: {.pf-step #eps-N-uniform-convergence}
Fix $\eps > 0$.
Since $f_n \to f$ uniformly on $I$, there is $N$ with $\norm{f_n - f}_\infty < \eps/3$ for all $n \geq N$.

::: pf-proof
Definition of uniform convergence.
:::

:::

::: {.pf-step #delta-uniform-continuity-fN}
$f_N$ is uniformly continuous, so there is $\delta > 0$ with $\abs{f_N(x) - f_N(y)} < \eps/3$ whenever $x, y \in I$ and $\abs{x - y} < \delta$.

::: pf-proof
Definition of uniform continuity of $f_N$.
:::

:::

::: {.pf-step #triangle-inequality-bound}
For $x, y \in I$ with $\abs{x - y} < \delta$, $$\abs{f(x) - f(y)} \leq \abs{f(x) - f_N(x)} + \abs{f_N(x) - f_N(y)} + \abs{f_N(y) - f(y)} < \frac{\eps}{3} + \frac{\eps}{3} + \frac{\eps}{3} = \eps.$$

::: pf-proof
Triangle inequality; the first and third terms are $< \eps/3$ by step [](#eps-N-uniform-convergence){.pf-ref} and the middle by step [](#delta-uniform-continuity-fN){.pf-ref}.
:::

:::

::: pf-step
Hence $f$ is uniformly continuous.

::: pf-proof
By step [](#triangle-inequality-bound){.pf-ref}, the $\delta$ of step [](#delta-uniform-continuity-fN){.pf-ref} works uniformly in $x, y$; $\eps > 0$ was arbitrary.
:::

:::

:::

::: pf-qed
This proves (c).
:::

:::

::: {.pf-step #d-is-false}
Statement (d) is false.

::: pf-proof

::: pf-step
Let $E = S^1 = \theset{(x_1, x_2) \in \RR^2 : x_1^2 + x_2^2 = 1}$ (connected), and choose smooth bump functions $\varphi, \psi: \RR \to \RR$ as follows: $\psi \equiv 1$ on $[-1/4, 1/4]$ and $\psi \equiv 0$ outside $(-1/2, 1/2)$; $\varphi'$ is supported in $(-3/4, 3/4)$ with $\int_{-1}^{1} \varphi' = 1$ (so $\varphi(1) - \varphi(-1) = 1$). Define $f(x_1, x_2) = \varphi(x_1) \psi(x_2)$.

::: pf-proof
Such $\varphi, \psi \in C^\infty(\RR)$ exist: take $\varphi$ to be an antiderivative of a nonnegative smooth function supported in $(-3/4, 3/4)$ with integral $1$, and, with $\rho(s) = e^{-1/s}$ for $s > 0$ and $\rho(s) = 0$ for $s \le 0$, take $\psi(x) = \frac{\rho(1/2 - \abs{x})}{\rho(1/2 - \abs{x}) + \rho(\abs{x} - 1/4)}$, whose denominator never vanishes and which is identically $1$ near $0$. Then $f$ is $C^\infty$ on $\RR^2$, hence differentiable on $E$ in every sense.
:::

:::

::: pf-step
Take $x = (1, 0) \in E$ and $y = (-1, 0) \in E$; then $x - y = (2, 0)$.

::: pf-proof
Explicit points.
:::

:::

::: {.pf-step #fx-minus-fy-equals-one}
$f(x) - f(y) = \varphi(1)\psi(0) - \varphi(-1)\psi(0) = \psi(0)(\varphi(1) - \varphi(-1)) = 1 \cdot 1 = 1$.

::: pf-proof
$\psi(0) = 1$ since $0 \in [-1/4, 1/4]$; $\varphi(1) - \varphi(-1) = \int_{-1}^{1} \varphi' = 1$ by the fundamental theorem of calculus.
:::

:::

::: {.pf-step #partial1-f-zero}
For every $z = (z_1, z_2) \in E$, $\partial_1 f(z) = \varphi'(z_1) \psi(z_2) = 0$.

::: pf-proof
If $\abs{z_2} \leq 1/2$, then $\abs{z_1} = \sqrt{1 - z_2^2} \geq \sqrt{3}/2 > 3/4$, so $\varphi'(z_1) = 0$ because $\varphi'$ is supported in $(-3/4, 3/4)$. If $\abs{z_2} > 1/2$, then $\psi(z_2) = 0$.
In both cases the product is $0$.
:::

:::

::: {.pf-step #gradient-dot-difference-zero}
$\nabla f(z) \cdot (x - y) = 2 \partial_1 f(z) + 0 \cdot \partial_2 f(z) = 0$ for every $z \in E$.

::: pf-proof
Substitute $x - y = (2, 0)$ and use step [](#partial1-f-zero){.pf-ref}.
:::

:::

:::

::: pf-qed
By step [](#fx-minus-fy-equals-one){.pf-ref} the left side of $f(x) - f(y) = \nabla f(z)(x - y)$ is $1$, and by step [](#gradient-dot-difference-zero){.pf-ref} the right side is $0$ for every $z \in E$. So no $z \in E$ satisfies the equation, and (d) is false.
:::

:::

::: pf-qed
Steps [](#a-is-false){.pf-ref}, [](#b-is-true){.pf-ref}, [](#c-is-true){.pf-ref}, and [](#d-is-false){.pf-ref} settle parts (a), (b), (c), and (d).
:::

:::
