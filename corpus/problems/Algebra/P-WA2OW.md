---
schema: qual/card@1
id: P-WA2OW
kind: problem
title: The group algebra over $\CC$ versus other fields, and when the characteristic
  divides $|G|$
classification:
  areas:
  - algebra
  topics:
  - Group Rings
  - Representation Theory
  - Characteristic
relations: []
review: draft
---

::: {.problem}
For a finite group $G$ and a field $k$, describe the group algebra $k[G]$. What is special about $k=\CC$, and what changes when $\operatorname{char}k$ divides $|G|$?
:::

::: {.solution}
The group algebra $k[G]$ is the $k$-vector space with basis $G$ and multiplication obtained by extending the group law $k$-bilinearly:
\[
\left(\sum_g a_g g\right)\left(\sum_h b_h h\right)
=\sum_{g,h}a_gb_h(gh).
\]
A representation of $G$ on a $k$-vector space is equivalently a left $k[G]$-module.

Nothing in the definition requires $k=\CC$. The special feature of characteristic not dividing $|G|$ is Maschke's theorem:
\[
\operatorname{char}k\nmid |G|
\quad\Longrightarrow\quad
k[G]\text{ is semisimple}.
\]
Equivalently, every finite-dimensional $k$-representation is completely reducible. The proof averages a projection over $G$ and divides by $|G|$.

Over $\CC$ one also has a splitting field for every finite group: every irreducible complex representation is absolutely irreducible, and
\[
\CC[G]\cong\prod_i M_{n_i}(\CC)
\]
by Artin--Wedderburn.

If $\operatorname{char}k=p$ divides $|G|$, the averaging argument cannot divide by $|G|$, and Maschke's theorem fails: $k[G]$ is not semisimple. For example, if $C_p=\langle g\rangle$, then in characteristic $p$,
\[
(g-1)^p=g^p-1=0,
\]
so $k[C_p]$ contains the nonzero nilpotent element $g-1$ and is not semisimple.
:::
