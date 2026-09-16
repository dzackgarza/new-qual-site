---
schema: qual/card@1
id: PR-UVUS6
kind: proposition
title: Structure theorem for finitely generated modules over a PID
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Modules
  - Principal Ideal Domains
relations: []
review: draft
---

::: {.proposition}
Let $R$ be a [[D-HTIL5|principal ideal domain]] and $M$ a finitely generated $R$-module.
Then there are an integer $r\geq0$, nonzero nonunits $r_1 \divides r_2 \divides \cdots\divides r_m$ of $R$, and primes $p_1,\ldots,p_s$ of $R$, not necessarily distinct, with exponents $e_i\geq1$, such that
$$
M \cong R^r\oplus \bigoplus_{i=1}^m R/(r_i)
\qquad\text{and}\qquad
M \cong R^r\oplus \bigoplus_{i=1}^s R/(p_i^{e_i}).
$$
The first is the invariant factor decomposition and the second the elementary divisor decomposition.
The rank $r$ is unique, the $r_i$ are unique up to units, and the $p_i^{e_i}$ are unique up to units and reordering.
:::
