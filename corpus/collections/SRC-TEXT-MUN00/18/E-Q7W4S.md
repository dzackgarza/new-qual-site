---
schema: qual/card@1
id: E-Q7W4S
kind: problem
title: Separate continuity does not imply continuity
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $F: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ be defined by the equation

$$
F(x \times y) =
\begin{cases}
xy/(x^2 + y^2) & \text{if } x \times y \neq 0 \times 0, \\
0 & \text{if } x \times y = 0 \times 0.
\end{cases}
$$

(a) Show that $F$ is continuous in each variable separately.

(b) Compute the function $g: \mathbb{R} \to \mathbb{R}$ defined by $g(x) = F(x \times x)$.

(c) Show that $F$ is not continuous.
:::

::: {.solution}
(a) Fix $x_0\in\mathbb R$. If $x_0=0$, then
\[
y\longmapsto F(0,y)
\]
is identically zero, hence continuous. If $x_0\ne0$, then
\[
y\longmapsto \frac{x_0y}{x_0^2+y^2}
\]
is an ordinary continuous rational function, since the denominator never vanishes. Thus $F$ is continuous in the second variable with the first fixed. The same argument, by symmetry, proves continuity in the first variable with the second fixed.

(b) Along the diagonal,
\[
g(x)=F(x,x)=
\begin{cases}
\frac12,&x\ne0,\\
0,&x=0.
\end{cases}
\]

(c) The diagonal map $d:\mathbb R\to\mathbb R^2$, $d(x)=(x,x)$, is continuous. If $F$ were continuous, then $g=F\circ d$ would be continuous. But $g(x)=1/2$ for all $x\ne0$ and $g(0)=0$, so $g$ is discontinuous at $0$. Hence $F$ is not continuous.
:::
