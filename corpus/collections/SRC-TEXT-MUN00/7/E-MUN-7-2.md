---
schema: qual/card@1
id: E-MUN-7-2
kind: problem
title: Bijections in the countability proofs for $\mathbb{Q}$
classification:
  areas:
  - topology
  topics:
  - Countable and Uncountable Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 7, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Show that the maps $f$ and $g$ of Examples 1 and 2 are bijections.
:::

::: {.solution}
For Example 1, the map \(f:\mathbb Z\to\mathbb Z_+\) is
\[
f(n)=
\begin{cases}
2n,&n>0,\\
-2n+1,&n\le0.
\end{cases}
\]
Positive integers go to the positive even integers, while nonpositive integers go to the positive odd integers. These two image sets are disjoint and together exhaust \(\mathbb Z_+\). Explicitly,
\[
f^{-1}(m)=
\begin{cases}
m/2,&m\text{ even},\\
(1-m)/2,&m\text{ odd}.
\end{cases}
\]
Thus \(f\) is bijective.

For Example 2, let
\[
A=\{(x,y)\in\mathbb Z_+^2:y\le x\}.
\]
The first map is
\[
F:\mathbb Z_+^2\to A,
\qquad
F(x,y)=(x+y-1,y).
\]
Since \(x\ge1\), the first coordinate is at least \(y\), so \(F\) maps into \(A\). Its inverse is
\[
F^{-1}(u,v)=(u-v+1,v),
\]
which is well-defined because \(u\ge v\). Hence \(F\) is bijective.

The second map is
\[
G:A\to\mathbb Z_+,
\qquad
G(x,y)=\frac{x(x-1)}2+y.
\]
For fixed \(x\), as \(y\) runs from \(1\) to \(x\), the values of \(G\) are precisely
\[
\frac{x(x-1)}2+1,\ldots,\frac{x(x+1)}2.
\]
These consecutive blocks are pairwise disjoint and concatenate to
\[
1,2,3,\ldots.
\]
Thus every positive integer occurs exactly once, so \(G\) is bijective.
:::
