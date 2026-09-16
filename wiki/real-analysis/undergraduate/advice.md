---
title: Techniques and standard facts
order: 5
---

# Techniques and standard facts

## Proof techniques

- **Limits via $\limsup$ and $\liminf$.** For a real sequence $(a_n)$, $\limsup_n a_n$ and $\liminf_n a_n$ exist in $[-\infty,\infty]$, and $\lim_n a_n = c$ if and only if $\limsup_n a_n\leq c\leq\liminf_n a_n$. The limit fails to exist exactly when $\liminf_n a_n<\limsup_n a_n$.

- **Equality from two inequalities.** $a=b$ if and only if $a\leq b$ and $b\leq a$.

- **An $\varepsilon$ of room.** If $a<b+\varepsilon$ for every $\varepsilon>0$, then $a\leq b$; if $\norm a<\varepsilon$ for every $\varepsilon>0$, then $a=0$.

- **Approximate infima.** If $s = \inf S$ for a nonempty $S\subseteq\RR$ bounded below, then for every $\varepsilon>0$ there is $x\in S$ with $s\leq x<s+\varepsilon$.

- **Local to global.** A property of a function that is local, such as continuity or differentiability at each point, holds on $\RR^n$ if it holds on every ball $B_R(0)$.

- **Good and bad sets.** An integral $\int_X\abs f$ is bounded by splitting $X = G\sqcup B$, with $f$ controlled pointwise on $G$ and $\mu(B)$ small; for two functions, $X = \theset{f>g}\sqcup\theset{f=g}\sqcup\theset{f<g}$.

- **Local singularities and tails.** $\int_{\RR^n}\abs f = \int_{\abs x\leq1}\abs f + \int_{\abs x>1}\abs f$, and on $(1,\infty)$, $\int_1^\infty\abs f = \sum_{k\geq0}\int_{2^k}^{2^{k+1}}\abs f$.

- **Add and subtract.** For example, $\norm{T_nx_n - Tx}\leq\norm{T_nx_n - Tx_n} + \norm{Tx_n - Tx}\leq\norm{T_n-T}\norm{x_n}+\norm T\norm{x_n-x}$.

- **Reduction to nice sets and functions.** A statement about measurable sets can often be proved for bounded or compact sets, or for finite unions of rectangles, and extended using regularity and continuity of measure; for unbounded $E$, $E = \bigcup_{n\geq1}(E\cap B_n(0))$. A statement continuous in $f\in L^p$, $1\leq p<\infty$, can be proved on a dense class, such as simple functions or $C_c$, and extended by approximation in norm.

- **Subsequences.** A sequence converging in $L^p$ has an almost everywhere convergent subsequence, and a bounded sequence in $\RR^n$ has a convergent subsequence.

- **Sequential criteria.** $\lim_{\varepsilon\to0}g(\varepsilon) = L$ if and only if $g(\varepsilon_n)\to L$ for every sequence $\varepsilon_n\to0$ with $\varepsilon_n\neq0$.

## Standard facts

- If $\sup_x\abs{f_n(x)} = M_n\to0$, then $f_n\to0$ uniformly; $M_n$ can often be computed from $f_n'$ by the first derivative test.

- If $\sum_n f_n$ converges uniformly on a neighborhood of $x$ and each $f_n$ is continuous at $x$, then $\sum_n f_n$ is continuous at $x$.

- Uniform convergence of $\sum_n f_n$ on $A$ follows from the Weierstrass $M$-test: $\sup_{A}\abs{f_n}\leq M_n$ with $\sum_n M_n<\infty$.

- A continuous function with compact support on $\RR^n$ is bounded and uniformly continuous.

- $\ell^1(\ZZ)\subsetneq\ell^2(\ZZ)$: for example $(1/(\abs k+1))_{k\in\ZZ}\in\ell^2\setminus\ell^1$.

- If $\mu(X)<\infty$ and $1\leq p<q\leq\infty$, then $L^q(\mu)\subseteq L^p(\mu)$, by Hölder's inequality. For counting measure on $\ZZ$, $\ell^p\subseteq\ell^q$. For Lebesgue measure on $\RR$, neither inclusion holds.

- A function fails to be in $L^p(\RR^n)$ because of a local singularity, such as $\abs x^{-n/p}$ near $0$, or a slowly decaying tail, such as $\abs x^{-n/p}$ near $\infty$.

- Every Lebesgue measurable set $E\subseteq\RR^n$ is $H\sqcup N$ with $H$ an $F_\sigma$ set and $N$ null.

- An absolutely continuous function on $[a,b]$ has bounded variation, and $f(x) = f(a)+\int_a^x f'$.

- For $f,g$ in conjugate spaces $L^p$ and $L^q$, $\abs{\int fg}\leq\norm f_p\norm g_q$.

