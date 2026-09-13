---
schema: qual/card@1
id: P-UCLAB07S-06
kind: problem
title: Uniqueness for a Lipschitz integral equation
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Consider
\[
y(t)=y_0+\int_0^t f(s,y(s))\,ds,
\]
where $f$ is continuous on $[0,T]\times\mathbb R$ and Lipschitz in its second variable with constant $K$. Assume the Picard iterates
\[
y^n(t)=y_0+\int_0^t f(s,y^{n-1}(s))\,ds,
\qquad y^0(t)\equiv y_0,
\]
converge uniformly to a solution $y$. Show that if $Y$ is another solution satisfying $|Y(t)-y_0|\le C$ on $[0,T]$, then $Y(t)=y(t)$ for all $t\in[0,T]$.
:::
