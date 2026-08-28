---
schema: qual/card@1
id: E-01BSA
kind: exercise
title: Isometries of compact metric spaces are surjective
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(X, d)$ be a metric space.
If $f: X \to X$ satisfies the condition

$$
d(f(x), f(y)) = d(x, y)
$$

for all $x, y \in X$, then $f$ is called an isometry of $X$.
Show that if $f$ is an isometry and $X$ is compact, then $f$ is bijective and hence a homeomorphism.
[Hint: If $a \notin f(X)$, choose $\epsilon$ so that the $\epsilon$-neighborhood of $a$ is disjoint from $f(X)$. Set $x_1 = a$, and $x_{n+1} = f(x_n)$ in general. Show that $d(x_n, x_m) \geq \epsilon$ for $n \neq m$.]
:::

::: solution
**Goal:** Prove that an isometry $f: X \to X$ on a compact metric space $(X, d)$ is surjective, and deduce that $f$ is a homeomorphism.

<1>1. $f$ is injective and continuous:
    *Proof:*
    <2>1. If $f(x) = f(y)$, then $d(x, y) = d(f(x), f(y)) = 0$, which implies $x = y$. Thus $f$ is injective.
    <2>2. For any $\varepsilon > 0$, setting $\delta = \varepsilon$ ensures $d(x, y) < \delta \implies d(f(x), f(y)) = d(x, y) < \varepsilon$. Thus $f$ is uniformly continuous.

<1>2. The image $f(X)$ is compact and closed in $X$:
    *Proof:* Since $X$ is compact and $f$ is continuous (<1>1), $f(X)$ is a compact subset of the metric space $X$, hence $f(X)$ is closed in $X$.

<1>3. $f$ is surjective ($f(X) = X$):
    *Proof by contradiction:*
    <2>1. Suppose $f(X) \neq X$, so there exists a point $a \in X \setminus f(X)$.
    <2>2. Since $f(X)$ is closed and $a \notin f(X)$, the distance $\varepsilon = d(a, f(X)) = \inf_{y \in f(X)} d(a, y)$ is strictly positive: $\varepsilon > 0$.
    <2>3. Define a sequence $(x_n)_{n=1}^\infty$ in $X$ inductively by $x_1 = a$ and $x_{n+1} = f(x_n) = f^n(a)$ for all $n \ge 1$.
    <2>4. For any positive integers $n > m \ge 1$, since $f^{m-1}$ is an isometry:
        $$d(x_n, x_m) = d(f^{m-1}(x_{n-m+1}), f^{m-1}(x_1)) = d(x_{n-m+1}, x_1) = d(x_{n-m+1}, a).$$
    <2>5. Since $n > m$, $n - m + 1 \ge 2$, so $x_{n-m+1} = f(x_{n-m}) \in f(X)$.
    <2>6. By definition of $\varepsilon$, $d(x_{n-m+1}, a) \ge \varepsilon > 0$.
    <2>7. Thus $d(x_n, x_m) \ge \varepsilon > 0$ for all $n \neq m$.
    <2>8. The sequence $(x_n)$ contains no Cauchy subsequence, so it has no convergent subsequence.
    <2>9. This contradicts the sequential compactness of the compact metric space $X$.
    <2>10. Therefore $f(X) = X$, so $f$ is surjective.

<1>4. $f$ is a homeomorphism:
    *Proof:*
    <2>1. By <1>1 and <1>3, $f$ is a continuous bijection.
    <2>2. A continuous bijection from a compact space to a Hausdorff space is a closed map, hence a homeomorphism (its inverse $f^{-1}$ is continuous and is an isometry as well). Q.E.D.
:::
