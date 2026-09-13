---
schema: qual/card@1
id: P-UCLARA16F-07
kind: problem
title: UCLA analysis Fall 2016, Problem 7
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $H$ be the space of holomorphic functions $f$ on the unit disk $D=\{z\in\mathbb C:|z|<1\}$ such that
\[
\int_D |f(z)|^2\,dA(z)<\infty.
\]
Here integration is with respect to Lebesgue measure $A$ on $D$.
The vector space $H$ is a Hilbert space if equipped with the inner product
\[
\langle f,g\rangle=\int_D f(z)\overline{g(z)}\,dA(z)
\]
for $f,g\in H$.
Fix $z_0\in D$ and define $L_{z_0}(f)=f(z_0)$ for $f\in H$.

(a) Show that $L_{z_0}:H\to\mathbb C$ is a bounded linear functional on $H$.

(b) Find an explicit function $g_{z_0}\in H$ such that
\[
L_{z_0}(f)=f(z_0)=\langle f,g_{z_0}\rangle
\]
for all $f\in H$.
:::
