---
schema: qual/card@1
id: PR-5A64G
kind: proposition
title: Zeros and their orders
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Power Series
  - Holomorphic Functions
relations: []
review: draft
---

::: {.proposition}
Let $\Omega\subseteq\CC$ be a connected open set, let $f$ be [[D-V6UQJ|analytic]] on $\Omega$ and not identically zero, and let $z_0\in\Omega$ with $f(z_0)=0$.
Then there exist a unique integer $n\ge1$, a neighborhood $U\subseteq\Omega$ of $z_0$, and a function $g$ holomorphic and nonvanishing on $U$ such that
$$
f(z) = (z-z_0)^n g(z)\quad\text{for all } z\in U.
$$
This $n$ is the order of the [[D-65VIK|zero]] $z_0$, and it is characterized by each of the following:

- $f^{(k)}(z_0)=0$ for $0\le k\le n-1$ and $f^{(n)}(z_0)\neq0$;

- the Taylor expansion of $f$ at $z_0$ has the form $f(z) = \sum_{k\geq n} c_k (z-z_0)^k$ with $c_n\neq 0$.
:::

::: {.proof}
Write $f(z)=\sum_{k\ge0}c_k(z-z_0)^k$ on a disc $U$ about $z_0$, with $c_k=f^{(k)}(z_0)/k!$.
If every $c_k$ vanished, $f$ would vanish on $U$, and by the identity theorem on the connected set $\Omega$, $f$ would be identically zero.
So there is a least $n$ with $c_n\neq0$, and $n\ge1$ because $c_0=f(z_0)=0$; this $n$ satisfies both characterizations.
Put $g(z)\coloneqq\sum_{k\ge n}c_k(z-z_0)^{k-n}$, which converges on $U$, is holomorphic there, and satisfies $f(z)=(z-z_0)^ng(z)$ and $g(z_0)=c_n\neq0$; shrinking $U$, continuity makes $g$ nonvanishing on $U$.
If also $f(z)=(z-z_0)^mh(z)$ near $z_0$ with $h(z_0)\neq0$ and, say, $m>n$, then $g(z)=(z-z_0)^{m-n}h(z)$ near $z_0$, forcing $g(z_0)=0$; hence $n$ is unique.
:::
