---
schema: qual/card@1
id: T-3QNBQ
kind: theorem
title: Weierstrass approximation theorem
prompts:
- State the Weierstrass approximation theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Stone-Weierstrass
  - Density
  - Polynomials
relations: []
review: draft
---

::: {.theorem}
Let $a<b$ and let $f\colon[a,b]\to\CC$ be continuous.
For every $\varepsilon>0$ there exists a polynomial $p$ such that
$$
\sup_{x\in[a,b]}\abs{f(x)-p(x)}<\varepsilon .
$$
If $f$ is real-valued, $p$ may be taken with real coefficients.
Equivalently, the polynomials are [[D-KJBAK|dense]] in the [[D-BG455|Banach space]] $C([a,b])$ with the norm $\norm{g}_\infty\coloneqq\sup_{x\in[a,b]}\abs{g(x)}$.
:::
