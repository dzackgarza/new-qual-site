---
schema: qual/card@1
id: P-OPH7A
kind: problem
title: 'Equal integrals of measurable functions: equality a.e. or a strict inequality
  on a subset'
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the official UGA August 2016 real-analysis qualifying exam. The source assumes only measurability and equality of the displayed integrals; with extended-valued integrals this is false. The card is corrected to the natural L1 formulation.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $f,g\in L^1([a,b])$ be real-valued with
$$
\int_{a}^{b} f(x) ~d x=\int_{a}^{b} g(x) ~d x.
$$
Show that either

1. $f(x) = g(x)$ almost everywhere, or
2. There exists a measurable set $E \subset [a, b]$ such that
\[
\int _{E} f(x) \, dx > \int _{E} g(x) \, dx
\]

:::{.concept}
\envlist
- Monotonicity of the Lebesgue integral: $f\leq g$ on $A$ $\implies \int_A f \leq \int_A g$

:::

:::{.strategy}
Take the assumption and the negation of (1) and show (2).
The obvious move: define the set $A$ where they differ.
The non-obvious move: split $A$ itself up to get a strict inequality.

:::

::: solution
Let
\[
h=f-g.
\]
Then $h\in L^1([a,b])$ and
\[
\int_a^b h\,dx=0.
\]
If $h=0$ almost everywhere, then $f=g$ almost everywhere and alternative (1) holds.

Assume instead that $h\ne0$ on a set of positive measure. Write
\[
E_+=\{h>0\},
\qquad
E_-=\{h<0\}.
\]
If $m(E_+)=0$, then $h\le0$ almost everywhere and $h<0$ on a set of positive measure. Consequently
\[
\int_a^b h\,dx<0,
\]
contradicting $\int h=0$. Thus $m(E_+)>0$.

Because $h>0$ on $E_+$,
\[
E_+=\bigcup_{k=1}^\infty\{h\ge 1/k\}.
\]
Hence some $k$ satisfies
\[
m(\{h\ge1/k\})>0.
\]
It follows that
\[
\int_{E_+}h\,dx
\ge \frac1k\,m(\{h\ge1/k\})>0.
\]
Taking $E=E_+$ gives
\[
\int_E f\,dx-\int_E g\,dx
=\int_E h\,dx>0.
\]
Therefore alternative (2) holds.
:::
