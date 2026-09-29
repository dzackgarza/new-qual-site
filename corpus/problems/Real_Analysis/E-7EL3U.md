---
schema: qual/card@1
id: E-7EL3U
kind: problem
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

::: {.exercise}
- Show that

  - $f_n: [a, b]\to \RR$ are continuously differentiable with derivatives $f_n'$

  - The sequence of derivatives $f_n'$ converges uniformly to some function $g$

  - There exists *at least one* point $x_0$ such that $\lim_n f_n(x_0)$ exists,

  - Then $f_n \to f$ uniformly to some differentiable $f$, and $f' = g$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$g$ is continuous on $[a,b]$.

::: pf-proof

$g$ is the uniform limit of the continuous functions $f_n'$.

:::

:::

::: {.pf-step #s2}

For every $x \in [a,b]$, $f_n(x) = f_n(x_0) + \int_{x_0}^x f_n'(t) \, dt$.

::: pf-proof

This is the fundamental theorem of calculus, since $f_n$ is continuously differentiable.

:::

:::

::: {.pf-step #s3}

Let $c = \lim_n f_n(x_0)$ and $f(x) \coloneqq c + \int_{x_0}^x g(t)\,dt$. Then $f_n \to f$ uniformly on $[a,b]$.

::: pf-proof

The limit $c$ exists by hypothesis, and $f$ is defined because $g$ is continuous by step [](#s1){.pf-ref}.
By step [](#s2){.pf-ref}, for every $x \in [a,b]$,
$$
\abs{f_n(x) - f(x)} \leq \abs{f_n(x_0) - c} + \abs{\int_{x_0}^x (f_n'(t) - g(t))\,dt} \leq \abs{f_n(x_0) - c} + (b-a)\norm{f_n' - g}_\infty,
$$
and the right-hand side does not depend on $x$ and tends to $0$.

:::

:::

::: {.pf-step #s4}

$f$ is differentiable and $f' = g$.

::: pf-proof

Since $g$ is continuous by step [](#s1){.pf-ref}, the fundamental theorem of calculus applied to $f(x) = c + \int_{x_0}^x g(t)\,dt$ gives $f'(x) = g(x)$ for every $x \in [a,b]$. In particular $f \in C^1[a,b]$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives $f_n \to f$ uniformly, and step [](#s4){.pf-ref} gives that $f$ is differentiable with $f' = g$.

:::

:::

:::
