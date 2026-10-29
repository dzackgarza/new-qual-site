---
schema: qual/card@1
id: E-LXPI7
kind: problem
title: Constructing functions with specified singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Singularities
  - Essential Singularities
  - Poles
  - Removable Singularities
relations: []
review: draft
---

::: {.exercise}
Determine a function with

- An essential singularity at $z=1$
- An essential singularity at $z=0$
- A pole of order 1 at $z=1-i$
- A pole of order 2 at $z=1+i$
- A removable singularity at $z=7$

:::

::: {.solution}
A product of one function per singularity can fail, because a zero of one factor can cancel a pole of another. A sum cannot: near each prescribed point, the other summands are holomorphic.

::: pf

::: pf-step
$f(z)\coloneqq e^{1/(z-1)}+e^{1/z}+\dfrac1{z-(1-i)}+\dfrac1{(z-(1+i))^2}+\dfrac{z-7}{\sin(z-7)}$ has the required singularities.

::: pf-proof
Each summand is holomorphic near every prescribed point other than its own: the last summand is singular only at $7+k\pi$, $k\in\ZZ$, none of which is $0$, $1$, or $1\pm i$. Adding a function holomorphic near a point does not change the type of an isolated singularity there. At its own point, $e^{1/(z-1)}$ and $e^{1/z}$ have essential singularities (their Laurent series have infinitely many negative powers), the third and fourth summands have poles of orders $1$ and $2$, and $\frac{z-7}{\sin(z-7)}\to1$ as $z\to7$.
:::

:::

:::

:::
