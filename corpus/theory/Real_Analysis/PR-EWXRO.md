---
schema: qual/card@1
id: PR-EWXRO
kind: proposition
title: Closure of measurable functions under algebraic operations and limits
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
Let $(X,\mcm)$ be a measurable space [@Fol13, §2.1].

(a) If $f,g\colon X\to\RR$ are [[D-DHFN4|measurable]], then $f+g$, $fg$, $\max(f,g)$, and $\min(f,g)$ are measurable.

(b) If $f_n\colon X\to[-\infty,\infty]$ are measurable for $n\geq1$, then $\sup_n f_n$, $\inf_n f_n$, $\limsup_n f_n$, and $\liminf_n f_n$ are measurable; if $f(x)\coloneqq\lim_n f_n(x)$ exists for every $x\in X$, then $f$ is measurable.

(c) For $E\subseteq X$, the characteristic function $\chi_E$ is measurable if and only if $E\in\mcm$.
:::
