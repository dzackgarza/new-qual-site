---
order: 29
title: "Real analysis qual prep week 2: measure theory and Fubini--Tonelli"
---

# Real analysis qual prep week 2: measure theory and Fubini--Tonelli

References:

- [@Fol13, chap. 1]

- [@SS05, chaps. 1-2]

## Metrics and convergence

::: {.definition}
A \dfn{metric} on a set $X$ is a function $\rho\colon X\times X\to[0,\infty)$ such that $\rho(x,y)=0$ if and only if $x=y$, $\rho(x,y)=\rho(y,x)$ for all $x,y\in X$, and $\rho(x,z)\leq\rho(x,y)+\rho(y,z)$ for all $x,y,z\in X$.

:::

To prove $x=y$ in a metric space it suffices to show $\rho(x,y)<\varepsilon$ for every $\varepsilon>0$, and the triangle inequality splits an estimate of $\rho(x,z)$ through an intermediate point.

::: {.definition}
Let $f_n, f\colon S\to\RR$.
The sequence $(f_n)$ \dfn{converges uniformly} to $f$ if
$$
(\forall\varepsilon>0)\,(\exists n_0)\,(\forall x\in S)\,(\forall n>n_0)\quad \abs{f_n(x)-f(x)}<\varepsilon,
$$
and \dfn{converges pointwise} to $f$ if
$$
(\forall\varepsilon>0)\,(\forall x\in S)\,(\exists n_0 = n_0(x,\varepsilon))\,(\forall n>n_0)\quad \abs{f_n(x)-f(x)}<\varepsilon.
$$

:::

::: {.remark}
Uniform convergence fails exactly when
$$
(\exists\varepsilon>0)\,(\forall n_0)\,(\exists n>n_0)\,(\exists x = x(n)\in S)\quad \abs{f_n(x)-f(x)}\geq\varepsilon,
$$
where the point $x$ may depend on $n$.
Uniform convergence implies pointwise convergence, and $x^n$ on $[0,1]$ converges pointwise but not uniformly.
For a series $\sum_{k\geq1}a_k(x)$, uniform convergence means uniform convergence of the partial sums $f_n\coloneqq\sum_{k\leq n}a_k$.

:::

With $\norm{f}_\infty \coloneqq \sup_{x\in S} \abs{f(x)}$, $f_n\to f$ uniformly if and only if there are $M_n\to0$ with $\norm{f_n-f}_\infty\leq M_n$ for all large $n$.

::: {.theorem title="Uniform limit theorem"}
If $f_n\to f$ uniformly and each $f_n$ is continuous, then $f$ is continuous.

:::

::: {.proof}
Given $\varepsilon>0$ and $x$, choose $N$ with $\norm{f_N-f}_\infty<\varepsilon/3$ and $\delta>0$ with $\abs{f_N(x)-f_N(y)}<\varepsilon/3$ for $\abs{x-y}<\delta$.
Then $\abs{f(x)-f(y)}\leq\abs{f(x)-f_N(x)}+\abs{f_N(x)-f_N(y)}+\abs{f_N(y)-f(y)}<\varepsilon$ for $\abs{x-y}<\delta$.

:::

::: {.theorem title="Weierstrass $M$-test"}
Let $f_n$ be real- or complex-valued functions on a set $A$ and $M_n\geq0$ with $\abs{f_n(x)}\leq M_n$ for all $n\geq1$ and $x\in A$, and $\sum_{n\geq1}M_n<\infty$.
Then $\sum_{n\geq1}f_n(x)$ converges absolutely and uniformly on $A$.

:::

::: {.fact}
The supremum of a set of real numbers is its least upper bound and the infimum its greatest lower bound.
The series $\sum_{n\geq 1} n^{-p}$ converges if and only if $p>1$.
If $\sum_{n\geq 1} a_n$ converges, then $\lim_{N\to\infty}\sum_{n\geq N} a_n = 0$, so bounding $\norm{f_n-f}_\infty$ by a tail of a convergent series proves uniform convergence.
For $\varepsilon>0$, $\sum_{n\geq1}\varepsilon2^{-n} = \varepsilon$, which distributes an error $\varepsilon$ over countably many terms.

