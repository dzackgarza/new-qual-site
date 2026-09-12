---
schema: qual/card@1
id: E-IXKVS
kind: problem
title: Root location from small lower coefficients
classification:
  areas:
  - topology
  topics:
  - Fundamental Theorem of Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Given a polynomial equation

$$
x^n + a_{n-1}x^{n-1} + \dots + a_1 x + a_0 = 0
$$

with real or complex coefficients.
Show that if $\abs{a_{n-1}} + \cdots + \abs{a_1} + \abs{a_0} < 1$, then all the roots of the equation lie interior to the unit ball $B^2$.
[Hint: Let $g(x) = 1 + a_{n-1}x + \cdots + a_1 x^{n-1} + a_0 x^n$, and show that $g(x) \neq 0$ for $x \in B^2$.]
:::

::: {.solution}
Let
\[
p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0
\]
and assume
\[
|a_{n-1}|+\cdots+|a_0|<1.
\]
Suppose \(p(z)=0\) and \(|z|\ge1\). Since \(z\ne0\), divide by \(z^n\):
\[
1=-\left(\frac{a_{n-1}}z+\frac{a_{n-2}}{z^2}+\cdots+\frac{a_0}{z^n}\right).
\]
Taking absolute values and using \(|z|\ge1\),
\[
1\le \frac{|a_{n-1}|}{|z|}+\frac{|a_{n-2}|}{|z|^2}+\cdots+\frac{|a_0|}{|z|^n}
\le |a_{n-1}|+\cdots+|a_0|<1,
\]
a contradiction. Hence every root satisfies \(|z|<1\), so all roots lie in the interior of the unit disk.

Equivalently, with \(w=1/z\), the polynomial from the hint
\[
g(w)=1+a_{n-1}w+\cdots+a_0w^n
\]
has no zero with \(|w|\le1\), since the nonconstant part has absolute value strictly less than \(1\).
:::
