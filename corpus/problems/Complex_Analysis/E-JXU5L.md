---
schema: qual/card@1
id: E-JXU5L
kind: problem
title: Dirichlet function is nowhere continuous and not Riemann integrable
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Integrability
  - Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
Show that the Dirichlet function $f(x) = \chi_{I \intersect \QQ}$ is not Riemann integrable and is everywhere discontinuous.
:::

::: {.solution}
Check $\sup f = 1$ and $\inf f = 0$ on every sub-interval, so $L(f, P) = 0$ and $U(f, P) = 1$ for every partition $P$ of $[0, 1]$.
Hence the upper and lower Darboux integrals differ ($\overline{\int_0^1} f = 1 \neq 0 = \underline{\int_0^1} f$), so $f$ is not Riemann integrable.

Discontinuity: fix $x \in [0,1]$.
Every open interval around $x$ contains both rational and irrational points (both $\QQ$ and $\RR \setminus \QQ$ are dense in $\RR$).
On the rational points of any such interval, $f$ takes the value $1$; on the irrational points, $f$ takes the value $0$.
Therefore, for any $\delta > 0$ there are points $y, z$ with $|y - x| < \delta$ and $|z - x| < \delta$ such that $f(y) = 1$ and $f(z) = 0$, so $|f(y) - f(z)| = 1$.
This means $f$ fails the $\varepsilon$-$\delta$ definition of continuity at $x$ for any $\varepsilon < 1$ (indeed, no limit $\lim_{y \to x} f(y)$ can exist, since approaching $x$ along rationals gives $1$ and along irrationals gives $0$).
Since $x$ was arbitrary, $f$ is discontinuous at every point of $[0,1]$.
:::
