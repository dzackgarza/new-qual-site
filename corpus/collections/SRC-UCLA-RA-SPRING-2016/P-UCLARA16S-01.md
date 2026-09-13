---
schema: qual/card@1
id: P-UCLARA16S-01
kind: problem
title: UCLA analysis Spring 2016, Problem 1
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
Let
\[
K_t(x)=(4\pi t)^{-3/2}e^{-|x|^2/(4t)},\qquad x\in\mathbb R^3,\ t>0,
\]
where $|x|$ is the Euclidean norm of $x\in\mathbb R^3$.

(a) Show that the linear map
\[
L^3(\mathbb R^3)\ni f\longmapsto t^{1/2}K_t*f\in L^\infty(\mathbb R^3)
\]
is bounded, uniformly in $t>0$. Here
\[
K_t*f(x)=\int_{\mathbb R^3}K_t(x-y)f(y)\,dy.
\]

(b) Prove that $t^{1/2}\lVert K_t*f\rVert_{L^\infty}\to0$ as $t\to0$, for $f\in L^3(\mathbb R^3)$.
:::
