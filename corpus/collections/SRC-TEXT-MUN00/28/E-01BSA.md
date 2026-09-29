---
schema: qual/card@1
id: E-01BSA
kind: problem
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

::: {.solution}
**Goal:** Prove that an isometry $f: X \to X$ on a compact metric space $(X, d)$ is surjective, and deduce that $f$ is a homeomorphism.

::: pf

::: {.pf-step #f-injective-continuous}
$f$ is injective and continuous:

::: pf-proof

::: pf-step
If $f(x) = f(y)$, then $d(x, y) = d(f(x), f(y)) = 0$, which implies $x = y$. Thus $f$ is injective.
:::

::: pf-step
For any $\varepsilon > 0$, setting $\delta = \varepsilon$ ensures $d(x, y) < \delta \implies d(f(x), f(y)) = d(x, y) < \varepsilon$. Thus $f$ is uniformly continuous.
:::

:::

:::

::: pf-step
The image $f(X)$ is compact and closed in $X$:

::: pf-proof
Since $X$ is compact and $f$ is continuous (step [](#f-injective-continuous){.pf-ref}), $f(X)$ is a compact subset of the metric space $X$, hence $f(X)$ is closed in $X$.
:::

:::

::: {.pf-step #f-surjective}
$f$ is surjective ($f(X) = X$):

::: pf-proof
By contradiction.

::: pf-step
Suppose $f(X) \neq X$, so there exists a point $a \in X \setminus f(X)$.
:::

::: pf-step
Since $f(X)$ is closed and $a \notin f(X)$, the distance $\varepsilon = d(a, f(X)) = \inf_{y \in f(X)} d(a, y)$ is strictly positive: $\varepsilon > 0$.
:::

::: pf-step
Define a sequence $(x_n)_{n=1}^\infty$ in $X$ inductively by $x_1 = a$ and $x_{n+1} = f(x_n) = f^n(a)$ for all $n \ge 1$.
:::

::: pf-step
For any positive integers $n > m \ge 1$, since $f^{m-1}$ is an isometry:
$$d(x_n, x_m) = d(f^{m-1}(x_{n-m+1}), f^{m-1}(x_1)) = d(x_{n-m+1}, x_1) = d(x_{n-m+1}, a).$$
:::

::: pf-step
Since $n > m$, $n - m + 1 \ge 2$, so $x_{n-m+1} = f(x_{n-m}) \in f(X)$.
:::

::: pf-step
By definition of $\varepsilon$, $d(x_{n-m+1}, a) \ge \varepsilon > 0$.
:::

::: pf-step
Thus $d(x_n, x_m) \ge \varepsilon > 0$ for all $n \neq m$.
:::

::: pf-step
The sequence $(x_n)$ contains no Cauchy subsequence, so it has no convergent subsequence.
:::

::: pf-step
This contradicts the sequential compactness of the compact metric space $X$.
:::

::: pf-step
Therefore $f(X) = X$, so $f$ is surjective.
:::

:::

:::

::: pf-step
$f$ is a homeomorphism:

::: pf-proof

::: pf-step
By steps [](#f-injective-continuous){.pf-ref} and [](#f-surjective){.pf-ref}, $f$ is a continuous bijection.
:::

::: pf-step
A continuous bijection from a compact space to a Hausdorff space is a closed map, hence a homeomorphism (its inverse $f^{-1}$ is continuous and is an isometry as well). Q.E.D.
:::

:::

:::

:::

:::
