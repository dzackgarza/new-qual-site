---
schema: qual/card@1
id: P-VMXFR
kind: problem
title: Two two-generator descriptions of $S_n$
classification:
  areas:
  - algebra
  topics:
  - Permutations
  - Group Presentations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the Hungerford I.6 exercise statement reproduced in the UGA algebra problem-set archive.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that $S_n \cong \left\langle (12), (123\cdots n)\right\rangle$ and also that $S_n \cong \left\langle (12), (23\cdots n)\right\rangle$
:::

::: solution
Let
\[
\sigma=(1\ 2\ \cdots\ n),\qquad \tau=(2\ 3\ \cdots\ n).
\]
In each case it is enough to show that the indicated permutations generate all
transpositions of a standard generating set for $S_n$.

<1>1. The permutations $(12)$ and $\sigma$ generate $S_n$.
::: proof
For $0\le k\le n-2$, conjugation gives
\[
\sigma^k(12)\sigma^{-k}=(k+1\ k+2).
\]
Thus $\langle(12),\sigma\rangle$ contains every adjacent transposition
\[
(12),(23),\ldots,(n-1\ n).
\]
Every permutation is a product of adjacent transpositions, so
\[
\langle(12),\sigma\rangle=S_n.
\]
:::

<1>2. The permutations $(12)$ and $\tau$ generate $S_n$.
::: proof
For $0\le k\le n-2$,
\[
\tau^k(12)\tau^{-k}=(1\ \tau^k(2)).
\]
As $k$ varies, $\tau^k(2)$ runs through $2,3,\ldots,n$. Hence
\[
\langle(12),\tau\rangle
\]
contains every transposition $(1j)$ with $2\le j\le n$.

These transpositions generate $S_n$, since for distinct $i,j>1$,
\[
(ij)=(1i)(1j)(1i).
\]
Therefore
\[
\langle(12),\tau\rangle=S_n.
\]
:::
:::
