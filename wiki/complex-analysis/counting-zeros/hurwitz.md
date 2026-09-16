---
title: Hurwitz's theorem
order: 30
topics:
- Hurwitz

---

# Hurwitz's theorem

[[D-G42SR]]

[[D-OHFRH]]

[[T-FZWEC]]

::: {.slogan}
Near a zero of order $n$ of the limit, the $n$ zeros of $f_k$ for large $k$ converge to that zero.
:::

::: {.corollary}
Let $\Omega$ be a connected open set and let $f_k\to f$ locally uniformly on $\Omega$, with each $f_k$ holomorphic and nowhere zero on $\Omega$.
Then $f$ is nowhere zero on $\Omega$ or identically zero.
:::

::: {.proof}
If $f$ is not identically zero and $f(z_0)=0$, then $z_0$ is a zero of finite order $n\geq 1$ by the identity principle, and [[T-FZWEC]] gives zeros of $f_k$ near $z_0$ for large $k$, a contradiction.
:::

::: {.remark}
In the proof of the [[complex-analysis/conformal-maps/the-riemann-mapping-theorem|Riemann mapping theorem]], [[complex-analysis/conformal-maps/normal-families-and-montel|Montel's theorem]] produces a locally uniform limit of univalent maps, and [[T-SULVA]] shows the limit is univalent because its derivative at the base point is nonzero, so it is not constant.
:::

[[T-SULVA]]
