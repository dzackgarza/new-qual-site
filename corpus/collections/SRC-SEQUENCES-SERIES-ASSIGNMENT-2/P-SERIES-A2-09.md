---
schema: qual/card@1
id: P-SERIES-A2-09
kind: problem
title: Sequences and series Assignment 2, problem 9
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
(a) Let $\{a_n\}$ be a sequence of positive real numbers. Show that
\[
\liminf_{n\to\infty}\frac{a_{n+1}}{a_n}
\le \liminf_{n\to\infty}\sqrt[n]{a_n}
\le \limsup_{n\to\infty}\sqrt[n]{a_n}
\le \limsup_{n\to\infty}\frac{a_{n+1}}{a_n}.
\]
You may assume all four quantities are finite.

(b) Show that if $\sum a_n$ converges by the ratio test, then it also converges by the root test.

(c) Let
\[
a_n=\frac1{2^{n+(-1)^n}}.
\]
Compute $\limsup\sqrt[n]{|a_n|}$ and $\limsup|a_{n+1}/a_n|$. Show that the series converges by the root test. Does the ratio test decide convergence?

(d) Let $b_n=n^n/n!$. Show that
\[
\lim_{n\to\infty}\sqrt[n]{b_n}=e.
\]
:::
