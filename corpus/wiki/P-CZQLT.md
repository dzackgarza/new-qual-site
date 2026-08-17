---
schema: qual/card@1
id: P-CZQLT
kind: problem
title: "Let $\\ts{f_n}_{n=1}^\\infty$ is a sequence of holomorphic functions on\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - uniform-convergence
  - sequences-of-functions
  - cauchy-integral-formula
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Let $\ts{f_n}_{n=1}^\infty$ is a sequence of holomorphic functions on $\DD$ and $f$ is also holomorphic on $\DD$. 
Show that the following are equivalent:

- $f_n\to f$ uniformly on compact subsets of $\DD$.
- For $0 < r < 1$,
\[
\int_{\abs z = r} \abs{f_n(z) - f(z)} \abs{dz} \convergesto{n\to\infty}0
.\]

> Note: $\abs{\dz} = \abs{\gamma'(t)}\dt$ for $\gamma$ a parameterization of the curve.

:::

:::{.solution}
$\implies$: 

- Fix $r \in (0, 1)$ and let $\gamma = \ts{\abs{z} = r}$.
  This is compact, so $f_n\to f$ uniformly on $\gamma$:
\[
\int_\gamma \abs{f_n(z) - f(z) } \dz 
&\leq\int_\gamma \sup_{w\in \gamma } \abs{f_n(w) - f(w) } \dz \\
&\leq\int_\gamma \norm{f_n(w) - f(w) }_{\infty} \dz \\
&= \norm{f_n(w) - f(w) }_{\infty} \int_\gamma \dz \\
&= \norm{f_n(w) - f(w) }_{\infty} \length(\gamma) \\
&\convergesto{n\to\infty} 0
.\]

$\impliedby$:

- Let $K$ be compact, then choose $\gamma$ enclosing but not intersecting $K$.
- Since $\gamma, K$ are disjoint compact sets, define $M \da \inf \ts{\abs{z-\xi} \st z\in K, \xi\in \gamma}$, the $0<M<\infty$.

- Apply Cauchy's formula to the function $F_n(z) \da f_n(z) - f(z)$, where we want to show $\abs{F_n(z)} < \eps$:
\[
F_n(z) 
&= {1\over 2\pi i} \int_\gamma { F_n(\xi) \over z-\xi} \dxi \\
\implies \abs{f_n(z) - f(z) } 
&\leq {1\over 2\pi }\int_\gamma \abs{f_n(\xi) - f(\xi) \over z-\xi} \dxi \\
&\leq {1\over 2\pi} \int_\gamma {\abs{ f_n(\xi) - f(\xi) } \over 
M} \dxi \\
&\leq {1\over 2\pi M} \int_\gamma {\abs{ f_n(\xi) - f(\xi) } } \abs{\dxi} \\
,\]
where by hypothesis we can bound this integral by an $\eps$.
So given $\eps$, choose $n$ large enough to bound the integral as above by some $\eps$ depending only on $n$ and not on $z$.
Taking $\sup$ of both sides yields $\norm{f_n - f}_{\infty, K} \leq {\eps\over 2\pi M}$, so $f_n\to f$ uniformly on $K$.
:::
