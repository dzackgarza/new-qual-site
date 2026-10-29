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
Write $0$ for the origin, $|\cdot|$ for the Euclidean norm, and $p_n = (2/n, 0, 0)$ for the point of $S_n$ opposite $0$.

::: pf

::: {.pf-step #pieces}
$X$ is path-connected, and $X \setminus \{0\}$ is the disjoint union of the sets $S_n \setminus \{0\}$, each open in $X$.

::: pf-proof
A point $x$ lies on $S_n$ exactly when $|x|^2 = 2x_1/n$.
If $x \in S_n \cap S_m$ with $n \ne m$, then $2x_1/n = 2x_1/m$, so $x_1 = 0$ and $|x| = 0$; hence $S_n \cap S_m = \{0\}$.
Every $S_n$ is path-connected and contains $0$, so $X$ is path-connected.
The set $\{0\} \cup \bigcup_{m \ne n} S_m$ is closed in $\RR^3$, because a convergent sequence of points from infinitely many distinct spheres $S_m$ has norms at most $2/m \to 0$ and so converges to $0$.
Its complement in $X$ is $S_n \setminus \{0\}$, which is therefore open in $X$.
:::

:::

::: {.pf-step #small-homotopy}
Let $g \colon [a,b] \to S_n$ be a path with $g(a) = g(b) = 0$, and let $M = \max |g|$.
Then $g$ is homotopic rel endpoints, inside $S_n$, to the constant path at $0$ by a homotopy $G$ with $|G(s,t)| \le M$ for all $s, t$.

::: pf-proof
If $p_n$ lies in the image of $g$, then $M = 2/n$; take any homotopy rel endpoints in $S_n$ to the constant path, which exists because $S_n$ is simply connected, and every point of $S_n$ has norm at most $2/n = M$.
Otherwise let $\sigma \colon S_n \setminus \{p_n\} \to P$ be stereographic projection from $p_n$ onto the plane $P$ tangent to $S_n$ at $0$, so $\sigma(0) = 0$, and set $G(s,t) = \sigma^{-1}((1-t)\,\sigma(g(s)))$.
This is a homotopy rel endpoints from $g$ to the constant path at $0$.
For $y \in S_n \setminus \{p_n\}$ let $\theta \in [0, \pi/2)$ be the angle at $p_n$ between the segments to $0$ and to $y$; the triangle $0\,y\,p_n$ has a right angle at $y$ because $0p_n$ is a diameter, so $|y| = (2/n)\sin\theta$ and $|\sigma(y)| = (2/n)\tan\theta$.
Both are increasing in $\theta$, so $|y|$ is an increasing function of $|\sigma(y)|$; as $|(1-t)\sigma(g(s))| \le |\sigma(g(s))|$, we get $|G(s,t)| \le |g(s)| \le M$.
:::

:::

::: {.pf-step #excursions}
Let $f \colon [0,1] \to X$ be a loop at $0$.
Then $U = f^{-1}(X \setminus \{0\})$ is a disjoint union of countably many open intervals $J = (a_J, b_J)$, with $f(a_J) = f(b_J) = 0$ and $f(J) \subset S_{n(J)} \setminus \{0\}$ for one index $n(J)$; moreover, for each $\varepsilon > 0$ only finitely many $J$ have $M_J = \max_{\overline{J}} |f| \ge \varepsilon$.

::: pf-proof
$U$ is open in $[0,1]$ and misses $0$ and $1$, so it is a countable disjoint union of open intervals, and their endpoints lie outside $U$.
Each $J$ is connected, so by step [](#pieces){.pf-ref} it maps into one of the disjoint open sets $S_n \setminus \{0\}$.
By uniform continuity of $f$, choose $\delta > 0$ with $|f(s) - f(s')| < \varepsilon$ whenever $|s - s'| < \delta$.
If $M_J \ge \varepsilon$, then some $s \in J$ has $|f(s) - f(a_J)| \ge \varepsilon$, so $J$ has length at least $\delta$; at most $1/\delta$ disjoint intervals in $[0,1]$ have this length.
:::

:::

::: {.pf-step #homotopy}
Define $F \colon [0,1] \times [0,1] \to X$ by $F = G_J$ on $\overline{J} \times [0,1]$, where $G_J$ is the homotopy of step [](#small-homotopy){.pf-ref} for $f|_{\overline{J}}$, and $F(s,t) = 0$ when $f(s) = 0$.
Then $F$ is well defined and continuous, and it is a homotopy rel $\{0,1\}$ from $f$ to the constant loop.

::: pf-proof
The closed intervals $\overline{J}$ meet each other and the zero set of $f$ only at endpoints, where every $G_J$ equals $0$; so $F$ is well defined, $F(s,0) = f(s)$, $F(s,1) = 0$, and $F(0,t) = F(1,t) = 0$.
$F$ is continuous on the open sets $J \times [0,1]$, so it remains to check continuity at $(s_0, t_0)$ with $f(s_0) = 0$, where $F(s_0,t_0) = 0$.
Let $\varepsilon > 0$.
By step [](#excursions){.pf-ref} only finitely many intervals $J$ have $M_J \ge \varepsilon$; choose a neighbourhood $V$ of $s_0$ meeting only those among them whose closure contains $s_0$ (at most two).
For each of those, $G_J$ is continuous on $\overline{J} \times [0,1]$ and vanishes on $\{s_0\} \times [0,1]$, so by compactness of $[0,1]$ we may shrink $V$ so that $|G_J| < \varepsilon$ on $(V \cap \overline{J}) \times [0,1]$.
At any other point $s \in V$, either $f(s) = 0$ and $F(s,t) = 0$, or $s$ lies in an interval $J$ with $M_J < \varepsilon$ and $|F(s,t)| \le M_J < \varepsilon$ by step [](#small-homotopy){.pf-ref}.
So $|F| < \varepsilon$ on $V \times [0,1]$.
:::

:::

::: pf-qed
Every loop at $0$ is nullhomotopic by step [](#homotopy){.pf-ref}, so $\pi_1(X, 0) = 0$, and $X$ is path-connected by step [](#pieces){.pf-ref}; hence $X$ is simply connected.
:::

:::

:::
