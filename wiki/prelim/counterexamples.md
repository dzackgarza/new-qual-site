---
title: Counterexamples
order: 3
topics:
- Counterexamples
---

# Counterexamples

Each item refutes one implication, and states the example that refutes it.

## Limits and continuity

::: {.example title="Continuity does not imply differentiability"}
$\abs x$ is continuous on $\RR$ and has no derivative at $0$, the difference quotient being $1$ to the right and $-1$ to the left.
The Weierstrass function $\sum_{k\geq0} a^k\cos(b^k\pi x)$, for $0<a<1$ and $b$ an odd integer with $ab>1+3\pi/2$, is continuous on $\RR$ and differentiable at no point.

:::

::: {.example title="Differentiability does not imply continuous differentiability"}
The function $f(x) = x^2\sin(1/x)$ for $x\neq0$ and $f(0) = 0$ is differentiable on $\RR$, with $f'(0) = 0$ and $f'(x) = 2x\sin(1/x) - \cos(1/x)$ for $x\neq0$, and $f'$ has no limit at $0$.

:::

::: {.example title="Continuity on a bounded interval does not imply uniform continuity"}
$1/x$ is continuous on $(0,1)$, and on the sequence $x_n = 1/n$ the difference $\abs{1/x_n - 1/x_{2n}} = n$ is unbounded, so the function is not uniformly continuous there.
A continuous function on a closed bounded interval is uniformly continuous.

:::

::: {.example title="A continuous function on a bounded interval need not attain its bounds"}
$x$ on $(0,1)$ has supremum $1$ and infimum $0$, and attains neither.
A continuous function on a compact set attains both.

:::

## Sequences and series

::: {.example title="Terms tending to zero do not imply convergence"}
The harmonic series $\sum_n 1/n$ diverges, though $1/n\to0$: its partial sums satisfy $\sum_{n=2^k}^{2^{k+1}-1}1/n \geq 2^k/2^{k+1} = 1/2$, so they are unbounded.

:::

::: {.example title="Convergence does not imply absolute convergence"}
$\sum_n (-1)^{n+1}/n$ converges by the alternating series test, and $\sum_n 1/n$ diverges.
By [[T-REARR|Riemann's rearrangement theorem]] the terms of a series that converges but not absolutely can be rearranged to any prescribed pair of limit points, so the sum of this one is a property of the order of its terms and not of the set of them.

:::

::: {.example title="A convergent sequence need not be eventually monotone"}
$(-1)^n/n$ converges to $0$ and alternates in sign for every $n$, so it is monotone on no tail.

:::

::: {.example title="Pointwise convergence does not preserve continuity"}
$x^n$ on $[0,1]$ converges pointwise to the function that is $0$ on $[0,1)$ and $1$ at $1$, and each $x^n$ is continuous.

:::

::: {.example title="Uniform convergence does not preserve differentiability"}
$f_n(x) = \sqrt{x^2 + 1/n}$ is differentiable, and $f_n\to\abs x$ uniformly on $\RR$, since $0\leq f_n(x)-\abs x\leq 1/\sqrt n$.
The limit $\abs x$ is not differentiable at $0$.
Uniform convergence does preserve continuity and Riemann integrability, and if each $f_n$ is continuously differentiable and $f_n'$ converges uniformly, then $f = \lim f_n$ is differentiable with $f' = \lim f_n'$.

:::

## Derivatives and integrals

::: {.example title="A derivative need not be continuous"}
The derivative of $x^2\sin(1/x)$, extended by $0$ at $0$, is $2x\sin(1/x) - \cos(1/x)$ away from $0$ and $0$ at $0$, so it is discontinuous at $0$.

:::

::: {.example title="A function with the intermediate value property need not be continuous"}
Every derivative has the intermediate value property ([[P-BKF15-3A|Darboux's theorem]]), so a function without that property is not a derivative: the step function equal to $0$ on $[0,1/2)$ and $1$ on $[1/2,1]$ takes neither value strictly between $0$ and $1$, and is therefore no derivative.

:::

::: {.example title="A bounded function need not be Riemann integrable"}
The indicator function of $\QQ\intersect[0,1]$ is bounded by $1$, and on every subinterval of a partition it has supremum $1$ and infimum $0$, so every upper sum is $1$ and every lower sum is $0$.
Its set of discontinuities is all of $[0,1]$, of measure $1$, which is also what excludes it from the Riemann integrable functions under [[PR-TDH2A|Lebesgue's criterion for Riemann integrability]].

:::

::: {.example title="$f' = 0$ implies that $f$ is constant only on an interval"}
On the open set $(0,1)\union(2,3)$, the function equal to $0$ on $(0,1)$ and to $1$ on $(2,3)$ has derivative $0$ everywhere and is not constant.

:::

## Algebra and linear algebra

::: {.example title="Repeated eigenvalues do not prevent diagonalizability"}
The identity matrix $I_2$ has the single eigenvalue $1$, repeated, and is diagonal.

:::

::: {.example title="A real square matrix need not have a real eigenvector"}
The rotation $\matt{0}{-1}{1}{0}$ has characteristic polynomial $x^2 + 1$, so its eigenvalues are $\pm i$ and it has no real eigenvector.

:::

::: {.example title="Equal characteristic polynomials do not imply similarity"}
The matrices $\matt{0}{0}{0}{0}$ and $\matt{0}{1}{0}{0}$ both have characteristic polynomial $x^2$, and the second has rank $1$ while the first has rank $0$, so they are not similar.
The matrices $J_2(0)\oplus J_2(0)$ and $J_2(0)\oplus J_1(0)\oplus J_1(0)$ have the same characteristic polynomial $x^4$ and the same minimal polynomial $x^2$, and their kernels have dimensions $2$ and $3$.

:::

::: {.example title="A group of prime power order need not be abelian"}
Groups of order $p$ and of order $p^2$ are abelian, and the dihedral group $D_4$ of order $8 = 2^3$ is not: its rotation $r$ and reflection $s$ satisfy $rs = sr^{-1}\neq sr$.

:::
