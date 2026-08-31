---
schema: qual/card@1
id: E-7EL3U
kind: exercise
title: If $f_n\in C^1[a,b]$ with $f_n'\to g$ uniformly and $f_n(x_0)$ convergent,
  then $f_n\to f$ uniformly with $f'=g$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Show that

  - $f_n: [a, b]\to \RR$ are continuously differentiable with derivatives $f_n'$

  - The sequence of derivatives $f_n'$ converges uniformly to some function $g$

  - There exists *at least one* point $x_0$ such that $\lim_n f_n(x_0)$ exists,

  - Then $f_n \to f$ uniformly to some differentiable $f$, and $f' = g$.
:::

::: {.solution}
**Goal:** Show that if $f_n \in C^1[a,b]$, the derivatives $f_n'$ converge uniformly to some $g$, and $f_n(x_0)$ converges for some $x_0 \in [a,b]$, then $f_n \to f$ uniformly, $f$ is differentiable, and $f' = g$.

<1>1. $f_n \to f$ uniformly for some continuous $f$.
<2>1. For every $x \in [a,b]$, $f_n(x) = f_n(x_0) + \int_{x_0}^x f_n'(t) \, dt$.
::: {.proof}
the Fundamental Theorem of Calculus, since $f_n$ is continuously differentiable.
:::
<2>2. $f_n(x_0)$ converges to some real number $c$.
::: {.proof}
hypothesis: $\lim_n f_n(x_0)$ exists.
:::
<2>3. $\int_{x_0}^x f_n'(t) \, dt \to \int_{x_0}^x g(t) \, dt$ uniformly in $x$.
::: {.proof}
$\left|\int_{x_0}^x (f_n'(t) - g(t))\,dt\right| \leq \|f_n' - g\|_\infty |x - x_0| \leq \|f_n' - g\|_\infty (b - a) \to 0$ by uniform convergence of the derivatives.
:::
<2>4. Define $f(x) := c + \int_{x_0}^x g(t)\,dt$; then $f_n \to f$ uniformly.
::: {.proof}
by <2>1–<2>3, $\|f_n - f\|_\infty \leq |f_n(x_0) - c| + (b-a)\|f_n' - g\|_\infty \to 0$.
:::
<2>5. $f$ is continuous.
::: {.proof}
$f$ is the uniform limit of the continuous functions $f_n$ (or directly: an indefinite integral of a continuous function).
:::

<1>2. $f$ is differentiable and $f' = g$.
<2>1. $g$ is continuous.
::: {.proof}
$g$ is the uniform limit of the continuous functions $f_n'$.
:::
<2>2. $f'(x) = g(x)$ for every $x \in [a,b]$.
::: {.proof}
by the Fundamental Theorem of Calculus applied to $f(x) = c + \int_{x_0}^x g(t)\,dt$ with $g$ continuous: $f$ is differentiable and $f' = g$.
:::
(In particular $f \in C^1[a,b]$.)
<2>3. Q.E.D.
::: {.proof}
<1>4 and <2>2 give the uniform convergence, differentiability, and $f' = g$.
:::
:::
