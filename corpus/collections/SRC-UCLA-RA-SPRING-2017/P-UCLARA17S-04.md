---
schema: qual/card@1
id: P-UCLARA17S-04
kind: problem
title: Binary digit functionals on measures have no weak-star convergent subsequence
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
For $n\ge1$, let $a_n:[0,1)\to\{0,1\}$ denote the $n$th digit in the binary expansion of $x$, so that
\[
x=\sum_{n\ge1}a_n(x)2^{-n}\qquad(x\in[0,1)).
\]
Remove ambiguity by requiring $\liminf a_n(x)=0$ for all $x\in[0,1)$. Let $M([0,1))$ denote the Banach space of finite complex Borel measures on $[0,1)$ and define linear functionals $L_n$ on $M([0,1))$ by
\[
L_n(\mu)=\int_0^1 a_n(x)\,d\mu(x).
\]
Show that no subsequence of $L_n$ converges in the weak-* topology on $M([0,1))^*$.
:::
