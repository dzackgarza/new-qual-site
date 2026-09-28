---
schema: qual/card@1
id: P-UCLAB18F-05
kind: problem
title: Lipschitz extension from the boundary of the unit ball
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $B=\{x\in\mathbb R^n:|x|\le1\}$ and let $g:\partial B\to\mathbb R$ be $1$-Lipschitz.

(a) Show that
\[
f(x)=\inf_{y\in\partial B}\bigl(g(y)+|x-y|\bigr)
\]
is $1$-Lipschitz on $B$.

(b) Let $M(g)$ be the set of all $1$-Lipschitz $h:B\to\mathbb R$ satisfying $h|_{\partial B}=g$.
Show that $M(g)$ is compact in $C(B)$ with the supremum norm.
:::
