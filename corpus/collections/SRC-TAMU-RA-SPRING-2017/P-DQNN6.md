---
schema: qual/card@1
id: P-DQNN6
kind: problem
title: Equidistribution on $[0,1]$ iff empirical measures converge weakly against
  $C[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
---

::: {.problem}
We say a sequence $\{a_n\}$ in $[0,1]$ is equi-distributed if for all intervals $[c,d] \subset [0,1]$, $\lim_{n\to\infty} \frac{\cardinality{\{a_1,\dots,a_n\}\cap[c,d]}}{n} = d-c$.
Prove that $\{a_n\}$ in $[0,1]$ is equi-distributed iff $\lim_{n\to\infty} \int f d\mu_n = \int f dm$ for all $f \in C[0,1]$, where $\mu_n = \frac{1}{n}\sum_{k=1}^n \delta_{a_k}$.
:::

::: {.solution}

No retained solution set covers this exercise, and the printed statement is **false as printed**: it counts $\cardinality{\theset{a_{1},\dots,a_{n}}\cap[c,d]}$, the number of *distinct* values, whereas the identity with $\int\chi_{[c,d]}d\mu_{n}$ requires the count *with multiplicity*. The counterexample is step [](#defect){.pf-ref}; the corrected equivalence, with multiplicity, is proved in the remaining steps.

Let $\mu_{n}=\frac1n\sum_{k\le n}\delta_{a_{k}}$ and $m$ be Lebesgue measure on $[0,1]$; then $\int\chi_{[c,d]}d\mu_{n}=\frac{\#\set{k\le n\mid a_{k}\in[c,d]}}{n}$, a count with multiplicity.

::: pf

::: {.pf-step #defect}
The printed equivalence fails: with $a_{2k-1}=a_{2k}=\{k\alpha\}$ for irrational $\alpha$, the measures $\mu_{n}$ converge weakly to $m$ while $\frac{\cardinality{\theset{a_{1},\dots,a_{2N}}\cap[0,1]}}{2N}\to\frac12\ne1$.

::: pf-proof
$\{k\alpha\}$ is equidistributed mod $1$ (Kronecker), so for $n=2N$ one has $\mu_{2N}=\frac{1}{N}\sum_{k\le N}\delta_{\{k\alpha\}}$, whose interval masses tend to $d-c$; hence $\int f\,d\mu_{n}\to\int f\,dm$ for all continuous $f$. But the set of distinct values among $a_{1},\dots,a_{2N}$ is exactly $\theset{\{k\alpha\}\mid k\le N}$, so on $[0,1]$ its cardinality is $N$, and the printed ratio is $\frac{N}{2N}=\frac12$.
:::

:::

::: {.pf-step #forward}
If the convergence with multiplicity holds for every interval, it holds for every $f\in C[0,1]$.

::: pf-proof
Given continuous $f$ and $\varepsilon>0$, uniform continuity gives a step function $s=\sum_{j}c_{j}\chi_{I_{j}}$ with $\sup\abs{f-s}\le\varepsilon$; then $\abs{\int f\,d\mu_{n}-\int f\,dm}\le\abs{\int s\,d\mu_{n}-\int s\,dm}+2\varepsilon$, and the first term is a finite combination of interval differences, each tending to $0$. So the limsup is at most $2\varepsilon$.
:::

:::

::: {.pf-step #backward}
If the convergence holds for every $f\in C[0,1]$, it holds for every interval, with multiplicity.

::: pf-proof
Fix $[c,d]$ and $\varepsilon>0$, and choose continuous $f^{-}\le\chi_{[c,d]}\le f^{+}$ with $\int f^{+}dm\le d-c+\varepsilon$ and $\int f^{-}dm\ge d-c-\varepsilon$ (linear ramps on $[c-\varepsilon,c]$, $[d,d+\varepsilon]$ and on $[c,c+\varepsilon]$, $[d-\varepsilon,d]$, with the obvious changes at the endpoints of $[0,1]$). Then $\int\chi_{[c,d]}d\mu_{n}\le\int f^{+}d\mu_{n}\le d-c+2\varepsilon$ for large $n$, and symmetrically from below, so the limit is $d-c$.
:::

:::

::: {.pf-step #multiplicity}
Hence: the interval counts *with multiplicity* converge to the lengths if and only if $\int f\,d\mu_{n}\to\int f\,dm$ for all $f\in C[0,1]$.

::: pf-proof
The equivalence is steps [](#forward){.pf-ref} and [](#backward){.pf-ref}, together with the identity $\int\chi_{[c,d]}d\mu_{n}=\frac{\#\set{k\le n\mid a_{k}\in[c,d]}}{n}$ noted above.
:::

:::

::: {.pf-qed}
The printed version, with distinct-value cardinalities, is refuted by step [](#defect){.pf-ref}; the true statement, with the multiplicity count, is step [](#multiplicity){.pf-ref}. A card that restated the printed claim without this remark would be asserting something false.
:::

:::

:::
