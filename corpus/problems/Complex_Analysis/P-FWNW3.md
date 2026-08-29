---
schema: qual/card@1
id: P-FWNW3
kind: problem
title: Uniform approximation of holomorphic functions by polynomials
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Uniform Convergence
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that any holomorphic function $f$ on a simply connected domain (or compact set with connected complement) can be uniformly approximated by polynomials on compact subsets.
:::

::: solution
**Goal:** State and prove Runge's Polynomial Approximation Theorem for holomorphic functions on compact sets with connected complement (or simply connected domains).

<1>1. Setting and statement of Runge's Theorem:
    *Proof:*
    <2>1. **Theorem (Runge, 1885):** Let $K \subset \mathbb{C}$ be a compact set such that $\mathbb{C} \setminus K$ is connected. If $f$ is holomorphic on an open neighborhood $U$ of $K$, then for every $\varepsilon > 0$, there exists a polynomial $P(z) \in \mathbb{C}[z]$ such that:
        $$\sup_{z \in K} |f(z) - P(z)| < \varepsilon.$$

<1>2. Step 1: Approximation by rational functions via Cauchy's Integral Formula:
    *Proof:*
    <2>1. Choose a smooth cycle (or union of grid squares) $\gamma = \partial \Omega$ lying in $U \setminus K$ with winding number $\operatorname{Ind}_\gamma(z) = 1$ for all $z \in K$ and $\operatorname{Ind}_\gamma(z) = 0$ for all $z \notin U$.
    <2>2. By Cauchy's Integral Formula, for all $z \in K$:
        $$f(z) = \frac{1}{2\pi i} \int_\gamma \frac{f(\zeta)}{\zeta - z} \, d\zeta.$$
    <2>3. Approximating the integral by Riemann sums: there exist points $\zeta_j \in \gamma$ and weights $c_j \in \mathbb{C}$ such that the rational function:
        $$R_1(z) = \sum_{j=1}^m \frac{c_j}{\zeta_j - z}$$
        satisfies $\sup_{z \in K} |f(z) - R_1(z)| < \varepsilon / 3$.
    <2>4. The poles $\zeta_j$ of $R_1(z)$ all lie on $\gamma \subset \mathbb{C} \setminus K$.

<1>3. Step 2: Pole shifting to $\infty$:
    *Proof:*
    <2>1. Since $\mathbb{C} \setminus K$ is connected, for each pole $\zeta_j \in \mathbb{C} \setminus K$, there exists a continuous path $\Gamma_j$ in $\mathbb{C} \setminus K$ connecting $\zeta_j$ to a point $w$ outside a large disk $\{|z| > R\}$ containing $K$.
    <2>2. By repeatedly expanding in Taylor series along small steps of the path $\Gamma_j$ (pole pushing), each simple pole $\frac{1}{\zeta_j - z}$ can be uniformly approximated on $K$ by a rational function with pole at $w$.
    <2>3. Hence there is a rational function $R_2(z)$ with poles only in $\{|z| > R\}$ such that $\sup_{z \in K} |R_1(z) - R_2(z)| < \varepsilon / 3$.

<1>4. Step 3: Taylor expansion to obtain a polynomial:
    *Proof:*
    <2>1. Since all poles of $R_2(z)$ have modulus strictly greater than $R \ge \sup_{z \in K} |z|$, $R_2(z)$ is holomorphic on the open disk $D(0, R)$ which contains $K$.
    <2>2. The Taylor series of $R_2(z)$ about $0$:
        $$R_2(z) = \sum_{n=0}^\infty a_n z^n$$
        converges uniformly on every compact subset of $D(0, R)$, and in particular uniformly on $K$.
    <2>3. Truncating the series at a sufficiently large degree $N$ gives a polynomial $P(z) = \sum_{n=0}^N a_n z^n$ such that:
        $$\sup_{z \in K} |R_2(z) - P(z)| < \frac{\varepsilon}{3}.$$

<1>5. Total error estimate:
    *Proof:*
    <2>1. By the triangle inequality:
        $$\sup_{z \in K} |f(z) - P(z)| \le \sup_{z \in K} |f - R_1| + \sup_{z \in K} |R_1 - R_2| + \sup_{z \in K} |R_2 - P| < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

<1>6. Conclusion:
    Any holomorphic function on a compact set with connected complement (or a simply connected domain) can be uniformly approximated by polynomials on compact subsets. Q.E.D.
:::
