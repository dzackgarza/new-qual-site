---
schema: qual/card@1
id: E-4T2MK
kind: problem
title: Connected fibers over a connected base connect the total space
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §23 Exercise 11, printed p. 152, with Lemma 23.2
    and Theorem 23.3; the stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.11, PDF p. 3. A connected fibre meeting one
    side of a would-be separation of X lies in it, so the sides are saturated, and being
    open and saturated they have open images that would separate Y. (tmp/sources/munkres-
    solutions-positron-ch3.pdf).
---

::: {.exercise}

Let $p: X \to Y$ be a quotient map.
Show that if each set $p^{-1}(\theset{y})$ is connected, and if $Y$ is connected, then $X$ is connected.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.11, PDF p. 3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the saturation argument is theirs.

Let $p:X\to Y$ be a quotient map with every fibre $p^{-1}(\{y\})$ connected and $Y$ connected. Suppose $X=U\cup V$ is a separation.

For $y\in p(U)$ pick $x\in U$ with $p(x)=y$. The fibre $p^{-1}(\{y\})$ is connected and meets $U$ (in $x$), so by Lemma 23.2 the whole fibre lies in $U$. Hence $p^{-1}(p(U))\subset U$, and the reverse inclusion always holds, so $U=p^{-1}(p(U))$ is saturated; likewise $V$.

Since $p$ is a quotient map and $U$, $V$ are open and saturated, $p(U)$ and $p(V)$ are open in $Y$; they are disjoint (a common point would give a point of $U\cap V$), they are nonempty ($p$ is surjective and $U,V\ne\varnothing$), and $p(U)\cup p(V)=Y$. So $p(U),p(V)$ separate $Y$, contradicting the connectedness of $Y$. Hence $X$ is connected.
:::
