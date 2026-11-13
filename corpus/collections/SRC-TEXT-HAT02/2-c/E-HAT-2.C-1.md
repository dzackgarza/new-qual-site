---
schema: qual/card@1
id: E-HAT-2.C-1
kind: problem
title: Minimum number of edges for simplicial map $S^1 \to S^1$ of degree $n$
classification:
  areas:
  - topology
  topics:
  - Simplicial Approximation
  - Degree
  - Graphs
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.C, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified the simplicial, Lefschetz-trace, or surface argument against the preceding section results.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 1, printed page
    184; the statement matches the book word for word. Proof checked: a simplicial
    map carries each edge of K onto an edge or a vertex, so f_*(z_K) = n z_L forces
    at least |n| edges of K over each edge of L, whence e(K) >= |n| e(L) >= 3|n| with
    e(L) >= 3; the polygon with 3|n| edges mapped periodically around a triangle
    attains the bound, and n = 0 is attained by two triangles with a constant map.
    No defect. Not claimed by the card: the total e(K) + e(L) minimised over e(L),
    which is 3|n| + 3 for the same reason.
- event: solution-written
  by: claude
  date: 2026-11-08
  note: >-
    Replaces the solution with the complete published fundamental-cycle argument in the answer to
    Simplicial map of the circle S1 (2019), at
    https://math.stackexchange.com/questions/3590105/simplicial-map-of-the-circle-s1. The lower
    bound is proved first from f_*(z_K)=n z_L: each target edge needs at least |n| nondegenerate
    preimages. A 3|n|-gon over a triangle attains it, and n=0 is attained by a constant map
    between triangles. This is a full source argument, not a citation attached to a different proof.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Read the published answer and checked it against Hatcher p.184. Each simplicial edge is sent
    to a vertex or homeomorphically to an edge, so signed coefficient n on a target edge requires
    at least |n| domain edges. Period three wraps the triangle |n| times with the required sign.
- event: source-checked
  by: claude
  date: 2026-11-13
  note: >-
    Re-read the printed statement for #123: the exercise is Exercise 1 of §2.C on printed p. 184,
    identical in the current online text, and the card states it word for word. The obligation that
    #123 records is unchanged and stays open: the retained solution sets do not solve this exercise,
    and none was located elsewhere. The card's citation is the final answer to MSE question 3590105,
    which is not a published solution set; the argument transcribed from it is checked on the card.
    Searched without result in the retained sets (Sam, Li, DeMason, Poulsen, Stanford Math 215C
    Solution Sets 1--5, the UCR Math 205B help file, May, Bredon, Maxim's Math 752 notes) and in
    Hatcher's text and errata.
---
---

::: {.problem}
What is the minimum number of edges in simplicial complex structures $K$ and $L$ on $S^1$ such that there is a simplicial map $K \to L$ of degree $n$?
:::

::: {.solution}
Use the complete fundamental-cycle argument in **[*Simplicial map of the circle $S^1$* (2019), final answer](https://math.stackexchange.com/questions/3590105/simplicial-map-of-the-circle-s1)**. Let $e(K)$ and $e(L)$ be the numbers of edges, and orient both simplicial circles.

::: pf

::: {.pf-step #bound}
If $f:K\to L$ is a simplicial map of degree $n\ne0$, then
$$
e(K)\ge |n|e(L)\ge 3|n|.
$$

::: pf-proof
Write the fundamental cycles as $z_K=\sum_e\epsilon_e e$ and $z_L=\sum_a\epsilon_a a$. A simplicial map sends an edge either to a vertex or homeomorphically to an edge, so its coefficient on chains is $0$ or $\pm1$. Since $f_*(z_K)=n z_L$, every target edge receives total signed coefficient $n$, which requires at least $|n|$ distinct domain edges. Hence $e(K)\ge|n|e(L)$. A simplicial complex on $S^1$ has at least three edges: it cannot have a loop edge or two edges with the same endpoint pair.
:::

:::

::: {.pf-step #attain}
The lower bound is attained for every $n\ne0$.

::: pf-proof
Let $L$ be a triangle and $K$ a polygon with $3|n|$ edges. Map successive triples of edges of $K$ around the three edges of $L$, repeating exactly $|n|$ times. Use the positive orientation if $n>0$ and the reverse orientation if $n<0$. This vertex map extends simplicially and satisfies $f_*(z_K)=n z_L$.
:::

:::

::: pf-step
The case $n=0$ has the same minimum $e(K)=e(L)=3$.

::: pf-proof
Take both complexes to be triangles and use a constant simplicial map. It has degree zero.
:::

:::

:::

The minimum is therefore
$$
\boxed{e(L)=3,\qquad e(K)=3\max\{1,|n|\}.}
$$
:::
