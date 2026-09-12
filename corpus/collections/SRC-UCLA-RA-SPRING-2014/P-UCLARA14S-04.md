---
schema: qual/card@1
id: P-UCLARA14S-04
kind: problem
title: Functionals on C[0,1] and L-infinity not represented by L1 densities
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2014 section.
---

::: {.problem}
Let $(a_n)\subset[0,1]$ and define, for $f\in C([0,1])$,
\[
\varphi(f)=\sum_{n=1}^{\infty}2^{-n}f(a_n).
\]

(a) Prove that there is no $g\in L^1([0,1])$ such that
\[
\varphi(f)=\int_0^1 f(x)g(x)\,dx
\]
for every $f\in C([0,1])$.

(b) Each $g\in L^1([0,1])$ defines a continuous functional $T_g$ on $L^\infty([0,1])$ by
\[
T_g(f)=\int_0^1 f(x)g(x)\,dx.
\]
Prove that there are continuous linear functionals on $L^\infty([0,1])$ that are not of this form.
:::
