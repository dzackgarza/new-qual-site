---
schema: qual/card@1
id: P-UCLARA17F-09
kind: problem
title: UCLA analysis Fall 2017, Problem 9
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 9. Consider a map $F:\mathbb C\times\mathbb C\to\mathbb C$ with the following properties:

1. For each fixed $z\in\mathbb C$, the map $w\mapsto F(z,w)$ is injective.
2. For each fixed $w\in\mathbb C$, the map $z\mapsto F(z,w)$ is holomorphic.
3. $F(0,w)=w$ for $w\in\mathbb C$.

Show that
\[
F(z,w)=a(z)w+b(z)
\]
for $z,w\in\mathbb C$, where $a$ and $b$ are entire functions with $a(0)=1$, $b(0)=0$, and $a(z)\ne0$ for $z\in\mathbb C$.

Hint: Consider
\[
\frac{F(z,w)-F(z,0)}{F(z,1)-F(z,0)}.
\]
:::
