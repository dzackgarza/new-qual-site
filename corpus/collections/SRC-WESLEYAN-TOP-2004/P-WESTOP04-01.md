---
schema: qual/card@1
id: P-WESTOP04-01
kind: problem
title: Source-sensitive interval-image theorem from the August 2004 Wesleyan exam
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The retained extraction corrupted the source interval brackets as braces. Direct inspection of page 3 of assets/attachments/topology_2005-2003.pdf shows that the source reads f:[a,b]→R.
---

::: {.problem}
For $a<b$ and a continuous function
\[
f:[a,b]\to\mathbb R,
\]
prove that the image of $f$ is a closed bounded interval.
:::

::: pf

::: pf-step

The interval
$$
[a,b]
$$
is compact and connected.


::: pf-proof

By the Heine--Borel theorem, a closed bounded interval in
$$
\mathbb R
$$
is compact.

It is connected because every interval in
$$
\mathbb R
$$
is connected.

:::

:::

::: pf-step

The image
$$
f([a,b])
$$
is compact.


::: pf-proof

The function
$$
f
$$
is continuous by hypothesis.
The continuous image of a compact space is compact.
Applying this to step <1>1 gives compactness of
$$
f([a,b]).
$$

:::

:::

::: pf-step

Hence
$$
f([a,b])
$$
is closed and bounded in
$$
\mathbb R.
$$


::: pf-proof

By the Heine--Borel theorem, compact subsets of
$$
\mathbb R
$$
are exactly the closed bounded subsets.
Apply this to step <1>2.

:::

:::

::: pf-step

The image
$$
f([a,b])
$$
is connected.


::: pf-proof

The interval
$$
[a,b]
$$
is connected by step <1>1, and a continuous image of a connected space is connected.
Therefore
$$
f([a,b])
$$
is connected.

:::

:::

::: pf-step

Every connected subset of
$$
\mathbb R
$$
is an interval.


::: pf-proof

Let
$$
S\subseteq\mathbb R
$$
be connected, and suppose
$$
x<z<y
$$
with
$$
x,y\in S.
$$
If
$$
z\notin S,
$$
then
$$
S
=
\bigl(S\cap(-\infty,z)\bigr)
\cup
\bigl(S\cap(z,\infty)\bigr)
$$
is a union of two disjoint nonempty relatively open sets, contradicting connectedness.
Thus every point between two points of
$$
S
$$
also lies in
$$
S,
$$
which is exactly the interval property.

:::

:::

::: pf-step

Therefore
$$
f([a,b])
$$
is an interval.


::: pf-proof

Step <1>4 gives connectedness, and step <1>5 characterizes connected subsets of
$$
\mathbb R
$$
as intervals.

:::

:::

::: pf-step

Consequently,
$$
\boxed{
f([a,b])
\text{ is a closed bounded interval}.}
$$


::: pf-proof

Step <1>3 gives closedness and boundedness, while step <1>6 gives the interval property.

:::

:::

::: pf-qed

Step <1>7 is exactly the required conclusion.

:::

:::
