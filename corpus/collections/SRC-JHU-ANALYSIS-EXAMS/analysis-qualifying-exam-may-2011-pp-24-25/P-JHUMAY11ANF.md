---
schema: qual/card@1
id: P-JHUMAY11ANF
kind: problem
title: Absolutely summable Fourier coefficients give a continuous representative
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 6 of the May 2011 JHU analysis qualifying exam in the preserved compiled source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Let $f \in L^1(S^1)$ such that $\widehat{f} \in \ell^1(\mathbb{Z})$.
Prove that $f \in C(S^1)$ (that is, $f$ is equal almost everywhere to a continuous function on the circle $S^1$).
:::

::: {.solution}
Write $\widehat f(n)=\frac1{2\pi}\int_{-\pi}^\pi f(x)e^{-inx}\,dx$ and let $g(x)\definedas\sum_{n\in\ZZ}\widehat f(n)e^{inx}$.

::: pf

::: {.pf-step #s1}

$g$ is continuous on $S^1$.

::: pf-proof

$\abs{\widehat f(n)e^{inx}}=\abs{\widehat f(n)}$ and $\sum_n\abs{\widehat f(n)}<\infty$, so by the Weierstrass $M$-test the series converges uniformly on $\RR$. Its terms are continuous and $2\pi$-periodic, so $g$ is too.

:::

:::

::: {.pf-step #s2}

$\widehat g(k)=\widehat f(k)$ for all $k\in\ZZ$.

::: pf-proof

Uniform convergence allows integrating term by term, and $\frac1{2\pi}\int_{-\pi}^\pi e^{i(n-k)x}\,dx$ is $1$ for $n=k$ and $0$ otherwise.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $f-g\in L^1(S^1)$ has all Fourier coefficients $0$, so $f-g=0$ almost everywhere by the uniqueness theorem for Fourier coefficients of $L^1(S^1)$ functions, a consequence of Fejér's theorem [@SS03a]. By step [](#s1){.pf-ref}, $f$ equals the continuous function $g$ almost everywhere.

:::

:::

:::
