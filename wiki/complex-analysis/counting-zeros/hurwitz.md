---
title: Hurwitz's theorem
order: 30
topics:
- Hurwitz

---

# Hurwitz's theorem

[[D-AIQG3]]

[[D-OHFRH]]

[[T-FZWEC]]

::: {.example title="A double zero born from two simple ones"}
The functions $f_k(z) = z^2 + z/k = z(z+1/k)$ converge locally uniformly to $f(z) = z^2$, which has a double zero at $0$.
Hurwitz's theorem predicts exactly two zeros of $f_k$ near $0$ for large $k$, and there they are: $0$ and $-1/k$, each simple, both inside $\abs z<\delta$ as soon as $1/k<\delta$; the count is two with multiplicity, matching the order of the limit's zero.
Outside a fixed neighbourhood of $0$ the limit vanishes nowhere, and for large $k$ neither do the $f_k$.
:::

::: {.slogan}
Near a zero of order $n$ of the limit, the $n$ zeros of $f_k$ for large $k$ converge to that zero.
:::

::: {.corollary}
Let $\Omega$ be a connected open set and let $f_k\to f$ [[D-AIQG3|locally uniformly]] on $\Omega$, with each $f_k$ holomorphic and nowhere zero on $\Omega$.
Then $f$ is nowhere zero on $\Omega$ or identically zero.

This is [@Ahl73, ch. 5, §1.1, Theorem 2], Hurwitz's theorem in the book's numbering: analytic functions that vanish nowhere in a region, converging uniformly on every compact subset, have a limit that is identically zero or vanishes nowhere. The connectedness above is what the region of the theorem provides.
:::

::: {.remark}
In the proof of the [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|Riemann mapping theorem]], [[complex-analysis/conformal-maps/normal-families-and-montel|Montel's theorem]] produces a locally uniform limit of univalent maps, and [[T-SULVA]] shows the limit is univalent because its derivative at the base point is nonzero, so it is not constant.
:::

[[T-SULVA]]
