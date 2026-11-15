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

---

::: {.exercise}

Consider the seventeen properties listed at the head of the Supplementary Exercises (Review of the Basics), printed p. 228.

Which of these properties does a compact Hausdorff space have?
:::

::: {.solution}
Of the properties numbered in Supplementary Exercise 1, every compact Hausdorff space has these eight, and no others are guaranteed:

| Number | Property | Deciding result |
| --- | --- | --- |
| 5 | Compact | Hypothesis |
| 6 | Limit point compact | Compactness implies limit point compactness, Theorem 28.1 |
| 7 | Locally compact Hausdorff | The whole space is a compact subspace containing a neighbourhood of each point, which is the definition of local compactness in §29; Hausdorffness is the hypothesis |
| 8 | Hausdorff | Hypothesis |
| 9 | Regular | The space is normal by Theorem 32.3, and a normal space is regular (§31) |
| 10 | Completely regular | The Urysohn lemma, Theorem 33.1, applies to a normal space, and a normal space is completely regular (§33) |
| 11 | Normal | Theorem 32.3 |
| 14 | Lindelöf | Every open cover has a finite subcover, so it has a countable one (§30) |

The remaining nine properties are not guaranteed, and two spaces exclude all of them.

**The Cantor set** $C \subset [0,1]$, Exercise 27.6, is compact Hausdorff. It is totally disconnected, Exercise 27.6(a), and has no isolated points, Exercise 27.6(d), so no point of it has a connected neighbourhood: a connected neighbourhood of $x$ would be a connected set containing $x$, hence the point $x$ itself, and $\{x\}$ is not open. This excludes connectedness, path connectedness, local connectedness and local path connectedness — properties 1 to 4. A path connected space is connected and a locally path connected space is locally connected, so the two path entries follow as well.

**The ordinal interval** $\overline S_\Omega = [0,\omega_1]$ is compact Hausdorff: it is the one-point compactification of $S_\Omega$, Exercise 29.7 with Theorem 29.1. It is not first countable at $\omega_1$: every neighbourhood of $\omega_1$ contains a final segment $(\alpha,\omega_1]$, the supremum of countably many ordinals below $\omega_1$ is again below $\omega_1$, and the final segment above that supremum contains none of countably many such neighbourhoods, so no countable family of them is a local base. It is not separable: a countable set of ordinals below $\omega_1$ is bounded, so if $D$ is countable and $\beta$ bounds the ordinals of $D$ that lie below $\omega_1$, then $\beta < \omega_1$ and the nonempty open interval $(\beta, \omega_1)$ misses $D$, the point $\omega_1$ itself not lying in it; so $D$ is not dense. A metrizable space is first countable, the balls $B(x,1/n)$ forming a countable basis at $x$ (§21), and a second countable space is first countable, its basis elements containing a point forming a countable basis there (§30). Since $\overline S_\Omega$ has no countable basis at $\omega_1$, it is neither second countable nor metrizable, which is properties 13 and 17. It is not locally metrizable either: a neighbourhood of $\omega_1$ contains a final segment $(\alpha,\omega_1]$, which is not first countable at $\omega_1$ and so is not metrizable, property 16. That leaves no unaccounted property, and the count is eight guaranteed and nine not.
:::