- $\mu(X) = \norm{1}_{L^1(\mu)} = \int_X 1\,d\mu$.

- Littlewood's principles, on a set of finite measure: measurable sets are nearly finite unions of intervals, measurable functions are nearly continuous, and almost everywhere convergent sequences are nearly uniformly convergent; see [[real-analysis/measure/littlewoods-principles|Littlewood's three principles]].

## Standard results

[[PR-IGVTV]]

[[T-ERNLN]]

::: {.proof}
Let $\varepsilon>0$ and $x$ in the domain.
Choose $N$ with $\sup_y\abs{F_N(y)-F(y)}<\varepsilon/3$, and $\delta>0$ with $\abs{F_N(x)-F_N(y)}<\varepsilon/3$ for $\abs{x-y}<\delta$, by continuity of $F_N$.
Then for $\abs{x-y}<\delta$,
$$
\abs{F(x) - F(y)} \leq
\abs{F(x) - F_N(x)} + \abs{F_N(x) - F_N(y)} + \abs{F_N(y) - F(y)}
< \varepsilon.
$$

:::

[[PR-L7LNZ]]

[[PR-6WMSR]]

[[FF-IAUQG]]

[[PR-PIVFR]]

::: {.proof title="Borel characterization of measurable sets"}
For each $n\geq1$ there is a closed $K_n\subseteq E$ with $m(E\setminus K_n) \leq \frac 1 n$.
Let $H\coloneqq\bigcup_n K_n$, an $F_\sigma$ set contained in $E$.
Then $N\coloneqq E\setminus H\subseteq E\setminus K_n$ for every $n$, so $m(N)\leq\frac1n$ for every $n$ and $m(N)=0$.

:::

[[T-IIKSW]]

::: {.proof title="Approximation of measurable sets"}
(1) Suppose first $m(E)<\infty$.
By the definition of outer measure there are closed cubes $Q_i$ with $E\subseteq\bigcup_iQ_i$ and $\sum_i\abs{Q_i}<m(E)+\varepsilon/2$; enlarging each $Q_i$ to an open cube $Q_i'$ with $\abs{Q_i'}<\abs{Q_i}+\varepsilon2^{-i-1}$, the open set $O\coloneqq\bigcup_iQ_i'$ satisfies $m(O)<m(E)+\varepsilon$, so $m(O\setminus E)<\varepsilon$.
In general write $E=\bigcup_kE_k$ with $m(E_k)<\infty$, choose open $O_k\supseteq E_k$ with $m(O_k\setminus E_k)<\varepsilon2^{-k}$, and let $O\coloneqq\bigcup_kO_k$.

(2) Apply (1) to $E^c$ to get an open $O\supseteq E^c$ with $m(O\setminus E^c)<\varepsilon$, and let $F\coloneqq O^c$.
Then $F$ is closed, $F\subseteq E$, and $E\setminus F = O\setminus E^c$, so $m(E\setminus F)<\varepsilon$.

(3) Assume $m(E)<\infty$; for $E=\RR^n$ no compact $K$ has $m(E\setminus K)<\infty$.
By (2) choose a closed $F\subseteq E$ with $m(E\setminus F)<\varepsilon/2$, and let $K_n\coloneqq F\cap\overline{B_n(0)}$, which is compact.
The sets $E\setminus K_n$ decrease to $E\setminus F$ and $m(E)<\infty$, so $m(E\setminus K_n)\to m(E\setminus F)$, and $m(E\setminus K_n)<\varepsilon$ for $n$ large.

:::

## Exercises

[[E-OMK54]]

[[PR-6NDTF]]

::: {.proposition title="The region under a graph"}
Let $f\colon\RR^n\to[0,\infty)$ and $A\coloneqq\theset{(x,y)\in\RR^n\times\RR \st 0\leq y\leq f(x)}$.
Then $f$ is Lebesgue measurable if and only if $A$ is Lebesgue measurable in $\RR^{n+1}$, and in that case $m(A) = \int_{\RR^n}f(x)\dx$.

:::

::: {.proof}
Suppose $f$ is measurable.
The functions $F(x,y)\coloneqq f(x)$ and $G(x,y)\coloneqq y$ are measurable on $\RR^{n+1}$, since $\theset{F>a} = \theset{f>a}\times\RR$ and $\theset{G>a} = \RR^n\times(a,\infty)$.
Hence $A = \theset{G\leq F}\cap\theset{G\geq0}$ is measurable.

Suppose $A$ is measurable.
For every $x$, the slice $A_x = [0,f(x)]$ has $m(A_x) = f(x)$.
By [[PR-6NDTF]], $x\mapsto m(A_x) = f(x)$ is measurable and $m(A) = \int_{\RR^n}m(A_x)\dx = \int_{\RR^n}f(x)\dx$.

:::
