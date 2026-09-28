---
schema: qual/card@1
id: P-UCLARA13F-10
kind: problem
title: Fourier transforms and self-convolutions of L2 functions
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Fall 2013 section.
---

::: {.problem}
(a) Let $f\in L^2(\mathbb R)$ and define
\[
h(x)=\int_{\mathbb R}f(x-y)f(y)\,dy.
\]
Show that there exists $g\in L^1(\mathbb R)$ such that
\[
h(\xi)=\int_{\mathbb R}e^{-i\xi x}g(x)\,dx.
\]

(b) Conversely, show that if $g\in L^1(\mathbb R)$, then there exists $f\in L^2(\mathbb R)$ whose self-convolution
\[
h(x)=\int_{\mathbb R}f(x-y)f(y)\,dy
\]
is the Fourier transform of $g$.
:::
