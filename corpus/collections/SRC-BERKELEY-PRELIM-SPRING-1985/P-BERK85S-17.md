---
schema: qual/card@1
id: P-BERK85S-17
kind: problem
title: Comparison theorem for scalar autonomous differential equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Let $v_1,v_2:\mathbb R\to\mathbb R$ be continuous and satisfy
\[
v_1(x)<v_2(x)
\]
for every $x$. Let $\varphi_1,\varphi_2$ solve
\[
x'=v_1(x)
\qquad\text{and}\qquad
x'=v_2(x),
\]
respectively, on an interval $(a,b)$. If
\[
\varphi_1(t_0)=\varphi_2(t_0)
\]
for some $t_0\in(a,b)$, prove that
\[
\varphi_1(t)\le\varphi_2(t)
\]
for every $t\in(t_0,b)$.
:::
