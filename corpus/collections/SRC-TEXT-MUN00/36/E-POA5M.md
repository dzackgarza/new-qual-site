---
schema: qual/card@1
id: E-POA5M
kind: problem
title: Compact locally imbeddable spaces imbed in euclidean space
classification:
  areas:
  - topology
  topics:
  - Manifolds
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 36: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-36-imbeddings-of-manifolds/problem-2-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-36-imbeddings-of-manifolds/problem-2-solution.txt), checked against
    Munkres, Topology (2000), Section 36 Exercise 2, printed p. 227, Theorem 36.1 and Theorem 26.7.
    Its route is the card's in substance -- a finite subcover by chartable open sets, functions
    supported inside them, and the map whose coordinates are the support functions and their
    products with the chart maps; the source reaches the support functions through the partition of
    unity of Theorem 36.1, and the card builds them by Urysohn's lemma from the double shrinking
    x in V_i inside cl(V_i) inside W_i inside cl(W_i) inside U_i. What was corrected: the source's
    display "F = (g_1, ..., g_n, f_1 . g_1, ..., f_n . g_n): X -> R^{n + k_1 + ... + k_n}" omits that
    each product f_i . g_i takes values in R^{k_i} and that f_i is only defined on U_i, so that the
    product must be read as zero off W_i; the card defines F_i piecewise and checks continuity at
    the boundary of U_i.
---

::: {.exercise}

Let $X$ be a compact Hausdorff space.
Suppose that for each $x \in X$, there is a neighborhood $U$ of $x$ and a positive integer $k$ such that $U$ can be imbedded in $\RR^k$.
Show that $X$ can be imbedded in $\RR^N$ for some positive integer $N$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own piecing argument is completed, with the shrinking, the Urysohn functions and the injectivity of the assembled map as separate steps.

Let $X$ be compact Hausdorff, and for each $x$ let $U_{x}\ni x$ be a neighbourhood admitting an imbedding $e_{x}:U_{x}\to\RR^{k_{x}}$.

::: pf

::: {.pf-step #shrinking}
There are finitely many points $x_{1},\dots,x_{m}$ and open sets $V_{i}\subseteq\overline{V_{i}}\subseteq W_{i}\subseteq\overline{W_{i}}\subseteq U_{i}$ with $\bigcup_{i}V_{i}=X$.

::: pf-proof
$X$ is compact Hausdorff, hence normal (Theorem 32.3, printed p. 202). Given $x\in U_{x}$ with $U_{x}$ open, normality gives an open $W_{x}$ with $x\in W_{x}\subseteq\overline{W_{x}}\subseteq U_{x}$; applying normality again to $x$ and $X\setminus W_{x}$ gives open $V_{x}$ with $x\in V_{x}\subseteq\overline{V_{x}}\subseteq W_{x}$. The sets $V_{x}$ cover $X$, so finitely many $V_{1},\dots,V_{m}$ do, and we relabel the corresponding $W,U,e$.
:::

:::

::: {.pf-step #urysohn}
There are continuous $\phi_{i}:X\to[0,1]$ with $\phi_{i}=1$ on $\overline{V_{i}}$ and $\phi_{i}=0$ off $W_{i}$.

::: pf-proof
$\overline{V_{i}}$ and $X\setminus W_{i}$ are disjoint closed sets (the second contains the complement of $\overline{W_{i}}\supseteq X\setminus W_{i}$'s interior... precisely, $\overline{V_{i}}\subseteq W_{i}$ implies $\overline{V_{i}}\cap(X\setminus W_{i})=\varnothing$), so Urysohn's lemma in a normal space gives such a function.
:::

:::

::: {.pf-step #assemble}
For each $i$ the map $\psi_{i}:X\to\RR^{k_{i}}$, $\psi_{i}(z)=\phi_{i}(z)\,e_{i}(z)$ on $W_{i}$ and $0$ off $W_{i}$, is well defined and continuous.

::: pf-proof
On $W_{i}$ both factors are continuous ($\phi_{i}$ on $X$, $e_{i}$ on $U_{i}\supseteq W_{i}$); off $W_{i}$ we have $\phi_{i}=0$, so the two formulas agree on the overlap $\partial W_{i}$-side, and continuity follows by the pasting lemma over the closed sets $\overline{W_{i}}$ and $X\setminus W_{i}$, whose union is $X$.
:::

:::

::: {.pf-step #injective}
$\Psi:X\to\RR^{m}\times\RR^{k_{1}}\times\cdots\times\RR^{k_{m}}$, $\Psi(z)=\big(\phi_{1}(z),\dots,\phi_{m}(z),\psi_{1}(z),\dots,\psi_{m}(z)\big)$, is injective.

::: pf-proof
Suppose $\Psi(y)=\Psi(z)$ with $y\ne z$. Since the $V_{i}$ cover $X$, some $i$ has $y\in V_{i}$, so $\phi_{i}(y)=1$; equal images give $\phi_{i}(z)=1$, hence $z\in W_{i}$ because $\phi_{i}$ vanishes off $W_{i}$. Then $\psi_{i}(y)=1\cdot e_{i}(y)$ and $\psi_{i}(z)=1\cdot e_{i}(z)$, and $\psi_{i}(y)=\psi_{i}(z)$ gives $e_{i}(y)=e_{i}(z)$, so $y=z$ by injectivity of $e_{i}$ — a contradiction. Hence $\Psi$ is injective.
:::

:::

::: {.pf-step #embed}
$\Psi$ is an imbedding of $X$ into $\RR^{N}$ for $N=m+k_{1}+\cdots+k_{m}$.

::: pf-proof
$\Psi$ is continuous, and injective by step [](#injective){.pf-ref}; a continuous injection from the compact space $X$ to the Hausdorff space $\RR^{N}$ is an imbedding (Theorem 26.6, printed p. 167).
:::

:::

::: {.pf-qed}
If $X=\varnothing$ the statement is trivial; otherwise $\Psi$ imbeds $X$ in $\RR^{N}$ with $N=m+k_{1}+\cdots+k_{m}$ by step [](#embed){.pf-ref}.
:::

:::

:::
