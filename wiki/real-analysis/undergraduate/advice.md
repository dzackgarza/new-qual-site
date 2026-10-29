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

- **Reduction to nice sets and functions.** For Lebesgue measurable $E\subseteq\RR^n$, $m(E) = \lim_n m(E\cap B_n(0))$ by continuity from below; if $m(E)<\infty$, then for every $\varepsilon>0$ there are a compact $K\subseteq E$ with $m(E\setminus K)<\varepsilon$ and a finite union of rectangles $R$ with $m(E\,\triangle\,R)<\varepsilon$. For $1\leq p<\infty$, two continuous maps on $L^p$ that agree on simple functions, or on $C_c(\RR^n)$, agree on $L^p$.

- **Subsequences.** A sequence converging in $L^p$ has an almost everywhere convergent subsequence, and a bounded sequence in $\RR^n$ has a convergent subsequence.

- **Sequential criteria.** $\lim_{\varepsilon\to0}g(\varepsilon) = L$ if and only if $g(\varepsilon_n)\to L$ for every sequence $\varepsilon_n\to0$ with $\varepsilon_n\neq0$.

## Standard facts

- If $\sup_x\abs{f_n(x)} = M_n\to0$, then $f_n\to0$ uniformly; $M_n$ can often be computed from $f_n'$ by the first derivative test.

- If $\sum_n f_n$ converges uniformly on a neighborhood of $x$ and each $f_n$ is continuous at $x$, then $\sum_n f_n$ is continuous at $x$.

- Uniform convergence of $\sum_n f_n$ on $A$ follows from the Weierstrass $M$-test: $\sup_{A}\abs{f_n}\leq M_n$ with $\sum_n M_n<\infty$.

- A continuous function with compact support on $\RR^n$ is bounded and uniformly continuous.

- $\ell^1(\ZZ)\subsetneq\ell^2(\ZZ)$: for example $(1/(\abs k+1))_{k\in\ZZ}\in\ell^2\setminus\ell^1$.

- If $\mu(X)<\infty$ and $1\leq p<q\leq\infty$, then $L^q(\mu)\subseteq L^p(\mu)$, by Hölder's inequality. For counting measure on $\ZZ$, $\ell^p\subseteq\ell^q$. For Lebesgue measure on $\RR$, neither inclusion holds.

- For $a>0$ and $1\leq p<\infty$, $\abs x^{-a}\chi_{\theset{\abs x\leq1}}\in L^p(\RR^n)$ if and only if $ap<n$, and $\abs x^{-a}\chi_{\theset{\abs x>1}}\in L^p(\RR^n)$ if and only if $ap>n$; so $\abs x^{-n/p}$ fails to be in $L^p$ both near $0$ and near $\infty$.

- An absolutely continuous function on $[a,b]$ has bounded variation, and $f(x) = f(a)+\int_a^x f'$.

- For $f,g$ in conjugate spaces $L^p$ and $L^q$, $\abs{\int fg}\leq\norm f_p\norm g_q$.

- $\mu(X) = \norm{1}_{L^1(\mu)} = \int_X 1\,d\mu$.

- Littlewood's principles, on a set of finite measure: measurable sets are nearly finite unions of intervals, measurable functions are nearly continuous, and almost everywhere convergent sequences are nearly uniformly convergent; see [[real-analysis/measure/littlewoods-principles|Littlewood's three principles]].

## Standard results

[[PR-IGVTV]]

[[T-ERNLN]]

[[PR-L7LNZ]]

[[PR-6WMSR]]

[[FF-IAUQG]]

[[PR-PIVFR]]

[[T-IIKSW]]

## Exercises

[[P-4EOE5]]

[[PR-6NDTF]]

::: {.proposition title="The region under a graph"}
Let $f\colon\RR^n\to[0,\infty)$ and $A\coloneqq\theset{(x,y)\in\RR^n\times\RR \st 0\leq y\leq f(x)}$.
Then $f$ is Lebesgue measurable if and only if $A$ is Lebesgue measurable in $\RR^{n+1}$, and in that case $m(A) = \int_{\RR^n}f(x)\dx$.

:::
