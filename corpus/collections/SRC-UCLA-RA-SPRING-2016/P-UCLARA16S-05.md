---
schema: qual/card@1
id: P-UCLARA16S-05
kind: problem
title: UCLA analysis Spring 2016, Problem 5
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
For $f\in C_0^\infty(\mathbb R^2)$ define $u(x,t)$ by
\[
u(x,t)=\int_{\mathbb R^2}e^{ix\cdot\xi}\frac{\sin(t|\xi|)}{|\xi|}f(\xi)\,d\xi,
\qquad x\in\mathbb R^2,\ t>0.
\]
Show that
\[
\lim_{t\to\infty}\lVert u(\cdot,t)\rVert_{L^2}=\infty
\]
for a set of $f$ that is dense in $L^2(\mathbb R^2)$.
:::
