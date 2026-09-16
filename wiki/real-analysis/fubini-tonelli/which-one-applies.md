---
title: Which one applies?
order: 0
topics:
- Fubini-Tonelli
- Repeated Integration
---

# Which one applies?

Let $(X,\mu)$ and $(Y,\nu)$ be measure spaces and $f$ a $\mu\times\nu$-measurable function on $X\times Y$.
The exact statements are on [[real-analysis/fubini-tonelli/statements|The statements]].

## Hypotheses of each theorem

- **Tonelli.** If $\mu$ and $\nu$ are $\sigma$-finite and $f \geq 0$, then the two iterated integrals and $\int_{X\times Y} f\,d(\mu\times\nu)$ are equal, possibly all equal to $+\infty$.

- **Fubini.** If $\mu$ and $\nu$ are $\sigma$-finite and $f \in L^1(\mu\times\nu)$, then the two iterated integrals are finite and equal to $\int_{X\times Y} f\,d(\mu\times\nu)$.

::: {.proposition}
If $\mu$ and $\nu$ are $\sigma$-finite and one iterated integral of $\abs f$ is finite, then $f\in L^1(\mu\times\nu)$, and the iterated integrals of $f$ are equal.

:::

::: {.proof}
By Tonelli's theorem applied to $\abs f$, $\int_{X\times Y}\abs f\,d(\mu\times\nu)$ equals the finite iterated integral, so $f\in L^1(\mu\times\nu)$, and Fubini's theorem applies to $f$.

:::

## Counterexamples without the hypotheses

::: {.example title="Without $\sigma$-finiteness"}
Let $\mu$ be Lebesgue measure and $\nu$ counting measure on $[0,1]$, and let $f\coloneqq\chi_\Delta$ for the diagonal $\Delta\subseteq[0,1]^2$.
Then $\int\qty{\int f(x,y)\,d\nu(y)}d\mu(x) = \int_0^1 1\dx = 1$ and $\int\qty{\int f(x,y)\,d\mu(x)}d\nu(y) = \sum_{y} 0 = 0$.

:::

::: {.example title="Without nonnegativity or integrability"}
On $[0,1]^2$ with Lebesgue measure, $f(x,y) \coloneqq \frac{x^2-y^2}{(x^2+y^2)^2}$ has
$$
\int_0^1\int_0^1 f(x,y)\dy\dx = \frac\pi4, \qquad \int_0^1\int_0^1 f(x,y)\dx\dy = -\frac\pi4,
$$
so $f\notin L^1([0,1]^2)$.

:::

## Other applications

::: {.example title="Computing a single integral as a double integral"}
Since $\frac1x = \int_0^\infty e^{-xt}\dt$ for $x>0$, applying Fubini's theorem on $[0,A]\times[0,\infty)$ to $e^{-xt}\sin x$ and letting $A\to\infty$ gives $\int_0^\infty \frac{\sin x}{x}\dx = \int_0^\infty\frac{\dt}{1+t^2} = \frac\pi2$.

:::

::: {.proposition title="Layer cake formula"}
If $\mu$ is $\sigma$-finite and $f$ is measurable, then $\int \abs f\,d\mu = \int_0^\infty \mu(\theset{\abs f > t})\dt$.

:::

::: {.proof}
Apply Tonelli's theorem to $\chi_{\theset{(x,t) \st 0<t<\abs{f(x)}}}$ on $X\times(0,\infty)$.

:::

The basic properties of convolution are also consequences of Tonelli's and Fubini's theorems; see [[real-analysis/fourier/convolution|Convolution]].
