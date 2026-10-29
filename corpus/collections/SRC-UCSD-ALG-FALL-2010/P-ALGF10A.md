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
$$
H=\langle r_1,\ldots,r_m\rangle\subseteq (\QQ,+)
$$
be finitely generated.

::: pf

::: {.pf-step #common-denominator}
There is a positive integer $D$ such that
$$
H\subseteq \frac1D\ZZ.
$$

::: pf-proof
Write
$$
r_i=\frac{a_i}{b_i}
\qquad
(a_i\in\ZZ,\ b_i\in\ZZ_{>0}).
$$
Let
$$
D:=\operatorname{lcm}(b_1,\ldots,b_m).
$$
Then for each $i$ there is an integer $c_i$ such that
$$
r_i=\frac{c_i}{D}.
$$
Every element of $H$ is an integral linear combination of the $r_i$, hence belongs to $D^{-1}\ZZ$.
:::

:::

::: {.pf-step #subgroups-of-d-inverse-z-cyclic}
Every subgroup of $D^{-1}\ZZ$ is cyclic.

::: pf-proof
The map
$$
D^{-1}\ZZ\longrightarrow\ZZ,
\qquad
\frac{k}{D}\longmapsto k
$$
is an isomorphism of additive groups.
Thus a subgroup of $D^{-1}\ZZ$ corresponds to a subgroup of $\ZZ$.
Every subgroup of $\ZZ$ has the form
$$
d\ZZ
$$
for some integer $d\ge0$: if the subgroup is nonzero, take its least positive element $d$ and use Euclidean division to show every element is divisible by $d$.
Therefore every subgroup of $D^{-1}\ZZ$ is cyclic.
:::

:::

::: pf-step
Hence $H$ is cyclic.

::: pf-proof
By step [](#common-denominator){.pf-ref}, $H$ is a subgroup of $D^{-1}\ZZ$, and by step [](#subgroups-of-d-inverse-z-cyclic){.pf-ref} every such subgroup is cyclic.
:::

:::

:::
:::
