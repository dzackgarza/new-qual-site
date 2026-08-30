---
order: 28
---

# Useful Tricks

## Repeated Integration by Parts

When you see an integral of the form $\int P(x) e^{ax} \, dx$ or $\int P(x) \sin(bx) \, dx$ where $P$ is a polynomial, apply integration by parts repeatedly until the polynomial is differentiated away.
Each round reduces the degree of $P$ by one.

The tabular method organizes this: write $P$ and its derivatives in one column, and $e^{ax}$ (or $\sin/\cos$) and its integrals in another.
Alternate signs starting with $+$, multiply across, and sum.

![](Pasted image 20211031235625.png)

A common exam pattern: $\int x^2 e^x \, dx$ requires two rounds.
Don't try to be clever with substitution — just grind through the parts.

## Common Series

These show up constantly on qualifying exams.
Memorize the geometric series, the exponential series, and the geometric-series-derivative trick for $\sum n x^n$.

![](Pasted image 20211031235650.png)

The key identity: if $\sum x^n = \frac{1}{1-x}$, then differentiating gives $\sum n x^{n-1} = \frac{1}{(1-x)^2}$, and multiplying by $x$ gives $\sum n x^n = \frac{x}{(1-x)^2}$.
This handles any power-law weight on a geometric series.
