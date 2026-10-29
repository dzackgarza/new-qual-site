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
f:[a,b]\to\RR,
\]
prove that the image of $f$ is a closed bounded interval.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The interval
$$
[a,b]
$$
is compact and connected.


::: pf-proof

By the Heine--Borel theorem, a closed bounded interval in
$$
\RR
$$
is compact.

It is connected because every interval in
$$
\RR
$$
is connected.

:::

:::

::: {.pf-step #s1-2}

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
Applying this to step [](#s1-1){.pf-ref} gives compactness of
$$
f([a,b]).
$$

:::

:::

::: {.pf-step #s1-3}

Hence
$$
f([a,b])
$$
is closed and bounded in
$$
\RR.
$$


::: pf-proof

By the Heine--Borel theorem, compact subsets of
$$
\RR
$$
are exactly the closed bounded subsets.
Apply this to step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

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
is connected by step [](#s1-1){.pf-ref}, and a continuous image of a connected space is connected.
Therefore
$$
f([a,b])
$$
is connected.

:::

:::

::: {.pf-step #s1-5}

Every connected subset of
$$
\RR
$$
is an interval.


::: pf-proof

Let
$$
S\subseteq\RR
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

::: {.pf-step #s1-6}

Therefore
$$
f([a,b])
$$
is an interval.


::: pf-proof

Step [](#s1-4){.pf-ref} gives connectedness, and step [](#s1-5){.pf-ref} characterizes connected subsets of
$$
\RR
$$
as intervals.

:::

:::

::: {.pf-step #s1-7}

Consequently,
$$
\boxed{
f([a,b])
\text{ is a closed bounded interval}.}
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives closedness and boundedness, while step [](#s1-6){.pf-ref} gives the interval property.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is exactly the required conclusion.

:::

:::

:::
