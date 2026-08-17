---
schema: qual/card@1
id: P-UKIC7
kind: problem
title: "Suppose that $f,g:\\mathbb{R}\\to\\mathbb{R}$ are"
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Suppose that $f,g:\mathbb{R}\to\mathbb{R}$ are differentiable, that $f(x)\leq g(x)$ for all $x\in\mathbb{R}$, and that $f(x_0)=g(x_0)$ for some $x_0$.
Prove that $f'(x_0)=g'(x_0)$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to a non-negative function with a minimum at $x_0$.
Proof: set $h = g - f$; then $h \ge 0$, $h(x_0) = 0$, and $h$ is differentiable with $h' = g' - f'$.
It suffices to show $h'(x_0) = 0$.
<1>2. Right-hand difference quotients of $h$ at $x_0$ are non-negative.
Proof: for $x > x_0$, $h(x) \ge 0 = h(x_0)$, so $(h(x) - h(x_0))/(x - x_0) \ge 0$; hence the right derivative $h'_+(x_0) = \lim_{x \to x_0^+}\frac{h(x)-h(x_0)}{x-x_0} \ge 0$.
<1>3. Left-hand difference quotients are non-positive.
Proof: for $x < x_0$, $x - x_0 < 0$ and $h(x) - h(x_0) \ge 0$, so $(h(x)-h(x_0))/(x-x_0) \le 0$; hence $h'_-(x_0) \le 0$.
<1>4. $h'(x_0) = 0$, hence $f'(x_0) = g'(x_0)$.
Proof: $h$ is differentiable at $x_0$, so $h'(x_0) = h'_+(x_0) = h'_-(x_0)$; by <1>2 and <1>3 this common value satisfies $0 \le h'(x_0) \le 0$, so $h'(x_0) = 0$.
Since $h' = g' - f'$, the claim follows.
<1>5. Q.E.D.
:::
