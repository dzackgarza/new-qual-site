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
Egorov's theorem discards a set of measure less than $\varepsilon$ and makes an almost everywhere convergent sequence converge uniformly on the rest; Lusin's theorem discards such a set and makes a measurable function continuous on the rest.
In both theorems the remaining set is closed, and it depends on $\varepsilon$.

## Egorov: almost uniform convergence

[[FT-OGS76]]

[[FR-GG457]]

::: {.remark}
The finite-measure hypothesis is not a technical convenience: on $\RR$, $f_n \coloneqq \chi_{[n,n+1]}$ converges pointwise to $0$, while every set on which the convergence is uniform has complement of measure at least $1$ ([[real-analysis/measure/littlewoods-principles|Littlewood's three principles]]).
On a set of finite measure, almost everywhere convergence therefore implies [[FD-D7HOH|convergence in measure]].
:::

## Lusin: almost continuity

[[T-CGFCU]]

::: {.remark}
The exceptional set cannot be removed altogether: for $f \coloneqq \chi_{\QQ\cap[0,1]}$ on $E=[0,1]$, the restriction $\restrictionof{f}{E}$ is discontinuous at every point, so $F_\varepsilon = E$ is impossible.
Continuity of $\restrictionof{f}{F_\varepsilon}$ is a statement about the relative topology of $F_\varepsilon$, not about the continuity of $f$ at the points of $F_\varepsilon$.
:::

Both theorems express one of [[real-analysis/measure/littlewoods-principles|Littlewood's three principles]]: measurable sets are nearly finite unions of intervals, measurable functions are nearly continuous, and almost everywhere convergent sequences are nearly uniformly convergent.
