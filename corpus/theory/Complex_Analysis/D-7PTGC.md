---
schema: qual/card@1
id: D-7PTGC
kind: definition
title: Modular form
prompts:
- What is a modular form of weight $k$ for $\SL_2(\ZZ)$?
- Why is there no modular form of odd weight?
classification:
  areas:
  - complex-analysis
  topics:
  - Modular Forms
  - Upper Half-Plane
relations: []
review: draft
---

::: {.definition}
Let $k$ be an even integer.
A \dfn{modular form of weight $k$ for $\SL_2(\ZZ)$} is a [[D-E7A5W|holomorphic]] function $f\colon\HH\to\CC$ such that
$$
f\qty{\frac{az+b}{cz+d}} = (cz+d)^{k}f(z)\qquad\text{for all }\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\SL_2(\ZZ)\text{ and all }z\in\HH,
$$
and such that $f$ is holomorphic at $\infty$: writing $q\coloneqq e^{2\pi iz}$, the function $f$ has an expansion $f(z) = \sum_{n\geq0}a_nq^n$ on $\theset{\Im z>1}$ with no negative powers of $q$.
A modular form is a \dfn{cusp form} if moreover $a_0 = 0$ [@Ser73, ch. 7].
:::

::: {.proposition}
There is no nonzero modular form of odd weight.
:::

::: {.remark}
Because $-I\in\SL_2(\ZZ)$ acts trivially on $\HH$ and the factor $(cz+d)^k$ becomes $(-1)^k$, a function satisfying the transformation law for an odd $k$ satisfies $f=-f$, hence vanishes.
The $q$-expansion is the Fourier expansion of $f$ in the local coordinate $q = e^{2\pi iz}$ at $\infty$.
:::
