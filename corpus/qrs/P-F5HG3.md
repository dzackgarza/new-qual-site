---
schema: qual/card@1
id: P-F5HG3
kind: problem
title: "Let $f, g \\in L^1(\\RR)$ be Borel measurable."
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - l1
  - fubini-tonelli
relations: []
review: draft
solved: true
---

::: problem
Let $f, g \in L^1(\RR)$ be Borel measurable.

1. Show that

- The function $$F(x, y) \definedas f(x-y) g(y)$$ is Borel measurable on $\RR^2$, and

- For almost every $y\in \RR$, $$F_y(x) \definedas f(x-y)g(y)$$ is integrable with respect to $y$.

2. Show that $f\ast g \in L^1(\RR)$ and
\[
\|f * g\|_{1} \leq \|f\|_{1} \|g\|_{1}
\]
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $F(x,y) = f(x - y)g(y)$ is Borel measurable on $\RR^2$.
<2>1. The map $(x,y) \mapsto (x - y, y)$ is continuous, hence Borel measurable.
Proof: continuity of subtraction and projection.
<2>2. The map $(u,y) \mapsto f(u)g(y)$ is Borel measurable on $\RR^2$.
Proof: $f$ and $g$ are Borel, so $(u,y) \mapsto f(u)$ and $(u,y) \mapsto g(y)$ are Borel (compositions with coordinate projections), and their product is Borel.
<2>3. Q.E.D. Proof: $F$ is the composition of the maps in <2>1 and <2>2.

<1>2. For every $y \in \RR$ (a fortiori a.e.), $F_y(x) = f(x - y)g(y)$ is integrable with respect to $x$, with $\int |F_y(x)|\,dx = |g(y)|\,\|f\|_1$.
Proof: translation invariance of the integral: $\int |f(x - y)|\,dx = \int |f(u)|\,du = \|f\|_1$, and $|g(y)|$ is a constant for fixed $y$.

<1>3. $f \ast g \in L^1(\RR)$ and $\|f \ast g\|_1 \le \|f\|_1\|g\|_1$.
<2>1. $|f \ast g(x)| \le \int |f(x - y)||g(y)|\,dy$ for every $x$.
Proof: triangle inequality on the defining integral.
<2>2. $\int_\RR\int_\RR |f(x - y)||g(y)|\,dy\,dx = \|f\|_1\|g\|_1$.
Proof: Tonelli (non-negative integrand, measurable by <1>1 applied to $|f|, |g|$): $\int\int|f(x-y)||g(y)|dx\,dy = \int |g(y)|\left(\int|f(x-y)|dx\right)dy = \int|g(y)|\|f\|_1\,dy = \|f\|_1\|g\|_1$, using <1>2. <2>3. Q.E.D. Proof: <2>1 and <2>2 give $\int|f\ast g| \le \|f\|_1\|g\|_1 < \infty$, so $f \ast g \in L^1$ with the claimed norm bound.
:::
