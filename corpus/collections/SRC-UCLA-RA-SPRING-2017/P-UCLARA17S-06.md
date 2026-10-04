---
schema: qual/card@1
id: P-UCLARA17S-06
kind: problem
title: Swiss cheese sets have positive area
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
Let
\[
\mathbb D=\{z\in\mathbb C:|z|<1\}
\]
be the open unit disk and let $\overline{\mathbb D}$ be the closed unit disk. Let $\{p_n\}$ be distinct points in $\mathbb D$, and let $r_n>0$ be such that the disks
\[
D_n=\{z:|z-p_n|\le r_n\}
\]
satisfy (i) $D_n\subset\mathbb D$; (ii) $D_n\cap D_m=\varnothing$ if $n\ne m$; and (iii) $\sum_n r_n<\infty$. Prove that
\[
X=\overline{\mathbb D}\setminus\bigcup_n D_n
\]
has positive area.

Hint: for $-1<x<1$ consider $\#\{n:D_n\cap\{\operatorname{Re}z=x\}\ne\varnothing\}$.
:::
