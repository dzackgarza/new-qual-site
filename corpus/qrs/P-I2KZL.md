---
schema: qual/card@1
id: P-I2KZL
kind: problem
title: "Prove that $f(z) = \\abs{z}^2$ has a derivative at $z=0$ and nowhere else."
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-riemann
  - holomorphic-functions
  - counterexamples
relations: []
review: draft
solved: true
---

::: problem
Prove that $f(z) = \abs{z}^2$ has a derivative at $z=0$ and nowhere else.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that $f(z) = \abs z^2$ is complex-differentiable at $z = 0$ and at no other point of $\CC$.

<1>1. $f$ is differentiable at $z = 0$, with $f'(0) = 0$.
<2>1. Write the difference quotient: $\frac{f(h) - f(0)}{h} = \frac{\abs h^2}{h} = \frac{h\bar h}{h} = \bar h$ for $h \neq 0$.
Proof: $\abs h^2 = h\bar h$.
<2>2. $\bar h \to 0$ as $h \to 0$.
Proof: $\abs{\bar h} = \abs h \to 0$.
<2>3. Hence the limit exists and equals $0$.
Proof: <2>1 and <2>2.

<1>2. Fix $z_0 \neq 0$ and compute the difference quotient at $z_0$.
<2>1. $\frac{f(z_0 + h) - f(z_0)}{h} = z_0 \frac{\bar h}{h} + \bar z_0 + \bar h$ for $h \neq 0$.
Proof: $\abs{z_0 + h}^2 - \abs{z_0}^2 = (z_0 + h)(\bar z_0 + \bar h) - z_0\bar z_0 = z_0 \bar h + \bar z_0 h + \abs h^2$; divide by $h$.
<2>2. $\frac{\bar h}{h}$ has no limit as $h \to 0$.
Proof: For $h = re^{i\theta}$, $\bar h/h = e^{-2i\theta}$ depends on the direction $\theta$; e.g. taking $h$ real gives $1$ while taking $h$ purely imaginary gives $-1$.
<2>3. The difference quotient has no limit.
Proof: As $h \to 0$, the terms $\bar z_0 + \bar h$ converge to $\bar z_0$, but the term $z_0 \cdot \bar h/h$ (with $z_0 \neq 0$) fails to converge by <2>2; the sum of a convergent and a divergent quantity is divergent.

<1>3. Q.E.D. Proof: <1>1 shows differentiability at $0$; <1>2 shows failure of differentiability at every $z_0 \neq 0$.
:::
