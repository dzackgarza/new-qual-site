---
order: 29
title: "Real analysis qual prep week 2: measure theory and Fubini--Tonelli"
---

# Real analysis qual prep week 2: measure theory and Fubini--Tonelli

References:

- [@Fol13, chap. 1]

- [@SS05, chaps. 1-2]

## Metrics and convergence

[[D-E2XVI]]

To prove $x=y$ in a metric space it suffices to show $\rho(x,y)<\varepsilon$ for every $\varepsilon>0$, and the triangle inequality splits an estimate of $\rho(x,z)$ through an intermediate point.

[[D-YZC3C]] [[D-IYDZU]]

::: {.example}
Uniform convergence implies pointwise convergence, and $x^n$ on $[0,1]$ converges pointwise but not uniformly.

:::

[[T-ERNLN]]

[[FF-IAUQG]]

::: {.fact}
If $\sum_{n\geq 1} a_n$ converges, then $\lim_{N\to\infty}\sum_{n\geq N} a_n = 0$, so bounding $\norm{f_n-f}_\infty$ by a tail of a convergent series proves uniform convergence.
For $\varepsilon>0$, $\sum_{n\geq1}\varepsilon2^{-n} = \varepsilon$, which distributes an error $\varepsilon$ over countably many terms.

:::

## Measure theory

[[D-RPOGQ]]

[[D-P8RSF]]

[[D-QYLPH]]

Countable additivity implies finite additivity.

[[T-7LQ7X]]

[[PR-KKJ6O]]

[[FS-ACP4W]]

[[D-79EWM]]

::: {.proposition}
Let $\mathcal E\subseteq\mathcal P(X)$ and $\rho\colon\mathcal E\to[0,\infty]$ with $\varnothing, X\in\mathcal E$ and $\rho(\varnothing)=0$.
For $A\subseteq X$ let
$$
\mu^*(A)\coloneqq\inf\theset{\sum_{j\geq1}\rho(E_j) \st E_j\in\mathcal E,\ A\subseteq\bigcup_{j\geq1}E_j}.
$$
Then $\mu^*$ is an [[D-79EWM|outer measure]].

:::

[[D-3XE77]]

A property holds almost everywhere if the set where it fails has measure zero.

::: {.definition}
For sets $E_n$,
$$
\limsup_n E_n \coloneqq \bigcap_{k\geq1}\bigcup_{n\geq k}E_n, \qquad \liminf_n E_n\coloneqq\bigcup_{k\geq1}\bigcap_{n\geq k}E_n,
$$
so $\limsup_nE_n = \theset{x \st x\in E_n\text{ for infinitely many } n}$ and $\liminf_nE_n = \theset{x \st x\in E_n\text{ for all but finitely many } n}$.
De Morgan's laws state $\qty{\bigcup_\alpha E_\alpha}^c = \bigcap_\alpha E_\alpha^c$ and $\qty{\bigcap_\alpha E_\alpha}^c = \bigcup_\alpha E_\alpha^c$.

:::

::: {.theorem}
Let $\mu$ be a Lebesgue--Stieltjes measure on $\RR$ with $\sigma$-algebra $\mathcal M_\mu$.
If $E\in\mathcal M_\mu$, then
$$
\mu(E) = \inf\theset{\mu(U) \st U\supseteq E,\ U\text{ open}} = \sup\theset{\mu(K) \st K\subseteq E,\ K\text{ compact}}.
$$
For $E\subseteq\RR$ the following are equivalent: (a) $E\in\mathcal M_\mu$; (b) $E = V\setminus N_1$ with $V$ a $G_\delta$ set and $\mu(N_1)=0$; (c) $E = H\cup N_2$ with $H$ an $F_\sigma$ set and $\mu(N_2)=0$.

:::

## Fubini--Tonelli

::: {.definition}
For $f$ on $\RR^{d_1}\times\RR^{d_2}$, $x\in\RR^{d_1}$, and $y\in\RR^{d_2}$, the \dfn{slices} of $f$ are $f^y(x)\coloneqq f(x,y)$ and $f_x(y)\coloneqq f(x,y)$; for $E\subseteq\RR^{d_1}\times\RR^{d_2}$, the slices are $E^y\coloneqq\theset{x \st (x,y)\in E}$ and $E_x\coloneqq\theset{y \st (x,y)\in E}$.

:::

[[T-4GPEF]]

[[FT-4JRQX]]

[[T-X7XZX]]

[[PR-6NDTF]]

::: {.remark}
The converse fails: a set whose slices are all measurable need not be measurable.
For a non-measurable $\mathcal N\subseteq[0,1]$, let $E\coloneqq\mathcal N\times[0,1]$.
Every slice $E_x$ is $[0,1]$ or $\varnothing$, hence measurable, but $E$ is not measurable: Tonelli's theorem applied to $\chi_E$ would make $E^y$ measurable for almost every $y$, whereas $E^y = \mathcal N$ for every $y\in[0,1]$.

:::

::: {.corollary}
Let $f\geq0$ on $\RR^d$ and $\mathcal A\coloneqq\theset{(x,y)\in\RR^d\times\RR \st 0\leq y\leq f(x)}$.
Then $f$ is measurable if and only if $\mathcal A$ is measurable in $\RR^{d+1}$, and in that case $\int_{\RR^d}f(x)\dx = m(\mathcal A)$.

:::

## Qual problems

[[P-8RA35]]

[[P-OPH7A]]

[[P-4NYI7]]

[[P-ZCE6E]]
