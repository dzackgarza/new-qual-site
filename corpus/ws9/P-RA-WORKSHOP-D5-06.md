---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-06
kind: problem
title: 'Equality at a point under an order bound forces equal derivatives'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(June 2007 #3a) Suppose that $f,g:\mathbb R\to\mathbb R$ are differentiable, that $f(x)\le g(x)$ for all $x\in\mathbb R$, and that $f(x_0)=g(x_0)$ for some $x_0$.
Prove that $f'(x_0)=g'(x_0)$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. Reduce to $h = g - f \ge 0$ with $h(x_0) = 0$.
Proof: $h$ is differentiable (difference of differentiable functions), $h(x) \ge 0$ for all $x$, and $h(x_0) = g(x_0) - f(x_0) = 0$.
So $h$ attains its global minimum at $x_0$.
<1>2. $h'(x_0) = 0$.
Proof: since $h$ has a local minimum at $x_0$ and $h$ is differentiable at $x_0$, the derivative vanishes: for $t < 0$ small, $\frac{h(x_0 + t) - h(x_0)}{t} = \frac{h(x_0+t)}{t} \le 0$ (numerator $\ge 0$, denominator $< 0$), so the left-hand derivative is $\le 0$; for $t > 0$ the quotient is $\ge 0$, so the right-hand derivative is $\ge 0$; both equal $h'(x_0)$, hence $h'(x_0) = 0$.
<1>3. Conclude.
Proof: $f'(x_0) = g'(x_0) - h'(x_0) = g'(x_0)$.
<1>4. Q.E.D.
:::
