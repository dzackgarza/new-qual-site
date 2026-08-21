---
schema: qual/card@1
id: E-E2LGY
kind: exercise
title: Pointwise limits of entire functions, uniform on segments, are entire and compactly
  convergent
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Uniform Convergence
  - Sequences of Functions
  - Morera
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of entire functions where

- $f_n \to g$ pointwise for some $g:\CC\to\CC$.
- On every line segment in $\CC$, $f_n \to g$ uniformly.

Show that 

- $g$ is entire, and
- $f_n\to g$ uniformly on every compact subset of $\CC$.
:::

:::{.solution}
Note that $g$ is entire by Morera's theorem, since $0 = \int_T f_n \to \int_T g$ by uniform convergence and the $f_n$ are holomorphic.
By Cauchy's theorem, up to a constant we have
\[
f_n(z) = \oint_T {f_n(\xi) \over \xi - z}\dxi
g(z) = \oint_T {g(\xi) \over \xi - z}\dxi
,\]
Thus fixing $K$ and $\eps$, for any $T \subseteq K$ containing $z$,
\[
\abs{f_n(z) - g(z)}
&= \abs{ 
\oint_T {f_n(\xi) \over \xi - z}\dxi
- \oint_T {g(\xi) \over \xi - z}\dxi
} \\
&\leq \oint_T {\abs{f_n(\xi) - g(\xi)} \over \xi - z }\dxi \\
&\leq \oint_T { \sup_{\xi\in T}\abs{f_n(\xi) - g(\xi)} \over \xi - z }\dxi \\
&\leq \oint_T { \eps \over \xi - z }\dxi \\
&= \eps C \to 0
,\]
where $n = n(\eps, T)$ can be chosen to produce this $\eps$ using that $f_n\to g$ uniformly on $T$.
Taking a sup over the $z$ enclosed by $T$ on the LHS yields a bound on the open region enclosed by $T$.
Taking a union of all such $T$ in $K$ yields an open cover of $K$, which by compactness has a finite subcover. 
This yields a finite collection $\ts{n = n(\eps, T_k)}_{k\leq N}$, and taking the maximum such $n$ yields a uniform bound for all of $K$.
:::



