---
schema: qual/card@1
id: P-UCLARA12F-06
kind: problem
title: A maximal-function route to differentiation
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
Let $f\in L^1(\mathbb R)$ and let $Mf$ denote its maximal function,
\[
(Mf)(x)=\sup_{0<r<\infty}\frac1{2r}\int_{-r}^{r}|f(x-y)|\,dy.
\]
By the Hardy--Littlewood maximal function theorem,
\[
|\{x\in\mathbb R:(Mf)(x)>\lambda\}|\le 3\lambda^{-1}\|f\|_{L^1}
\qquad(\lambda>0).
\]
Using this, show that
\[
\limsup_{r\to0}\frac1{2r}\int_{-r}^{r}|f(y)-f(x)|\,dy=0
\]
for almost every $x\in\mathbb R$.
:::
