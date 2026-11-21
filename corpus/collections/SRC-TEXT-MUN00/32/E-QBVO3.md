---
schema: qual/card@1
id: E-QBVO3
kind: problem
title: Normality of topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Normal Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 32 Exercise 10, printed p. 207, and against
    Exercise 32.9 of the same section and Theorem 19.6 (a map into a product is continuous iff its
    components are, printed p. 117), which gives continuity of the group operations of R^J
    coordinatewise. No published solution was located: Orellana's Section 32 stops at Exercise 5, "Doug's
    World" stops at Problem 32.7, and the other retained sets do not reach Chapter 4; the search is
    recorded in the COMPLAINTS.md entry for this batch. What was corrected: the card attributed the
    Stone theorem to "the first exercise of this section", and it is Exercise 9.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: dbFin, "Section 32: Problem 10 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-32-normal-spaces/problem-10-solution/ (read
    2026-11-10; kept at tmp/sources/dbfin/section-32-normal-spaces/problem-10-solution.txt), checked
    against Munkres, Topology (2000), Section 32 Exercise 10, printed p. 207, and Exercise 32.9 of
    the same section. The source's answer is "No ... it does not have to be normal", by the
    preceding exercise, together with the remark that a topological group is regular; the card
    names the group R^J with the product topology, whose group operations are continuous
    coordinatewise (Theorem 19.6, printed p. 117) and which is not normal for uncountable J by
    Exercise 9. What was corrected: the card attributed the Stone theorem to "the first exercise of
    this section" and it is Exercise 9 (recorded in the previous note on this card); the source
    cites "the previous exercises" with the same effect. This supersedes the previous note, which
    recorded that no published solution had been found.
---

::: {.exercise}

Is every topological group normal?
:::

::: {.solution}

No retained solution set covers this exercise: the answer is the one Munkres himself indicates, and the only published proof of the non-normality used is the one the book supplies inside §32 Exercise 9 (attributed there to A. H. Stone as adapted in [S-S]), so the card's argument is its own apart from that citation. The statement was checked against Munkres, *Topology* (2000), §32 Exercise 10, printed p. 207, with the definition of a topological group on printed p. 145, Theorem 19.6 on printed p. 117, Theorem 21.5 on printed p. 131, and the theorem of §32 Exercise 9 on printed p. 206.

Throughout, $J$ is an uncountable set, $G\coloneqq\RR^{J}$ carries coordinatewise addition and the product topology, and $\pi_{\alpha}\colon G\to\RR$ is the projection to the coordinate $\alpha$.

::: pf

::: {.pf-step #operations}
Addition and inversion are continuous on $G$.

:::: pf-proof

::: {.pf-step #coordinates}
For each $\alpha$ the composite $\pi_{\alpha}\circ{+}$ and $\pi_{\alpha}\circ\iota$, where ${+}$ is addition on $G\times G$ and $\iota$ is inversion on $G$, are continuous real-valued functions.

::: pf-proof
The projections $\pi_{\alpha}$ are continuous: by Theorem 19.6 (printed p. 117) a map into a product is continuous exactly when all its coordinate functions are, and applying this to the identity map of $G$ gives the continuity of each $\pi_{\alpha}$. The projections $\mathrm{pr}_{1},\mathrm{pr}_{2}\colon G\times G\to G$ are continuous for the same reason. Now $\pi_{\alpha}\circ{+}=\pi_{\alpha}\circ\mathrm{pr}_{1}+\pi_{\alpha}\circ\mathrm{pr}_{2}$ and $\pi_{\alpha}\circ\iota=0-(\pi_{\alpha})$, sums and differences of continuous real-valued functions are continuous by Theorem 21.5 (printed p. 131), and the constant $0$ is continuous.
:::

:::

::: {.pf-step #both}
${+}$ and $\iota$ are continuous.

::: pf-proof
By Theorem 19.6 (printed p. 117), a map into the product $G$ is continuous exactly when each of its coordinate functions is; step [](#coordinates){.pf-ref} verifies that for ${+}\colon G\times G\to G$ and for $\iota\colon G\to G$.
:::

:::

::::

:::

::: {.pf-step #hausdorff}
$G$ is Hausdorff, so its one-point sets are closed.

:::: pf-proof

::: {.pf-step #separate}
Distinct points of $G$ have disjoint open neighbourhoods.

::: pf-proof
Let $\mathbf{x}\neq\mathbf{y}$ in $G$; then $x_{\beta}\neq y_{\beta}$ for some $\beta$, and $\RR$ is Hausdorff, so there are disjoint open sets $U,V\subset\RR$ with $x_{\beta}\in U$, $y_{\beta}\in V$. The preimages $\pi_{\beta}^{-1}(U)$ and $\pi_{\beta}^{-1}(V)$ are open because $\pi_{\beta}$ is continuous, they contain $\mathbf{x}$ and $\mathbf{y}$, and they are disjoint because $U\cap V=\varnothing$.
:::

:::

::: {.pf-step #closed-points}
One-point sets in $G$ are closed.

::: pf-proof
Given $\mathbf{x}\in G$ and $\mathbf{y}\neq\mathbf{x}$, step [](#separate){.pf-ref} gives disjoint open sets containing $\mathbf{x}$ and $\mathbf{y}$, and the one containing $\mathbf{y}$ lies in the complement of $\theset{\mathbf{x}}$; so that complement is open and $\theset{\mathbf{x}}$ is closed.
:::

:::

::::

:::

::: {.pf-step #group}
$G$ is a topological group.

::: pf-proof
$G$ is a group under coordinatewise addition, which is inherited from the abelian group $(\RR,+)$; it satisfies the $T_{1}$ axiom by step [](#hausdorff){.pf-ref}; and its addition and inversion are continuous by step [](#operations){.pf-ref}. That is exactly the definition of a topological group (§22 Supplementary Exercises, printed p. 145).
:::

:::

::: {.pf-step #not-normal}
$G$ is not normal.

::: pf-proof
$J$ is uncountable, so $\RR^{J}$ is not normal: this is the theorem proved in §32 Exercise 9 (printed p. 206), due there to A. H. Stone as adapted in [S-S], and it is the only ingredient of this card that is taken from the book rather than argued here.
:::

:::

::: pf-step
Therefore not every topological group is normal; the answer is no.

::: pf-proof
Steps [](#group){.pf-ref} and [](#not-normal){.pf-ref} exhibit $\RR^{J}$ for an uncountable $J$ as a topological group that is not normal, so the class of topological groups is not contained in the class of normal spaces:
$$
\boxed{\text{no, and } \RR^{J}\text{ with }J\text{ uncountable is a counterexample.}}
$$
:::

:::

:::

:::
