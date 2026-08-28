---
schema: qual/card@1
id: P-JHUFA02CAD
kind: problem
title: "for each , there is a unique such that $$"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convex Sets
  - Orthogonal Projection
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

4. Let K be a closed convex subset of a Hilbert space H. Show that for each $x \in H$ , there is a unique $y \in K$ such that

$$
| | x - y | | = i n f _ { z \in K } | | x - z | |
$$

::: {.solution}
**Goal.** For a closed convex subset $K$ of a Hilbert space $H$, show each $x \in H$ has a unique closest point $y \in K$.

<1>1. Existence.
<2>1. Let $d = \inf_{z \in K} \|x - z\|$.
Proof: define the distance.
<2>2. Choose a sequence $z_n \in K$ with $\|x - z_n\| \to d$.
Proof: definition of infimum.
<2>3. By the parallelogram law, $\|z_n - z_m\|^2 = 2\|z_n - x\|^2 + 2\|z_m - x\|^2 - 4\|\frac{z_n + z_m}{2} - x\|^2$.
Proof: parallelogram identity.
<2>4. Since $K$ is convex, $\frac{z_n + z_m}{2} \in K$, so $\|\frac{z_n+z_m}{2} - x\| \ge d$.
Proof: convexity and definition of $d$.
<2>5. Hence $\|z_n - z_m\|^2 \le 2\|z_n - x\|^2 + 2\|z_m - x\|^2 - 4d^2 \to 2d^2 + 2d^2 - 4d^2 = 0$.
Proof: take limits.
<2>6. Hence $(z_n)$ is Cauchy, so it converges to some $y \in H$.
Proof: $H$ is complete.
<2>7. $y \in K$ (since $K$ is closed) and $\|x - y\| = d$.
Proof: closedness and continuity of the norm.

<1>2. Uniqueness.
<2>1. Suppose $y_1, y_2 \in K$ both satisfy $\|x - y_1\| = \|x - y_2\| = d$.
Proof: assume two closest points.
<2>2. By the parallelogram law, $\|y_1 - y_2\|^2 = 2\|y_1 - x\|^2 + 2\|y_2 - x\|^2 - 4\|\frac{y_1+y_2}{2} - x\|^2 \le 2d^2 + 2d^2 - 4d^2 = 0$.
Proof: $\frac{y_1+y_2}{2} \in K$ (convexity), so $\|\frac{y_1+y_2}{2} - x\| \ge d$.
<2>3. Hence $y_1 = y_2$.
Proof: $\|y_1 - y_2\| = 0$.

<1>3. Q.E.D.
Proof: <1>1 gives existence; <1>2 gives uniqueness.
:::
