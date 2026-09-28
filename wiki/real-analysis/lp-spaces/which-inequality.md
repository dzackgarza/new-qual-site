---
title: Which inequality?
order: 0
topics:
- Lp Spaces
- Norms
---

# Which inequality?

Let $(X,\mu)$ be a measure space and $\frac1p+\frac1q=1$ with $1\leq p,q\leq\infty$.
The full statements are on [[real-analysis/inequalities|Inequalities]].

| Quantity bounded | Inequality | Statement |
| --- | --- | --- |
| $\int \abs{fg}$ | Hölder | $\norm{fg}_1 \leq \norm f_p \norm g_q$ |
| $\norm{f+g}_p$, $1\leq p\leq\infty$ | Minkowski | $\norm{f+g}_p\leq\norm f_p+\norm g_p$ |
| $\mu(\theset{\abs f > t})$, $0<p<\infty$ | Chebyshev | $\mu(\theset{\abs f > t}) \leq t^{-p}\norm f_p^p$ |
| $\varphi\qty(\int f)$, $\varphi$ convex, $\mu(X)=1$ | Jensen | $\varphi\qty(\int f) \leq \int \varphi\circ f$ |
| $\norm{f * g}_r$ on $\RR^n$ | Young | $\norm{f*g}_r\leq\norm f_p\norm g_q$ for $\frac1r = \frac1p+\frac1q-1$, $1\leq p,q,r\leq\infty$ |

## Consequences of Hölder's inequality

- **Inclusions.** If $\mu(X)<\infty$ and $p < q$, Hölder's inequality applied to $\abs f^p\cdot 1$ gives $L^q \subseteq L^p$.
  On $(1,\infty)$ with Lebesgue measure, $x^{-1}\in L^2\setminus L^1$, and on $\RR$, $\frac{\sin x}{x}\in L^2(\RR)\setminus L^1(\RR)$.

- **Interpolation.** If $0<p<r<q\leq\infty$ and $\frac1r = \frac\theta p + \frac{1-\theta}q$ with $\theta\in(0,1)$, then $\norm f_r \leq \norm f_p^{\theta}\norm f_q^{1-\theta}$, by Hölder's inequality applied to $\abs f^{r\theta}\cdot\abs f^{r(1-\theta)}$ with exponents $\frac{p}{r\theta}$ and $\frac{q}{r(1-\theta)}$.

- **Duality.** For $g\in L^q$, $\abs{\int fg}\leq\norm f_p\norm g_q$, so $f\mapsto\int fg$ is a bounded linear functional on $L^p$ of norm at most $\norm g_q$.

For $1<p<\infty$ and $\norm f_p,\norm g_q\in(0,\infty)$, equality holds in Hölder's inequality if and only if $\abs f^p/\norm f_p^p = \abs g^q/\norm g_q^q$ almost everywhere.

## Chebyshev's inequality

A bound on $\norm f_p$ bounds the measure of $\theset{\abs f>t}$.
Combined with the Borel--Cantelli lemma: if $\sum_n\norm{f_n}_p^p<\infty$, then $f_n\to0$ almost everywhere.

## Particular exponents

- $p = 1$: for $\sigma$-finite $\mu$, $(L^1)^* \cong L^\infty$; for Lebesgue measure on $[0,1]$ the natural map $L^1\to(L^\infty)^*$ is not surjective.

- $p = 2$: $L^2$ is a Hilbert space with $\inner fg\coloneqq\int f\bar g$; if $X$ contains disjoint sets of positive finite measure, $L^p$ is a Hilbert space only for $p=2$.

- $p = \infty$: $\norm f_\infty$ is the essential supremum, the least $M$ with $\abs f\leq M$ almost everywhere.

- $0<p<1$: $\norm f_p\coloneqq\qty{\int\abs f^p}^{1/p}$ is not a norm; on $[0,2]$, $\norm{\chi_{[0,1]}+\chi_{[1,2]}}_p = 2^{1/p}>2$.
