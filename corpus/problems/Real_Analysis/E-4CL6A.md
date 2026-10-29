---
schema: qual/card@1
id: E-4CL6A
kind: problem
title: Complete totally bounded subsets of a metric space are compact
classification:
  areas:
  - real-analysis
  topics:
  - Compactness
  - Completeness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that if a subset of a metric space is complete and totally bounded, then it is compact.
:::

::: {.solution}
Let $X$ be the subset with the restricted metric $d$, so $(X,d)$ is a complete, totally bounded metric space. A metric space is compact if and only if it is sequentially compact, so it suffices to show that an arbitrary sequence $(x_n)$ in $X$ has a convergent subsequence.

::: pf

::: {.pf-step #nested}
There are nested subsequences $(x_{m,k})_{k\ge1}$, $m\ge1$, each a subsequence of the previous one (with $(x_{0,k})=(x_n)$), and points $y_m\in X$ with $x_{m,k}\in B(y_m,1/m)$ for all $k$.

::: pf-proof
Given $(x_{m-1,k})$, total boundedness covers $X$ by finitely many balls of radius $1/m$. By the pigeonhole principle one of them, $B(y_m,1/m)$, contains $x_{m-1,k}$ for infinitely many $k$; let $(x_{m,k})$ be the subsequence of those terms.
:::

:::

::: {.pf-step #cauchy}
The diagonal sequence $z_j=x_{j,j}$ is a Cauchy subsequence of $(x_n)$.

::: pf-proof
By step [](#nested){.pf-ref}, $(z_j)$ is a subsequence of $(x_n)$, and for each $m$ the tail $(z_j)_{j\ge m}$ is a subsequence of $(x_{m,k})$, so $z_j\in B(y_m,1/m)$ for $j\ge m$. Hence for $j,\ell\ge m$,
$$
d(z_j,z_\ell)\le d(z_j,y_m)+d(y_m,z_\ell)<\frac2m,
$$
which is less than any given $\varepsilon>0$ once $m>2/\varepsilon$.
:::

:::

::: pf-step
$(x_n)$ has a subsequence converging in $X$, so $X$ is compact.

::: pf-proof
By step [](#cauchy){.pf-ref} and completeness of $X$, $(z_j)$ converges to a point of $X$.
:::

:::

:::

:::
