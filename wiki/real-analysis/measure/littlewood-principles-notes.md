---
title: "Littlewood's principles: proofs"
order: 60
---

# Littlewood's principles: proofs

For Lebesgue measure $m$ on $\RR^d$, Egorov's theorem and Lusin's theorem each replace a measure-theoretic hypothesis by a classical one on a closed set whose complement has arbitrarily small measure.

## Egorov: almost uniform convergence

[[FT-OGS76]]

[[FR-GG457]]

::: {.proof title="Egorov's theorem"}
Let $E\subseteq\RR^d$ be measurable with $m(E)<\infty$ and let $f_k\to f$ almost everywhere on $E$; removing a null set, assume $f_k(x)\to f(x)$ for every $x\in E$.
For integers $n\geq1$ and $k\geq0$, let
$$
E_k^n\coloneqq\theset{x\in E \st \abs{f_j(x)-f(x)}<1/n \text{ for all } j>k}.
$$
For fixed $n$, $E_k^n\subseteq E_{k+1}^n$ and $\bigcup_k E_k^n = E$, so by continuity of measure from below and $m(E)<\infty$ there is $k_n$ with $m(E\setminus E_{k_n}^n)<2^{-n}$.
By construction, $\abs{f_j(x)-f(x)}<1/n$ whenever $j>k_n$ and $x\in E_{k_n}^n$.

Given $\varepsilon>0$, choose $N$ with $\sum_{n\geq N}2^{-n}<\varepsilon/2$ and let $\tilde A_\varepsilon\coloneqq\bigcap_{n\geq N}E_{k_n}^n$.
Then
$$
m(E\setminus\tilde A_\varepsilon)\leq\sum_{n\geq N}m(E\setminus E_{k_n}^n)<\varepsilon/2.
$$
For $\delta>0$, choose $n\geq N$ with $1/n<\delta$; every $x\in\tilde A_\varepsilon$ lies in $E_{k_n}^n$, so $\abs{f_j(x)-f(x)}<\delta$ for all $j>k_n$.
Hence $f_k\to f$ uniformly on $\tilde A_\varepsilon$.
Finally, by inner regularity of Lebesgue measure choose a closed $A_\varepsilon\subseteq\tilde A_\varepsilon$ with $m(\tilde A_\varepsilon\setminus A_\varepsilon)<\varepsilon/2$; then $m(E\setminus A_\varepsilon)<\varepsilon$ and $f_k\to f$ uniformly on $A_\varepsilon$.

:::

## Lusin: almost continuity

[[T-CGFCU]]

[[FT-XIVPL]]

::: {.proof title="Lusin's theorem"}
Let $E\subseteq\RR^d$ be measurable with $m(E)<\infty$ and $f$ measurable and finite almost everywhere on $E$, and let $\varepsilon>0$.
Choose step functions $f_n$ with $f_n\to f$ almost everywhere on $E$.
Each step function is continuous outside the boundaries of finitely many rectangles, so there are sets $E_n$ with $m(E_n)<2^{-n}$ such that $f_n$ is continuous on $E\setminus E_n$.
By Egorov's theorem there is $A_{\varepsilon/3}\subseteq E$ with $m(E\setminus A_{\varepsilon/3})\leq\varepsilon/3$ on which $f_n\to f$ uniformly.
Choose $N$ with $\sum_{n\geq N}2^{-n}<\varepsilon/3$ and let
$$
F'\coloneqq A_{\varepsilon/3}\setminus\bigcup_{n\geq N}E_n.
$$
For $n\geq N$, $f_n$ is continuous on $F'$, so the uniform limit $f$ is continuous on $F'$.
By inner regularity choose a closed $F_\varepsilon\subseteq F'$ with $m(F'\setminus F_\varepsilon)<\varepsilon/3$.
Then $f$ is continuous on $F_\varepsilon$ and $m(E\setminus F_\varepsilon)<\varepsilon$.

:::