:::

## Measure theory

::: {.definition}
An $F_\sigma$ set is a countable union of closed sets, and a $G_\delta$ set is a countable intersection of open sets.
A $\sigma$-algebra on $X$ is a collection of subsets of $X$ containing $X$ and closed under complements and countable unions, hence under countable intersections.

:::

::: {.definition}
Let $\mathcal M$ be a $\sigma$-algebra on $X$.
A \dfn{measure} on $\mathcal M$ is a function $\mu\colon\mathcal M\to[0,\infty]$ with $\mu(\varnothing)=0$ and $\mu\qty{\bigcup_{j\geq1}E_j} = \sum_{j\geq1}\mu(E_j)$ for every sequence of disjoint $E_j\in\mathcal M$ (countable additivity), which implies finite additivity.

:::

::: {.theorem}
Let $(X,\mathcal M,\mu)$ be a measure space.

(a) If $E,F\in\mathcal M$ and $E\subseteq F$, then $\mu(E)\leq\mu(F)$.

(b) If $E_j\in\mathcal M$, then $\mu\qty{\bigcup_jE_j}\leq\sum_j\mu(E_j)$.

(c) If $E_1\subseteq E_2\subseteq\cdots$ in $\mathcal M$, then $\mu\qty{\bigcup_jE_j} = \lim_j\mu(E_j)$.

(d) If $E_1\supseteq E_2\supseteq\cdots$ in $\mathcal M$ and $\mu(E_1)<\infty$, then $\mu\qty{\bigcap_jE_j} = \lim_j\mu(E_j)$.

:::

::: {.remark}
The proof of continuity of measure replaces a sequence of sets by disjoint sets with the same union: if $A_1 \subseteq A_2 \subseteq \cdots$, set $F_1\coloneqq A_1$ and $F_k \coloneqq A_k \setminus A_{k-1}$ for $k\geq 2$; then $\bigcup_{k\geq 1} A_k = \bigsqcup_{k\geq 1} F_k$.

:::

::: {.definition}
An \dfn{outer measure} on a nonempty set $X$ is a function $\mu^*\colon\mathcal P(X)\to[0,\infty]$ with $\mu^*(\varnothing)=0$, $\mu^*(A)\leq\mu^*(B)$ for $A\subseteq B$, and $\mu^*\qty{\bigcup_jA_j}\leq\sum_j\mu^*(A_j)$.

:::

::: {.proposition}
Let $\mathcal E\subseteq\mathcal P(X)$ and $\rho\colon\mathcal E\to[0,\infty]$ with $\varnothing, X\in\mathcal E$ and $\rho(\varnothing)=0$.
For $A\subseteq X$ let
$$
\mu^*(A)\coloneqq\inf\theset{\sum_{j\geq1}\rho(E_j) \st E_j\in\mathcal E,\ A\subseteq\bigcup_{j\geq1}E_j}.
$$
Then $\mu^*$ is an outer measure.

:::

::: {.definition}
The Lebesgue outer measure of $E\subseteq\RR^n$ is $m_*(E)\coloneqq\inf\sum_i\abs{Q_i}$, the infimum over countable covers of $E$ by closed cubes $Q_i$.

:::

A property holds \dfn{almost everywhere} if the set where it fails has measure zero.

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

::: {.theorem title="Fubini's theorem [@SS05, Chapter 2, Theorem 3.1]"}
If $f$ is integrable on $\RR^{d_1}\times\RR^{d_2}$, then for almost every $y\in\RR^{d_2}$ the slice $f^y$ is integrable on $\RR^{d_1}$, the function $y\mapsto\int_{\RR^{d_1}}f^y(x)\dx$ is integrable on $\RR^{d_2}$, and
$$
\int_{\RR^{d_2}}\qty{\int_{\RR^{d_1}}f(x,y)\dx}\dy = \int_{\RR^d}f.
$$
By symmetry the same holds with $x$ and $y$ exchanged, so both iterated integrals equal $\int_{\RR^d}f$.

:::

