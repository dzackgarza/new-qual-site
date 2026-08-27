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

::: problem
Prove or disprove each of the following statements.

(a) If $f$ is of bounded variation on $[0,1]$, then it is continuous on $[0,1]$.

(b) If $f : [0, 1] \to [0, 1]$ is a continuous function, then there exists $x_0 \in [0, 1]$ such that $f(x_0) = x_0$.

(c) Let $\{f_n\}$ be a sequence of uniformly continuous functions on an interval $I$.
If $\{f_n\}$ converges uniformly to a function $f$ on $I$, then $f$ is also uniformly continuous on $I$.

(d) If $f$ is differentiable on a connected set $E \subset \mathbb{R}^n$, then for any $x, y \in E$, there exists $z \in E$ such that $f(x) - f(y) = \nabla f(z)(x - y)$.
:::

::: {.solution}
**Goal:** Prove or disprove each of (a)–(d).

<1>1. Statement (a) is FALSE. <2>1. Counterexample: the step function $f(x) = 0$ on $[0, 1/2]$ and $f(x) = 1$ on $(1/2, 1]$.
Proof: Explicit function.
<2>2. $f$ has bounded variation on $[0,1]$.
Proof: For any partition $0 = x_0 < \dots < x_k = 1$, all increments $\abs{f(x_j) - f(x_{j-1})}$ vanish except the single one crossing $1/2$, which is $\leq 1$; hence the total variation is $\leq 1$.
<2>3. $f$ is not continuous at $1/2$.
Proof: $\lim_{x \to 1/2^-} f(x) = 0 \neq 1 = f(1/2)$.
<2>4. Q.E.D. Proof: This disproves (a).

<1>2. Statement (b) is TRUE. <2>1. Define $g(x) \definedas f(x) - x$ on $[0,1]$; then $g$ is continuous, $g(0) = f(0) \geq 0$, and $g(1) = f(1) - 1 \leq 0$.
Proof: $f: [0,1] \to [0,1]$, so $f(0) \in [0,1]$ and $f(1) \in [0,1]$; continuity of $g$ follows from continuity of $f$.
<2>2. By the intermediate value theorem, there is $x_0 \in [0,1]$ with $g(x_0) = 0$, i.e. $f(x_0) = x_0$.
Proof: IVT applied to $g$: $0$ lies between $g(0) \geq 0$ and $g(1) \leq 0$.
<2>3. Q.E.D. Proof: This proves (b).

<1>3. Statement (c) is TRUE. <2>1. Fix $\eps > 0$.
Since $f_n \to f$ uniformly on $I$, there is $N$ with $\norm{f_n - f}_\infty < \eps/3$ for all $n \geq N$.
Proof: Definition of uniform convergence.
<2>2. $f_N$ is uniformly continuous, so there is $\delta > 0$ with $\abs{f_N(x) - f_N(y)} < \eps/3$ whenever $x, y \in I$ and $\abs{x - y} < \delta$.
Proof: Definition of uniform continuity of $f_N$.
<2>3. For $x, y \in I$ with $\abs{x - y} < \delta$, $$\abs{f(x) - f(y)} \leq \abs{f(x) - f_N(x)} + \abs{f_N(x) - f_N(y)} + \abs{f_N(y) - f(y)} < \frac{\eps}{3} + \frac{\eps}{3} + \frac{\eps}{3} = \eps.$$ Proof: Triangle inequality; the first and third terms are $< \eps/3$ by <2>1 and the middle by <2>2. <2>4. Hence $f$ is uniformly continuous.
Proof: By <2>3, the $\delta$ of <2>2 works uniformly in $x, y$; $\eps > 0$ was arbitrary.
<2>5. Q.E.D. Proof: This proves (c).

<1>4. Statement (d) is FALSE. <2>1. Counterexample setup: let $E = S^1 = \theset{(x_1, x_2) \in \RR^2 : x_1^2 + x_2^2 = 1}$ (connected), and choose smooth bump functions $\varphi, \psi: \RR \to \RR$ as follows: $\psi \equiv 1$ on $[-1/4, 1/4]$ and $\psi \equiv 0$ outside $(-1/2, 1/2)$; $\varphi'$ is supported in $(-3/4, 3/4)$ with $\int_{-1}^{1} \varphi' = 1$ (so $\varphi(1) - \varphi(-1) = 1$). Define $f(x_1, x_2) = \varphi(x_1) \psi(x_2)$.
Proof: Such bumps exist in $C^\infty(\RR)$ by standard constructions; $f$ is $C^\infty$ on $\RR^2$, hence differentiable on $E$ in every sense.
<2>2. Take $x = (1, 0) \in E$ and $y = (-1, 0) \in E$; then $x - y = (2, 0)$.
Proof: Explicit points.
<2>3. $f(x) - f(y) = \varphi(1)\psi(0) - \varphi(-1)\psi(0) = \psi(0)(\varphi(1) - \varphi(-1)) = 1 \cdot 1 = 1$.
Proof: $\psi(0) = 1$ since $0 \in [-1/4, 1/4]$; $\varphi(1) - \varphi(-1) = \int_{-1}^{1} \varphi' = 1$ by the fundamental theorem of calculus.
<2>4. For every $z = (z_1, z_2) \in E$, $\partial_1 f(z) = \varphi'(z_1) \psi(z_2) = 0$.
Proof: Two cases.
If $\abs{z_2} \leq 1/2$, then $\abs{z_1} = \sqrt{1 - z_2^2} \geq \sqrt{3}/2 > 3/4$, so $\varphi'(z_1) = 0$ (support of $\varphi'$ is inside $(-3/4, 3/4)$). If $\abs{z_2} > 1/2$, then $\psi(z_2) = 0$.
In both cases the product is $0$.
<2>5. Hence $\nabla f(z) \cdot (x - y) = 2 \partial_1 f(z) + 0 \cdot \partial_2 f(z) = 0$ for every $z \in E$.
Proof: Substitute $x - y = (2, 0)$ and use <2>4. <2>6. No $z \in E$ satisfies $f(x) - f(y) = \nabla f(z)(x - y)$, since the left side is $1$ (<2>3) and the right side is $0$ for all $z \in E$ (<2>5). Proof: $1 \neq 0$.
<2>7. Q.E.D. Proof: This disproves (d).
:::
