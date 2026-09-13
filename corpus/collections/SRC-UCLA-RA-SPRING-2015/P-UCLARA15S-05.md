---
schema: qual/card@1
id: P-UCLARA15S-05
kind: problem
title: UCLA analysis Spring 2015, Problem 5
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $u\in L^2(\mathbb R)$ and set
\[
U(x,\xi)=\int_{\mathbb R}e^{-(x+i\xi-y)^2/2}u(y)\,dy,
\qquad x,\xi\in\mathbb R.
\]
Show that $U(x,\xi)$ is well defined on $\mathbb R^2$ and that there exists a constant $C>0$ such that for all $u\in L^2(\mathbb R)$,
\[
\iint_{\mathbb R^2}|U(x,\xi)|^2e^{-\xi^2}\,dx\,d\xi
=C\int_{\mathbb R}|u(y)|^2\,dy.
\]
Determine $C$ explicitly.
:::
