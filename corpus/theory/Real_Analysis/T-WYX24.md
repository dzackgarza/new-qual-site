---
schema: qual/card@1
id: T-WYX24
kind: theorem
title: Generalized dominated convergence theorem
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Integrals
  - Integrals
  - L¹
relations: []
review: draft
---

::: {.theorem}
Let $(X,\mcm,\mu)$ be a [[D-QYLPH|measure]] space, and let $f_n\colon X\to\CC$ and $g_n\colon X\to[0,\infty)$ for $n\geq1$, $f\colon X\to\CC$, and $g\colon X\to[0,\infty)$ be [[D-DHFN4|measurable]].
Suppose that

- $f_n\to f$ almost everywhere;

- $g_n\in L^1(X,\mu)$ and $\abs{f_n}\leq g_n$ almost everywhere, for every $n$;

- $g_n\to g$ almost everywhere, $g\in L^1(X,\mu)$, and $\lim_{n\to\infty}\int_X g_n\dmu=\int_X g\dmu$.

Then $f\in L^1(X,\mu)$ and
$$
\lim_{n\to\infty}\int_X f_n\dmu=\int_X f\dmu.
$$
:::

::: {.remark}
The [[FT-LCR5P|dominated convergence theorem]] is the case $g_n=g$ for all $n$: the single dominating function $g$ is replaced by dominating functions $g_n$ that converge to $g$ almost everywhere and in integral.
:::
