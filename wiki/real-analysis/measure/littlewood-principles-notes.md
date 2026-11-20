---
title: "Egorov and Lusin"
order: 60
topics:
- Measure Theory
- Egorov
- Convergence of Functions
---

# Egorov and Lusin

Let $m$ be Lebesgue measure on $\RR^d$, let $E\subseteq\RR^d$ be measurable with $m(E)<\infty$, and let $\varepsilon>0$.
The remaining set in both theorems is closed and depends on $\varepsilon$: Egorov's discards one of measure less than $\varepsilon$ and makes an almost everywhere convergent sequence converge uniformly on the rest, and Lusin's discards such a set and makes a measurable function continuous on the rest.

## Egorov: almost uniform convergence

[[FT-OGS76]]

On a set of finite measure, almost everywhere convergence implies [[FD-D7HOH|convergence in measure]] ([[FR-GG457|a direct proof]], [@Fol99, Theorem 2.33 and Exercise 2.39]).

The finite-measure hypothesis is needed: [[real-analysis/measure/littlewoods-principles|Littlewood's three principles]] gives a sequence for which no set of finite complement carries uniform convergence.

## Lusin: almost continuity

[[T-CGFCU]]

::: {.remark}
Continuity of $\restrictionof{f}{F_\varepsilon}$ is a statement about the relative topology of $F_\varepsilon$, not about the continuity of $f$ at the points of $F_\varepsilon$.
:::

Both theorems express one of [[real-analysis/measure/littlewoods-principles|Littlewood's three principles]]: measurable sets are nearly finite unions of intervals, measurable functions are nearly continuous, and almost everywhere convergent sequences are nearly uniformly convergent.
