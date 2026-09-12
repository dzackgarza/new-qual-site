---
schema: qual/card@1
id: P-HFGO20
kind: problem
title: When separable degree equals extension degree
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
For a finite field extension, when does its separable degree equal its degree?
:::

::: solution
Let $E/F$ be finite. Its separable degree equals its total degree exactly when
$E/F$ is separable.

<1>1. If $E/F$ is separable, then
\[
[E:F]_{\mathrm{sep}}=[E:F].
\]
::: proof
By definition, the separable degree is the number of $F$-embeddings of $E$ into
an algebraic closure of $F$. A finite separable extension has exactly
$[E:F]$ such embeddings.
:::

<1>2. Conversely, if
\[
[E:F]_{\mathrm{sep}}=[E:F],
\]
then $E/F$ is separable.
::: proof
For every finite extension,
\[
[E:F]=[E:F]_{\mathrm{sep}}\,[E:F]_{\mathrm{insep}},
\]
where the inseparable degree is a positive power of the characteristic exponent.
Equality of the separable and total degrees forces
\[
[E:F]_{\mathrm{insep}}=1,
\]
which is equivalent to separability.
:::

Thus the equality holds if and only if every element of $E$ is separable over
$F$.
:::
