---
order: 28
---

# Useful tricks

## Repeated integration by parts

For integrals $\int P(x) e^{ax} \dx$ or $\int P(x) \sin(bx) \dx$ with $P$ a polynomial, each integration by parts with $u$ the polynomial factor lowers its degree by one, so $\deg P + 1$ integrations by parts reduce the integral to an elementary one.

The tabular method records this: one column lists $P$ and its successive derivatives, the other lists $e^{ax}$ (or $\sin(bx)$) and its successive antiderivatives, and the integral is the sum of the products along the diagonals with alternating signs starting from $+$.

![](Pasted image 20211031235625.png)

::: {.example}
$$
\int x^2 e^x \dx = x^2e^x - 2xe^x + 2e^x + C.
$$
:::

## Power series from the geometric series

![](Pasted image 20211031235650.png)

For $\abs x<1$, $\sum_{n\geq0} x^n = \frac{1}{1-x}$.
Differentiating term by term gives $\sum_{n\geq1} n x^{n-1} = \frac{1}{(1-x)^2}$, and multiplying by $x$ gives $\sum_{n\geq1} n x^n = \frac{x}{(1-x)^2}$.
Repeating the operation $x\frac{d}{dx}$ gives $\sum_n n^kx^n$ for each $k\geq 1$.
