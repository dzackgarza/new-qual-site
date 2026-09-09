---
schema: qual/card@1
id: P-HCAO47
kind: problem
title: A base-ring element invertible in an integral extension is already invertible
classification:
  areas:
  - algebra
  topics:
  - Integral Extensions
  - Unit Groups
  - Rings
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Commutative Algebra oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $A\subseteq B$ be commutative rings, with $B$ integral over $A$.
If $x\in A$ is a unit in $B$, show that $x$ is a unit in $A$.
:::

::: solution
Let $y=x^{-1}\in B$. Since $B$ is integral over $A$, the element $y$ is
integral over $A$. Hence there is a monic relation
\[
y^n+a_{n-1}y^{n-1}+\cdots+a_1y+a_0=0,
\qquad a_i\in A.
\]
Multiplying by $x^{n-1}$ and using $xy=1$ gives
\[
y+a_{n-1}+a_{n-2}x+\cdots+a_1x^{n-2}+a_0x^{n-1}=0.
\]
Therefore
\[
y=-a_{n-1}-a_{n-2}x-\cdots-a_0x^{n-1}\in A.
\]
But $xy=1$, so $x$ has an inverse $y$ already in $A$. Thus $x\in A^\times$.
:::
