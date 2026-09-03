---
schema: qual/card@1
id: E-5VQHD
kind: problem
title: Heine–Cantor theorem
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that if $f: A\to B$ is a continuous map between metric spaces and $K\subset A$ is compact, then $\restrictionof{f}{K}$ is uniformly continuous.
:::

::: solution
**Goal:** Prove the Heine–Cantor Theorem: any continuous map $f: (A, d_A) \to (B, d_B)$ between metric spaces is uniformly continuous when restricted to a compact subset $K \subseteq A$.

<1>1. Setting and goal: Let $\varepsilon > 0$.
We must find $\delta > 0$ such that for all $x, y \in K$: $$d_A(x, y) < \delta \implies d_B(f(x), f(y)) < \varepsilon.$$

<1>2. Construction of covering by half-radius balls: *Proof:* <2>1. For each point $x \in K$, continuity of $f$ at $x$ guarantees the existence of a radius $\delta_x > 0$ such that: $$d_A(z, x) < \delta_x \implies d_B(f(z), f(x)) < \frac{\varepsilon}{2}.$$ <2>2. Consider the open ball $B\left(x, \frac{\delta_x}{2}\right) = \{z \in A \mid d_A(z, x) < \frac{\delta_x}{2}\}$.
<2>3. The family $\left\{ B\left(x, \frac{\delta_x}{2}\right) \right\}_{x \in K}$ forms an open cover of the compact set $K$.

<1>3. Extraction of finite subcover and choice of $\delta$: *Proof:* <2>1. By compactness of $K$, there exists a finite set of points $\{x_1, \dots, x_n\} \subseteq K$ such that: $$K \subseteq \bigcup_{i=1}^n B\left(x_i, \frac{\delta_{x_i}}{2}\right).$$ <2>2. Define $\delta = \min\left\{ \frac{\delta_{x_1}}{2}, \dots, \frac{\delta_{x_n}}{2} \right\}$.
<2>3. Since $\delta$ is the minimum of finitely many positive numbers, $\delta > 0$.

<1>4. Verification of uniform continuity: *Proof:* <2>1. Let $x, y \in K$ with $d_A(x, y) < \delta$.
<2>2. Since the finite collection covers $K$, there exists an index $k \in \{1, \dots, n\}$ such that $x \in B\left(x_k, \frac{\delta_{x_k}}{2}\right)$, so $d_A(x, x_k) < \frac{\delta_{x_k}}{2} < \delta_{x_k}$.
<2>3. By <1>2, $d_B(f(x), f(x_k)) < \frac{\varepsilon}{2}$.
<2>4. For $y$, the triangle inequality yields: $$d_A(y, x_k) \le d_A(y, x) + d_A(x, x_k) < \delta + \frac{\delta_{x_k}}{2} \le \frac{\delta_{x_k}}{2} + \frac{\delta_{x_k}}{2} = \delta_{x_k}.$$ <2>5. Thus $d_A(y, x_k) < \delta_{x_k}$, which by <1>2 implies $d_B(f(y), f(x_k)) < \frac{\varepsilon}{2}$.
<2>6. Combining these via the triangle inequality in $(B, d_B)$: $$d_B(f(x), f(y)) \le d_B(f(x), f(x_k)) + d_B(f(x_k), f(y)) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

<1>5. Conclusion: The restriction $f|_K$ is uniformly continuous on $K$.
Q.E.D.
:::
