---
schema: qual/card@1
id: P-C62HS
kind: problem
title: A contraction of a compact metric space has a fixed point
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Metric Spaces
  - Compactness
relations: []
review: draft
---

::: problem
Prove that if $(X, d)$ is a non-empty compact metric space and $f: X \to X$ is a contraction map (that is, there exists a constant $C \in (0, 1)$ such that $d(f(x), f(y)) \le C \cdot d(x, y)$ for all $x, y \in X$), then $f$ has a unique fixed point in $X$.
:::

::: solution
**Goal:** Prove that a contraction map on a compact metric space attains a unique fixed point by minimizing the displacement function $g(x) = d(x, f(x))$.

<1>1. Continuity of the displacement function $g: X \to \mathbb{R}$:
    *Proof:*
    <2>1. Define $g(x) = d(x, f(x))$ for all $x \in X$.
    <2>2. Let $x, y \in X$. By the triangle inequality:
    $$d(x, f(x)) \le d(x, y) + d(y, f(y)) + d(f(y), f(x)).$$
    <2>3. Rearranging terms:
    $$g(x) - g(y) = d(x, f(x)) - d(y, f(y)) \le d(x, y) + d(f(x), f(y)).$$
    <2>4. Using the contraction hypothesis $d(f(x), f(y)) \le C \cdot d(x, y)$:
    $$g(x) - g(y) \le d(x, y) + C \cdot d(x, y) = (1 + C) d(x, y).$$
    <2>5. By symmetry between $x$ and $y$:
    $$|g(x) - g(y)| \le (1 + C) d(x, y).$$
    <2>6. Thus $g$ is Lipschitz continuous with Lipschitz constant $1 + C$, hence continuous on $X$.

<1>2. Existence of a minimum for $g$:
    *Proof:*
    <2>1. $X$ is a non-empty compact topological space.
    <2>2. By the Extreme Value Theorem, the continuous real-valued function $g$ attains its global minimum on $X$.
    <2>3. Thus there exists a point $x_0 \in X$ such that
    $$g(x_0) = \inf_{x \in X} g(x) \le g(x) \quad \text{for all } x \in X.$$

<1>3. Proof that $x_0$ is a fixed point ($f(x_0) = x_0$):
    *Proof:*
    <2>1. Suppose for contradiction that $f(x_0) \ne x_0$.
    <2>2. By the metric property, $d(x_0, f(x_0)) > 0$.
    <2>3. Evaluate $g$ at the image point $f(x_0) \in X$:
    $$g(f(x_0)) = d(f(x_0), f(f(x_0))).$$
    <2>4. By the contraction property of $f$:
    $$d(f(x_0), f(f(x_0))) \le C \cdot d(x_0, f(x_0)).$$
    <2>5. Since $0 < C < 1$ and $d(x_0, f(x_0)) > 0$:
    $$g(f(x_0)) \le C \cdot d(x_0, f(x_0)) < d(x_0, f(x_0)) = g(x_0).$$
    <2>6. This strictly contradicts the minimality of $g(x_0) = \inf_{x \in X} g(x)$.
    <2>7. Therefore $d(x_0, f(x_0)) = 0$, which proves $f(x_0) = x_0$.

<1>4. Uniqueness of the fixed point:
    *Proof:*
    <2>1. Suppose $x, y \in X$ are two fixed points of $f$, so $f(x) = x$ and $f(y) = y$.
    <2>2. Applying the contraction property:
    $$d(x, y) = d(f(x), f(y)) \le C \cdot d(x, y).$$
    <2>3. Rearranging: $(1 - C) d(x, y) \le 0$.
    <2>4. Since $C < 1$, $1 - C > 0$, forcing $d(x, y) \le 0 \implies d(x, y) = 0$.
    <2>5. Thus $x = y$.

<1>5. Conclusion:
    *Proof:*
    $f$ has a unique fixed point $x_0 \in X$.
:::

