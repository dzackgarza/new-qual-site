---
schema: qual/card@1
id: P-CASP22D
kind: problem
title: "Equivalence of two-component complement and rational approximation with prescribed poles"
classification:
  areas:
  - complex-analysis
  topics:
  - Rational Approximation
  - Runge Theorem
  - Simply Connected
relations: []
review: draft
---

::: {.problem}
Let $G \subset \mathbb{C}$ be a region such that $0 \notin G$ and $G$ is not simply connected.
Show that the following are equivalent:

(i) $\mathbb{C}_\infty \setminus G$ has precisely two components $F_0, F_\infty$ such that $0 \in F_0$, $\infty \in F_\infty$.

(ii) Every $f \in H(G)$ can be approximated in $H(G)$ by rational functions with poles only in $\{0, \infty\}$.
:::

::: {.solution}
We use the pole-set form of Runge's theorem: if $A\subset\mathbb C_\infty
\setminus G$, then rational functions whose poles lie in $A$ are dense in
$H(G)$ if and only if $A$ meets every connected component of
$\mathbb C_\infty\setminus G$.

Assume (i). The set
\[
A=\{0,\infty\}
\]
meets both complementary components, because $0\in F_0$ and
$\infty\in F_\infty$. Runge's theorem therefore gives (ii).

Conversely assume (ii). By the same characterization, the allowed pole set
$\{0,\infty\}$ must meet every component of
$\mathbb C_\infty\setminus G$. Hence the complement has at most two
components. It cannot have only one: for a plane region, connectedness of the
complement in the Riemann sphere is equivalent to simple connectedness, while
$G$ is assumed not simply connected. Thus there are exactly two complementary
components. Since $0\notin G$ and $\infty\notin G$, they must be the components
$F_0$ and $F_\infty$ containing $0$ and $\infty$, respectively. This is (i).
:::
