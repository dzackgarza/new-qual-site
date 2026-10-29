---
schema: qual/card@1
id: P-DPYAI
kind: problem
title: $S^n$ minus $k$ points is a wedge of $k-1$ spheres
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Retracts
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source text stated the lemma with = in place of homotopy equivalence and followed it with a proof sketch that retracts onto a wedge of circles, which is false for n > 2. The statement now asks for the homotopy equivalence for n >= 2 and k >= 1 distinct points; the sketch is removed."
---

::: {.problem}
Let $n\ge2$ and $k\ge1$, and let $p_1,\ldots,p_k\in S^n$ be distinct points. Show that
$$S^n\setminus\theset{p_1,\ldots,p_k}\simeq\bigvee_{k-1}S^{n-1}.$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For $k\ge1$, stereographic projection identifies $S^n$ minus one chosen point with $\RR^n$, so removing $k$ points from $S^n$ reduces to removing $k-1$ points from $\RR^n$.

::: pf-proof

Choose one of the removed points as the projection point.

:::

:::

::: {.pf-step #s2}

If $n\ge2$, $\RR^n$ minus $r$ points deformation retracts onto a wedge of $r$ copies of $S^{n-1}$.

::: pf-proof

Choose disjoint small balls around the removed points and connect their boundary spheres to a common basepoint by disjoint arcs forming a tree. The complement deformation retracts onto the union of these boundary spheres and arcs; collapsing the tree gives the wedge of the $r$ spheres.

:::

:::

::: pf-step

Hence for $n\ge2$,
$$\boxed{S^n\setminus\theset{p_1,\ldots,p_k}\simeq\bigvee^{k-1}S^{n-1}.}$$

::: pf-proof

Apply steps [](#s1){.pf-ref} and [](#s2){.pf-ref} with $r=k-1$.

:::

:::

:::

:::
