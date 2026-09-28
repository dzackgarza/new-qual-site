---
schema: qual/card@1
id: P-UCLAB16S-05
kind: problem
title: Lagrange multiplier condition for a constrained global minimum
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $f,g:\mathbb R^2\to\mathbb R$ be continuously differentiable.
Assume that $g$ attains the value $0$ at at least one point and that $\nabla g\ne0$ everywhere on $\mathbb R^2$.
Suppose $(x_0,y_0)$ satisfies
\[
f(x_0,y_0)=\inf\{f(x,y):x,y\in\mathbb R,\ g(x,y)=0\}.
\]
Show that there is $\lambda\in\mathbb R$ such that
\[
\nabla f(x_0,y_0)=\lambda\nabla g(x_0,y_0).
\]
:::
