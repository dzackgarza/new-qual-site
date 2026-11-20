---
title: Techniques and standard facts
order: 5
---

# Techniques and standard facts

## Proof techniques

- Limits via $\limsup$ and $\liminf$: for a real sequence $(a_n)$, the [[D-HOKQD|limit superior and limit inferior]] exist in $[-\infty,\infty]$, and $\lim_n a_n = c$ if and only if $\limsup_n a_n\leq c\leq\liminf_n a_n$; the two are always ordered $\liminf_n a_n\leq\limsup_n a_n$, so together the inequalities say both equal $c$. The limit fails to exist exactly when $\liminf_n a_n<\limsup_n a_n$.

- Equality from two inequalities: $a=b$ if and only if $a\leq b$ and $b\leq a$.

- An $\varepsilon$ of room: if $a<b+\varepsilon$ for every $\varepsilon>0$, then $a\leq b$; if $\norm a<\varepsilon$ for every $\varepsilon>0$, then $a=0$.

- Approximate infima: if $s = \inf S$ for a nonempty $S\subseteq\RR$ bounded below, then for every $\varepsilon>0$ there is $x\in S$ with $s\leq x<s+\varepsilon$.

- Local to global: a property of a function that is local, such as [[D-WGYSB|continuity]] or differentiability at each point, holds on $\RR^n$ if it holds on every ball $B_R(0)$, since $\RR^n=\bigcup_{R>0}B_R(0)$ and a local property is decided at each point, each of which lies in one of the balls.

- Good and bad sets: an integral $\int_X\abs f$ is bounded by splitting $X = G\sqcup B$, with $f$ controlled pointwise on $G$ and $\mu(B)$ small; for two functions, $X = \theset{f>g}\sqcup\theset{f=g}\sqcup\theset{f<g}$.

- Local singularities and tails: $\int_{\RR^n}\abs f = \int_{\abs x\leq1}\abs f + \int_{\abs x>1}\abs f$, and on $(1,\infty)$, $\int_1^\infty\abs f = \sum_{k\geq0}\int_{2^k}^{2^{k+1}}\abs f$.

- Add and subtract: for example, $\norm{T_nx_n - Tx}\leq\norm{T_nx_n - Tx_n} + \norm{Tx_n - Tx}\leq\norm{T_n-T}\norm{x_n}+\norm T\norm{x_n-x}$.

- Reduction to nice sets and functions: for [[D-MDJII|Lebesgue measurable]] $E\subseteq\RR^n$, $m(E) = \lim_n m(E\cap B_n(0))$ by [[PR-KKJ6O|continuity of measure from below]], the sets $E\cap B_n(0)$ increasing to $E$; if $m(E)<\infty$, a compact $K\subseteq E$ and a finite union of cubes $R$ satisfy $m(E\setminus K)<\varepsilon$ and $m(E\,\triangle\,R)<\varepsilon$ for every $\varepsilon>0$, the first by [[T-IIKSW]] and the second by applying it to an open $O\supseteq E$ with $m(O\setminus E)<\varepsilon$ and a finite subunion of a cubical decomposition of $O$. For $1\leq p<\infty$, two continuous maps on $L^p$ that agree on simple functions, or on $C_c(\RR^n)$, agree on $L^p$, both families being [[PR-NFB7Q|dense in $L^p$]].

- Subsequences: a sequence converging in $L^p$ has an almost everywhere convergent subsequence ([[FF-I6VGK]]), and a bounded sequence in $\RR^n$ has a convergent subsequence ([[T-YKVFQ|Bolzano--Weierstrass]]).

- Sequential criteria: $\lim_{\varepsilon\to0}g(\varepsilon) = L$ if and only if $g(\varepsilon_n)\to L$ for every sequence $\varepsilon_n\to0$ with $\varepsilon_n\neq0$.

## Standard results

[[PR-WUZSG]]

[[PR-IGVTV]]

[[T-ERNLN]]

[[PR-L7LNZ]]

[[PR-6WMSR]]

[[FF-IAUQG]]

[[PR-PIVFR]]

[[T-IIKSW]]

[[FT-GQRV2]]

[[PR-7BGSE]]

[[T-SM8EW]]

[[T-RIY2P]]

[[PR-4OXGZ]]

[[PR-26CWE]]

[[T-BFOJT]]

## Exercises

[[P-4EOE5]]

[[PR-6NDTF]]
