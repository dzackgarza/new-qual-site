---
schema: qual/card@1
id: P-HCAX13
kind: problem
title: Boundary signs constrain linear combinations of harmonic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Principle
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $f_1,\ldots,f_n$ be harmonic on the unit disk and continuous on its closure.
Show that no linear combination of the $f_i$ can be negative on the boundary and positive at an interior point.
:::

::: {.solution}
<1>1. Any linear combination $u = \sum_{k=1}^n c_k f_k$ is harmonic on $\mathbb{D}$ and continuous on $\overline{\mathbb{D}}$: <2>1. Let $c_1, \dots, c_n \in \mathbb{R}$ and define $u(z) = \sum_{k=1}^n c_k f_k(z)$.
::: {.proof}
definition of linear combination.
:::
<2>2. The Laplacian $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ is a linear differential operator:
\[
\Delta u = \sum_{k=1}^n c_k \Delta f_k = \sum_{k=1}^n c_k \cdot 0 = 0.
\]
::: {.proof}
linearity of differentiation and harmonicity of each $f_k$.
:::
<2>3. Since each $f_k$ is continuous on $\overline{\mathbb{D}}$, the finite linear combination $u$ is continuous on the compact set $\overline{\mathbb{D}}$.
::: {.proof}
linear combinations of continuous functions are continuous.
:::

<1>2. Apply the Maximum Principle for harmonic functions: <2>1. Suppose for contradiction that $u(z) < 0$ (or $u(z) \le 0$) for all $z \in \partial\mathbb{D}$, and that $u(z_0) > 0$ for some interior point $z_0 \in \mathbb{D}$.
::: {.proof}
proof by contradiction setup.
:::
<2>2. By the Extreme Value Theorem, the continuous function $u$ attains a maximum on the compact set $\overline{\mathbb{D}}$ at some point $w \in \overline{\mathbb{D}}$:
\[
u(w) = \max_{z \in \overline{\mathbb{D}}} u(z) \ge u(z_0) > 0.
\]
::: {.proof}
Extreme Value Theorem.
:::
<2>3. Since $u(z) \le 0$ for all $z \in \partial\mathbb{D}$ and $u(w) > 0$, the maximum point $w$ cannot lie on the boundary $\partial\mathbb{D}$.
Thus $w \in \mathbb{D}$.
::: {.proof}
$u(w) > 0 \ge \sup_{z\in\partial\mathbb{D}} u(z)$.
:::
<2>4. By the Strong Maximum Principle for harmonic functions on connected domains, if $u$ attains a global maximum at an interior point $w \in \mathbb{D}$, then $u$ must be identically constant on $\mathbb{D}$.
::: {.proof}
Strong Maximum Principle for harmonic functions.
:::
<2>5. If $u(z) = C$ is constant on $\mathbb{D}$ with $C = u(w) > 0$, then by continuity on $\overline{\mathbb{D}}$, $u(z) = C > 0$ for all $z \in \partial\mathbb{D}$.
::: {.proof}
boundary value of a continuous constant function.
:::
<2>6. This contradicts the hypothesis that $u < 0$ (or $u \le 0$) on $\partial\mathbb{D}$.
::: {.proof}
$C > 0$ contradicts $C \le 0$.
:::

<1>3. Conclusion: No linear combination of $f_1, \dots, f_n$ can be negative on the boundary $\partial\mathbb{D}$ and positive at an interior point of $\mathbb{D}$.
::: {.proof}
<1>2.
:::
Q.E.D.
:::
