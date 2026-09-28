---
schema: qual/card@1
id: P-WESRA16-B4
kind: problem
title: 'Limits of integrals of powers of a nonnegative function'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B4 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $f:\mathbb R\to[0,\infty)$ be measurable with $\operatorname{supp}f\subset[0,1]$.
Put
\[
X=\{f>1\},\qquad Y=\{f=1\},\qquad Z=\{f<1\}.
\]
Assuming
\[
\lim_{n\to\infty}\int_{\mathbb R}f^n
\]
exists in $[0,\infty]$, prove that there are $\alpha,\beta,\gamma\in[0,\infty]$ such that
\[
\lim_{n\to\infty}\int_{\mathbb R}f^n
=\alpha\lambda(X)+\beta\lambda(Y)+\gamma\lambda(Z).
\]
Determine the relevant contributions using monotone and dominated convergence.
:::
