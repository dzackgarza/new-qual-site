---
schema: qual/card@1
id: E-PER08-5.2
kind: problem
title: Proper local diffeomorphisms are covering maps
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Do this exercise if you know the basic facts about smooth manifolds.
Suppose Y and X are smooth n-manifolds, and p: Y $\\to$ X a smooth, proper map whose derivative Dp: TxY $\\to$ Tp(x)X is an isomorphism for all x $\\in$ Y . Then p is a (finite-sheeted) covering map.
:::

::: {.solution}
The map is a proper local diffeomorphism, hence a finite-sheeted covering.

<1>1. Every point of $Y$ has a neighbourhood on which $p$ is a diffeomorphism.
::: {.proof}
Since $Dp_y:T_yY\to T_{p(y)}X$ is an isomorphism, the inverse function theorem gives open neighbourhoods $V_y\ni y$ and $U_y\ni p(y)$ such that $p|_{V_y}:V_y\to U_y$ is a diffeomorphism.
:::

<1>2. Every fibre $p^{-1}(x)$ is finite.
::: {.proof}
It is discrete by <1>1. It is also compact because $p$ is proper and $\{x\}$ is compact.
A compact discrete space is finite.
:::

<1>3. A sufficiently small neighbourhood of $x$ is evenly covered.
::: {.proof}
Write $p^{-1}(x)=\{y_1,\dots,y_r\}$.
Choose pairwise disjoint inverse-function neighbourhoods $V_i$ of the $y_i$, with $p(V_i)$ containing an open neighbourhood of $x$.
After shrinking, choose an open $U\ni x$ with $U\subseteq\bigcap_i p(V_i)$.

We claim that, after shrinking $U$ once more, $p^{-1}(U)\subseteq\bigcup_iV_i$.
Otherwise there would be a sequence $x_j\to x$ and points $z_j\notin\bigcup_iV_i$ with $p(z_j)=x_j$.
Properness makes $p^{-1}(K)$ compact for a compact neighbourhood $K$ containing all sufficiently large $x_j$; a convergent subsequence $z_{j_k}\to z$ would satisfy $p(z)=x$, hence $z=y_i$ for some $i$, contradicting $z_{j_k}\notin V_i$ eventually.

Thus
\[
p^{-1}(U)=\coprod_{i=1}^r(V_i\cap p^{-1}(U)),
\]
and each summand maps diffeomorphically onto $U$.
Hence $p$ is a covering with $r<\infty$ sheets.
:::
:::
