---
schema: qual/card@1
id: E-HAT-1.2-19
kind: problem
title: Union of spheres of radius $1/n$ centered at $(1/n, 0, 0)$ is simply-connected
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Simply Connected
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}
Show that the subspace $X \subset \RR^3$ that is the union of the spheres $S_n$ of radius $1/n$ and center $(1/n, 0, 0)$ for $n = 1, 2, 3, \dots$ is simply-connected.
:::

::: {.solution}
::: pf

::: {.pf-step #x-path-connected}

$X$ is path-connected, and its spheres meet pairwise only at the origin.

::: pf-proof

::: pf-step

For each $n \ge 1$, let $S_n = \{x \in \RR^3 : \|x - (1/n, 0, 0)\| = 1/n\}$ be the 2-sphere of diameter $2/n$ passing through the origin $0 = (0, 0, 0)$.

:::

::: pf-step

The spheres pairwise intersect only at the origin: $S_n \cap S_m = \{0\}$ for all $n \neq m$.

:::

::: pf-step

Since each $S_n$ is path-connected and contains $0$, the union $X = \bigcup_{n=1}^\infty S_n$ is path-connected.

:::

::: pf-step

For each $n \ge 1$, let $p_n = (2/n, 0, 0) \in S_n$ denote the pole of $S_n$ opposite to the origin.

:::

:::

:::

::: {.pf-step #s2}

Each $X \setminus \{p_n\}$ deforms onto $\bigcup_{m \neq n} S_m$ by a homotopy that moves points only inside $S_n$.

::: pf-proof

::: pf-step

The punctured 2-sphere $S_n \setminus \{p_n\}$ is homeomorphic to $\RR^2$ via stereographic projection from $p_n$.

:::

::: pf-step

Hence there is a continuous deformation retraction $H_n: (S_n \setminus \{p_n\}) \times [0, 1] \to S_n \setminus \{p_n\}$ that contracts $S_n \setminus \{p_n\}$ to the origin $0$, keeping $0$ stationary:
    $$H_n(x, 0) = x, \quad H_n(x, 1) = 0, \quad H_n(0, t) = 0 \quad \text{for all } t \in [0, 1].$$

:::

::: pf-step

Extend $H_n$ to the entire space $X \setminus \{p_n\}$ by setting $H_n(x, t) = x$ for all $x \in S_m$ ($m \neq n$). Since $S_n \cap S_m = \{0\}$ and $H_n(0, t) = 0$, this extended map is continuous on $(X \setminus \{p_n\}) \times [0, 1]$.

:::

::: pf-step

Throughout the deformation $H_n$, every point moves within $S_n$, so $\|H_n(x, t) - x\| \le \operatorname{diam}(S_n) = 2/n$ for all $x \in X \setminus \{p_n\}$ and $t \in [0, 1]$.

:::

:::

:::

::: pf-step

A loop at the origin is homotopic to a loop that misses the pole $p_n$ of a given sphere.

::: pf-proof

::: pf-step

Let $f: [0, 1] \to X$ be a continuous loop based at the origin: $f(0) = f(1) = 0$.

:::

::: pf-step

For each $n \ge 1$, the preimage $f^{-1}(S_n \setminus \{0\})$ is an open subset of $(0, 1)$, hence a countable union of disjoint open intervals $f^{-1}(S_n \setminus \{0\}) = \bigcup_j (a_{n,j}, b_{n,j})$.

:::

::: pf-step

On each interval $(a_{n,j}, b_{n,j})$, the path $f$ is a path in $S_n$ starting and ending at $0$.

:::

::: pf-step

Since the 2-sphere $S_n$ has dimension 2, any continuous path in $S_n$ can be perturbed relative to its endpoints to miss the pole $p_n$ (by the Simplicial Approximation Theorem or Stone–Weierstrass density of paths missing a point).

:::

::: pf-step

Applying this perturbation to each interval $(a_{n,j}, b_{n,j})$ produces a loop $f_n$ homotopic to $f$ whose image in $S_n$ misses $p_n$: $p_n \notin f_n([0, 1])$.

:::

:::

:::

::: pf-step

Every loop at the origin is null-homotopic, so $\pi_1(X, 0) = 0$.

::: pf-proof

::: pf-step

Perturb $f$ simultaneously on all spheres $S_n$ so that $f(I)$ misses every pole $p_n$ for all $n \ge 1$.

:::

::: pf-step

For each $n \ge 1$, apply the deformation retraction $H_n$ on $S_n \setminus \{p_n\}$ from step [](#s2){.pf-ref}.

:::

::: pf-step

Concatenating these homotopies over all $n \ge 1$ (rescaling the $n$-th homotopy to the time parameter interval $[1 - 2^{-(n-1)}, 1 - 2^{-n}]$) defines a homotopy $H: [0, 1] \times [0, 1] \to X$.

:::

::: pf-step

Continuity of $H$ at $t = 1$: For any $\varepsilon > 0$, choose $N > 2/\varepsilon$. For all stages $n \ge N$, every point moves by at most $\operatorname{diam}(S_n) = 2/n < \varepsilon$, and the image at stage $N$ is contained in the $\varepsilon$-neighborhood $\bigcup_{n \ge N} S_n \subset B(0, \varepsilon)$.

:::

::: pf-step

Thus $H$ is a continuous homotopy in $X$ between the loop $f$ and the constant loop at $0$.

:::

::: pf-step

Therefore $[f] = 0$ in $\pi_1(X, 0)$, so $\pi_1(X, 0) = 0$.

:::

:::

:::

::: pf-qed

$X$ is path-connected by step [](#x-path-connected){.pf-ref}, and $\pi_1(X, 0) = 0$, so $X$ is simply connected.

:::

:::

:::
