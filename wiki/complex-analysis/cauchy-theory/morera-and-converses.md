---
title: Morera and converses
order: 40
topics:
- Morera

---

# Morera and converses

By Goursat's theorem, a holomorphic function has vanishing integrals over triangles.
Morera's theorem is the converse for continuous functions, and it shows that [[D-AIQG3|locally uniform]] limits and series of holomorphic functions are holomorphic.

## Morera's theorem

[[T-LHSMY]]

::: {.slogan}
A continuous function whose integral over every triangle vanishes is holomorphic.

:::

::: {.remark title="Rectangles"}
The conclusion also holds for continuous $f$ whose integrals over the boundaries of all closed rectangles in $\Omega$ with sides parallel to the axes vanish.

:::

## Locally uniform limits

[[C-TODSQ]]

::: {.remark}
Applied to partial sums, [[C-TODSQ|the holomorphy of locally uniform limits]] shows that a series $\sum_k f_k$ of holomorphic functions converging uniformly on compact subsets of $\Omega$ is holomorphic and can be differentiated term by term.

:::

::: {.example title="A series that is holomorphic without a closed form for its sum"}
On $\DD$ the series $f(z)\coloneqq\sum_{k\geq1}z^k/k^2$ converges uniformly, since $\abs{z^k/k^2}\leq1/k^2$ and $\sum_k1/k^2<\infty$, so $f$ is the uniform limit of its polynomial partial sums.
By the limit theorem $f$ is holomorphic on $\DD$ and
$$
f'(z) = \sum_{k\geq1}{z^{k-1}\over k} = -{\log(1-z)\over z},
$$
the differentiated series converging uniformly on every compact subset of $\DD$; at $z=1/2$ the two series give $f(1/2) = 0.5822405\ldots$ and $f'(1/2) = 1.3862943\ldots$, the latter equal to $-\log(1/2)/(1/2)$.
:::

## Goursat

Goursat's theorem proves Cauchy's theorem for triangles and rectangles with no continuity assumption on $f'$.

[[T-B3BDO]]

## Problems

[[E-QO2S7]]
