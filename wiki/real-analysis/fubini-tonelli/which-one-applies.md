---
title: Which one applies?
order: 0
topics:
- Fubini-Tonelli
- Repeated Integration
---

# Which one applies?

The choice between Tonelli and Fubini is determined by the hypotheses: nonnegativity supports Tonelli, while absolute integrability supports Fubini.

## The rule

- **Tonelli** applies when $f \geq 0$ and the measures are $\sigma\dash$finite.
  No integrability hypothesis is needed: the iterated integrals and the double integral all agree, possibly all equal to $+\infty$.

- **Fubini** applies when $f \in L^1$ of the product.
  Then the iterated integrals agree with the double integral and with each other.

So the standard move is to run Tonelli on $\abs f$ first: if the iterated integral of $\abs f$ is finite, then $f\in L^1$ and Fubini applies to $f$.
This two-step reduction is standard.

## What each hypothesis is doing

- **$\sigma\dash$finiteness** is a hypothesis in the standard Tonelli--Fubini theorem used here.
  Without it, equality of the two iterated integrals can fail: on $[0,1]$ with Lebesgue measure against counting measure, the characteristic function of the diagonal has iterated integrals $1$ and $0$.

- **Nonnegativity** in Tonelli is what allows $+\infty$ as an answer; without it the two iterated integrals can be $\infty - \infty$ in different orders.

- **Integrability** in Fubini is exactly what rules that out.
  The standard witness is $f(x,y) = \frac{x^2-y^2}{(x^2+y^2)^2}$ on $[0,1]^2$, whose iterated integrals are $\pi/4$ and $-\pi/4$.

## What it is used for besides interchanging

Three uses that are not about swapping the order:

- **Computing a single integral** by writing it as a double one, the standard example being $\int_0^\infty \frac{\sin x}{x}\dx$ via $\frac1x = \int_0^\infty e^{-xt}\dt$.

- **The layer cake formula** $\int \abs f = \int_0^\infty \mu(\abs f > t)\dt$, which is Tonelli applied to the region under the graph.

- **Convolution**, whose basic properties are all Tonelli, on [[real-analysis/fourier/index|Fourier]].
