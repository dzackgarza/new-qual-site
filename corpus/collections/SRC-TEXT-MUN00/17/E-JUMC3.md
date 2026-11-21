---
schema: qual/card@1
id: E-JUMC3
kind: problem
title: Differences of open and closed sets
classification:
  areas:
  - topology
  topics:
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 4, printed p. 100; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.4, PDF p. 6. The two identities X - (U - A) =
    (X - U) cup A and X - (A - U) = (X - A) cup U give the two conclusions as a union of two
    closed sets and a union of two open sets. (tmp/sources/munkres-solutions-positron-
    ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08: the two complement identities, then the openness of $U-A$ and the closedness of $A-U$. The identities are pointwise and each complement of a union of two closed, respectively two open, sets was re-checked against the definitions on printed p. 95. No statement change.
---

::: {.exercise}

Show that if $U$ is open in $X$ and $A$ is closed in $X$, then $U - A$ is open in $X$, and $A - U$ is closed in $X$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.4** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two complements are theirs. Whitman proves the same two statements on his printed p. 160 by way of a set identity and its corollary.

Throughout, $A$ and $U$ are subsets of $X$ with $U$ open and $A$ closed.

::: pf

::: {.pf-step #complements}

$X-(U-A)=(X-U)\cup A$ and $X-(A-U)=(X-A)\cup U$.

::: pf-proof

A point $x\in X$ lies in $U-A$ exactly when $x\in U$ and $x\notin A$, so it lies in $X-(U-A)$ exactly when $x\notin U$ or $x\in A$, which is the first identity; the second is the same computation with the roles of $U$ and $A$ exchanged.

:::

:::

::: pf-step

$U-A$ is open in $X$.

::: pf-proof

By step [](#complements){.pf-ref}, $X-(U-A)=(X-U)\cup A$. The set $X-U$ is closed because $U$ is open, and $A$ is closed by hypothesis, so $(X-U)\cup A$ is a union of two closed sets, hence closed; therefore its complement $U-A$ is open in $X$.

:::

:::

::: pf-step

$A-U$ is closed in $X$.

::: pf-proof

By step [](#complements){.pf-ref}, $X-(A-U)=(X-A)\cup U$. The set $X-A$ is open because $A$ is closed, and $U$ is open by hypothesis, so $(X-A)\cup U$ is a union of two open sets, hence open; therefore its complement $A-U$ is closed in $X$.

:::

:::

:::
:::
