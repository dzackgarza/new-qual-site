---
schema: qual/card@1
id: P-CASP08D
kind: problem
title: "Entire functions with polynomial growth and meromorphic functions with prescribed poles and growth"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(a) Let $m$ be a positive integer.
Describe the set of all entire functions $f$ for which there exist positive constants $C_1$ and $C_2$ such that $|f(z)| \le C_1 |z|^m$ for all $|z| \ge C_2$.

(b) Describe the set of all functions $R$, meromorphic in $\mathbb{C}$, analytic except at $z = \pm 1$, and satisfying all of the following:
(i) $R$ has a simple pole (order 1) at $z = 1$.
(ii) $R$ has a double pole (order 2) at $z = -1$.
(iii) $|R(z)| \le C|z|$ for all $|z| \ge 2$.
:::

::: solution
**Goal:** Characterize entire functions of polynomial growth as polynomials via Cauchy estimates / Liouville's Theorem, and classify meromorphic functions with prescribed principal parts and linear growth.

<1>1. Part (a): Polynomial Growth Implies $f$ is a Polynomial of Degree $\le m$:
    *Proof:*
    <2>1. Let $f(z) = \sum_{k=0}^\infty a_k z^k$ be the Taylor expansion of $f$ around the origin, which has infinite radius of convergence since $f$ is entire.
    <2>2. By **Cauchy's Estimate** on the circle $|z| = r$ for any $r \ge C_2$:
        $$|a_k| \le \frac{1}{r^k} \max_{|z|=r} |f(z)| \le \frac{C_1 r^m}{r^k} = C_1 r^{m-k}.$$
    <2>3. For any $k > m$, the exponent $m - k < 0$.
    <2>4. Taking the limit as $r \to \infty$:
        $$|a_k| \le \lim_{r \to \infty} C_1 r^{m-k} = 0 \implies a_k = 0 \quad \text{for all } k > m.$$
    <2>5. Therefore, the Taylor series terminates at degree $m$:
        $$f(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_m z^m.$$
    <2>6. Thus the set of such functions is precisely the set of all **polynomials of degree at most $m$**:
        $$\{ f \in \mathbb{C}[z] \mid \deg(f) \le m \}.$$

<1>2. Part (b): Principal Part Expansion and Entire Remainder:
    *Proof:*
    <2>1. By (i), the principal part of $R(z)$ at $z = 1$ is:
        $$\frac{A}{z - 1} \quad (A \ne 0).$$
    <2>2. By (ii), the principal part of $R(z)$ at $z = -1$ is:
        $$\frac{B}{(z + 1)^2} + \frac{D}{z + 1} \quad (B \ne 0).$$
    <2>3. Define the function $g(z)$ by subtracting the principal parts from $R(z)$:
        $$g(z) \coloneqq R(z) - \left( \frac{A}{z - 1} + \frac{B}{(z + 1)^2} + \frac{D}{z + 1} \right).$$
    <2>4. Since the principal parts cancel the singularities of $R(z)$ at $z = 1$ and $z = -1$, $g(z)$ has removable singularities at $z = \pm 1$, so $g$ is an **entire function**.

<1>3. Growth of the Entire Function $g(z)$:
    *Proof:*
    <2>1. For $|z| \ge 2$:
        $$\left| \frac{A}{z - 1} + \frac{B}{(z + 1)^2} + \frac{D}{z + 1} \right| \le \frac{|A|}{|z| - 1} + \frac{|B|}{(|z| - 1)^2} + \frac{|D|}{|z| - 1} \le \frac{|A| + |D|}{1} + \frac{|B|}{1} = M.$$
    <2>2. Since $|R(z)| \le C|z|$ for $|z| \ge 2$, the triangle inequality gives:
        $$|g(z)| \le |R(z)| + M \le C|z| + M \le (C + M)|z| \quad \text{for all } |z| \ge 2.$$
    <2>3. By Part (a) with $m = 1$, the entire function $g(z)$ must be a polynomial of degree at most 1:
        $$g(z) = \alpha z + \beta \quad (\alpha, \beta \in \mathbb{C}).$$

<1>4. Conclusion for Part (b):
    *Proof:*
    <2>1. Therefore, $R(z)$ must be of the form:
        $$R(z) = \alpha z + \beta + \frac{A}{z - 1} + \frac{D}{z + 1} + \frac{B}{(z + 1)^2}$$
        where $\alpha, \beta, A, D, B \in \mathbb{C}$ with $A \ne 0$ and $B \ne 0$.

<1>5. Conclusion:
    (a) All polynomials of degree $\le m$;
    (b) All rational functions $R(z) = \alpha z + \beta + \frac{A}{z - 1} + \frac{D}{z + 1} + \frac{B}{(z + 1)^2}$ with $A, B \in \mathbb{C}^\times$ and $\alpha, \beta, D \in \mathbb{C}$. Q.E.D.
:::
