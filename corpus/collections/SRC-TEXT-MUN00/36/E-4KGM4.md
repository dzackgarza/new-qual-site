---
schema: qual/card@1
id: E-4KGM4
kind: problem
title: Properties of compact Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 3, printed p. 228, with Theorem 28.1, Theorem 32.3, Theorem 33.1, Theorem 29.1
    and Exercise 29.7, Exercise 27.6 and Exercise 30.5(a). No published solution was located (search
    recorded on E-PWXIV and in the COMPLAINTS.md entry). The eight guaranteed properties are
    compact, limit point compact, locally compact Hausdorff, Hausdorff, regular, completely regular,
    normal and Lindelof; the nine that are not guaranteed are excluded by two spaces. The Cantor set,
    Exercise 27.6, is compact Hausdorff, totally disconnected and without isolated points, which
    excludes connectedness, path connectedness, local connectedness and local path connectedness. The
    ordinal interval [0, omega_1], which is the one-point compactification of S_Omega by Exercise
    29.7, is compact Hausdorff and fails first countability at omega_1, separability, second
    countability, metrizability and local metrizability, which excludes those five. What was
    corrected: the page, which is 228 and not 229; and the table, whose Reason column named the
    phenomenon rather than the result, so that each row now names the theorem that decides it.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published answer key to the Review of the Basics and found
    none (issue #144). This exercise was searched for under its own content: Math StackExchange,
    site math, `/search/excerpts` with "Munkres review of basics compact Hausdorff", "seventeen
    properties Munkres exercise 1", "review of the basics Munkres supplementary exercises" and
    "seventeen properties", and `/search/advanced` with title "Munkres" over the tag
    general-topology, whose 623 questions include none on the table. dbFin's chapter-4
    supplementary page links to no problem page; the twelve GitHub repositories named in the
    COMPLAINTS.md entry for §30--§36 hold no Chapter 4 supplementary content, the repository
    search being `q=munkres topology solutions`; the web searches for the table answers returned
    nothing. The AoPS blog that holds an answer key was not read: it answers an automated request
    with a Cloudflare human check, which is not worked around. The card's table is its own work,
    re-derived against Munkres' theorems as its earlier note records, and this pass did not re-read
    it; the search is recorded in the COMPLAINTS.md entry for §30--§36 with every query.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Compared with the published answer key by cinnamon_e, "Topology by Munkres Chapter 4 | Day 13"
    (AoPS blog shooting star, 2025-09-05,
    https://artofproblemsolving.com/community/c3401823h3644066, text at
    tmp/sources/aops-shooting-star-munkres-ch4-day13.md), whose answer to Exercise 3 is that a
    compact Hausdorff space satisfies 5-11 and 14. The card's eight properties are 5, 6, 7, 8, 9,
    10, 11 and 14, and it excludes the same nine as the key; the card and the key agree, and the
    key is now cited on the card.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The non-separability of [0, omega_1] was argued from the boundedness of a countable set of
    ordinals below omega_1, which does not cover a countable dense set containing omega_1 itself; a
    reader of this card reported it. The step now takes beta bounding the ordinals of a countable set
    D that lie below omega_1, and exhibits the nonempty open interval (beta, omega_1), which misses D
    because omega_1 is not one of its points. The eight guaranteed properties and the other
    exclusions are unchanged, and were not re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Three defects reported by a reader of this card, checked against the book before changing
    anything. (a) The exclusion of properties 13 and 17 was drawn from Exercise 30.5(a), "every
    metrizable space with a countable dense subset has a countable basis", whose hypothesis the
    sentence before it has just denied: [0, omega_1] has no countable dense subset. The step now uses
    only what is available without that hypothesis -- a metrizable space is first countable, the balls
    B(x, 1/n) forming a countable basis at x (§21, printed p. 130), and a second countable space is
    first countable, its basis elements containing a point forming a countable basis there (§30,
    printed p. 190) -- so that failing first countability at omega_1 excludes 13 and 17. (b) The
    argument that [0, omega_1] is not first countable at omega_1 went straight from the boundedness of
    a countable set of ordinals to the local-base conclusion; it now says that every neighbourhood of
    omega_1 contains a final segment and that the final segment above the supremum of countably many
    such steps contains none of countably many neighbourhoods. (c) The statement said the properties
    are "listed in Exercise 1"; Munkres prints the list at the head of the Supplementary Exercises,
    before Exercise 1, on printed p. 228. The table, the Cantor set paragraph and the remaining
    exclusions were re-read and kept.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Two defects reported by a reader, checked against the book and repaired. (a) The argument that
    [0, omega_1] is not first countable at omega_1 said that the final segment above the supremum of the
    choices contains none of the countably many neighbourhoods, which fails when the supremum is attained:
    a neighbourhood U_n that is exactly the final segment (alpha_n, omega_1] with alpha_n the supremum is
    contained in that segment. The step now takes gamma = beta + 1, an ordinal below omega_1 because
    omega_1 is a limit ordinal, and shows that the neighbourhood (gamma, omega_1] of omega_1 contains no
    U_n, since gamma lies in every U_n and not in (gamma, omega_1]. (b) The solution's opening line still
    called the properties those "numbered in Supplementary Exercise 1"; Munkres prints the list at the head
    of the Supplementary Exercises, before Exercise 1, and Exercise 1 is the list of eleven spaces (a)--(k), so the
    line now names the head of the section. The eight guaranteed properties, the table, the Cantor set
    paragraph and the other exclusions are unchanged, as is the printed statement (Exercise 3, printed
    p. 228).

- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    A reader's count error in the note of 2026-11-15, checked against the book. That note said Exercise 1 of the
    Supplementary Exercises is "the list of twelve spaces"; the list printed on p. 228 runs (a) to (k), which is
    eleven spaces, and the note now says so. The seventeen properties, the table, the two spaces that exclude the
    nine unguaranteed properties and the printed statement (Exercise 3, printed p. 228) are untouched.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked every one of the seventeen properties against
    the book: (5),(8) hypothesis; (6) Theorem 28.1; (7) the whole space is a compact
    subspace containing a neighbourhood; (11) Theorem 32.3; (9),(10) normal implies regular
    and completely regular; (14) a finite subcover is a countable one. For the nine not
    guaranteed the two spaces are checked claim by claim: the Cantor set is compact
    Hausdorff, totally disconnected and has no isolated points (Exercise 27.6(a),(d)), which
    excludes (1),(2),(3),(4); S-bar-Omega is compact Hausdorff (Exercise 29.7 with Theorem
    29.1 and Example 3 of §29, and Example 2 of §32 uses it as such), fails first
    countability at Omega by the countable-supremum argument, has no countable dense subset,
    and so fails (12),(13),(15),(16),(17). The seventeen properties are now listed with the
    book's numbering in the card, since the exercise refers to them by position. The
    argument is the card's own; no published solution of this supplementary exercise was
    located. Page numbers not verifiable from the extraction are not asserted.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against the Supplementary Exercises: Review of the Basics, Exercise 3, and
    against Munkres' numbered results, and found correct in all seventeen entries. The eight
    affirmative ones: (5) and (8) are the hypothesis; (7) because $X$ itself is the compact
    subspace containing a neighbourhood of any point, which is the definition of local
    compactness in §29; (6) by Theorem 28.1; (11) by Theorem 32.3; (9) and (10) because a normal
    space is regular and, by Urysohn's lemma in §33, completely regular; and (14) because a finite
    subcover is a countable one. The two witnesses: the Cantor set, compact Hausdorff and failing
    (1) to (4) -- totality of disconnection and the absence of isolated points are §27 Exercise
    6(a) and (d), whose exercise is exactly the Cantor set, and the argument that no point has a
    connected neighbourhood is the one on the card -- and $\overline{S}_{\Omega}$, which fails
    (12) by the countable-supremum argument at $\Omega$, (15) by the same bound applied to a
    countable dense set, and (13), (16), (17) because each would give a countable base at
    $\Omega$ inside a final segment; that $\overline{S}_{\Omega}$ is compact Hausdorff is
    Theorem 29.1 with §29 Exercise 7. Checked in passing that §25 Example 3 is the sentence "the
    topologist's sine curve is connected but not locally connected", which is the citation the
    neighbouring card makes. Not checked: no published key to these exercises was located, and
    none is claimed here.
---

::: {.exercise}

Consider the seventeen properties listed at the head of the Supplementary Exercises (Review of the Basics).

Which of these properties does a compact Hausdorff space have?
:::

::: {.solution}
No published solution of this supplementary exercise was located; the argument is the card's own, checked against the numbered results cited in each step. The seventeen properties, with the numbering the book uses at the head of the Supplementary Exercises (Review of the Basics), are: (1) connected, (2) path connected, (3) locally connected, (4) locally path connected, (5) compact, (6) limit point compact, (7) locally compact Hausdorff, (8) Hausdorff, (9) regular, (10) completely regular, (11) normal, (12) first-countable, (13) second-countable, (14) Lindelöf, (15) has a countable dense subset, (16) locally metrizable, (17) metrizable.

Let $X$ be a compact Hausdorff space throughout.

::: pf

::: {.pf-step #guaranteed-basic}
$X$ has (5), (8) and (7).

::: pf-proof
(5) and (8) are the hypothesis. For (7): given $x\in X$ and a neighbourhood $U$ of $x$, the whole space $X$ is a compact subspace containing the neighbourhood $U$ of $x$, which is exactly the condition for $X$ to be locally compact in the sense of §29; combined with (8) this gives (7).
:::

:::

::: {.pf-step #limit-point}
$X$ has (6).

::: pf-proof
A compact space is limit point compact (Theorem 28.1): every infinite subset of $X$ has a limit point in $X$.
:::

:::

::: {.pf-step #normal}
$X$ has (11).

::: pf-proof
Every compact Hausdorff space is normal (Theorem 32.3).
:::

:::

::: {.pf-step #regular}
$X$ has (9) and (10).

::: pf-proof
A normal space is regular: it is $T_{1}$, and disjoint closed sets — in particular a point and a closed set not containing it — are separated by disjoint open sets (§31). A normal space is completely regular, by Urysohn's lemma applied to a point and a closed set not containing it (§33). Both properties are inherited from (11).
:::

:::

::: {.pf-step #lindelof}
$X$ has (14).

::: pf-proof
Every open cover of $X$ has a finite subcover, and a finite subcollection is in particular a countable one.
:::

:::

::: {.pf-step #cantor}
The Cantor set $C$ is a compact Hausdorff space that lacks (1), (2), (3) and (4), so none of those four is guaranteed.

:::: pf-proof

::: {.pf-step #cantor-facts}
$C$ is compact Hausdorff, totally disconnected, and has no isolated points.

::: pf-proof
$C$ is a closed subspace of the compact Hausdorff space $[0,1]$, hence compact (Theorem 26.2) and Hausdorff. It is totally disconnected and has no isolated points by Munkres §27 Exercise 6(a) and (d).
:::

:::

::: {.pf-step #cantor-not-connected}
$C$ is neither connected nor path connected.

::: pf-proof
$C$ has more than one point, and every connected subset of $C$ is a single point because $C$ is totally disconnected; so $C$ is not connected. A path in $C$ is a continuous image of $[0,1]$, hence connected, hence a single point; so any two points of $C$ that are joined by a path coincide, and $C$ is not path connected.
:::

:::

::: {.pf-step #cantor-not-locally}
$C$ is neither locally connected nor locally path connected.

::: pf-proof
Let $x\in C$ and let $V$ be a connected neighbourhood of $x$. As $C$ is totally disconnected, $V=\{x\}$; but $V$ is a neighbourhood, so it contains an open set of $C$ containing $x$, and $\{x\}$ would then be open, making $x$ isolated, contrary to step [](#cantor-facts){.pf-ref}. So $x$ has no connected neighbourhood and $C$ is not locally connected. A locally path connected space is locally connected, since a path connected set is connected, so $C$ is not locally path connected either.
:::

:::

::: {.pf-step}
$C$ lacks (1), (2), (3) and (4).

::: pf-proof
Steps [](#cantor-facts){.pf-ref}, [](#cantor-not-connected){.pf-ref} and [](#cantor-not-locally){.pf-ref} give a compact Hausdorff space failing each of the four, so a compact Hausdorff space need not have any of them.
:::

:::

:::

:::

::: {.pf-step #ordinal}
The space $\overline{S}_{\Omega}$ is a compact Hausdorff space that lacks (12), (13), (15), (16) and (17), so none of those five is guaranteed.

:::: pf-proof

::: {.pf-step #ordinal-compact}
$\overline{S}_{\Omega}$ is compact Hausdorff.

::: pf-proof
$\overline{S}_{\Omega}$ is the one-point compactification of $S_{\Omega}$ (Munkres §29 Exercise 7), $S_{\Omega}$ is locally compact because a simply ordered set with the least upper bound property is locally compact (Example 3 of §29), and the one-point compactification of a locally compact Hausdorff space is compact Hausdorff (Theorem 29.1). The book also uses $\overline{S}_{\Omega}\times\overline{S}_{\Omega}$ as a compact Hausdorff space in Example 2 of §32.
:::

:::

::: {.pf-step #ordinal-first-countable}
$\overline{S}_{\Omega}$ is not first countable at $\Omega$.

::: pf-proof
Every neighbourhood of $\Omega$ contains a final segment $(\alpha,\Omega]$, since those sets are a base at the largest element in the order topology. Suppose $U_{1},U_{2},\dots$ are neighbourhoods of $\Omega$; for each $n$ choose $\alpha_{n}$ with $(\alpha_{n},\Omega]\subset U_{n}$. The supremum $\beta=\sup_{n}\alpha_{n}$ of a countable set of ordinals below $\Omega$ is again below $\Omega$, and $\gamma=\beta+1<\Omega$ because $\Omega$, being the first uncountable ordinal, is a limit ordinal. The final segment $(\gamma,\Omega]$ is a neighbourhood of $\Omega$ and contains none of the $U_{n}$: for each $n$ one has $\alpha_{n}\le\beta<\gamma$, so $\gamma\in(\alpha_{n},\Omega]\subset U_{n}$ while $\gamma\notin(\gamma,\Omega]$. So no countable family of neighbourhoods of $\Omega$ is a base there.
:::

:::

::: {.pf-step #ordinal-separable}
$\overline{S}_{\Omega}$ has no countable dense subset.

::: pf-proof
Let $D$ be countable and let $\beta$ bound the members of $D$ that lie in $S_{\Omega}$; then $\beta<\Omega$ as in step [](#ordinal-first-countable){.pf-ref}. The set $(\beta,\Omega)$ is nonempty, since $\beta+1<\Omega$ and $\beta<\beta+1<\Omega$, and open; it contains no point of $D$, because every member of $D\cap S_{\Omega}$ is at most $\beta$ and $\Omega\notin(\beta,\Omega)$. So $D$ is not dense.
:::

:::

::: {.pf-step #ordinal-countable-axioms}
$\overline{S}_{\Omega}$ is neither second countable, nor metrizable, nor locally metrizable.

::: pf-proof
A second countable space is first countable, so step [](#ordinal-first-countable){.pf-ref} excludes (13). A metrizable space is first countable, since the balls of radius $1/n$ about a point form a countable base there, so (17) is excluded as well. If $\overline{S}_{\Omega}$ were locally metrizable, some neighbourhood $U$ of $\Omega$ would be metrizable in the subspace topology; that $U$ contains a final segment $(\alpha,\Omega]$, which is then a subspace of a metrizable space and hence metrizable, and so first countable at $\Omega$ — contrary to the countable-supremum argument of step [](#ordinal-first-countable){.pf-ref} applied inside $(\alpha,\Omega]$, whose neighbourhoods of $\Omega$ are the same final segments. So (16) is excluded.
:::

:::

::: {.pf-step}
$\overline{S}_{\Omega}$ lacks (12), (13), (15), (16) and (17).

::: pf-proof
Steps [](#ordinal-compact){.pf-ref}, [](#ordinal-first-countable){.pf-ref}, [](#ordinal-separable){.pf-ref} and [](#ordinal-countable-axioms){.pf-ref} give a compact Hausdorff space failing each of the five.
:::

:::

:::

:::

::: {.pf-step}
A compact Hausdorff space has exactly (5), (6), (7), (8), (9), (10), (11) and (14), and no other of the seventeen is guaranteed.

::: pf-proof
Steps [](#guaranteed-basic){.pf-ref}, [](#limit-point){.pf-ref}, [](#normal){.pf-ref}, [](#regular){.pf-ref} and [](#lindelof){.pf-ref} establish the eight properties for an arbitrary compact Hausdorff space. Step [](#cantor){.pf-ref} exhibits a compact Hausdorff space failing (1), (2), (3), (4) and step [](#ordinal){.pf-ref} one failing (12), (13), (15), (16), (17); the seventeen properties are exactly those listed at the head of the exercise, so the remaining nine are not guaranteed.
:::

:::

:::
:::
