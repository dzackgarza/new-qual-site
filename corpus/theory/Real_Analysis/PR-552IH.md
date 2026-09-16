---
schema: qual/card@1
id: PR-552IH
kind: proposition
title: Closure properties of Lebesgue measurable functions
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

::: {.proposition}
All functions below are [[D-DHFN4|Lebesgue measurable]] functions with values in $[-\infty,\infty]$ unless stated otherwise.

- For a [[D-MDJII|Lebesgue measurable]] set $E\subseteq\RR^d$, the characteristic function $\chi_E$ is measurable.

- If $f_n\colon\RR^d\to[-\infty,\infty]$ are measurable for $n\geq1$, then $\abs{f_n}$, $\sup_n f_n$, $\inf_n f_n$, $\limsup_n f_n$, and $\liminf_n f_n$ are measurable, and so is $\lim_n f_n$ wherever the sequence converges everywhere.

- If $f,g\colon\RR^d\to\RR$ are measurable and finite-valued, then $f+g$ and $f-g$ are measurable.

- If $f\colon\RR^{d_1}\to[-\infty,\infty]$ is measurable, then $F\colon\RR^{d_1}\times\RR^{d_2}\to[-\infty,\infty]$, $F(x,y)\coloneqq f(x)$, is measurable.

- If $f\colon\RR^d\to[-\infty,\infty]$ is measurable and $T\colon\RR^d\to\RR^d$ is an invertible linear map, then $f\circ T$ is measurable.

- If $f\colon\RR^d\to[-\infty,\infty]$ is measurable, then $(x,y)\mapsto f(x-y)$ is measurable on $\RR^d\times\RR^d$.
:::
