---
schema: qual/card@1
id: P-UCLAB14S-10
kind: problem
title: Arzelà–Ascoli from boundedness and equicontinuity
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 10. Let $F$ be a set of continuous real-valued functions on $[0,1]$.
Assume that

(i) $F$ is uniformly bounded: there is $M<\infty$ such that $|f(x)|\leq M$ for all $f\in F$ and all $x\in[0,1]$; and

(ii) $F$ is equicontinuous: for every $\varepsilon>0$ there is $\delta>0$ such that for all $f\in F$ and $x,y\in[0,1]$,
\[
|x-y|<\delta\implies |f(x)-f(y)|<\varepsilon.
\]

Prove that every sequence from $F$ has a subsequence that converges uniformly on $[0,1]$.
:::
