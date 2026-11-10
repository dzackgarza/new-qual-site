---
schema: qual/card@1
id: E-KY2W7
kind: problem
title: The dictionary order plane is metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Order Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 2, printed p. 126, with Exercise
    16.9 and Theorem 20.1; the stored statement is the printed request.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.2, PDF p. 17. The dictionary order topology on
    R x R is R_d x R by Exercise 16.9, both factors are metrizable, and the maximum metric
    on a product induces the product topology. (tmp/sources/munkres-solutions-positron-
    ch2.pdf).
---

::: {.exercise}

Show that $\RR \times \RR$ in the dictionary order topology is metrizable.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.2, PDF p. 17** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the reduction and the product metric are theirs.

By Exercise 16.9 the dictionary order topology on $\RR\times\RR$ is the product topology $\RR_{d}\times\RR$, where $\RR_{d}$ is $\RR$ with the discrete topology. The discrete topology is induced by the discrete metric (the topology in which every set is open, Theorem 20.1/Example 1 of §20) and the usual topology of $\RR$ is induced by $d(a,b)=\abs{a-b}$. So it suffices to show that a product of two metrizable spaces is metrizable.

Let $X$ have metric $d$ and $Y$ have metric $d'$, and on $X\times Y$ put
$$
\rho(x\times y,\,w\times z)=\max\{d(x,w),\,d'(y,z)\}.
$$
This is a metric: it is nonnegative, vanishes exactly when $x=w$ and $y=z$, and is symmetric. For the triangle inequality let $w\times z$ be an intermediate point; then by the triangle inequality in each factor
$$
\rho(x\times y,u\times v)=\max\{d(x,u),d'(y,v)\}\le\max\{d(x,w)+d(w,u),\ d'(y,z)+d'(z,v)\}
\le\rho(x\times y,w\times z)+\rho(w\times z,u\times v),
$$
the last step because the maximum of a sum of two pairs is at most the sum of the maximums.

It induces the product topology. If $B_{d}(x,r_{1})\times B_{d'}(y,r_{2})$ is a product basis element and $r=\min\{r_{1},r_{2}\}$, then
$$
x\times y\in B_{\rho}(x\times y,r)\subset B_{d}(x,r_{1})\times B_{d'}(y,r_{2});
$$
conversely, for a $\rho$-ball at $x\times y$ of radius $\delta$,
$$
x\times y\in B_{d}(x,\delta)\times B_{d'}(y,\delta)\subset B_{\rho}(x\times y,\delta).
$$
So the two topologies coincide and $X\times Y$ is metrizable. Hence $\RR\times\RR$ in the dictionary order topology is metrizable.
:::
