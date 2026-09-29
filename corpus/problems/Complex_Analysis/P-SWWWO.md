---
schema: qual/card@1
id: P-SWWWO
kind: problem
title: A $C^1$ function with $F(0,0)=0$ and $\|\nabla F(0,0)\|<1$ satisfies $|F|<r$
  on some ball of radius $r$
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $F:\RR^2\to \RR$ be continuously differentiable with $F(0, 0) = 0$ and $\norm{\nabla F(0, 0)} < 1$.

Prove that there is some real number $r> 0$ such that $\abs{F(x, y)} < r$ whenever $\norm{(x, y)} < r$.
:::

::: {.solution}

::: pf

::: pf-step

Choose a constant $c \in \mathbb{R}$ such that $\|\nabla F(0, 0)\| < c < 1$.

::: pf-proof

$\|\nabla F(0, 0)\| < 1$ by hypothesis, so $c = \frac{\|\nabla F(0, 0)\| + 1}{2}$ satisfies the inequality.

:::

:::

::: {.pf-step #s2}

There exists $r > 0$ such that $\|\nabla F(u)\| \le c$ for all $u \in \mathbb{R}^2$ with $\|u\| \le r$.

::: pf-proof

::: pf-step

The function $F$ is $C^1$, so the gradient mapping $\nabla F: \mathbb{R}^2 \to \mathbb{R}^2$ is continuous.

::: pf-proof

definition of continuously differentiable function.

:::

:::

::: pf-step

The Euclidean norm $\|\cdot\|: \mathbb{R}^2 \to \mathbb{R}$ is continuous, so $u \mapsto \|\nabla F(u)\|$ is continuous on $\mathbb{R}^2$.

::: pf-proof

composition of continuous functions.

:::

:::

::: pf-step

Since $\|\nabla F(0, 0)\| < c$, the preimage $\{u \in \mathbb{R}^2 : \|\nabla F(u)\| < c\}$ is an open neighborhood of $(0, 0)$.

::: pf-proof

preimage of the open interval $(-\infty, c)$ under a continuous function.

:::

:::

::: pf-step

Hence there exists a radius $r > 0$ such that the closed ball $\bar{B}_r(0, 0) = \{u \in \mathbb{R}^2 : \|u\| \le r\}$ is contained in this neighborhood.

::: pf-proof

definition of an open set in $\mathbb{R}^2$.

:::

:::

:::

:::

::: {.pf-step #s3}

For any $(x, y) \in \mathbb{R}^2$ with $\|(x, y)\| < r$, $|F(x, y)| < r$.

::: pf-proof

::: pf-step

Fix $(x, y) \neq (0, 0)$ with $\|(x, y)\| < r$ (for $(x, y) = (0, 0)$, $|F(0, 0)| = 0 < r$).

::: pf-proof

case distinction.

:::

:::

::: pf-step

Define the single-variable function $g: [0, 1] \to \mathbb{R}$ by $g(t) = F(t x, t y)$.

::: pf-proof

restriction of $F$ to the line segment from $(0, 0)$ to $(x, y)$.

:::

:::

::: pf-step

$g$ is differentiable on $[0, 1]$ with derivative $g'(t) = \nabla F(t x, t y) \cdot (x, y)$ by the chain rule.

::: pf-proof

multivariable chain rule.

:::

:::

::: pf-step

By the single-variable Mean Value Theorem, there exists $t_0 \in (0, 1)$ such that:
\[
F(x, y) - F(0, 0) = g(1) - g(0) = g'(t_0) = \nabla F(t_0 x, t_0 y) \cdot (x, y).
\]

::: pf-proof

Mean Value Theorem for $g$ on $[0, 1]$.

:::

:::

::: pf-step

The intermediate point $u_0 = (t_0 x, t_0 y)$ satisfies $\|u_0\| = t_0 \|(x, y)\| < \|(x, y)\| < r$.

::: pf-proof

$t_0 \in (0, 1)$ and $\|(x, y)\| < r$.

:::

:::

::: pf-step

By step [](#s2){.pf-ref}, $\|\nabla F(u_0)\| \le c$.

::: pf-proof

$\|u_0\| < r$.

:::

:::

::: pf-step

Applying the Cauchy–Schwarz inequality to the dot product gives:
\[
|F(x, y)| = |F(x, y) - F(0, 0)| = |\nabla F(u_0) \cdot (x, y)| \le \|\nabla F(u_0)\| \|(x, y)\| \le c \|(x, y)\|.
\]

::: pf-proof

Cauchy–Schwarz inequality in $\mathbb{R}^2$ and $F(0, 0) = 0$.

:::

:::

::: pf-step

Since $c < 1$ and $\|(x, y)\| < r$, we have:
\[
|F(x, y)| \le c \|(x, y)\| < c r < r.
\]

::: pf-proof

$c < 1$ and $r > 0$.

:::

:::

:::

:::

::: pf-step

Conclusion: There exists $r > 0$ such that $|F(x, y)| < r$ whenever $\|(x, y)\| < r$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

Q.E.D.
:::
