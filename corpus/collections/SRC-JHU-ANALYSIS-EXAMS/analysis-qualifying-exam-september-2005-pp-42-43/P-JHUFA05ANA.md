---
schema: qual/card@1
id: P-JHUFA05ANA
kind: problem
title: '$\norm{f_n}_2^2\le n^{-2}$ forces $f_n\to0$ a.e.'
classification:
  areas:
  - real-analysis
  topics:
  - Convergence Theorems
  - Borel-Cantelli
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the JHU Analysis Qualifying Exam, September 2005, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $(f_n)$ be Lebesgue-measurable functions on $[0,1]$ satisfying
$$
\int_0^1 \abs{f_n(x)}^2\,dx\le \frac1{n^2}.
$$
Prove that
$$
f_n(x)\longrightarrow0
\qquad\text{for almost every }x\in[0,1].
$$
:::

::: {.solution}

The argument is the card's own: Chebyshev's inequality, the first Borel--Cantelli lemma for each level $1/m$, and a countable union of null exceptional sets. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $(f_{n})$ be Lebesgue measurable on $[0,1]$ with $\int_{0}^{1}\abs{f_{n}}^{2}\le n^{-2}$; all integrals are over $[0,1]$ and $m$ is Lebesgue measure there.

::: pf

::: {.pf-step #estimate}
For $m\ge1$ and $n\ge1$ the set $E_{n,m}=\{x:\abs{f_{n}(x)}>1/m\}$ is measurable with $m(E_{n,m})\le m^{2}/n^{2}$.

::: pf-proof
$f_{n}$ is measurable, so $E_{n,m}$ is measurable. On $E_{n,m}$ one has $1/m^{2}<\abs{f_{n}}^{2}$, hence
$$
\frac{1}{m^{2}}m(E_{n,m})=\int_{E_{n,m}}\frac{1}{m^{2}}\le\int_{E_{n,m}}\abs{f_{n}}^{2}\le\int_{0}^{1}\abs{f_{n}}^{2}\le\frac{1}{n^{2}},
$$
the last inequality by hypothesis; multiplying by $m^{2}$ gives the estimate.
:::

:::

::: {.pf-step #summable}
$\sum_{n\ge1}m(E_{n,m})\le m^{2}\sum_{n\ge1}n^{-2}<\infty$ for each fixed $m$.

::: pf-proof
Summing the estimate of step [](#estimate){.pf-ref} over $n$ and using $0\le m(E_{n,m})$ gives the first inequality, and $\sum n^{-2}$ converges.
:::

:::

::: {.pf-step #borel-cantelli}
For each $m$ there is a null set $N_{m}$ such that every $x\notin N_{m}$ satisfies $\abs{f_{n}(x)}\le1/m$ for all sufficiently large $n$.

::: pf-proof
By step [](#summable){.pf-ref} the sets $E_{n,m}$ have summable measures, so the first Borel--Cantelli lemma says that the set
$$
N_{m}=\limsup_{n}E_{n,m}=\{x:x\in E_{n,m}\ \text{for infinitely many }n\}
$$
has $m(N_{m})=0$. If $x\notin N_{m}$ then $x\in E_{n,m}$ for only finitely many $n$, so there is $N_{m}(x)$ with $x\notin E_{n,m}$, that is $\abs{f_{n}(x)}\le1/m$, for every $n\ge N_{m}(x)$.
:::

:::

::: {.pf-step #conclusion}
$f_{n}(x)\to0$ for almost every $x\in[0,1]$.

::: pf-proof
Let $N=\bigcup_{m\ge1}N_{m}$, a countable union of null sets and therefore null. Let $x\notin N$ and $\varepsilon>0$; choose $m$ with $1/m<\varepsilon$. Since $x\notin N_{m}$, step [](#borel-cantelli){.pf-ref} gives $N_{m}(x)$ with $\abs{f_{n}(x)}\le1/m<\varepsilon$ for all $n\ge N_{m}(x)$. So $f_{n}(x)\to0$ for every $x$ outside the null set $N$.
:::

:::

:::
:::
