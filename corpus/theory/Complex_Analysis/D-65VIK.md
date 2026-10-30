---
schema: qual/card@1
id: D-65VIK
kind: definition
title: Order of a zero of a holomorphic function
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Holomorphic Functions
relations: []
review: draft
---

::: {.definition}
Let $\Omega\subseteq\CC$ be open, let $f$ be [[D-E7A5W|holomorphic]] on $\Omega$, let $z_0\in\Omega$, and let $n\ge1$ be an integer.
The point $z_0$ is a \dfn{zero of order $n$} of $f$ if there exist an open neighborhood $U\subseteq\Omega$ of $z_0$ and a holomorphic function $g\colon U\to\CC$ with $g(z_0)\neq0$ such that
$$
f(z)=(z-z_0)^n g(z)\qquad\text{for all } z\in U.
$$
A zero of order $1$ is a \dfn{simple zero}.
:::

::: {.proposition}
Let $\Omega\subseteq\CC$ be a connected open set and let $f$ be holomorphic on $\Omega$ and not identically zero.
Then every $z_0\in\Omega$ with $f(z_0)=0$ is a zero of order $n$ of $f$ for exactly one integer $n\ge1$.
:::

::: {.remark title="Variations"}
The order $n$ is characterized by $f^{(k)}(z_0)=0$ for $0\le k\le n-1$ and $f^{(n)}(z_0)\neq0$, equivalently by the Taylor expansion $f(z)=\sum_{k\ge n}c_k(z-z_0)^k$ with $c_n\neq0$.
The neighborhood $U$ may be taken to be all of $\Omega$: the function $g(z)\coloneqq f(z)/(z-z_0)^n$ for $z\neq z_0$, with $g(z_0)\coloneqq f^{(n)}(z_0)/n!$, agrees near $z_0$ with the Taylor series $\sum_{k\ge n}c_k(z-z_0)^{k-n}$, so it is holomorphic on $\Omega$ and $f=(z-z_0)^ng$ on $\Omega$.
Shrinking $U$ instead, $g$ may be taken nonvanishing on $U$, by continuity.
:::
