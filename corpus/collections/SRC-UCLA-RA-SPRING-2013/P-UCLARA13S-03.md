---
schema: qual/card@1
id: P-UCLARA13S-03
kind: problem
title: Circular differentiation from Bourgain's maximal estimate
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
For continuous $f:\mathbb R^2\to\mathbb R$, define
\[
A_r f(x,y)=\frac1{2\pi}\int_{-\pi}^{\pi} f(x+r\cos\theta,y+r\sin\theta)\,d\theta,
\qquad
Mf(x,y)=\sup_{0<r<1} A_r f(x,y).
\]
By a theorem of Bourgain, there is an absolute constant $C$ such that
\[
\|Mf\|_{L^3(\mathbb R^2)}\le C\|f\|_{L^3(\mathbb R^2)}
\]
for all $f\in C_c(\mathbb R^2)$. Use this to show that if $K\subset\mathbb R^2$ is compact, then
\[
A_r\chi_K(x,y)\longrightarrow 1\qquad(r\to0)
\]
for almost every $(x,y)\in K$.
:::
