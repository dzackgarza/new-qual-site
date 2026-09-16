---
schema: qual/card@1
id: P-UCLARA18S-04
kind: problem
title: Strong maximal function and differentiation along parabolic rectangles
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 4.

(a) Fix $1<p<\infty$. Show that
\[
f\mapsto [Mf](x,y)
=\sup_{r>0,\rho>0}\frac1{4r\rho}
\int_{-r}^{r}\int_{-\rho}^{\rho} f(x+h,y+\ell)\,dh\,d\ell
\]
is bounded on $L^p(\mathbb R^2)$.

(b) Show that
\[
[A_rf](x,y)=\frac1{4r^3}
\int_{-r}^{r}\int_{-r^2}^{r^2}f(x+h,y+\ell)\,dh\,d\ell
\]
converges to $f$ almost everywhere in the plane as $r\to0$.
:::
