---
schema: qual/card@1
id: E-LP0GM
kind: problem
title: Uniqueness of the slicing over connected evenly covered sets
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against the located published solution: dbFin, "Section 53: Problem 2 Solution",
    https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-2-solution/
    (read 2026-11-11; kept at tmp/sources/dbfin/section-53-covering-spaces/problem-2-solution.txt), and against Munkres, Topology (2000), Section 53
    Exercise 2, printed p. 341, with the definition of a covering map on printed p. 336. dbFin's argument takes two partitions, picks a slice of one different from every slice of the other and derives a proper clopen subset of $U$; the card's is the same conclusion by a shorter route, that when $U$ is connected each slice is a connected clopen subset of $p^{-1}(U)$ and therefore a component, so the partition is the partition into components. Both are correct; nothing needed repair.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Rewrote the solution on 2026-11-19. It was a nested block whose steps had no
    labels, with a "Proof:" line inside a step and a closing paragraph citing
    "step s3", a label that existed nowhere; the corpus gate reported it as
    "lamport proof: reference to unknown step label: s3". The proof is now a
    single-level Lamport proof whose four steps carry labels, and it transcribes
    Solution 2 of dbFin, "Section 53: Problem 2 Solution"
    (https://dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-2-solution/),
    kept at tmp/sources/dbfin/section-53-covering-spaces/problem-2-solution.txt
    and read on 2026-11-11: two partitions into slices, a slice of one that is
    not a slice of the other, and the difference A - B, which is open and closed
    in p^{-1}(U) and carries under p restricted to A to a non-empty proper open
    and closed subset of U. The card's shorter argument, that a slice is a
    connected clopen subset and hence a component, is kept in the remark as an
    equivalent route. Checked against the book in
    tmp/sources/munkres-2000-topology.md and on the retained PDF page by page:
    the definition of an evenly covered set, with the term "partition of
    p^{-1}(U) into slices", on printed p. 336 (PDF p. 351, folio 336, printed
    page = PDF page - 15); the exercise on printed p. 341 (PDF p. 356); and the
    criterion that a connected space has no non-empty proper subset that is both
    open and closed on printed p. 148 (PDF p. 163). No statement changes.
---

::: {.exercise}

Let $p: E \to B$ be continuous and surjective.
Suppose that $U$ is an open set of $B$ that is evenly covered by $p$.
Show that if $U$ is connected, then the partition of $p^{-1}(U)$ into slices is unique.
:::

::: {.solution}

::: pf

::: {.pf-step #slices}
Each slice of a partition of $p^{-1}(U)$ is an open subset of $p^{-1}(U)$ that $p$ carries homeomorphically onto $U$.

::: pf-proof
This is the definition, Munkres, *Topology* (2000), printed p. 336: the open set $U$ of $B$ is evenly covered by $p$ when $p^{-1}(U)$ is the union of disjoint open sets $V_\alpha$ in $E$ such that, for each $\alpha$, the restriction of $p$ to $V_\alpha$ is a homeomorphism of $V_\alpha$ onto $U$, and the collection $\{V_\alpha\}$ is called a partition of $p^{-1}(U)$ into slices.
:::

:::

::: {.pf-step #clopen}
Every slice of a partition of $p^{-1}(U)$ is also closed in $p^{-1}(U)$.

::: pf-proof
Let $B$ be the slice $V_{\alpha_0}$ of a partition $\{V_\alpha\}$. Its complement $p^{-1}(U)\setminus B=\bigcup_{\alpha\ne\alpha_0}V_\alpha$ is a union of open sets, hence open, so $B$ is closed in the subspace $p^{-1}(U)$.
:::

:::

::: {.pf-step #two-partitions}
If the partition of $p^{-1}(U)$ into slices is not unique, there are partitions $\{A_\alpha\}$ and $\{B_\beta\}$ and slices $A=A_{\alpha_0}$, $B=B_{\beta_0}$ with $A\ne B$, $A\cap B\ne\emptyset$ and $A\setminus B\ne\emptyset$.

::: pf-proof
Take a slice $A$ of the first partition that is not a member of the second. Both families cover $p^{-1}(U)$ and $A$ is non-empty, so $A$ meets some slice $B=B_\beta$ of the second partition, whence $A\cap B\ne\emptyset$; and $B\ne A$ because $A$ is not among the $B_\beta$, so $A\setminus B\ne\emptyset$.
:::

:::

::: {.pf-step #no-second-partition}
No such pair of partitions exists, so the partition of $p^{-1}(U)$ into slices is unique.

::: pf-proof
Let $A$ and $B$ be as in step [](#two-partitions){.pf-ref}. By steps [](#slices){.pf-ref} and [](#clopen){.pf-ref}, $A$ and $B$ are open and closed in $p^{-1}(U)$, so $A\setminus B=A\cap(p^{-1}(U)\setminus B)$ is open and closed in $p^{-1}(U)$, hence in the subspace $A$. Since $p\restriction_A:A\to U$ is a homeomorphism by step [](#slices){.pf-ref}, the image $p(A\setminus B)$ is open and closed in $U$; it is non-empty because $A\setminus B$ is, and proper because $p\restriction_A$ is injective and $A\setminus B\subsetneq A$. A connected space has no non-empty proper subset that is both open and closed (Munkres, printed p. 148), and that contradicts the hypothesis on $U$; so the partitions are equal.
:::

:::

:::

:::

::: {.remark title="Published solution"}
The argument is Solution 2 of dbFin, "Section 53: Problem 2 Solution" (dbfin.com/topology/munkres/chapter-9/section-53-covering-spaces/problem-2-solution/): two partitions of $p^{-1}(U)$ into slices, a slice $A$ of one that is not a slice of the other, and then $A\setminus B$, which is open and closed in $p^{-1}(U)$ and carries to a non-empty proper open and closed subset of $U$. The same conclusion follows at once from step [](#clopen){.pf-ref}: a slice is homeomorphic to the connected space $U$, so it is a connected clopen subset of $p^{-1}(U)$ and therefore a connected component, and a space has only one partition into connected components. The exercise is Munkres, *Topology* (2000), Section 53, Exercise 2.
:::
