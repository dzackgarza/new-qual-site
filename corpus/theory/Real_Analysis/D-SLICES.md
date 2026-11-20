---
schema: qual/card@1
id: D-SLICES
kind: definition
title: Slices of a function and of a set
prompts:
- What is a slice of a function on a product?
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Fubini-Tonelli
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be sets, let $f\colon X\times Y\to Z$, and let $E\subseteq X\times Y$.
For $x\in X$ and $y\in Y$, the \dfn{slices} of $f$ are
$$
f^y\colon X\to Z,\quad f^y(x)\coloneqq f(x,y),
\qquad
f_x\colon Y\to Z,\quad f_x(y)\coloneqq f(x,y),
$$
and the slices of $E$ are
$$
E^y\coloneqq\theset{x\in X\st (x,y)\in E},
\qquad
E_x\coloneqq\theset{y\in Y\st (x,y)\in E}.
$$
:::

::: {.remark}
The measurable-slice theorem for these slices is [[PR-6NDTF]].
:::
