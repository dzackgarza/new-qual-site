---
schema: qual/card@1
id: P-ALGF10A
kind: problem
title: "A finitely generated subgroup of the additive group of rationals is cyclic"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 1 of the official UCSD Algebra Qualifying Examination, Fall 2010; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the common-denominator reduction and the classification of subgroups of the infinite cyclic group.
---

::: {.problem}
Show that a finitely generated subgroup of the additive group of the rationals is cyclic.
:::


::: {.solution}
Let
\[
H=\langle r_1,\ldots,r_m\rangle\subseteq (\mathbb Q,+)
\]
be finitely generated.

<1>1. There is a positive integer \(D\) such that
\[
H\subseteq \frac1D\mathbb Z.
\]
::: {.proof}
Write
\[
r_i=\frac{a_i}{b_i}
\qquad
(a_i\in\mathbb Z,\ b_i\in\mathbb Z_{>0}).
\]
Let
\[
D:=\operatorname{lcm}(b_1,\ldots,b_m).
\]
Then for each \(i\) there is an integer \(c_i\) such that
\[
r_i=\frac{c_i}{D}.
\]
Every element of \(H\) is an integral linear combination of the \(r_i\), hence belongs to \(D^{-1}\mathbb Z\).
:::

<1>2. Every subgroup of \(D^{-1}\mathbb Z\) is cyclic.
::: {.proof}
The map
\[
D^{-1}\mathbb Z\longrightarrow\mathbb Z,
\qquad
\frac{k}{D}\longmapsto k
\]
is an isomorphism of additive groups.
Thus a subgroup of \(D^{-1}\mathbb Z\) corresponds to a subgroup of \(\mathbb Z\).
Every subgroup of \(\mathbb Z\) has the form
\[
d\mathbb Z
\]
for some integer \(d\ge0\): if the subgroup is nonzero, take its least positive element \(d\) and use Euclidean division to show every element is divisible by \(d\).
Therefore every subgroup of \(D^{-1}\mathbb Z\) is cyclic.
:::

<1>3. Hence \(H\) is cyclic.
::: {.proof}
By <1>1, \(H\) is a subgroup of \(D^{-1}\mathbb Z\), and by <1>2 every such subgroup is cyclic.
:::
:::
