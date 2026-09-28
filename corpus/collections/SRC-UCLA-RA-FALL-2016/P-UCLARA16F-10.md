---
schema: qual/card@1
id: P-UCLARA16F-10
kind: problem
title: Filled Julia set of $z^2-1$
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
Consider the quadratic polynomial $f(z)=z^2-1$ on $\mathbb C$.
We are interested in the iterates $f^n$ of $f$, defined by $f^0=\operatorname{id}_{\mathbb C}$ and
\[
f^n=\underbrace{f\circ\cdots\circ f}_{n\text{ factors}}
\]
for $n\in\mathbb N$.

(a) Find an explicit constant $M>0$ such that for each $z\in\mathbb C$ either (i) $|f^n(z)|\to\infty$ as $n\to\infty$, or (ii) $|f^n(z)|\le M$ for all $n\in\mathbb N_0$.

(b) Let $U$ be the set of all $z\in\mathbb C$ for which (i) holds and $K$ the set of all $z\in\mathbb C$ for which (ii) holds.
Show that $U$ is open and $K$ is compact without “holes”, i.e. $\mathbb C\setminus K$ has no bounded connected components.
:::
