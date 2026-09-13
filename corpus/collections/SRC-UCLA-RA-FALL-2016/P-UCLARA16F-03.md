---
schema: qual/card@1
id: P-UCLARA16F-03
kind: problem
title: UCLA analysis Fall 2016, Problem 3
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
If $X$ is a compact metric space, denote by $P(X)$ the set of positive Borel measures $\mu$ on $X$ with $\mu(X)=1$.

(a) Let $\phi:X\to[0,\infty]$ be a lower-semicontinuous function on a compact metric space $X$.
Show that if $\mu$ and $\mu_n$, for $n\in\mathbb N$, are in $P(X)$ and $\mu_n\to\mu$ with respect to the weak-star topology on $P(X)$, then
\[
\int \phi\,d\mu\le \liminf_{n\to\infty}\int \phi\,d\mu_n.
\]

(b) Let $K\subset\mathbb R^d$ be compact.
For $\mu\in P(K)$ define
\[
E(\mu)=\int_K\int_K\frac{1}{|x-y|}\,d\mu(x)\,d\mu(y).
\]
Here $|z|$ denotes the Euclidean norm of $z\in\mathbb R^d$.
Show that $E:P(K)\to[0,\infty]$ attains its minimum on $P(K)$ (which could possibly be $\infty$).
:::
