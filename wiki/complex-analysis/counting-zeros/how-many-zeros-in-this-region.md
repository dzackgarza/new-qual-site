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

The zeros of a holomorphic function in a region can be counted by factoring, by Rouché's theorem, by the argument principle, or, for a locally uniform limit, by Hurwitz's theorem.
Each applies under different information about the function.

## Explicit factorization

For a polynomial whose roots can be computed, the factorization gives the zeros and their multiplicities.

::: {.fact}
\envlist

- A zero of $f$ of multiplicity $m \geq 2$ is a zero of $f'$, and a solution of $f(z) = a$ of multiplicity $m\geq 2$ is a zero of $f'$.

- $f$ and $f-w$ have the same derivative, so the multiple solutions of $f(z)=w$, for every $w$, lie among the zeros of $f'$.
:::

## A dominant term on the boundary

**Rouché's theorem.**
If $f = M + m$ with $\abs{m} < \abs{M}$ on the boundary curve $\gamma$, then $f$ and $M$ have the same number of zeros minus poles inside $\gamma$ ([[T-CJCKL]]).
This applies when $M$ is a term whose zeros inside $\gamma$ are known, such as one monomial of a polynomial that dominates on $\abs z = R$, or an entire function compared with a polynomial.
The dominant term depends on the curve: for $z^4+6z+3$, it is $z^4$ on $\abs z = 2$ and $6z$ on $\abs z = 1$ ([[complex-analysis/counting-zeros/rouches-theorem|Rouché's theorem]]).

The inequality must be strict at every point of $\gamma$, and for meromorphic functions the conclusion is an equality of zeros minus poles.

## The image of the boundary curve

**Argument principle.**
For $f$ meromorphic with no zeros or poles on $\gamma$, the number of zeros minus poles inside $\gamma$ is the winding number of $f\circ\gamma$ about $0$ ([[T-52HK6]]).
It applies when the image curve $f\circ\gamma$ or the change of $\arg f$ along $\gamma$ is known, and it counts zeros and poles together.

## A locally uniform limit

**Hurwitz's theorem.**
If $f_n \to f$ locally uniformly on a connected open set, then near a zero of order $n$ of $f$, the functions $f_k$ have exactly $n$ zeros for large $k$ ([[T-FZWEC]]).
Consequently a limit of nowhere-zero functions is nowhere zero or identically zero, and a limit of univalent functions is univalent or constant ([[T-SULVA]]).

## Solutions of $f(z) = w$

Rouché's theorem applies to $f - w$.
The argument principle expresses the number of solutions in $\Omega$ as
$$
F(w) \coloneqq {1\over 2\pi i} \oint_{\bd \Omega} {f'(z) \over f(z) - w} \dz
,$$
which is continuous and integer valued on each connected component of $\CC\sm f(\bd\Omega)$, hence constant there.
So the number of solutions of $f(z)=w$ in $\Omega$ is the same for all $w$ in one component of $\CC\sm f(\bd\Omega)$.

## Comparison

|  | Argument principle | Rouché |
| --- | --- | --- |
| Input | $f\circ\gamma$, or the change of $\arg f$ along $\gamma$ | a decomposition $f=M+m$ with $\abs m<\abs M$ on $\gamma$ |
| Conclusion | $Z_f - P_f$ equals a winding number | $Z_f - P_f = Z_M - P_M$ |

Rouché's theorem is proved from the argument principle.
