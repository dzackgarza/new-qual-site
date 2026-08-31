---
schema: qual/card@1
id: P-UKIC7
kind: problem
title: Differentiable $f\le g$ with $f(x_0)=g(x_0)$ satisfy $f'(x_0)=g'(x_0)$
classification:
  areas:
  - real-analysis
  topics:
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Suppose that $f,g:\mathbb{R}\to\mathbb{R}$ are differentiable, that $f(x)\leq g(x)$ for all $x\in\mathbb{R}$, and that $f(x_0)=g(x_0)$ for some $x_0$.
Prove that $f'(x_0)=g'(x_0)$.
:::
::: {.solution}
<1>1. Reduce to a non-negative function with a minimum at $x_0$.
::: {.proof}
set $h = g - f$; then $h \ge 0$, $h(x_0) = 0$, and $h$ is differentiable with $h' = g' - f'$.
:::
It suffices to show $h'(x_0) = 0$.
<1>2. Right-hand difference quotients of $h$ at $x_0$ are non-negative.
::: {.proof}
for $x > x_0$, $h(x) \ge 0 = h(x_0)$, so $(h(x) - h(x_0))/(x - x_0) \ge 0$; hence the right derivative $h'_+(x_0) = \lim_{x \to x_0^+}\frac{h(x)-h(x_0)}{x-x_0} \ge 0$.
:::
<1>3. Left-hand difference quotients are non-positive.
::: {.proof}
for $x < x_0$, $x - x_0 < 0$ and $h(x) - h(x_0) \ge 0$, so $(h(x)-h(x_0))/(x-x_0) \le 0$; hence $h'_-(x_0) \le 0$.
:::
<1>4. $h'(x_0) = 0$, hence $f'(x_0) = g'(x_0)$.
::: {.proof}
$h$ is differentiable at $x_0$, so $h'(x_0) = h'_+(x_0) = h'_-(x_0)$; by <1>2 and <1>3 this common value satisfies $0 \le h'(x_0) \le 0$, so $h'(x_0) = 0$.
:::
Since $h' = g' - f'$, the claim follows.
<1>5. Q.E.D.
:::
