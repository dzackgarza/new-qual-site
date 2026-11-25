---
order: 29
title: "Real analysis qual prep week 2: measure theory and Fubini--Tonelli"
---

# Real analysis qual prep week 2: measure theory and Fubini--Tonelli

References:

- [@Fol99, chap. 1]

- [@SS05, chaps. 1-2]

## Metrics and convergence

[[D-E2XVI]]

To prove $x=y$ in a metric space it suffices to show $\rho(x,y)<\varepsilon$ for every $\varepsilon>0$, and the triangle inequality splits an estimate of $\rho(x,z)$ through an intermediate point.

[[D-YZC3C]] [[D-IYDZU]]

::: {.example}
Uniform convergence implies pointwise convergence, and $x^n$ on $[0,1]$ converges pointwise but not uniformly ([[PR-SCTER]]).

Pointwise convergence is [@Rud76, ch. 7, Definition 7.1]; for $x^n$ the limit is $0$ on $[0,1)$ and $1$ at $1$, so the limit is discontinuous while every $x^n$ is continuous, and uniform convergence would preserve continuity by [@Rud76, ch. 7, Theorem 7.12].
:::

[[T-ERNLN]]

[[FF-IAUQG]]

[[PR-IGVTV]]

## Measure theory

[[D-RPOGQ]]

[[D-P8RSF]]

[[D-QYLPH]]

[[D-ALMOSTEVERY]]

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
Then $\mu^*$ is an [[D-79EWM|outer measure]] [@Fol99, Proposition 1.10].
:::

[[D-3XE77]]

[[D-PAEDW]]

[[T-7X52J]]

## Fubini--Tonelli

[[D-SLICES]]

[[T-4GPEF]]

[[FT-4JRQX]]

[[T-X7XZX]]

[[PR-6NDTF]]

::: {.example title="A set with measurable $x$-slices that is not measurable"}
The converse fails: a set all of whose $x$-slices are measurable need not be measurable.
For a non-measurable $\mathcal N\subseteq[0,1]$, let $E\coloneqq\mathcal N\times[0,1]$.
Every slice $E_x$ is $[0,1]$ or $\varnothing$, hence measurable, but $E$ is not measurable: if it were, [[PR-6NDTF]] would make $x\mapsto m(E_x)=\chi_{\mathcal N}(x)$ measurable.

:::

::: {.corollary}
Let $f\geq0$ on $\RR^d$ and $\mathcal A\coloneqq\theset{(x,y)\in\RR^d\times\RR \st 0\leq y\leq f(x)}$.
Then $f$ is measurable if and only if $\mathcal A$ is measurable in $\RR^{d+1}$, and in that case $\int_{\RR^d}f(x)\dx = m(\mathcal A)$ [@Fol99, Exercise 2.50].

The direction from $f$ to $\mathcal A$ and the identity of the two integrals are Folland's Exercise 2.50; the converse is the section direction of the [[PR-6NDTF|measurable-slice theorem]].
:::

::: {.remark}
The slices $\mathcal A_x=[0,f(x)]$ being intervals does not by itself make $\mathcal A$ measurable: the non-measurable $E$ above has every $x$-slice measurable.
:::

## Qual problems

[[P-8RA35]]

[[P-OPH7A]]

[[P-4NYI7]]

[[P-ZCE6E]]
