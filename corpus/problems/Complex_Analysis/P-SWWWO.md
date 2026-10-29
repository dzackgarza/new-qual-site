---
schema: qual/card@1
id: P-SWWWO
kind: problem
title: A $C^1$ function with $F(0,0)=0$ and $\norm{\nabla F(0,0)}<1$ satisfies $\abs{F}<r$
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

::: {.pf-step #c}

There is a constant $c$ with $\norm{\nabla F(0, 0)} < c < 1$.

::: pf-proof

Take $c = \frac{1}{2}\qty(\norm{\nabla F(0, 0)} + 1)$.

:::

:::

::: {.pf-step #ball}

There exists $r > 0$ such that $\norm{\nabla F(u)} \le c$ for all $u \in \RR^2$ with $\norm{u} \le r$.

::: pf-proof

Since $F$ is $C^1$, the map $u \mapsto \norm{\nabla F(u)}$ is continuous on $\RR^2$. By step [](#c){.pf-ref}, the set $\{u \in \RR^2 : \norm{\nabla F(u)} < c\}$ is therefore an open neighborhood of $(0, 0)$, so it contains a closed ball $\{u : \norm{u} \le r\}$ for some $r > 0$.

:::

:::

::: {.pf-step #mvt}

For every $(x, y)$ with $\norm{(x, y)} < r$ there is a point $u_0$ with $\norm{u_0} < r$ and $F(x, y) = \nabla F(u_0) \cdot (x, y)$.

::: pf-proof

For $(x, y) = (0, 0)$ take $u_0 = (0, 0)$; both sides vanish. Otherwise define $g(t) = F(tx, ty)$ for $t \in [0, 1]$. By the chain rule, $g$ is differentiable with $g'(t) = \nabla F(tx, ty) \cdot (x, y)$. By the mean value theorem there is $t_0 \in (0, 1)$ with
$$
F(x, y) = F(x, y) - F(0, 0) = g(1) - g(0) = g'(t_0) = \nabla F(t_0 x, t_0 y) \cdot (x, y).
$$
Put $u_0 = (t_0 x, t_0 y)$; then $\norm{u_0} = t_0 \norm{(x, y)} < r$.

:::

:::

::: pf-step

If $\norm{(x, y)} < r$, then $\abs{F(x, y)} < r$.

::: pf-proof

By step [](#mvt){.pf-ref}, the Cauchy--Schwarz inequality, and step [](#ball){.pf-ref},
$$
\abs{F(x, y)} = \abs{\nabla F(u_0) \cdot (x, y)} \le \norm{\nabla F(u_0)}\, \norm{(x, y)} \le c \norm{(x, y)} < r,
$$
where the last inequality uses $c < 1$ from step [](#c){.pf-ref} and $\norm{(x, y)} < r$.

:::

:::

:::

:::
