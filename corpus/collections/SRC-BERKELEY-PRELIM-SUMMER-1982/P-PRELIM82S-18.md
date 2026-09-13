---
schema: qual/card@1
id: P-PRELIM82S-18
kind: problem
title: A quadratic integral functional attains its maximum on a unit Lipschitz ball
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $E$ be the set of continuous functions $u:[0,1]\to\mathbb R$ such that
\[
|u(x)-u(y)|\le |x-y|
\qquad(0\le x,y\le1),
\]
and $u(0)=0$.
Define
\[
\varphi(u)=\int_0^1\bigl(u(x)^2-u(x)\bigr)\,dx.
\]
Show that $\varphi$ attains its maximum value at some $u\in E$.
:::