::: {.theorem title="Tonelli's theorem [@SS05, Chapter 2, Theorem 3.2]"}
If $f$ is a nonnegative measurable function on $\RR^{d_1}\times\RR^{d_2}$, then for almost every $y\in\RR^{d_2}$ the slice $f^y$ is measurable on $\RR^{d_1}$, the function $y\mapsto\int_{\RR^{d_1}}f^y(x)\dx$ is measurable on $\RR^{d_2}$, and
$$
\int_{\RR^{d_2}}\qty{\int_{\RR^{d_1}}f(x,y)\dx}\dy = \int_{\RR^d}f
$$
in $[0,\infty]$.

:::

::: {.remark}
To compute $\int_{\RR^d}f$ for measurable $f$, apply Tonelli's theorem to $\abs f$: if an iterated integral of $\abs f$ is finite, then $f$ is integrable and Fubini's theorem applies to $f$.

:::

Let $L^+$ denote the measurable functions $X\to[0,\infty]$ on a measure space $(X,\mathcal M,\mu)$.

::: {.theorem title="Fubini--Tonelli theorem [@Fol13, Theorem 2.37]"}
Let $(X,\mathcal M,\mu)$ and $(Y,\mathcal N,\nu)$ be $\sigma$-finite measure spaces.

(a) If $f\in L^+(X\times Y)$, then $g(x)\coloneqq\int f_x\,d\nu$ and $h(y)\coloneqq\int f^y\,d\mu$ are in $L^+(X)$ and $L^+(Y)$, and
$$
\int f\,d(\mu\times\nu) = \int\qty[\int f(x,y)\,d\nu(y)]d\mu(x) = \int\qty[\int f(x,y)\,d\mu(x)]d\nu(y).
$$

(b) If $f\in L^1(\mu\times\nu)$, then $f_x\in L^1(\nu)$ for almost every $x$, $f^y\in L^1(\mu)$ for almost every $y$, the almost everywhere defined $g$ and $h$ are in $L^1(\mu)$ and $L^1(\nu)$, and the same equalities hold.

:::

::: {.corollary}
If $E\subseteq\RR^{d_1}\times\RR^{d_2}$ is measurable, then for almost every $y\in\RR^{d_2}$ the slice $E^y$ is measurable, $y\mapsto m(E^y)$ is measurable, and $m(E) = \int_{\RR^{d_2}}m(E^y)\dy$.

:::

::: {.proof}
Apply Tonelli's theorem to $\chi_E$.

:::

::: {.remark}
The converse fails: a set whose slices are all measurable need not be measurable.
For a non-measurable $\mathcal N\subseteq[0,1]$, let $E\coloneqq\mathcal N\times[0,1]$.
Every slice $E_x$ is $[0,1]$ or $\varnothing$, hence measurable, but $E$ is not measurable, since otherwise the preceding corollary would make the slices $E^y = \mathcal N$ measurable for almost every $y\in[0,1]$.

:::

::: {.corollary}
Let $f\geq0$ on $\RR^d$ and $\mathcal A\coloneqq\theset{(x,y)\in\RR^d\times\RR \st 0\leq y\leq f(x)}$.
Then $f$ is measurable if and only if $\mathcal A$ is measurable in $\RR^{d+1}$, and in that case $\int_{\RR^d}f(x)\dx = m(\mathcal A)$.

:::

::: {.proof}
If $f$ is measurable, then $F(x,y)\coloneqq y-f(x)$ is measurable on $\RR^{d+1}$, so $\mathcal A = \theset{y\geq0}\cap\theset{F\leq0}$ is measurable.
If $\mathcal A$ is measurable, each slice $\mathcal A_x = [0,f(x)]$ has $m(\mathcal A_x)=f(x)$, so the preceding corollary, with the roles of $x$ and $y$ exchanged, shows that $f$ is measurable and $m(\mathcal A) = \int m(\mathcal A_x)\dx = \int f(x)\dx$.

:::

## Qual problems

Problems suggested by Peter Woolfitt:

[[P-8RA35]]

[[P-OPH7A]]

[[P-4NYI7]]

[[P-ZCE6E]]
