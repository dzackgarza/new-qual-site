---
schema: qual/card@1
id: D-OM7TD
kind: definition
title: Separation axioms $T_0$ through $T_4$
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Separation Axioms
  - Counterexamples
relations:
- kind: variant-of
  target: D-4DXA7
review: draft
---

::: {.definition}
Let $X$ be a topological space.
Separating two sets by neighborhoods means finding disjoint open sets containing them.

- $X$ is \dfn{$T_0$} if for all $x_1\neq x_2$ in $X$ some open set contains exactly one of $x_1,x_2$.

- $X$ is \dfn{$T_1$} if for all $x_1\neq x_2$ in $X$ there is an open set containing $x_1$ but not $x_2$, and an open set containing $x_2$ but not $x_1$.

- $X$ is \dfn{$T_2$} if any two distinct points are separated by neighborhoods; this is the [[D-6FMP3|Hausdorff]] condition.

- $X$ is \dfn{$T_{2.5}$} if any two distinct points $x_1,x_2$ have open neighborhoods $U_1\ni x_1$ and $U_2\ni x_2$ with $\overline{U_1}\cap\overline{U_2}=\emptyset$.

- $X$ is \dfn{$T_3$} if it is $T_0$ and [[D-EPTMG|regular]]: for every $x\in X$ and every closed $F\subseteq X$ with $x\notin F$, the sets $\ts{x}$ and $F$ are separated by neighborhoods.

- $X$ is \dfn{$T_{3.5}$} if it is $T_0$ and \dfn{completely regular}: for every $x\in X$ and every closed $F\subseteq X$ with $x\notin F$ there is a continuous $f\colon X\to[0,1]$ with $f(x)=0$ and $f(F)\subseteq\ts{1}$.

- $X$ is \dfn{$T_4$} if it is $T_1$ and [[D-YEQC3|normal]]: any two disjoint closed subsets of $X$ are separated by neighborhoods.
:::

::: {.remark}
A space is $T_1$ if and only if every one-point subset is closed.
:::

::: {.example}
A space that is not $T_0$: let $\mathcal L^2(\RR)$ be the set of measurable $f\colon\RR\to\CC$ with $\int_\RR\abs{f}^2<\infty$, topologized by the pseudometric $d(f,g)=\qty{\int_\RR\abs{f-g}^2}^{1/2}$.
If $f\neq g$ agree almost everywhere, then $d(f,g)=0$, so every open set containing one of them contains the other.
:::

::: {.example}
A space that is $T_0$ but not $T_1$: for a commutative ring $R$ with a prime ideal that is not maximal, $\Spec R$ with the Zariski topology.
The closure of the point $\mathfrak p$ is $V(\mathfrak p)=\ts{\mathfrak q\in\Spec R \st \mathfrak q\supseteq\mathfrak p}$, so a prime that is not maximal is not a closed point; distinct primes have distinct closures, which gives $T_0$.
:::
