---
title: How many zeros in this region?
order: 0
topics:
- Zeros
- Zeros of Holomorphic Functions
- Zeros of Polynomials
- Polynomial Roots
- Polynomials
---

# How many zeros in this region?

The zeros of a holomorphic function in a region are counted by factoring, by Rouché's theorem, by the argument principle, or, for a locally uniform limit, by Hurwitz's theorem.
The two contour criteria take different inputs and give the same kind of conclusion:

| | Argument principle | Rouché |
| --- | --- | --- |
| Input | $f\circ\gamma$, or the change of $\arg f$ along $\gamma$ | a decomposition $f=M+m$ with $\abs m<\abs M$ on $\gamma$ |
| Conclusion | $Z_f-P_f$ equals a winding number | $Z_f-P_f = Z_M-P_M$ |

## Explicit factorization

For a polynomial whose roots can be computed, the factorization gives the zeros and their multiplicities.

::: {.fact}
\envlist

- A zero of $f$ of multiplicity $m\geq2$ is a zero of $f'$, and a solution of $f(z) = a$ of multiplicity $m\geq2$ is a zero of $f'$.

- $f$ and $f-w$ have the same derivative, so the multiple solutions of $f(z) = w$, for every $w$, lie among the zeros of $f'$.

Both follow from the factorisation of a [[D-65VIK|zero of order $m$]]: $f(z)=(z-z_0)^mg(z)$ with $g(z_0)\neq0$ gives $f'=(z-z_0)^{m-1}\qty{mg+(z-z_0)g'}$, whose bracket is $mg(z_0)\neq0$ at $z_0$, so $f'$ vanishes at $z_0$ to order $m-1\ge1$; and $f-w$ differs from $f$ by a constant, so the two have the same derivative.
:::

## A dominant term on the boundary

[[T-CJCKL]]

The criterion applies when $M$ is a term whose zeros inside $\gamma$ are known, such as one monomial of a polynomial that dominates on $\abs z = R$, or an entire function compared with a polynomial.
The dominant term depends on the curve: for $z^4+6z+3$ it is $z^4$ on $\abs z = 2$ and $6z$ on $\abs z = 1$ ([[complex-analysis/counting-zeros/rouches-theorem|Rouché's theorem]]).

::: {.example title="Rouché's theorem fails with $\abs m\leq\abs M$ on $\gamma$"}
On $\gamma = \theset{\abs z = 1}$, take $M(z)\coloneqq z$ and $m(z)\coloneqq -1$, so $\abs m\leq\abs M$ on $\gamma$ with equality everywhere.
Then $M$ has one zero in $\DD$, while $M+m = z-1$ has none in $\DD$; its zero lies on $\gamma$.
:::

## The image of the boundary curve

[[T-52HK6]]

The criterion applies when the image curve $f\circ\gamma$ or the change of $\arg f$ along $\gamma$ is known, and it counts zeros and poles together.

## A locally uniform limit

[[T-FZWEC]]

Consequently, on a connected open set, a limit of nowhere-zero functions is nowhere zero or identically zero, and a limit of univalent functions is univalent or constant ([[T-SULVA]]).
Applying [[T-CJCKL|Rouché's theorem]] to $f-w$ counts the solutions of $f(z) = w$ in $\Omega$ for each $w$, and [[complex-analysis/counting-zeros/the-argument-principle#Solutions of an equation|the argument principle]] shows the count is constant on each component of $\CC\sm f(\bd\Omega)$.

