---
schema: qual/card@1
id: P-UCLAB15S-04
kind: problem
title: Intermediate value property plus closed fibers implies continuity
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\mathbb R$ satisfy the intermediate value property: whenever $0\le a<b\le1$ and $y$ lies between $f(a)$ and $f(b)$, there exists $x\in(a,b)$ such that $f(x)=y$.
Assume that for every $y\in\mathbb R$, the preimage $f^{-1}(\{y\})$ is closed.
Prove that $f$ is continuous.
:::
