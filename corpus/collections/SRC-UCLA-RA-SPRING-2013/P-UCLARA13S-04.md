---
schema: qual/card@1
id: P-UCLARA13S-04
kind: problem
title: Existence of an equilibrium measure for Newtonian energy
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $K\subset\mathbb R^3$ be nonempty and compact.
For every Borel probability measure $\mu$ on $K$, define
\[
I(\mu)=\int_K\int_K \frac{1}{|x-y|}\,d\mu(x)\,d\mu(y)\in(0,\infty],
\]
and let
\[
R_K=\inf\{I(\mu):\mu\text{ is a Borel probability measure on }K\}.
\]
Show that there exists a Borel probability measure $\mu$ on $K$ such that $I(\mu)=R_K$.
:::
