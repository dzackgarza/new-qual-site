---
schema: qual/card@1
id: P-ZAS5Z
kind: problem
title: $x^{1/3}(1+xy)^{-3/2}$ on $\{0\le x\le y\}$ is in $L^1(\RR^2)$
classification:
  areas:
  - real-analysis
  topics:
  - fubini-tonelli
  - integrals
  - l1
relations: []
review: draft
solved: true
---

::: problem
Define
$$
f(x, y):=\left\{\begin{array}{ll}{\frac{x^{1 / 3}}{(1+x y)^{3 / 2}}} & {\text { if } 0 \leq x \leq y} \\ {0} & {\text { otherwise }}\end{array}\right.
$$

Carefully show that $f \in L^1(\RR^2)$.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. $f$ is measurable.
Proof: $f$ is given by a rational expression on the measurable region $\{0 \le x \le y\}$ and is $0$ elsewhere; rational functions are continuous (hence measurable) on their domain.

<1>2. Compute the integral by Tonelli: $\int_{\RR^2}|f| = \int_0^\infty\int_x^\infty \frac{x^{1/3}}{(1+xy)^{3/2}}\,dy\,dx$.
Proof: $|f| = f \ge 0$ on the region $0 \le x \le y$ and $0$ elsewhere, so Tonelli allows iterating; the region is $\{(x,y) : x \ge 0, y \ge x\}$.

<1>3. The inner integral is $\int_x^\infty \frac{x^{1/3}}{(1+xy)^{3/2}}\,dy = 2x^{-2/3}(1 + x^2)^{-1/2}$.
Proof: substitute $u = 1 + xy$, $du = x\,dy$: $\int_x^\infty \frac{x^{1/3}}{(1+xy)^{3/2}}\,dy = x^{1/3}\int_{1+x^2}^\infty u^{-3/2}\frac{du}{x} = x^{-2/3}\cdot 2(1+x^2)^{-1/2}$.

<1>4. $\int_0^\infty 2x^{-2/3}(1+x^2)^{-1/2}\,dx < \infty$.
Proof: near $0$ the integrand is $\sim 2x^{-2/3}$, integrable since $-2/3 > -1$; near $\infty$ it is $\sim 2x^{-5/3}$, integrable since $-5/3 < -1$.

<1>5. Q.E.D. Proof: <1>1, <1>2, and <1>4 show $\int|f| < \infty$ with the value $2\int_0^\infty \frac{x^{-2/3}}{(1+x^2)^{1/2}}\,dx$, so $f \in L^1(\RR^2)$.
:::
