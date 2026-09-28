---
schema: qual/card@1
id: FD-JTWOB
kind: definition
title: Invariant factors of a module over a PID
prompts:
- What divisibility condition do the invariant factors satisfy?
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Canonical Forms
relations: []
review: draft
---

::: {.definition}
Let $R$ be a [[D-HTIL5|principal ideal domain]] and $M$ a finitely generated $R$-module.
By the [[PR-UVUS6|structure theorem]], there are an integer $r\geq 0$ and nonzero nonunits $r_1,\ldots,r_m\in R$ with
$$
M\cong R^r\oplus\bigoplus_{i=1}^m R/(r_i)
\qquad\text{and}\qquad
r_1 \divides r_2 \divides \cdots \divides r_m,
$$
and $r_1,\ldots,r_m$ are unique up to units.
The elements $r_1,\ldots,r_m$ are the \dfn{invariant factors} of $M$.
:::
