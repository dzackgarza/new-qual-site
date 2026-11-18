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

No retained solution set covers this exercise: the card's own two directions are set out as separate steps, with the uniform approximation by step functions in one direction and the squeeze by continuous functions in the other.

Let $\mu_{n}=\frac1n\sum_{k\le n}\delta_{a_{k}}$ and $m$ be Lebesgue measure on $[0,1]$; note $\int f\,d\mu_{n}=\frac1n\sum_{k\le n}f(a_{k})$ and $\int\chi_{[c,d]}d\mu_{n}=\frac{\#\set{k\le n\mid a_{k}\in[c,d]}}{n}$.

::: pf

::: {.pf-step #indicators}
The sequence is equi-distributed exactly when $\int\chi_{[c,d]}d\mu_{n}\to\int\chi_{[c,d]}dm$ for every interval $[c,d]\subseteq[0,1]$.

::: pf-proof
Both sides are the same numbers: $\int\chi_{[c,d]}d\mu_{n}=\frac{\#\set{k\le n\mid a_{k}\in[c,d]}}{n}$ and $\int\chi_{[c,d]}dm=d-c$. So the defining limit is literally this statement.
:::

:::

::: {.pf-step #forward}
If the convergence holds for every interval indicator, it holds for every $f\in C[0,1]$.

::: pf-proof
Let $f$ be continuous and $\varepsilon>0$. $f$ is uniformly continuous, so there is a partition of $[0,1]$ into finitely many intervals $I_{j}=[x_{j},x_{j+1}]$ on which $f$ varies by at most $\varepsilon$; choosing $c_{j}=f(x_{j})$ gives the step function $s=\sum_{j}c_{j}\chi_{I_{j}}$ with $\sup\abs{f-s}\le\varepsilon$ and $s\le M$ bounded. Then $\abs{\int f\,d\mu_{n}-\int f\,dm}\le\abs{\int s\,d\mu_{n}-\int s\,dm}+2\varepsilon$, and the first term is a finite combination of interval-indicator differences, each tending to $0$ by step [](#indicators){.pf-ref}. Hence the limsup is at most $2\varepsilon$, and $\varepsilon$ was arbitrary.
:::

:::

::: {.pf-step #backward}
If the convergence holds for every $f\in C[0,1]$, it holds for every interval indicator.

::: pf-proof
Fix $[c,d]$ and $\varepsilon>0$. There are continuous $f^{-}\le\chi_{[c,d]}\le f^{+}$ with $\int f^{+}dm\le d-c+\varepsilon$, $\int f^{-}dm\ge d-c-\varepsilon$ and $f^{+}\le1$, $f^{-}\ge0$: take $f^{+}$ equal to $1$ on $[c,d]$, $0$ off $(c-\varepsilon,d+\varepsilon)$ and linear in between, and $f^{-}$ equal to $1$ on $[c+\varepsilon,d-\varepsilon]$, $0$ off $(c,d)$ and linear in between (with the obvious modifications when $c=0$ or $d=1$). Then
$$\int\chi_{[c,d]}d\mu_{n}\le\int f^{+}d\mu_{n}\le\int f^{+}dm+\varepsilon\le d-c+2\varepsilon$$
for large $n$, and symmetrically $\int\chi_{[c,d]}d\mu_{n}\ge d-c-2\varepsilon$. So the limit exists and equals $d-c$.
:::

:::

::: {.pf-qed}
Equi-distributedness is the case of interval indicators (step [](#indicators){.pf-ref}); continuous test functions imply those by step [](#backward){.pf-ref} and are implied by them by step [](#forward){.pf-ref}. Hence the two conditions are equivalent.
:::

:::

:::
