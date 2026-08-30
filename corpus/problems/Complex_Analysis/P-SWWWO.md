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

::: problem
Let $F:\RR^2\to \RR$ be continuously differentiable with $F(0, 0) = 0$ and $\norm{\nabla F(0, 0)} < 1$.

Prove that there is some real number $r> 0$ such that $\abs{F(x, y)} < r$ whenever $\norm{(x, y)} < r$.
:::

::: {.solution}
<1>1. Choose a constant $c \in \mathbb{R}$ such that $\|\nabla F(0, 0)\| < c < 1$.
Proof: $\|\nabla F(0, 0)\| < 1$ by hypothesis, so $c = \frac{\|\nabla F(0, 0)\| + 1}{2}$ satisfies the inequality.

<1>2. There exists $r > 0$ such that $\|\nabla F(u)\| \le c$ for all $u \in \mathbb{R}^2$ with $\|u\| \le r$.
<2>1. The function $F$ is $C^1$, so the gradient mapping $\nabla F: \mathbb{R}^2 \to \mathbb{R}^2$ is continuous.
Proof: definition of continuously differentiable function.
<2>2. The Euclidean norm $\|\cdot\|: \mathbb{R}^2 \to \mathbb{R}$ is continuous, so $u \mapsto \|\nabla F(u)\|$ is continuous on $\mathbb{R}^2$.
Proof: composition of continuous functions.
<2>3. Since $\|\nabla F(0, 0)\| < c$, the preimage $\{u \in \mathbb{R}^2 : \|\nabla F(u)\| < c\}$ is an open neighborhood of $(0, 0)$.
Proof: preimage of the open interval $(-\infty, c)$ under a continuous function.
<2>4. Hence there exists a radius $r > 0$ such that the closed ball $\bar{B}_r(0, 0) = \{u \in \mathbb{R}^2 : \|u\| \le r\}$ is contained in this neighborhood.
Proof: definition of an open set in $\mathbb{R}^2$.

<1>3. For any $(x, y) \in \mathbb{R}^2$ with $\|(x, y)\| < r$, $|F(x, y)| < r$.
<2>1. Fix $(x, y) \neq (0, 0)$ with $\|(x, y)\| < r$ (for $(x, y) = (0, 0)$, $|F(0, 0)| = 0 < r$).
Proof: case distinction.
<2>2. Define the single-variable function $g: [0, 1] \to \mathbb{R}$ by $g(t) = F(t x, t y)$.
Proof: restriction of $F$ to the line segment from $(0, 0)$ to $(x, y)$.
<2>3. $g$ is differentiable on $[0, 1]$ with derivative $g'(t) = \nabla F(t x, t y) \cdot (x, y)$ by the chain rule.
Proof: multivariable chain rule.
<2>4. By the single-variable Mean Value Theorem, there exists $t_0 \in (0, 1)$ such that:
\[
F(x, y) - F(0, 0) = g(1) - g(0) = g'(t_0) = \nabla F(t_0 x, t_0 y) \cdot (x, y).
\]
Proof: Mean Value Theorem for $g$ on $[0, 1]$.
<2>5. The intermediate point $u_0 = (t_0 x, t_0 y)$ satisfies $\|u_0\| = t_0 \|(x, y)\| < \|(x, y)\| < r$.
Proof: $t_0 \in (0, 1)$ and $\|(x, y)\| < r$.
<2>6. By <1>2, $\|\nabla F(u_0)\| \le c$.
Proof: $\|u_0\| < r$.
<2>7. Applying the Cauchy–Schwarz inequality to the dot product gives:
\[
|F(x, y)| = |F(x, y) - F(0, 0)| = |\nabla F(u_0) \cdot (x, y)| \le \|\nabla F(u_0)\| \|(x, y)\| \le c \|(x, y)\|.
\]
Proof: Cauchy–Schwarz inequality in $\mathbb{R}^2$ and $F(0, 0) = 0$.
<2>8. Since $c < 1$ and $\|(x, y)\| < r$, we have:
\[
|F(x, y)| \le c \|(x, y)\| < c r < r.
\]
Proof: $c < 1$ and $r > 0$.

<1>4. Conclusion:
There exists $r > 0$ such that $|F(x, y)| < r$ whenever $\|(x, y)\| < r$. Q.E.D.
Proof: <1>2 and <1>3.
:::
