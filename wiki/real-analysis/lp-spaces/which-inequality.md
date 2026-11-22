---
title: Which inequality?
order: 0
topics:
- Lp Spaces
- Norms
---

# Which inequality?

Let $(X,\mu)$ be a measure space and $\frac1p+\frac1q=1$ with $1\leq p,q\leq\infty$.
The table names the quantity to bound and the inequality that bounds it; the statements are on [[real-analysis/appendices/appendix-inequalities|Common inequalities]].

| Quantity bounded | Inequality | Hypotheses |
| --- | --- | --- |
| An integral of a product | [[PR-7BGSE\|Hölder's inequality]] | conjugate $p,q$ |
| A norm of a sum | [[PR-XUVZY\|Minkowski's inequality]] | $1\leq p<\infty$ |
| The measure of a level set | [[PR-YO7MV\|Markov and Chebyshev]] | $0<p<\infty$, $t>0$ |
| A convex function of an average | [[PR-W4ICW\|Jensen's inequality]] | $\mu(X)=1$ |
| A convolution | [[PR-2C3SZ\|Young's convolution inequality]] | $\frac1r=\frac1p+\frac1q-1$ |

## Consequences of Hölder's inequality

[[FT-GQRV2]]

::: {.proposition title="Interpolation"}
For $0<p<r<q\leq\infty$ and $\frac1r=\frac\theta p+\frac{1-\theta}q$ with $\theta\in(0,1)$, Hölder's inequality applied to $\abs f^{r\theta}\cdot\abs f^{r(1-\theta)}$ gives
$$
\norm f_r \leq \norm f_p^{\theta}\norm f_q^{1-\theta}
$$
[@Fol99, Proposition 6.10].

:::

[[T-5BFVS]]

::: {.proposition title="The case of equality in Hölder's inequality"}
Let $1<p<\infty$ and let $q$ be its conjugate exponent.
For $f\in L^p$ and $g\in L^q$, equality holds in [[PR-7BGSE|Hölder's inequality]] exactly when $\alpha\abs f^p=\beta\abs g^q$ almost everywhere for some constants $\alpha,\beta\geq0$, not both zero [@Fol99, Theorem 6.2].

Folland prints the condition on the constants as $\alpha\beta\neq0$. With that restriction the statement omits the case $f=0$ or $g=0$ almost everywhere, where both sides of Hölder's inequality vanish and equality holds; allowing $\beta=0$ or $\alpha=0$ covers it, and when $\alpha\beta>0$ the two conditions agree.
:::


## Chebyshev's inequality

A bound on $\norm f_p$ bounds the measure of $\theset{\abs f>t}$ ([[PR-YO7MV]]).
With the Borel--Cantelli lemma ([[T-OTR5M]], which cites Royden--Fitzpatrick, Chapter 17, §17.1 for it): for $1\leq p<\infty$, if $\sum_n\norm{f_n}_p^p<\infty$, then $f_n\to0$ almost everywhere.

## Particular exponents

- $p=1$: for $\sigma$-finite $\mu$, $(L^1)^* \cong L^\infty$ ([[T-5BFVS]]); for Lebesgue measure on $[0,1]$ the natural map $L^1\to(L^\infty)^*$ is not surjective ([[PR-N7YFV]]).

- $p=2$: $L^2$ is a Hilbert space with $\inner fg\coloneqq\int f\bar g$ ([[PR-YFVA2]]); if $X$ contains disjoint sets of positive finite measure, $L^p$ is a Hilbert space only for $p=2$, by the parallelogram law ([[real-analysis/functional-analysis/banach-and-hilbert|Banach and Hilbert spaces]]).

- $p=\infty$: $\norm f_\infty$ is the [[D-YWRVG|essential supremum]], the least $M$ with $\abs f\leq M$ almost everywhere.

::: {.example title="The triangle inequality fails for $0<p<1$"}
On $[0,2]$, $\norm{\chi_{[0,1]}+\chi_{[1,2]}}_p = 2^{1/p}>2 = \norm{\chi_{[0,1]}}_p+\norm{\chi_{[1,2]}}_p$, so $\norm{\cdot}_p$ is not a norm.

:::
