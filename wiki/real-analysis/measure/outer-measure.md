---
title: Outer measure and the construction
order: 10
topics:
- Measure Theory
- Continuity of Measure
---

# Outer measure and the construction

Let $(X,\mathcal M,\mu)$ be a measure space.
Countable additivity gives continuity of measure: if $E_1\subseteq E_2\subseteq\cdots$ then $\mu\qty{\bigcup_n E_n} = \lim_n\mu(E_n)$, and if $E_1\supseteq E_2\supseteq\cdots$ with $\mu(E_1)<\infty$ then $\mu\qty{\bigcap_n E_n}=\lim_n\mu(E_n)$.
For arbitrary $E_n\in\mathcal M$, the sets $F_n\coloneqq E_n\setminus\bigcup_{k<n}E_k$ are disjoint with the same union, which reduces statements about $\bigcup_nE_n$ to countable additivity.

[[D-QYLPH]]

[[PR-A4J4G]]

[[T-7LQ7X]]

[[FS-ACP4W]]

[[PR-KKJ6O]]

[[FT-OMADI]]

## Outer measure

An outer measure $\mu^*$ on $X$ is defined on every subset of $X$, with $\mu^*(\varnothing)=0$, monotone, and countably subadditive.
A set $A$ is Carathéodory measurable if $\mu^*(E) = \mu^*(E\cap A)+\mu^*(E\setminus A)$ for every $E\subseteq X$.
By Carathéodory's theorem, the Carathéodory measurable sets form a $\sigma$-algebra on which $\mu^*$ is countably additive, hence a measure.

[[PR-LF7SW]]

[[D-UYOGE]]

[[FT-O4DRR]] [[FF-LA4J2]]

## Measures on $\RR^d$

Lebesgue measure $m$ on $\RR^d$ is translation invariant, satisfies $m(aE) = \abs a^d m(E)$ for $a\in\RR$, and assigns to a rectangle the product of its side lengths.
It is complete, and for every Lebesgue measurable $E$ and $\varepsilon>0$ there are an open $U\supseteq E$ and a closed $F\subseteq E$ with $m(U\setminus E)<\varepsilon$ and $m(E\setminus F)<\varepsilon$.
For measurable $E_n$, the set $\limsup_n E_n$ of points lying in infinitely many $E_n$ is measurable, and by the Borel--Cantelli lemma it is null when $\sum_n m(E_n)<\infty$.

[[PR-I4YON]]

[[PR-DXWWU]]

[[FR-7YFAU]]

[[T-KZNWM]]

[[PR-NULVE]]

[[T-OTR5M]]

[[FF-GNU7E]]

[[FR-CSUMF]]

[[PR-I44DD]]

[[PR-552IH]]

[[D-BXAUS]]

[[PR-UHWNM]]

::: {.remark}
A $\sigma$-finite measure space is a countable union of sets of finite measure, so theorems proved for finite measures, such as the Tonelli and Fubini theorems for product measures, extend to $\sigma$-finite measures by exhaustion.
For Lebesgue measure, every measurable set of finite measure $E$ also contains a compact $K$ with $m(E\setminus K)<\varepsilon$, which relates measurable sets to compact sets in topological arguments.

:::

[[PR-TGQFG]]
