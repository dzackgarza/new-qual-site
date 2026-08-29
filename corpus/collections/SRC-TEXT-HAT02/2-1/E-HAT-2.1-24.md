---
schema: qual/card@1
id: E-HAT-2.1-24
kind: exercise
title: $n$-simplices in barycentric subdivision defined by inequalities on barycentric coordinates
classification:
  areas:
  - topology
  topics:
  - Homology
  - Simplicial Complexes
  - Barycentric Subdivision
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

Show that each $n$ simplex in the barycentric subdivision of $\Delta^n$ is defined by $n$ inequalities $t_{i_0} \leq t_{i_1} \leq \dots \leq t_{i_n}$ in its barycentric coordinates, where $(i_0, \cdots, i_n)$ is a permutation of $(0, \cdots, n)$.

::: {.solution}
<1>1. The barycentric subdivision of $\Delta^n$ has one vertex for each nonempty face of $\Delta^n$, i.e. for each nonempty subset $S \subseteq \{0, \ldots, n\}$.
Proof: definition of barycentric subdivision.

<1>2. The vertex corresponding to $S$ is the barycenter of the face spanned by $\{e_i : i \in S\}$, whose barycentric coordinates are $t_i = 1/|S|$ for $i \in S$ and $t_i = 0$ for $i \notin S$.
Proof: the barycenter of a face.

<1>3. An $n$-simplex of the subdivision is spanned by a chain of faces $S_0 \subsetneq S_1 \subsetneq \cdots \subsetneq S_n$ with $|S_k| = k + 1$.
Proof: a maximal chain of faces gives an $n$-simplex of the subdivision.

<1>4. Such a chain corresponds to a permutation $(i_0, \ldots, i_n)$ of $(0, \ldots, n)$, where $S_k = \{i_0, \ldots, i_k\}$.
Proof: <1>3 (each step adds one new vertex).

<1>5. A point in the simplex spanned by the barycenters of $S_0, \ldots, S_n$ has barycentric coordinates satisfying $t_{i_0} \ge t_{i_1} \ge \cdots \ge t_{i_n}$.
Proof: the barycenter of $S_k$ has $t_{i_0} = \cdots = t_{i_k} = 1/(k+1)$ and $t_{i_{k+1}} = \cdots = t_{i_n} = 0$, so convex combinations of these barycenters have $t_{i_0} \ge t_{i_1} \ge \cdots \ge t_{i_n}$.

<1>6. Hence each $n$-simplex of the subdivision is defined by the $n$ inequalities $t_{i_0} \le t_{i_1} \le \cdots \le t_{i_n}$ (up to reversing the order), for a permutation $(i_0, \ldots, i_n)$.
Proof: <1>4 and <1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
