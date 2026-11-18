---
schema: qual/card@1
id: E-E3JL6
kind: problem
title: Products of Hausdorff spaces are Hausdorff
classification:
  areas:
  - topology
  topics:
  - Hausdorff Spaces
  - Product Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §17 Exercise 11, printed p. 101; the stored
    statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 17.11, PDF p. 7. If the first coordinates differ,
    disjoint neighbourhoods of them crossed with the whole second factor separate the two
    points; otherwise the same with the roles exchanged. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into STYLE-08 as three steps: the case $a\ne c$, the case $a=c$, and the exhaustive dichotomy that yields the Hausdorff property. $(U\times Y)\cap(V\times Y)=(U\cap V)\times Y$ was re-checked. No statement change.
---

::: {.exercise}

Show that the product of two Hausdorff spaces is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.11, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the proof is theirs. Whitman, printed p. 165, gives the same argument.

::: pf

::: {.pf-step #first-factor}

If $a\ne c$, then $(a,b)$ and $(c,d)$ have disjoint neighbourhoods in $X\times Y$.

::: pf-proof

The Hausdorff property of $X$ gives disjoint open sets $U\ni a$ and $V\ni c$. Then $U\times Y$ and $V\times Y$ are basis elements of $X\times Y$, hence open, they contain $(a,b)$ and $(c,d)$ respectively, and
$$
(U\times Y)\cap(V\times Y)=(U\cap V)\times Y=\varnothing .
$$

:::

:::

::: {.pf-step #second-factor}

If $a=c$, then $(a,b)$ and $(c,d)$ have disjoint neighbourhoods in $X\times Y$.

::: pf-proof

Here $b\ne d$, because $(a,b)\ne(c,d)$. The Hausdorff property of $Y$ gives disjoint open sets $U'\ni b$ and $V'\ni d$, and $X\times U'$ and $X\times V'$ are disjoint basis elements of $X\times Y$ containing $(a,b)$ and $(c,d)$ respectively, as in step [](#first-factor){.pf-ref} with the factors exchanged.

:::

:::

::: pf-step

$X\times Y$ is Hausdorff.

::: pf-proof

Let $(a,b)$ and $(c,d)$ be distinct points of $X\times Y$. Either $a\ne c$, and step [](#first-factor){.pf-ref} separates them, or $a=c$, and step [](#second-factor){.pf-ref} separates them; these cases exhaust the possibilities, so every two distinct points of $X\times Y$ have disjoint neighbourhoods.

:::

:::

:::
:::
