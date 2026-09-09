---
schema: qual/card@1
id: P-HFGO22
kind: problem
title: An algebraic extension need not be finite
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Is every algebraic field extension finite?
Prove the claim or give a counterexample.
:::

::: solution
No. The extension
\[
\overline{\mathbb Q}/\mathbb Q
\]
is algebraic but infinite.

<1>1. Every element of $\overline{\mathbb Q}$ is algebraic over $\mathbb Q$.
::: proof
This is the defining property of the algebraic closure: it is an algebraic
extension of the base field.
:::

<1>2. The degree $[\overline{\mathbb Q}:\mathbb Q]$ is infinite.
::: proof
For every positive integer $n$, the polynomial
\[
x^n-2
\]
is irreducible over $\mathbb Q$ by Eisenstein's criterion at $2$. Hence, if
$\alpha_n=\sqrt[n]{2}$, then
\[
[\mathbb Q(\alpha_n):\mathbb Q]=n.
\]
Each field $\mathbb Q(\alpha_n)$ lies inside $\overline{\mathbb Q}$. If the
degree of $\overline{\mathbb Q}/\mathbb Q$ were finite, every intermediate
extension would have degree bounded by that finite number, contradicting the
existence of these subextensions of arbitrarily large degree.
:::

Thus algebraic does not imply finite.
:::
