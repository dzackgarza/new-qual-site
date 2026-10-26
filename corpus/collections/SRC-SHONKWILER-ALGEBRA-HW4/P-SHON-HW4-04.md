---
schema: qual/card@1
id: P-SHON-HW4-04
kind: problem
title: Two generators for the symmetric group
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against exercise 3.5.4 in the retained Algebra HW 4 solution packet.
---

::: {.problem}
Show that
\[
S_n=\langle (12),(12\cdots n)\rangle
\]
for every $n\ge2$.
:::

Let
\[
\tau=(12\cdots n)
\]
and
\[
\sigma=(12).
\]
Set
\[
G=\langle \sigma,\tau\rangle.
\]

::: pf

::: pf-step

For each
\[
1\le i\le n-1,
\]
one has
\[
\boxed{
\tau^{i-1}\sigma\tau^{-(i-1)}
=
(i\,\,i+1)}.
\]


::: pf-proof

Conjugation sends a transposition \((a\,b)\) to
\[
(\tau^{i-1}(a)\,\,\tau^{i-1}(b)).
\]
Since
\[
\tau^{i-1}(1)=i
\]
and
\[
\tau^{i-1}(2)=i+1
\]
for \(1\le i\le n-1\), the formula follows.

:::

:::

::: pf-step

Therefore every adjacent transposition
\[
\boxed{
(12),(23),\dots,(n-1\,\,n)}
\]
belongs to \(G\).


::: pf-proof

Each one is one of the conjugates from step <1>1.

:::

:::

::: pf-step

Every transposition \((i\,j)\) with \(i<j\) can be written as a product of adjacent transpositions:
\[
\boxed{
(i\,j)
=
(j-1\,\,j)\cdots(i+1\,\,i+2)(i\,\,i+1)
(i+1\,\,i+2)\cdots(j-1\,\,j)}.
\]


::: pf-proof

The right-hand side moves \(i\) successively to \(j\), then moves the intermediate entries back, fixing all points except \(i\) and \(j\). Hence it is exactly the transposition \((i\,j)\).

:::

:::

::: pf-step

Thus every transposition in \(S_n\) belongs to \(G\).


::: pf-proof

Step <1>2 puts all adjacent transpositions in \(G\), and step <1>3 expresses any transposition as their product.

:::

:::

::: pf-step

The transpositions generate \(S_n\).


::: pf-proof

Every permutation decomposes into disjoint cycles, and every cycle
\[
(a_1a_2\cdots a_m)
\]
can be written as
\[
(a_1a_m)(a_1a_{m-1})\cdots(a_1a_2).
\]
Hence every permutation is a product of transpositions.

:::

:::

::: pf-step

Therefore
\[
S_n\subseteq G.
\]


::: pf-proof

By steps <1>4--<1>5, every element of \(S_n\) is a product of elements already in \(G\).

:::

:::

::: pf-step

Since by definition
\[
G\le S_n,
\]
one obtains
\[
\boxed{
S_n=\langle(12),(12\cdots n)\rangle}.
\]


::: pf-proof

Combine the two inclusions.

:::

:::

::: pf-qed

Step <1>7 is the required generation statement.

:::

:::
