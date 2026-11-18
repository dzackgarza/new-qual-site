---
schema: qual/card@1
id: P-JHUFA06ANG
kind: problem
title: '$L^2$ boundedness and vanishing $L^1$ norm imply weak convergence to $0$'
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 7 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The truncation is now justified (dominated convergence for the L^2 convergence, with |g|^2 as the dominating function), the two estimates are separated into the Cauchy-Schwarz part and the bounded part, and the two epsilons are kept distinct: eps for the truncation and M/J < eps for the mean part, so the final bound is 2 eps rather than an unstated epsilon/2 + epsilon/2. No retained solution set covers the exercise (the provenance is the JHU examination papers, and the card records only the statement), so the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $(f_j)$ be functions in $L^2([0,1])$ satisfying
$$
\int_0^1 \abs{f_j}\le \frac1j,
\qquad
\int_0^1 \abs{f_j}^2\le1.
$$
Prove that $f_j\rightharpoonup0$ weakly in $L^2([0,1])$.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the JHU examination papers and the card records only the statement. The argument is the card's own, and it is the standard truncation argument.

::: pf

::: {.pf-step #truncate}
For $g\in L^2([0,1])$ and $M>0$, $g_M=g\mathbf 1_{\{\abs g\le M\}}$ satisfies $\norm{g_M}_\infty\le M$ and $\norm{g-g_M}_2\to0$ as $M\to\infty$.

::: pf-proof
$\abs{g_M}=\abs g$ where $\abs g\le M$ and $0$ elsewhere, so $\abs{g_M}\le M$ almost everywhere. Also $\abs{g-g_M}^2=\abs g^2\mathbf 1_{\{\abs g>M\}}$ decreases pointwise to $0$ as $M\to\infty$ and is dominated by the integrable function $\abs g^2$, so $\norm{g-g_M}_2^2=\int\abs{g-g_M}^2\to0$ by dominated convergence.
:::

:::

::: {.pf-step #cf}
Given $g\in L^2$ and $\varepsilon>0$ there is $M>0$ with $\norm{g-g_M}_2<\varepsilon$ and, for every $j$,
$$
\abs{\int_0^1f_j\,(g-g_M)}\le\norm{f_j}_2\norm{g-g_M}_2<\varepsilon .
$$

::: pf-proof
Choose $M$ by step [](#truncate){.pf-ref} with $\norm{g-g_M}_2<\varepsilon$; this is possible because the norms decrease to $0$. Both $f_j$ and $g-g_M$ lie in $L^2$, so Hölder's inequality (or Cauchy-Schwarz) gives $\abs{\int f_j(g-g_M)}\le\norm{f_j}_2\norm{g-g_M}_2$, and $\norm{f_j}_2\le1$ by hypothesis.
:::

:::

::: {.pf-step #mean}
For that $M$ and every $j$, $\abs{\int_0^1f_jg_M}\le\dfrac Mj$.

::: pf-proof
$\abs{f_jg_M}\le M\abs{f_j}$ pointwise, so $\abs{\int f_jg_M}\le M\int\abs{f_j}\le M/j$ by the hypothesis $\int\abs{f_j}\le1/j$.
:::

:::

::: {.pf-step #weak}
$\int_0^1f_jg\to0$ for every $g\in L^2([0,1])$.

::: pf-proof
Fix $g$ and $\varepsilon>0$, take $M$ from step [](#cf){.pf-ref}, and let $J$ be an integer with $M/J<\varepsilon$. For $j\ge J$,
$$
\abs{\int_0^1f_jg}\le\abs{\int_0^1f_j(g-g_M)}+\abs{\int_0^1f_jg_M}<\varepsilon+\varepsilon,
$$
by steps [](#cf){.pf-ref} and [](#mean){.pf-ref}. So the sequence of integrals tends to $0$; as $g$ was arbitrary, $f_j\rightharpoonup0$ weakly in $L^2([0,1])$.
:::

:::

:::
:::
