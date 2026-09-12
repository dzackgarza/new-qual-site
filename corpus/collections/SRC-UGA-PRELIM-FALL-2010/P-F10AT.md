---
schema: qual/card@1
id: P-F10AT
kind: problem
title: $x-x^3/3 \le \arctan x \le x$ for $x\ge 0$
classification:
  areas:
  - prelim
  topics:
  - Inequalities
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Prove that $x - \frac{x^3}{3} \le \arctan x \le x$ for all $x \ge 0$.
:::

::: solution
For every $t\ge0$,
\[
1-t^2\le \frac1{1+t^2}\le1.
\]
The right inequality is immediate. For the left,
\[
\frac1{1+t^2}-(1-t^2)
=\frac{t^4}{1+t^2}\ge0.
\]
Integrating from $0$ to $x\ge0$ yields
\[
\int_0^x(1-t^2)\,dt
\le\int_0^x\frac{dt}{1+t^2}
\le\int_0^x1\,dt.
\]
Since the middle integral is $\arctan x$, this becomes
\[
\boxed{x-\frac{x^3}{3}\le\arctan x\le x}.
\]
:::
