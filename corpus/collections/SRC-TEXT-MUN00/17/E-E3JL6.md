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
---

::: {.exercise}

Show that the product of two Hausdorff spaces is Hausdorff.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 17.11, PDF p. 7** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the proof is theirs. Whitman, printed p. 165, gives the same argument.

Let $X$ and $Y$ be Hausdorff and let $(a,b)\ne(c,d)$ in $X\times Y$.

If $a\ne c$, the Hausdorff property of $X$ gives disjoint open sets $U\ni a$ and $V\ni c$. Then $U\times Y$ and $V\times Y$ are open in $X\times Y$ (they are basis elements), they contain $(a,b)$ and $(c,d)$ respectively, and
$$
(U\times Y)\cap(V\times Y)=(U\cap V)\times Y=\varnothing .
$$
If $a=c$ then $b\ne d$, and the same argument with the roles of $X$ and $Y$ exchanged gives disjoint open sets $X\times U'\ni(a,b)$ and $X\times V'\ni(c,d)$.

So distinct points of $X\times Y$ have disjoint neighbourhoods and $X\times Y$ is Hausdorff.
:::
