---
schema: qual/card@1
id: P-WESRA13A-II6
kind: problem
title: 'Absolute continuity implies bounded variation'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. Flash renders the interval delimiters as braces; the standard absolute-continuity/bounded-variation setting determines the interval $[0,1]$.
---

::: {.problem}
Let $f:[0,1]\to\RR$ be absolutely continuous.
Prove directly from the definitions that $f$ has bounded variation.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

By absolute continuity, there exists $\delta>0$ such that for every finite family of pairwise disjoint intervals
$$
(a_j,b_j)\subset[0,1]
$$
with
$$
\sum_j(b_j-a_j)<\delta,
$$
one has
$$
\sum_j\abs{f(b_j)-f(a_j)}<1.
$$


::: pf-proof

This is the definition of absolute continuity applied with $\varepsilon=1$.

:::

:::

::: {.pf-step #s1-2}

Choose an integer $M$ such that
$$
\frac1M<\delta,
$$
and let
$$
0=t_0<t_1<\cdots<t_M=1,
\qquad
 t_r=\frac rM.
$$
For any partition
$$
P:0=x_0<x_1<\cdots<x_n=1,
$$
let $P'$ be the common refinement obtained by adjoining all the points $t_1,\ldots,t_{M-1}$.
Then
$$
\sum_{i=1}^n\abs{f(x_i)-f(x_{i-1})}
\le
\sum_{[u,v]\in P'}\abs{f(v)-f(u)}.
$$


::: pf-proof

Each interval $[x_{i-1},x_i]$ is subdivided by $P'$ into finitely many consecutive subintervals
$$
[u_0,u_1],\ldots,[u_{r-1},u_r]
$$
with $u_0=x_{i-1}$ and $u_r=x_i$. The triangle inequality gives
$$
\abs{f(x_i)-f(x_{i-1})}
\le
\sum_{j=1}^r\abs{f(u_j)-f(u_{j-1})}.
$$
Summing over $i$ yields the stated inequality.

:::

:::

::: {.pf-step #s1-3}

For each $r=1,\ldots,M$, the sum of the increments of $f$ over those refined partition intervals contained in $[t_{r-1},t_r]$ is less than $1$.


::: pf-proof

Fix $r$. The refined partition intervals inside $[t_{r-1},t_r]$ are pairwise disjoint, and the sum of their lengths is exactly
$$
t_r-t_{r-1}=\frac1M<\delta.
$$
Apply step [](#s1-1){.pf-ref} to this finite family. The resulting sum of absolute increments is less than $1$.

:::

:::

::: {.pf-step #s1-4}

Every partition $P$ of $[0,1]$ satisfies
$$
\sum_{i=1}^n\abs{f(x_i)-f(x_{i-1})}<M.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the variation sum for $P$ is bounded by that of the refinement $P'$. Group the intervals of $P'$ according to the fixed subintervals
$$
[t_{r-1},t_r],
\qquad r=1,\ldots,M.
$$
By step [](#s1-3){.pf-ref}, each group contributes less than $1$. Hence the full refined sum is less than $M$.

:::

:::

::: {.pf-step #s1-5}

Therefore $f$ has bounded variation on $[0,1]$.


::: pf-proof

The total variation is
$$
V_0^1(f)
=
\sup_P
\sum_{i=1}^n\abs{f(x_i)-f(x_{i-1})},
$$
where the supremum is over all finite partitions of $[0,1]$. Step [](#s1-4){.pf-ref} gives the uniform bound
$$
V_0^1(f)\le M<\infty.
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is exactly the assertion that $f$ is of bounded variation.

:::

:::

:::
