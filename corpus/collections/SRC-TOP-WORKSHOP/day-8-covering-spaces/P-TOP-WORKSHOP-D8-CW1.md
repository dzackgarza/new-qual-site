---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-CW1
kind: problem
title: The real line as the universal cover of the circle (warm-up)
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Explicitly prove that $\mathbb R$ is that universal cover of $S^1$.
:::

::: {.solution}
<1>1. Define the covering map $p: \mathbb{R} \to S^1$: <2>1. View $S^1$ as the unit circle in the complex plane $\{z \in \mathbb{C} : |z| = 1\}$, and define $p(t) = e^{2\pi i t} = \cos(2\pi t) + i \sin(2\pi t)$.
Proof: standard exponential parametrization of $S^1$.
<2>2. $p$ is continuous and surjective.
Proof: trigonometric functions are continuous and periodic with range $[-1, 1]$.

<1>2. Show that every point in $S^1$ has an evenly covered open neighborhood: <2>1. Let $z_0 = e^{2\pi i t_0} \in S^1$ be an arbitrary point.
Proof: setup.
<2>2. Define the open neighborhood $U = S^1 \setminus \{-z_0\} = \{e^{2\pi i t} : t \in (t_0 - 1/2, t_0 + 1/2)\}$.
Proof: complement of a single point in $S^1$ is an open circular arc of angle $< 2\pi$.
<2>3. The preimage of $U$ under $p$ is:
\[
p^{-1}(U) = \bigsqcup_{k \in \mathbb{Z}} V_k, \quad \text{where } V_k = \left(t_0 - \frac{1}{2} + k, \; t_0 + \frac{1}{2} + k\right).
\]
Proof: $e^{2\pi i t} = e^{2\pi i s} \iff t - s \in \mathbb{Z}$.
<2>4. The intervals $V_k$ are pairwise disjoint open subsets of $\mathbb{R}$.
Proof: length of each interval is 1, and centers are spaced by 1. <2>5. For each $k \in \mathbb{Z}$, the restriction $p|_{V_k}: V_k \to U$ is a continuous bijection.
Proof: $t \mapsto e^{2\pi i t}$ is strictly monotone in argument on an interval of length 1. <2>6. The inverse map $(p|_{V_k})^{-1}: U \to V_k$ is continuous:
\[
(p|_{V_k})^{-1}(z) = t_0 + k + \frac{1}{2\pi} \operatorname{Arg}\left(z e^{-2\pi i t_0}\right),
\]
where $\operatorname{Arg}$ is the principal branch of the argument on $\mathbb{C} \setminus (-\infty, 0]$ with values in $(-\pi, \pi)$.
Proof: continuous branch of the logarithm.
<2>7. Thus $p|_{V_k}: V_k \to U$ is a homeomorphism for each $k \in \mathbb{Z}$, so $U$ is evenly covered.
Proof: <2>5 and <2>6. <2>8. Hence $p: \mathbb{R} \to S^1$ is a covering map.
Proof: <2>7 holds for all $z_0 \in S^1$.

<1>3. Show that $\mathbb{R}$ is the universal cover: <2>1. $\mathbb{R}$ is contractible: the map $H(t, s) = (1 - s)t$ for $(t, s) \in \mathbb{R} \times [0, 1]$ is a homotopy between the identity map on $\mathbb{R}$ and the constant map to $0$.
Proof: straight-line homotopy on the convex space $\mathbb{R}$.
<2>2. Since $\mathbb{R}$ is contractible, it is path-connected and simply connected: $\pi_1(\mathbb{R}, 0) = 0$.
Proof: contractible spaces have trivial homotopy groups.
<2>3. A simply connected covering space of a connected, locally path-connected space is its unique (up to isomorphism) universal covering space.
Proof: universal covering space theorem.
<2>4. Therefore $p: \mathbb{R} \to S^1$ is the universal cover of $S^1$.
Proof: <1>2, <2>2, and <2>3.

<1>4. Q.E.D. Proof: <1>3.
:::
