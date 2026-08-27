---
order: 20
title: Theorems
---

# Theorems

## Theorems

[[T-YOZX6]]

[[T-UW2GQ]]

[[T-2R7PC]]

[[PR-H4CYN]]

## Topology / Sets

[[T-YOAXZ]]

::: {.proof}
Fix $\eps>0$, we'll find a $\delta$ that works for all $x\in X$ uniformly.
For every $x\in X$, pick a $\delta_x$ neighborhood satisfying the conditions for (assumed) continuity.
Take an open cover by $\delta_x/2$ balls, extract a finite subcover, take $\delta$ the minimal radius.
:::

[[PR-25GM2]]

::: {.proof title="Compact iff sequentially compact, metric spaces"}
Let $(X,d)$ be a metric space.

- Compact $\implies$ sequentially compact.
  If a sequence $\theset{x_n}$ takes only finitely many values, some value occurs infinitely often and that constant subsequence converges.
  Otherwise pass to infinitely many distinct terms and write $S$ for their set.
  If no subsequence of $\theset{x_n}$ converges in $X$, then $S$ has no limit point in $X$, so $S$ is closed and discrete: each $s\in S$ has a ball $B_s$ with $B_s\cap S = \theset{s}$.
  Then $\theset{B_s}_{s\in S}$ together with $X\setminus S$ is an open cover with no finite subcover, so $X$ is not compact.

- Sequentially compact $\implies$ compact.
  A sequentially compact metric space is complete: a Cauchy sequence has a convergent subsequence, hence converges to the same limit.
  It is totally bounded: if not, some $\eps>0$ admits a sequence with $d(x_i,x_j)\geq \eps$ for $i\neq j$, and that sequence has no Cauchy (hence no convergent) subsequence.
  Complete and totally bounded metric spaces are compact: if an open cover $\mathcal{U}$ had no finite subcover, total boundedness would produce a nested sequence of nonempty closed sets $F_n$ with $\operatorname{diam} F_n \to 0$ and no $F_n$ covered by finitely many members of $\mathcal{U}$; completeness supplies a point of $\intersect_n F_n$, which lies in some $U\in\mathcal{U}$, and for large $n$ one has $F_n\subset U$.
:::

[[PR-FKJCO]]

::: {.proof}
Take $f_k(x) = x^n$, which converges to $\chi(x=1)$.
The limit is not continuous, so no subsequence can converge.
:::

[[T-QPTHZ]]

[[PR-6C3GQ]]

[[C-WR7YV]]

[[PR-JTFMW]]

::: {.proof}
Its complement is a union of open intervals, and can't contain an interval since intervals have positive measure and $m(C_n)$ tends to zero.
:::

[[C-44LL4]]

[[PR-OGEEA]]

[[T-DY44M]]

[[L-JBMRH]]

## Functions

[[PR-HRAOC]]

## Littlewood's Principles ("Almost" Theorems)

[[T-XZE3E]]

::: {.proof title="of Egorov"}

![](../../../../assets/assets/figures/2021-06-11_18-07-43.png)

![](../../../../assets/assets/figures/2021-06-11_18-07-58.png)
:::

[[T-CGFCU]]

::: {.proof title="of Lusin"}

![](../../../../assets/assets/figures/2021-06-11_18-04-52.png)
:::

## Unsorted

[[PR-SX6NO]]

[[PR-CZS5F]]
