---
title: Which inequality?
order: 0
problems:
  topics:
  - Lp Spaces
  - Norms
---

# Which inequality?

Almost every $L^p$ problem is one inequality applied once.
The question is which, and it is decided by the shape of what you are bounding.

| You are bounding | Use | Statement |
| --- | --- | --- |
| $\int \abs{fg}$ | Hölder | $\norm{fg}_1 \leq \norm f_p \norm g_q$, $\frac1p+\frac1q=1$ |
| $\norm{f+g}_p$ | Minkowski | the triangle inequality for $\norm\cdot_p$ |
| $\mu(\abs f > t)$ | Chebyshev | $\mu(\abs f > t) \leq t^{-p}\norm f_p^p$ |
| $\varphi\qty(\int f)$ for convex $\varphi$ | Jensen | $\varphi\qty(\int f) \leq \int \varphi\circ f$ on a probability space |
| $\norm{f * g}_r$ | Young | $\frac1r = \frac1p+\frac1q-1$ |

## Hölder is the one to try first

Its uses are not only bounding a product:

- **Nesting.** On a finite measure space, $p < q$ gives $L^q \subseteq L^p$, by Hölder against $g = 1$.
  On $\RR$ with Lebesgue measure there is no nesting in either direction, which is why $\sin(x)/x$ can be in $L^2$ and not $L^1$.

- **Interpolation.** $\norm f_r \leq \norm f_p^{\theta}\norm f_q^{1-\theta}$ for $\frac1r = \frac\theta p + \frac{1-\theta}q$, which is Hölder applied to $\abs f^{r\theta}\cdot\abs f^{r(1-\theta)}$.

- **Duality.** The pairing $\inner fg = \int fg$ is bounded exactly by Hölder, which is what makes $(L^p)^* = L^q$.

Equality in Hölder holds when $\abs f^p$ and $\abs g^q$ are proportional, and that case is often what a problem is really asking about.

## Chebyshev converts norms into measures

Any bound on $\norm f_p$ bounds the size of the set where $f$ is large, and that is the only way to get from an integral hypothesis to a pointwise one.
It is the first step of most a.e. convergence arguments, usually followed by Borel--Cantelli.

## The exponents to keep straight

- $p = 1$: no dual pairing with itself; $(L^1)^* = L^\infty$ but $(L^\infty)^* \supsetneq L^1$.

- $p = 2$: the only Hilbert space in the family, so orthogonality and projection are available and nothing else in the scale has them.

- $p = \infty$: the norm is an essential supremum, so "bounded" always means almost everywhere.

- $p < 1$: not a norm at all, since the triangle inequality reverses.
