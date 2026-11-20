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
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published answer key to the Review of the Basics and found
    none (issue #144). This exercise was searched for under its own content: Math StackExchange,
    site math, `/search/excerpts` with "hereditary property subspace", "which properties are
    preserved by continuous maps", "review of the basics Munkres supplementary exercises" and
    "seventeen properties", and `/search/advanced` with title "Munkres" over the tag
    general-topology, whose 623 questions include none on the three columns of this exercise.
    dbFin's chapter-4 supplementary page links to no problem page; the twelve GitHub repositories
    named in the COMPLAINTS.md entry for §30--§36 hold no Chapter 4 supplementary content; the web
    searches for the table answers returned nothing. The AoPS blog that holds an answer key was not
    read: it answers an automated request with a Cloudflare human check, which is not worked
    around. The card's table is its own work, re-derived against Munkres' theorems as its earlier
    note records, and this pass did not re-read it; the search is recorded in the COMPLAINTS.md
    entry for §30--§36 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Compared with the published answer key by cinnamon_e, "Topology by Munkres Chapter 4 | Day 13"
    (AoPS blog shooting star, 2025-09-05,
    https://artofproblemsolving.com/community/c3401823h3644066, text at
    tmp/sources/aops-shooting-star-munkres-ch4-day13.md), whose answer to Exercise 4 is that
    passing to a subspace preserves 8-10, 12-13 and 16-17, passing to a closed subspace preserves
    5-14 and 16-17, and passing to an open subspace preserves 3-4, 7-10, 12-13 and 15-17. The
    card's three columns are those three sets, entry by entry; the card and the key agree, and the
    key is now cited on the card.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    In the negative entries for compactness and limit point compactness the infinite subset of
    (0,1) was written {1/n}, the index running over the positive integers, which contains 1 and so is
    not a subset of (0,1); a reader of this card reported it. It is now {1/n : n >= 2}, whose only
    limit point in R is 0, and the step now says that compactness would supply a limit point by
    Theorem 28.1. The other 49 entries of the table are unchanged and were not re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader of this card reported that the statement says the seventeen properties are "listed in
    Exercise 1"; Munkres prints the list at the head of the Supplementary Exercises, before Exercise 1,
    on printed p. 228, where Exercises 1 to 5 also stand. The statement now says so. Only that
    reference changed: the table's 51 entries and their arguments were not re-read in this pass, the
    mathematics having been re-derived and compared with the published key in the two passes recorded
    above.

- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against the Supplementary Exercises: Review of the Basics, Exercise 4, and found
    correct in all fifty-one entries. Checked row by row against the numbered results the card
    cites, each read in the book: Theorem 25.3 and Theorem 25.4 for the open column of (3) and
    (4), with Example 3 of §25 -- "the topologist's sine curve is connected but not locally
    connected" -- as the closed-column witness; Theorem 26.2 and Exercise 28.3(b), whose part (b)
    is exactly the closed-subspace question, for (5) and (6), with the open interval $(0,1)$
    inside $[0,1]$ for the open column; Corollary 29.3, which reads "if $A$ is closed in $X$ or
    open in $X$, then $A$ is locally compact", for the two affirmative entries of (7), with
    Example 1 of §29 for $\QQ$; Theorems 31.2(a) and 31.2(b) and 33.2 for (8), (9) and (10);
    Exercise 32.1 and Example 2 of §32 for (11), the witness being $S_\Omega\times\overline
    S_\Omega$ inside the compact Hausdorff $\overline S_\Omega\times\overline S_\Omega$, in
    which $S_\Omega$ is open; Theorem 30.2 for (12) and (13); Exercise 30.9 with Example 5 of §30
    for (14), whose witness $I\times(0,1)$ is open in the ordered square; Example 3 of §31 for
    the closed, discrete, uncountable anti-diagonal of the separable Sorgenfrey plane, which
    settles (15)'s two negative columns; and Exercise 21.1, which is exactly "$d|A\times A$ is a
    metric for the subspace topology", for (16) and (17). The one entry whose reason is not a
    citation is (15) in the open column, and it is right: the trace of a countable dense set on an
    open subspace is countable and dense there, since a nonempty open subset of the subspace is
    open in the whole space. Not checked: no published key to these exercises was located, and
    none is claimed here.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was a table with one paragraph per group of rows and no
    numbered step. It is now a `pf` with nine steps, the table carried as the last step, each step
    holding a `pf-proof`. Cited by numbered statement only: Munkres, Topology, §36 Exercise 1,
    Theorem 25.3, Theorem 25.4, Theorem 26.2, Theorem 27.1, Theorem 28.1, Exercise 28.3(b),
    Corollary 29.3, Theorem 30.2, Exercise 30.9, Theorem 31.2(a) and (b), Theorem 33.2, Exercise
    21.1, Exercise 32.1, with Examples 1 of §29, 2 of §32, 3 of §25, 3 of §31, 5 of §30 as the
    witnesses. No retained published set answers the exercise, and the card's preamble says so.
    Checked: that each "yes" row names the theorem that gives it to the closed, open or arbitrary
    subspace as the column says, that each "no" row names a witness failing exactly that column,
    and that $(0,1)$ is an open subspace of $[0,1]$ with no limit point of $\{1/n:n\ge2\}$ inside
    it.

---

::: {.exercise}

Consider the seventeen properties listed at the head of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved when one passes to a subspace?
To a closed subspace?
To an open subspace?
:::

::: {.solution}

Number the properties as in [[E-PWXIV]]; each of the 51 entries is decided below by a numbered result of Munkres, *Topology*, or by an explicit witness. No retained published solution of §36 Exercise 1 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §30--§36 of `SRC-TEXT-MUN00`. "Arbitrary" below means an arbitrary subspace of a space having the property.

::: pf

::: {.pf-step #rows-hereditary}
(1) Hausdorff, regular, completely regular, first countable, second countable, locally metrizable and metrizable pass to every subspace.

::: pf-proof
Theorem 31.2(a) for Hausdorff, Theorem 31.2(b) for regular, Theorem 33.2 for completely regular; Theorem 30.2 for first and second countability. For the metric rows, Exercise 21.1: the restriction of a metric to a subspace induces the subspace topology, so a metrizable space has every subspace metrizable, and a metrizable neighbourhood in $X$ meets the subspace in a metrizable neighbourhood of any of its points, so local metrizability is hereditary too. A closed or open subspace is a subspace.
:::

:::

::: {.pf-step #rows-locally-connected}
(2) Locally connected and locally path connected pass to open subspaces only.

::: pf-proof
If $X$ is locally connected and $U\subseteq X$ is open, every set open in $U$ is open in $X$, so by Theorem 25.3 each component of an open subset of $U$ is open in $U$, which is local connectedness of $U$; Theorem 25.4 gives local path connectedness the same way. For the negative entries, the topologist's sine curve is closed in $\RR^2$, connected and not locally connected (Example 3 of §25), so closed subspaces fail; a locally path connected space is locally connected, so it fails for local path connectedness as well, and an arbitrary subspace includes the closed ones.
:::

:::

::: {.pf-step #rows-compact}
(3) Compactness and limit point compactness pass to closed subspaces only.

::: pf-proof
Theorem 26.2: a closed subspace of a compact space is compact; Exercise 28.3(b): a closed subspace of a limit point compact space is limit point compact. For the negative entries, $(0,1)$ is an open subspace of $[0,1]$, and it is neither compact nor limit point compact, since $\{1/n:n\ge2\}$ is an infinite subset of it with no limit point in $(0,1)$, its only limit point in $\RR$ being $0$; a compact space is limit point compact by Theorem 28.1. An open subspace is a subspace, so the arbitrary column fails too.
:::

:::

::: {.pf-step #rows-locally-compact}
(4) Local compact Hausdorffness passes to closed and to open subspaces but not to arbitrary ones.

::: pf-proof
Corollary 29.3 gives both positive entries. For the negative entry, $\QQ\subseteq\RR$ is neither closed nor open and is not locally compact (Example 1 of §29).
:::

:::

::: {.pf-step #rows-normal}
(5) Normality passes to closed subspaces only.

::: pf-proof
Exercise 32.1: a closed subspace of a normal space is normal. For the negative entries, $S_\Omega\times\overline S_\Omega$ is not normal (Example 2 of §32) and is an open subspace of the compact Hausdorff, hence normal, $\overline S_\Omega\times\overline S_\Omega$, because $S_\Omega$ is open in $\overline S_\Omega$; an open subspace is a subspace, so both the open and the arbitrary columns fail.
:::

:::

::: {.pf-step #rows-lindelof}
(6) Lindelöfness passes to closed subspaces only.

::: pf-proof
Exercise 30.9: a closed subspace of a Lindelöf space is Lindelöf. For the negative entries, $A=I\times(0,1)$ is an open subspace of the ordered square, which is compact hence Lindelöf (Theorem 27.1), and $A$ is not Lindelöf: the sets $\{x\}\times(0,1)$ are pairwise disjoint and open in $A$ and no proper subcollection covers $A$ (Example 5 of §30). Being open, $A$ settles the open and the arbitrary columns.
:::

:::

::: {.pf-step #rows-separable}
(7) Having a countable dense subset passes to open subspaces only.

::: pf-proof
If $D$ is countable and dense in $X$ and $U\subseteq X$ is open, then $D\cap U$ is countable, and a nonempty open subset of $U$ is open in $X$ and therefore meets $D$, so $D\cap U$ is dense in $U$. For the negative entries, the anti-diagonal $L=\{x\times(-x)\}$ of the Sorgenfrey plane is closed and discrete (Example 3 of §31), so no countable subset of $L$ is dense in $L$, while the Sorgenfrey plane itself is separable through its points with rational coordinates. $L$ is closed, so both the closed and the arbitrary columns fail.
:::

:::

::: {.pf-step #rows-connected}
(8) Connectedness and path connectedness pass to no subspace of the three kinds.

::: pf-proof
$[0,1]\cup[2,3]$ is a closed subspace of $\RR$ and is disconnected, so closed subspaces fail; $(0,1)\cup(2,3)$ is an open subspace of $\RR$ and is disconnected, so open subspaces fail; and a subspace includes the closed ones, so the arbitrary column fails. A path connected space is connected, so the two disconnected witnesses settle the path connected column as well, since a path connected subspace would be a connected one.
:::

:::

::: {.pf-step #table}
(9) The preservation table is:

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

::: pf-proof
Every "yes" is one of the positive statements of steps [#rows-hereditary]{.pf-ref}, [#rows-locally-connected]{.pf-ref}, [#rows-compact]{.pf-ref}, [#rows-locally-compact]{.pf-ref}, [#rows-normal]{.pf-ref}, [#rows-lindelof]{.pf-ref} and [#rows-separable]{.pf-ref}, and every "no" is the negative statement of one of them or of step [#rows-connected]{.pf-ref}; the rows are in the numbering of [[E-PWXIV]].
:::

:::

:::

:::
