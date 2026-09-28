---
schema: qual/card@1
id: P-UCLARA18S-02
kind: problem
title: Nonnegativity and closed sublevel sets of the second-difference form $Q(f,h)$
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 2. Given $f\in L^2(\mathbb R)$ and $h>0$, define
\[
Q(f,h)=\int_{\mathbb R}\frac{2f(x)-f(x+h)-f(x-h)}{h^2}\,\overline{f(x)}\,dx.
\]

(a) Show that
\[
Q(f,h)\ge0
\]
for all $f\in L^2(\mathbb R)$ and all $h>0$.

(b) Show that the set
\[
E=\left\{f\in L^2(\mathbb R):\limsup_{h\to0}Q(f,h)\le1\right\}
\]
is closed in $L^2(\mathbb R)$.
:::
