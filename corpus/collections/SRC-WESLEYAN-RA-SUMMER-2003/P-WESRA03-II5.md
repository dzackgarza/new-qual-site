---
schema: qual/card@1
id: P-WESRA03-II5
kind: problem
title: Failure of equality of iterated integrals with counting measure
classification:
  areas: [real-analysis]
  topics: [Tonelli-Fubini Theorem, Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 5 in the deterministic MinerU Flash extraction of analysis_2003-2007.pdf.
---

::: {.problem}
Let $X=\mathbb R$, let $\mathcal B(\mathbb R)$ be the Borel sigma-algebra, let $m$ be Lebesgue measure, and let $\sigma$ be counting measure on $\mathbb R$.
Define $f:\mathbb R^2\to\mathbb R$ by
\[
f(x,y)=
\begin{cases}
1,&x=y,\\
0,&x\ne y.
\end{cases}
\]
Show that
\[
\int_X\!\int_X f(x,y)\,dm(x)\,d\sigma(y)
\ne
\int_X\!\int_X f(x,y)\,d\sigma(y)\,dm(x).
\]
:::
