---
schema: qual/card@1
id: E-TM2Z4
kind: exercise
title: Images of sequences of poles converge to anything
classification:
  areas:
  - complex-analysis
  topics:
  - Casorati-Weierstrass
  - Poles
  - Singularities
  - Identity Theorem
relations: []
review: draft
---

::: {.exercise title="Images of sequences of poles converge to anything"}
Let $f$ be holomorphic in $0 < \abs{z-z_0} < r$, minus a sequence of poles $\ts{z_k} \to z_0$.
Show that for any $w\in \CC$, there is a sequence $\ts{w_k}\to z_0$ with $f(w_k)\to w$.
:::

::: {.solution}
Toward a contradiction, fix $w$ and suppose no such sequence exists.
Then for every sequence $w_k\to z_0$, there is an $\eps$ such that $\abs{f(w_k) - w} \geq \eps$ for all $k$.
So the function $g(z) \da {1\over f(z) - w}$ has no poles in $D_r(z_0)\smts{z_0}$, and since each $z_k$ is a pole of $f$, each is a zero of $g$.
If $z_0$ is a singularity, since $\abs{g(z)} \leq \eps$, it is removable and thus $g$ can be extended holomorphically over $z_0$.
By continuity, since $z_k\to z_0$ with $g(z_k) = 0$, we have $g(z_0) = 0$.
By the identity principle, $g\equiv 0$, which means that every $z\in D_r(z_0)\smts{z_0}$ is a zero of $g$ and thus a pole of $f$.
But this contradicts that $f$ is holomorphic on $D_r(z_0)\smts{z_k}$.
$\contradiction$
:::
