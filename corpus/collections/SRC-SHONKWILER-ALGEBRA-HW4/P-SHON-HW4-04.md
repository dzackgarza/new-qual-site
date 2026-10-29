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
$$
S_n=\langle (12),(12\cdots n)\rangle
$$
for every $n\ge2$.
:::

::: {.solution}

Let
$$
\tau=(12\cdots n)
$$
and
$$
\sigma=(12).
$$
Set
$$
G=\langle \sigma,\tau\rangle.
$$

::: pf

::: {.pf-step #s1-1}

For each
$$
1\le i\le n-1,
$$
one has
$$
\boxed{
\tau^{i-1}\sigma\tau^{-(i-1)}
=
(i\,\,i+1)}.
$$


::: pf-proof

Conjugation sends a transposition $(a\,b)$ to
$$
(\tau^{i-1}(a)\,\,\tau^{i-1}(b)).
$$
Since
$$
\tau^{i-1}(1)=i
$$
and
$$
\tau^{i-1}(2)=i+1
$$
for $1\le i\le n-1$, the formula follows.

:::

:::

::: {.pf-step #s1-2}

Therefore every adjacent transposition
$$
\boxed{
(12),(23),\dots,(n-1\,\,n)}
$$
belongs to $G$.


::: pf-proof

Each one is one of the conjugates from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Every transposition $(i\,j)$ with $i<j$ can be written as a product of adjacent transpositions:
$$
\boxed{
(i\,j)
=
(j-1\,\,j)\cdots(i+1\,\,i+2)(i\,\,i+1)
(i+1\,\,i+2)\cdots(j-1\,\,j)}.
$$


::: pf-proof

The right-hand side moves $i$ successively to $j$, then moves the intermediate entries back, fixing all points except $i$ and $j$. Hence it is exactly the transposition $(i\,j)$.

:::

:::

::: {.pf-step #s1-4}

Thus every transposition in $S_n$ belongs to $G$.


::: pf-proof

Step [](#s1-2){.pf-ref} puts all adjacent transpositions in $G$, and step [](#s1-3){.pf-ref} expresses any transposition as their product.

:::

:::

::: {.pf-step #s1-5}

The transpositions generate $S_n$.


::: pf-proof

Every permutation decomposes into disjoint cycles, and every cycle
$$
(a_1a_2\cdots a_m)
$$
can be written as
$$
(a_1a_m)(a_1a_{m-1})\cdots(a_1a_2).
$$
Hence every permutation is a product of transpositions.

:::

:::

::: pf-step

Therefore
$$
S_n\subseteq G.
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}, every element of $S_n$ is a product of elements already in $G$.

:::

:::

::: {.pf-step #s1-7}

Since by definition
$$
G\le S_n,
$$
one obtains
$$
\boxed{
S_n=\langle(12),(12\cdots n)\rangle}.
$$


::: pf-proof

Combine the two inclusions.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required generation statement.

:::

:::

:::
