---
schema: qual/card@1
id: D-VARTODD
kind: definition
title: The Todd class and the Todd genus
classification:
  areas:
  - algebraic-geometry
  topics:
  - Chern Classes
  - Hirzebruch--Riemann--Roch
  - Euler Characteristic
relations:
- kind: related-to
  target: T-SRFRR
- kind: related-to
  target: D-CHOWRING
review: draft
prompts:
- What is the Todd genus?
---

::: {.definition title="Todd class and Todd genus"}
Let $X$ be a smooth projective variety of dimension $n$ over an algebraically closed field, and let $\alpha_1, \ldots, \alpha_n$ be the Chern roots of $T_X$.
The \dfn{Todd class} of $X$ is
$$\operatorname{td}(X) = \prod_{i=1}^n \frac{\alpha_i}{1 - e^{-\alpha_i}} = 1 + \frac{c_1}{2} + \frac{c_1^2 + c_2}{12} + \frac{c_1 c_2}{24} + \cdots,$$
with $c_i = c_i(T_X)$.
The \dfn{Todd genus} of $X$ is the degree of its component $\operatorname{td}_n(X)$ in dimension $0$.
:::

::: {.theorem title="Hirzebruch--Riemann--Roch for the structure sheaf"}
The Todd genus of $X$ equals $\chi(X, \OO_X) = \sum_i (-1)^i h^i(X, \OO_X)$; in particular it is an integer.
:::

::: {.example}
For a curve of genus $g$, $\operatorname{td}_1 = c_1/2$ has degree $(2 - 2g)/2 = 1 - g = \chi(\OO_C)$.
For a surface, $c_1^2 = K_X^2$ and $c_2 = e(X)$ is the topological Euler characteristic, and the theorem is Noether's formula $\chi(\OO_X) = \frac{1}{12}(K_X^2 + e(X))$.
:::
