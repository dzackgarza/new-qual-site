---
schema: qual/card@1
id: P-UCLAB05S-LA4
kind: problem
title: Two-sided ideals of a full matrix algebra
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 4 of the official UCLA Basic Exam, May 2005 PDF; the source's displayed definition omits an explicit nonempty hypothesis.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The literal displayed definition admits the empty set; the solution records that defect and proves the intended nonempty statement.
---

::: {.problem}
Let $\mathcal A=M_n(\mathbb C)$.
The source calls a subset $\mathcal I\subseteq\mathcal A$ a two-sided ideal in $\mathcal A$ if

(i) for all $A,B\in\mathcal I$, one has $A+B\in\mathcal I$;

(ii) for all $A\in\mathcal I$ and $B\in\mathcal A$, both $AB$ and $BA$ belong to $\mathcal I$.

Show that the only two-sided ideals in $\mathcal A$ are $\{0\}$ and $\mathcal A$ itself.
:::

::: {.solution}
As literally defined in the source, the assertion has the additional vacuous example $\mathcal I=\varnothing$.
Thus a nonempty hypothesis is needed for the stated conclusion.

Assume $\mathcal I\ne\varnothing$.
If $\mathcal I$ contains only $0$, then $\mathcal I=\{0\}$.
Otherwise choose $A=(a_{ij})\in\mathcal I$ with some $a_{ij}\ne0$.
Let $E_{rs}$ denote the standard matrix units.
By two-sided closure,
\[
E_{pi}AE_{jq}=a_{ij}E_{pq}\in\mathcal I
\]
for every $p,q$.
Multiplying on either side by the scalar matrix $a_{ij}^{-1}I_n$ shows $E_{pq}\in\mathcal I$ for every $p,q$.
Closure under addition then gives every matrix in $M_n(\mathbb C)$, so $\mathcal I=\mathcal A$.
:::
