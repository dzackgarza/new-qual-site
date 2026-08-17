---
schema: qual/card@1
id: P-RA-WORKSHOP-D8-SEQ2
kind: problem
title: 'Uniform convergence of a variable-ratio geometric series on bounded intervals'
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
  - series-of-functions
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Show that the infinite series
$$
\sum_{n=0}^{\infty}x^n2^{-nx}
$$
converges uniformly on $[0,B]$ for any $B>0$.
Does this series converge uniformly on $[0,\infty)$?
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Show $\sum_{n=0}^\infty x^n2^{-nx}$ converges uniformly on $[0,B]$ for each $B > 0$; decide uniform convergence on $[0, \infty)$.

<1>1. Pointwise: the series is geometric with ratio $x2^{-x}$, so it converges on $[0, \infty)$.
Proof: for $x \ge 0$, $x^n2^{-nx} = (x2^{-x})^n$.
At $x = 0$ the terms are $1, 0, 0, \ldots$; for $x > 0$, $0 < x2^{-x} < 1$ (since $x2^{-x} = x/2^x$ and $2^x > x$ for $x > 0$), so $\sum (x2^{-x})^n$ converges to $\frac{1}{1 - x2^{-x}}$.

<1>2. $\sup_{x \ge 0} x2^{-x} = \rho_0 := \frac{1}{e\ln 2} < 1$.
Proof: $g(x) = x2^{-x} = x e^{-x\ln 2}$; $g'(x) = e^{-x\ln 2}(1 - x\ln 2)$, so the maximum on $[0,\infty)$ occurs at $x = 1/\ln 2$ with value $\frac{1}{e\ln 2} \approx 0.53 < 1$; $g(0) = 0$ and $g \to 0$ as $x \to \infty$.

<1>3. Uniform convergence on $[0, B]$ for any $B > 0$.
Proof: on $[0,B]$, $x^n2^{-nx} = (x2^{-x})^n \le \rho_B^n$ where $\rho_B := \max_{[0,B]}x2^{-x} < 1$ (continuous function on a compact set, strictly less than $1$ by <1>2, since $x2^{-x} \le \rho_0 < 1$); the Weierstrass M-test with $\sum\rho_B^n < \infty$ applies.

<1>4. The convergence is in fact uniform on all of $[0, \infty)$.
<2>1. The tail after $N$ is $\sum_{n=N+1}^\infty (x2^{-x})^n = \frac{(x2^{-x})^{N+1}}{1 - x2^{-x}}$.
Proof: geometric tail formula.
<2>2. $\sup_{x \ge 0}\frac{(x2^{-x})^{N+1}}{1 - x2^{-x}} \le \frac{\rho_0^{N+1}}{1 - \rho_0} \to 0$.
Proof: by <1>2, $x2^{-x} \le \rho_0$ and $1 - x2^{-x} \ge 1 - \rho_0 > 0$ for all $x \ge 0$; the numerator is maximized at $x2^{-x} = \rho_0$ and the denominator minimized there, so the displayed uniform bound holds.
<2>3. Q.E.D. Proof: <2>2 shows the tails are uniformly small, i.e. uniform convergence on $[0, \infty)$ (a fortiori on every $[0,B]$).

<1>5. Q.E.D. Proof: <1>3 and <1>4 answer both parts: yes on every $[0,B]$, and yes on $[0,\infty)$ as well.
:::
