---
schema: qual/card@1
id: P-UCLAB14S-08
kind: problem
title: A smooth cutoff function on Euclidean space
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Problem 8.

(a) Let $f:\mathbb R\to\mathbb R$ be defined by
\[
f(x)=
\begin{cases}
0,&x\leq 0,\\
e^{-1/x},&x>0.
\end{cases}
\]
Prove that $f$ is infinitely differentiable.

(b) In Euclidean space $\mathbb R^n$, for $n\geq 1$, find a function $\varphi\in C^\infty(\mathbb R^n)$ such that $\varphi(x)\geq 0$ for all $x$, $\varphi(x)=0$ if $|x|>1$, and
\[
\int_{\mathbb R^n}\varphi(x)\,dx=1.
\]
:::
