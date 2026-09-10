---
schema: qual/card@1
id: E-K4SU4
kind: problem
title: $R_p$ is a local ring for $p\in\operatorname{Spec} R$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Local Rings
  - Prime Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Used the characterization of the unique maximal ideal as the set of nonunits.
---

::: {.exercise}
Show that if $\mathfrak p\in\operatorname{Spec}(R)$, then $R_\mathfrak p$ is local with unique maximal ideal $\mathfrak pR_\mathfrak p$.
:::

::: {.solution}
Let $S=R\setminus\mathfrak p$, so $R_\mathfrak p=S^{-1}R$.
The extension
\[
\mathfrak m=\mathfrak pR_\mathfrak p
\]
is a proper ideal.

We claim that every element outside $\mathfrak m$ is a unit. Let $r/s\in R_\mathfrak p$ with $r/s\notin\mathfrak m$. If $r\in\mathfrak p$, then $r/s\in\mathfrak m$, so necessarily $r\notin\mathfrak p$, hence $r\in S$. Therefore
\[
\frac{s}{r}\in R_\mathfrak p
\]
and
\[
\frac rs\frac sr=1.
\]
Thus every nonunit lies in $\mathfrak m$.

Any proper ideal contains no unit, so every proper ideal of $R_\mathfrak p$ is contained in $\mathfrak m$. Hence $\mathfrak m$ is the unique maximal ideal, and $R_\mathfrak p$ is local.
:::
