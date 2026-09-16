---
schema: qual/card@1
id: P-BKF08-8A
kind: problem
title: Growth of the second moment of a solution of the heat equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8A of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
---

::: {.problem}
Let $u(x,t)$ be an infinitely differentiable real function satisfying the diffusion equation
\[
u_t=u_{xx},\qquad -\infty<x<\infty,\ t>0.
\]
Assume $u$ and all its partial derivatives of all orders are rapidly decreasing in $x$: in every strip $0<t<a$ they are bounded by a constant times $x^{-n}$ for every $n>0$.
Also assume
\[
\int_{-\infty}^{\infty}u(x,1)\,dx=1.
\]
Show that for $t>0$,
\[
\frac d{dt}\int_{-\infty}^{\infty}x^2u(x,t)\,dx=2.
\]
:::
