---
schema: qual/card@1
id: P-UCLARA17F-06
kind: problem
title: $L^2$ boundedness of the truncated Riesz potential $\int_{|w-z|\le1}\frac{|f(w)|}{|w-z|}\,dA(w)$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let $f\in L^2(\mathbb C)$. For $z\in\mathbb C$ define
\[
g(z)=\int_{\{w\in\mathbb C:|w-z|\le1\}}\frac{|f(w)|}{|w-z|}\,dA(w),
\]
where $dA$ denotes integration with respect to Lebesgue measure on $\mathbb C\cong\mathbb R^2$. Show that $|g(z)|<\infty$ for almost every $z\in\mathbb C$ and that $g\in L^2(\mathbb C)$.
:::
