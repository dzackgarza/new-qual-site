---
schema: qual/card@1
id: P-UCLARA12S-09
kind: problem
title: Jordan lemma on a quarter circle
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Spring 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Prove Jordan's lemma: if $f:\mathbb C\to\mathbb C$ is meromorphic, $R>0$, and $k>0$, then
\[
\left|\int_\Gamma f(z)e^{ikz}\,dz\right|\le \frac{100}{k}\sup_{z\in\Gamma}|f(z)|,
\]
where $\Gamma$ is the quarter-circle $z=Re^{i\theta}$, $0\le\theta\le\pi/2$.
:::
