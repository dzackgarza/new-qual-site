---
schema: qual/card@1
id: P-RASP25D
kind: problem
title: "Closed convex set in L^1 with no best approximation"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
Let $E$ be the Banach space $L^1([0,1])$ and
$$
C := \left\{u \in E : u(x) \geq 0 \text{ a.e. } x \in [0,1],\; \int_0^1 x u(x)\,dx \geq 1\right\}.
$$

Show that

(1) $C$ is nonempty, closed and convex in $E$.

(2) $d(0, C) := \inf\{\|u\| : u \in C\} = 1$.

Hint: try piecewise constant functions.

(3) There is no $u \in C$ such that $\|u\| = d(0, C) = 1$.
:::

::: {.solution}
**(1).**

<1>1. $C$ is nonempty: e.g. $u(x) = 2$ satisfies $u \ge 0$ and $\int_0^1 x \cdot 2\,dx = 1 \ge 1$.
Proof: $\int_0^1 2x\,dx = 1$.

<1>2. $C$ is convex.
Proof: if $u, v \in C$ and $0 \le t \le 1$, then $tu + (1-t)v \ge 0$ a.e. and $\int_0^1 x(tu + (1-t)v)\,dx = t\int xu + (1-t)\int xv \ge t + (1-t) = 1$.

<1>3. $C$ is closed.
Proof: the map $u \mapsto \int_0^1 x u(x)\,dx$ is continuous on $L^1$ (it is a bounded linear functional, since $|x| \le 1$), so the set $\{u : \int xu \ge 1\}$ is closed; and the set $\{u : u \ge 0 \text{ a.e.}\}$ is closed in $L^1$ (a limit of nonnegative functions is nonnegative a.e., passing to a subsequence). The intersection of closed sets is closed.

**(2).**

<1>1. For any $u \in C$, $\|u\| = \int_0^1 |u| = \int_0^1 u \ge \int_0^1 x u(x)\,dx \ge 1$.
Proof: $u \ge 0$ so $|u| = u$, and $x \le 1$ on $[0,1]$ so $u \ge xu$.

<1>2. Hence $d(0, C) \ge 1$.
Proof: <1>1.

<1>3. For $\varepsilon > 0$, define $u_\varepsilon(x) = \frac{1}{\varepsilon}\chi_{[1-\varepsilon, 1]}(x)$.
Proof: a piecewise constant function concentrated near $x = 1$.

<1>4. $\int_0^1 x u_\varepsilon(x)\,dx = \frac{1}{\varepsilon}\int_{1-\varepsilon}^1 x\,dx = \frac{1}{\varepsilon}\cdot\frac{1 - (1-\varepsilon)^2}{2} = 1 - \frac{\varepsilon}{2}$.
Proof: compute the integral.

<1>5. Define $v_\varepsilon(x) = \frac{u_\varepsilon(x)}{1 - \varepsilon/2} = \frac{1}{\varepsilon(1 - \varepsilon/2)}\chi_{[1-\varepsilon,1]}(x)$; then $\int_0^1 x v_\varepsilon = 1$, so $v_\varepsilon \in C$.
Proof: <1>4, scaled so the constraint is exactly $1$.

<1>6. $\|v_\varepsilon\| = \int_0^1 v_\varepsilon = \frac{1}{\varepsilon(1-\varepsilon/2)} \cdot \varepsilon = \frac{1}{1-\varepsilon/2} \to 1$ as $\varepsilon \to 0$.
Proof: compute the $L^1$ norm.

<1>7. Hence $d(0, C) \le 1$.
Proof: <1>6 (the infimum is at most $\lim_{\varepsilon \to 0} \|v_\varepsilon\| = 1$).

<1>8. Therefore $d(0, C) = 1$.
Proof: <1>2 and <1>7.

**(3).**

<1>1. Suppose $u \in C$ with $\|u\| = 1$.
Proof: assume a minimizer exists.

<1>2. Then $\int_0^1 u = 1$ and $\int_0^1 x u \ge 1$, so $\int_0^1 (1 - x) u(x)\,dx = \int_0^1 u - \int_0^1 xu \le 0$.
Proof: <1>1 and the constraint.

<1>3. But $1 - x \ge 0$ and $u \ge 0$ a.e., so $\int_0^1 (1-x)u(x)\,dx \ge 0$.
Proof: nonnegativity of the integrand.

<1>4. Hence $\int_0^1 (1-x)u(x)\,dx = 0$, so $(1-x)u(x) = 0$ a.e., i.e. $u = 0$ a.e. on $[0,1)$.
Proof: <1>2 and <1>3 (a nonnegative integrable function with zero integral is zero a.e.).

<1>5. Then $\int_0^1 x u(x)\,dx = 0$ (since $u = 0$ a.e. on $[0,1)$ and the point $x = 1$ has measure zero).
Proof: <1>4.

<1>6. This contradicts the constraint $\int_0^1 x u \ge 1$.
Proof: <1>5.

<1>7. Hence no $u \in C$ attains $\|u\| = 1$.
Proof: <1>6.

<1>8. Q.E.D.
Proof: <1>3 (1), <1>8 (2), <1>7 (3).
:::
