---
schema: qual/card@1
id: E-CJGFE
kind: problem
title: Heredity of the seventeen basic properties
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 4, printed p. 228, with Theorem 30.2, Theorem 31.2, Exercise 30.9 (closed
    subspaces of Lindelof spaces), Example 5 of §30 (the open subspace I x (0,1) of the compact
    ordered square is not Lindelof), Exercise 32.1 and Example 2 of §32 (the open subspace
    S_Omega x S_bar_Omega of the compact S_bar_Omega^2 is not normal). No published solution was
    located (search recorded on E-PWXIV and in the COMPLAINTS.md entry). All 51 entries of the table
    were re-derived: the hereditary ones are Hausdorff, regular, completely regular, first and second
    countable, locally metrizable and metrizable; compactness, limit point compactness, Lindelofness
    and normality pass to closed subspaces and fail for open ones (normality by Example 2 of §32);
    local compact Hausdorffness passes to open and to closed subspaces but not to arbitrary ones;
    local connectedness and local path connectedness pass to open subspaces only; separability passes
    to open subspaces because D cap U is dense in U, and fails even for closed subspaces, the
    anti-diagonal of the Sorgenfrey plane being an uncountable closed discrete subspace of a separable
    space; connectedness and path connectedness fail in all three columns.
---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved when one passes to a subspace?
To a closed subspace?
To an open subspace?
:::

::: {.solution}
Number the properties as in Exercise `E-PWXIV`. The preservation table is:

| property | arbitrary subspace | closed subspace | open subspace |
|---|:---:|:---:|:---:|
| (1) connected | no | no | no |
| (2) path connected | no | no | no |
| (3) locally connected | no | no | yes |
| (4) locally path connected | no | no | yes |
| (5) compact | no | yes | no |
| (6) limit point compact | no | yes | no |
| (7) locally compact Hausdorff | no | yes | yes |
| (8) Hausdorff | yes | yes | yes |
| (9) regular | yes | yes | yes |
| (10) completely regular | yes | yes | yes |
| (11) normal | no | yes | no |
| (12) first countable | yes | yes | yes |
| (13) second countable | yes | yes | yes |
| (14) Lindelöf | no | yes | no |
| (15) countable dense subset | no | no | yes |
| (16) locally metrizable | yes | yes | yes |
| (17) metrizable | yes | yes | yes |

Each of the 51 entries is decided by a numbered result of the book or by an explicit witness, row by row.

**1 Connected, 2 Path connected: no in all three columns.** $[0,1]\cup[2,3]$ is a closed subspace of $\RR$ and is disconnected, so closed subspaces fail, and with them arbitrary ones; $(0,1)\cup(2,3)$ is an open subspace of $\RR$ and is disconnected, so open subspaces fail. A path connected space is connected, so the two spaces settle the path column as well.

**3 Locally connected, 4 Locally path connected: yes for open subspaces, no for closed and arbitrary ones.** If $X$ is locally connected and $U\subseteq X$ is open, every open subset of $U$ is open in $X$, so by Theorem 25.3 each of its components is open in $U$ and $U$ is locally connected; Theorem 25.4 gives the same for local path connectedness. In the other direction the topologist's sine curve is closed in $\RR^2$, connected and not locally connected, Example 3 of §25, so closed subspaces and hence arbitrary subspaces fail; it is not locally path connected either, since a locally path connected space is locally connected.

**5 Compact, 6 Limit point compact: yes for closed subspaces, no otherwise.** Theorem 26.2 for compactness and Exercise 28.3(b) for limit point compactness. The open subspace $(0,1)$ of $[0,1]$ is neither compact nor limit point compact, the set $\{1/n\}$ in it being infinite with no limit point in $(0,1)$.

**7 Locally compact Hausdorff: yes for closed and for open subspaces, no for arbitrary ones.** Corollary 29.3. $\QQ\subset\RR$ is neither closed nor open and is not locally compact, Example 1 of §29.

**8 Hausdorff, 9 Regular, 10 Completely regular: yes in all three columns.** Theorems 31.2(a), 31.2(b) and 33.2: a subspace of a Hausdorff, of a regular, of a completely regular space has the same property.

**11 Normal: yes for closed subspaces, no otherwise.** Exercise 32.1. For the negative entries, $S_\Omega\times\overline S_\Omega$ is not normal, Example 2 of §32, and it is an open subspace of the compact Hausdorff, hence normal, $\overline S_\Omega\times\overline S_\Omega$, since $S_\Omega$ is open in $\overline S_\Omega$; an open subspace is a subspace, so this settles the open and the arbitrary columns at once.

**12 First countable, 13 Second countable: yes in all three columns.** Theorem 30.2: both axioms pass to subspaces.

**14 Lindelöf: yes for closed subspaces, no otherwise.** Exercise 30.9. For the negative entries, $A = I\times(0,1)$ is an open subspace of the ordered square, which is compact hence Lindelöf, and $A$ is not Lindelöf: the sets $\{x\}\times(0,1)$ are pairwise disjoint and open in $A$, and no proper subcollection of them covers $A$, Example 5 of §30. Being open, $A$ settles the open and the arbitrary columns.

**15 Countable dense subset: yes for open subspaces, no otherwise.** If $D$ is countable and dense in $X$ and $U\subseteq X$ is open, then $D\cap U$ is countable and dense in $U$: a nonempty open subset of $U$ is open in $X$ and meets $D$. For the negative entries, the anti-diagonal $L = \{x\times(-x)\}$ of the Sorgenfrey plane is closed and discrete, Example 3 of §31, so no countable set is dense in $L$; and the Sorgenfrey plane itself is separable, its points with rational coordinates being dense. $L$ is closed, so this settles the closed and the arbitrary columns.

**16 Locally metrizable, 17 Metrizable: yes in all three columns.** Exercise 21.1: the restriction of a metric to a subspace gives its topology. A metrizable neighbourhood of a point of $X$, met with the subspace, is a metrizable neighbourhood of the point in the subspace, so local metrizability is hereditary too.


:::
