---
schema: qual/card@1
id: P-UCLARA16F-06
kind: problem
title: Weakly convergent sequences in $\ell^1$ converge in norm
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
Consider the Banach space $\ell^1$ consisting of all sequences $u=\{x_i\}$ in $\mathbb R$ with
\[
\lVert u\rVert_1=\sum_{i=1}^{\infty}|x_i|<\infty,
\]
and the Banach space $\ell^\infty$ consisting of all sequences $v=\{y_i\}$ in $\mathbb R$ with
\[
\lVert v\rVert_\infty=\sup_{i\in\mathbb N}|y_i|<\infty.
\]
There is a well-defined dual pairing between $\ell^1$ and $\ell^\infty$ given by
\[
\langle u,v\rangle=\sum_{i=1}^{\infty}x_i y_i.
\]
With this dual pairing, $\ell^\infty=(\ell^1)^*$ is the dual space of $\ell^1$.

(a) Show that there exists no sequence $\{u_n\}$ in $\ell^1$ such that (i) $\lVert u_n\rVert_1\ge1$ for all $n\in\mathbb N$ and (ii) $\langle u_n,v\rangle\to0$ for each $v\in\ell^\infty$.

(b) Show that every weakly convergent sequence $\{u_n\}$ in $\ell^1$ converges in the norm topology of $\ell^1$.
:::
