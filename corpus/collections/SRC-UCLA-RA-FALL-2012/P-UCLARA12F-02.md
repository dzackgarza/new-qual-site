---
schema: qual/card@1
id: P-UCLARA12F-02
kind: problem
title: Vanishing Fourier moments against L1 densities
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
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Suppose $\mu$ is a Borel probability measure on the unit circle such that
\[
\lim_{n\to\infty}\int_{|z|=1} z^n\,d\mu(z)=0.
\]
For $f\in L^1(\mu)$, show that
\[
\lim_{n\to\infty}\int_{|z|=1} z^n f(z)\,d\mu(z)=0.
\]
:::
