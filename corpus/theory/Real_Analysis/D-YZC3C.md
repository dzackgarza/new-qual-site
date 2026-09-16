---
schema: qual/card@1
id: D-YZC3C
kind: definition
title: Uniform convergence
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
Let $S$ be a set, and let $f_n\colon S\to\CC$ for $n\geq 1$ and $f\colon S\to\CC$ be functions.
The sequence $(f_n)$ \dfn{converges uniformly} to $f$ on $S$ if
$$
(\forall \varepsilon>0)\,(\exists n_0 = n_0(\varepsilon))\,(\forall x \in S)\,(\forall n>n_0)\quad \abs{f_n(x)-f(x)}<\varepsilon.
$$
:::

::: {.remark}
Negating the quantifiers, $(f_n)$ does not converge uniformly to $f$ on $S$ if and only if
$$
(\exists \varepsilon>0)\,(\forall n_0)\,(\exists x = x(n_0) \in S)\,(\exists n>n_0)\quad \abs{f_n(x)-f(x)} \geq \varepsilon.
$$
The point $x$ at which the estimate fails may depend on $n_0$.
:::
