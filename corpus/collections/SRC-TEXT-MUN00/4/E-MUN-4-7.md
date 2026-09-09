---
schema: qual/card@1
id: E-MUN-4-7
kind: problem
title: Extending the laws of exponents to all integers
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $a \in \mathbb{R}$ and $a \neq 0$ . Define $a^0 = 1$, and for $n \in \mathbb{Z}_+$, $a^{-n} = 1 / a^n$ . Show that the laws of exponents hold for $a, b \neq 0$ and $n, m \in \mathbb{Z}$ .
:::

::: {.solution}
Let \(a,b\ne0\), with \(a^0=1\) and \(a^{-n}=1/a^n\) for \(n>0\).

We first extend
\[
a^ra^s=a^{r+s}
\]
to all integers \(r,s\). The positive-positive case is Exercise 6. If \(r,s>0\), then
\[
a^{-r}a^{-s}=\frac1{a^ra^s}=\frac1{a^{r+s}}=a^{-(r+s)}.
\]
For mixed signs, say \(r\ge0\) and \(s=-q<0\),
\[
a^ra^{-q}=\frac{a^r}{a^q}.
\]
If \(r\ge q\), Exercise 6 gives \(a^r=a^{r-q}a^q\), hence the quotient is \(a^{r-q}\). If \(r<q\), then \(a^q=a^ra^{q-r}\), hence the quotient is
\[
\frac1{a^{q-r}}=a^{r-q}.
\]
The other mixed case follows by commutativity. Thus the addition law holds for all integer exponents.

For the power law, if \(s>0\), repeated use of the addition law gives
\[
(a^r)^s=a^{rs}.
\]
For \(s=0\) both sides equal \(1\), and for \(s=-q<0\),
\[
(a^r)^s=\frac1{(a^r)^q}=\frac1{a^{rq}}=a^{-rq}=a^{rs}.
\]
Hence
\[
\boxed{(a^r)^s=a^{rs}}
\]
for all integers \(r,s\).

Finally, Exercise 6 gives \((ab)^m=a^mb^m\) for \(m>0\). For \(m=0\) both sides are \(1\), and for \(m=-q<0\),
\[
(ab)^{-q}=\frac1{(ab)^q}=\frac1{a^qb^q}=a^{-q}b^{-q}.
\]
Thus all three laws of exponents hold for nonzero bases and arbitrary integer exponents.
:::
