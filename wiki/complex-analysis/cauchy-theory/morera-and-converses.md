---
title: Morera and converses
order: 40
topics:
- Morera

---

# Morera and converses

By [[T-B3BDO|Goursat's theorem]], every holomorphic function satisfies the hypothesis of [[T-LHSMY|Morera's theorem]], which is the converse for continuous functions; it also gives the holomorphy of [[D-AIQG3|locally uniform]] limits of holomorphic functions.

## Morera's theorem

[[T-LHSMY]]

::: {.slogan}
A continuous function whose integral over every triangle vanishes is holomorphic.

:::

## Locally uniform limits

[[C-TODSQ]]

::: {.remark}
For series, apply [[C-TODSQ|the holomorphy of locally uniform limits]] to the partial sums; the term-by-term derivative is the second conclusion of that card.

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
