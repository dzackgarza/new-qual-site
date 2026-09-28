---
schema: qual/card@1
id: P-UCLARA18F-05
kind: problem
title: Pointwise limits of continuous functions converge locally uniformly on a dense set
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 5. Let $\{f_n\}$ be a sequence of continuous real-valued functions on $[0,1]$ and suppose $f_n(x)$ converges to another real-valued function $f(x)$ at every $x\in[0,1]$.

(a) Prove that for every $\varepsilon>0$ there is a dense subset $D_\varepsilon\subset[0,1]$ such that if $x\in D_\varepsilon$, then there are an open interval $I\ni x$ and a positive integer $N_x$ such that for all $n>N_x$,
\[
\sup_{y\in I}|f_n(y)-f(y)|\le\varepsilon.
\]

Hint: Consider the closed sets
\[
F_{N,\varepsilon}=\{y\in[0,1]:|f_n(y)-f_m(y)|\le\varepsilon\text{ for all }n,m>N\}.
\]

(b) Prove that $f$ cannot be the characteristic function $\chi_{\mathbb Q\cap[0,1]}$, where $\mathbb Q$ is the set of rational numbers.
:::
