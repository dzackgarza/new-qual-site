---
schema: qual/card@1
id: P-6LWY3
kind: problem
title: Pointwise convergence of $n^\beta x(1-x^2)^n$ on $[0,1]$, uniform if and only
  if $\beta<\frac12$
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $f_n(x) = n^\beta x(1-x^2)^n$, $x \in [0,1]$, $n \in \mathbb{N}$.

Prove that $\{f_n\}_{n=1}^\infty$ converges pointwise on $[0,1]$ for every $\beta \in \mathbb{R}$.

Show that the convergence in part (a) is uniform for all $\beta < \frac{1}{2}$, but not uniform for any $\beta \geq \frac{1}{2}$.
:::

::: {.solution}
<1>1. $f_n \to 0$ pointwise on $[0,1]$ for every $\beta \in \RR$.
<2>1. For $x = 0$: $f_n(0) = 0$ for all $n$.
Proof: the factor $x$ vanishes.
<2>2. For $0 < x \le 1$: $f_n(x) = n^\beta x(1 - x^2)^n \to 0$.
Proof: $(1 - x^2)^n$ decays exponentially in $n$ for $x > 0$ ($1 - x^2 \in [0,1)$), which beats the polynomial growth $n^\beta$; more precisely $n^\beta(1-x^2)^n = n^\beta e^{n\ln(1-x^2)} \to 0$ since $\ln(1 - x^2) < 0$.
<2>3. Q.E.D. Proof: <2>1 and <2>2.

<1>2. $\sup_{x \in [0,1]}|f_n(x)| = n^\beta \cdot \frac{1}{\sqrt{2n+1}}\left(\frac{2n}{2n+1}\right)^n$.
<2>1. Maximize $g(x) = x(1 - x^2)^n$: $g'(x) = (1 - x^2)^{n-1}(1 - (2n+1)x^2)$, so the maximum on $[0,1]$ is at $x_n = 1/\sqrt{2n+1}$.
Proof: derivative computation; $g' > 0$ for $x < x_n$ and $g' < 0$ for $x > x_n$; $g(0) = g(1) = 0$.
<2>2. $g(x_n) = \frac{1}{\sqrt{2n+1}}\left(1 - \frac{1}{2n+1}\right)^n = \frac{1}{\sqrt{2n+1}}\left(\frac{2n}{2n+1}\right)^n$.
Proof: $1 - x_n^2 = 1 - \frac{1}{2n+1} = \frac{2n}{2n+1}$.
<2>3. Q.E.D. Proof: $\|f_n\|_\infty = n^\beta g(x_n)$.

<1>3. Uniform convergence holds iff $\beta < \frac{1}{2}$.
<2>1. $\|f_n\|_\infty \asymp n^{\beta - 1/2}$: $\|f_n\|_\infty = n^\beta \cdot \frac{1}{\sqrt{2n+1}}\left(\frac{2n}{2n+1}\right)^n$, and $\left(\frac{2n}{2n+1}\right)^n = \left(1 - \frac{1}{2n+1}\right)^n \to e^{-1/2} > 0$.
Proof: $\frac{1}{\sqrt{2n+1}} \sim \frac{1}{\sqrt 2}n^{-1/2}$; the factor $\left(\frac{2n}{2n+1}\right)^n$ has a positive limit $e^{-1/2}$.
<2>2. If $\beta < 1/2$: $\|f_n\|_\infty \to 0$, so $f_n \to 0$ uniformly.
Proof: $n^{\beta - 1/2} \to 0$.
<2>3. If $\beta \ge 1/2$: $\|f_n\|_\infty \not\to 0$, so the convergence is not uniform.
Proof: $n^{\beta - 1/2} \not\to 0$ (it diverges for $\beta > 1/2$ and is bounded away from $0$ for $\beta = 1/2$), and uniform convergence to the pointwise limit $0$ would force $\|f_n\|_\infty \to 0$.
<2>4. Q.E.D. Proof: <2>2 and <2>3.
:::
