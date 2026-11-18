---
schema: qual/card@1
id: E-DX7N2
kind: problem
title: The seventeen basic properties under continuous maps
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Supplementary Exercises: Review of the
    Basics, Exercise 6, printed p. 229, with Theorem 23.5, the remark after Example 5 of Section 24,
    Theorem 26.5, Exercise 28.3(a), Exercise 30.11 and one witness for each of the eleven properties
    that fail. No published solution was located (search recorded on E-PWXIV and in the
    COMPLAINTS.md entry). What was corrected: the eleven witnesses are now written out. An earlier
    revision said only that "quotient maps give failures of Hausdorffness, regularity, normality, the
    countability axioms, and metrizability", and named as the witness for the countability axioms and
    for metrizability the quotient of the disjoint union of countably many circles "onto the Hawaiian
    earring". That is wrong on three counts. The map described is not a quotient map: it is a
    continuous bijection from a countable disjoint union of circles onto the earring, and for a
    continuous bijection the quotient topology on the target is its own topology exactly when the
    bijection is a homeomorphism, which this one is not -- the image of a small neighbourhood of a
    base point is an arc of one circle, and no open set of the earring containing the common point is
    that. The earring itself is first countable, being a subspace of R^2, so it cannot witness the
    failure of either countability axiom. And the space which fails first countability is the wedge,
    the quotient of the disjoint union which identifies all the base points, which is not the
    earring. Each failure is now carried by an explicit witness of the form "identity from a finer
    topology", which needs no quotient.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published answer key to the Review of the Basics and found
    none (issue #144). This exercise was searched for under its own content: Math StackExchange,
    site math, `/search/excerpts` with "which properties are preserved by continuous maps",
    "properties preserved by continuous maps Munkres list", "review of the basics Munkres
    supplementary exercises" and "seventeen properties", and `/search/advanced` with title
    "Munkres" over the tag general-topology, whose 623 questions include none on the column of
    properties preserved by continuous maps. dbFin's chapter-4 supplementary page links to no
    problem page; the twelve GitHub repositories named in the COMPLAINTS.md entry for §30--§36
    hold no Chapter 4 supplementary content; the web searches for the table answers returned
    nothing. The AoPS blog that holds an answer key was not read: it answers an automated request
    with a Cloudflare human check, which is not worked around. The card's table is its own work,
    re-derived against Munkres' theorems as its earlier note records, and this pass did not re-read
    it; the search is recorded in the COMPLAINTS.md entry for §30--§36 with every query.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Compared with the published answer key by cinnamon_e, "Topology by Munkres Chapter 4 | Day 13"
    (AoPS blog shooting star, 2025-09-05,
    https://artofproblemsolving.com/community/c3401823h3644066, text at
    tmp/sources/aops-shooting-star-munkres-ch4-day13.md), which answers Exercise 6 with the
    properties 1-2, 5 and 14-15. The card listed property 6, limit point compactness, as preserved
    as well, citing Exercise 28.3(a); that exercise asks whether a continuous image of a limit
    point compact space is limit point compact, and the answer is no, so the key is right and the
    card is corrected: the preserved properties are 1, 2, 5, 14 and 15, and the twelve others have
    witnesses. The proof the card carried for property 6 chose one point of each fibre over a
    countably infinite subset and took a limit point x of them, concluding that f(x) is a limit
    point of the image; that does not follow, the value f(x) itself possibly being one of the
    chosen points. The witness now given for 6 is Example 1 of §28, the product of the positive
    integers with the two-point space whose only open sets are itself and the empty set, which is
    limit point compact, together with the projection onto the discrete positive integers, which is
    continuous and surjective onto a space with no limit points at all. The other eleven negative
    entries stand as the earlier note records them, and the key agrees with all of them and with
    properties 1, 2, 5, 14 and 15 among the positives.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Three defects of the witnesses, reported by a reader of this card and checked against the book
    before changing anything. (a) Entries (12) and (13) used the co-countable topology on R as the
    target, calling that topology coarser than the usual one, and so they used an identity map that is
    not continuous: the set R - {1/n : n in Z_+} is co-countable, and it is not open in R, its
    complement accumulating at 0. The target is now R with the finite complement topology, whose
    closed sets are the finite ones and hence closed in R, so the identity from usual R is
    continuous; the two negative entries are reproved there, and the closing remark now says why the
    finite complement topology is the one that works and the co-countable one is not. (b) Entries
    (3), (7) and (11) said "the identity from N (discrete) onto Q" and "from R (discrete) onto
    R_l^2", which are not identity maps, the two sides being different sets; the maps are now named,
    a bijection out of the discrete space, which exists because |N| = |Q| and |R| = |R_l^2| =
    |R^2|, and out of a discrete space every map is continuous. (c) The paragraph introducing the
    twelve negative entries said only that the identity out of a discrete domain is continuous, which
    is false of a bijection between different sets as stated; it now says that every map out of a
    discrete space is continuous and that the maps onto a different underlying set are bijections.
    The five positive entries, the other eight negative ones and the answer to the exercise are
    unchanged, and were not re-read in this pass.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    Four defects reported by a reader of this card, each checked against the book before changing
    anything. (a) The paragraph introducing the twelve negative entries said that except in entry (6)
    the domain of each witness is a discrete space; entries (12) and (13) had the usual R as domain.
    The sentence now names (6) and (13) instead, and entry (12), whose target is R with the finite
    complement topology, takes R discrete for its domain, discreteness giving first countability. (b)
    The closing remark said that a finer topology inherits Hausdorffness, regularity and normality
    from a coarser one. That is false for the second and the third: R_K is strictly finer than R,
    Lemma 13.4 (printed p. 82), and is not regular, Example 1 of §31 (printed p. 197), which is this
    card's own witness for entry (9). The remark now states what the device uses -- that every map out
    of a discrete space is continuous and that a discrete space has properties 3, 4, 7-12, 16 and 17,
    and 13 as well when it is countable -- and says that it has the other seven only for small sets.
    (c) The same remark said that a witness for a countability axiom, for compactness or for local
    compactness needs a discrete domain, "which is what entries (8) to (11) use"; entries (8) to (11)
    are the separation properties, not those three, and the clause is gone with (b). The rejection of
    the co-countable topology as a target is kept, and the remark now also says why a discrete space is
    second countable only when it is countable. (d) The statement said
    the seventeen properties are "listed in Exercise 1"; Munkres prints the list at the head of the
    Supplementary Exercises, before Exercise 1, on printed p. 228, and Exercise 6 is printed on
    p. 229. The five positive entries and the other ten negative ones were re-read and kept.

---

::: {.exercise}

Consider the seventeen properties listed at the head of the Supplementary Exercises (Review of the Basics), printed p. 228.

Which of these properties are preserved by continuous maps?
:::

::: {.solution}

The survey is the card's own; no published solution of supplementary Exercise 3 of §36 was located, and the sets searched are recorded in the audit trail. The properties are numbered as in Exercise 1 of the Supplementary Exercises (Review of the Basics), printed p. 228.

::: pf

::: {.pf-step #positive}
The five properties (1), (2), (5), (14) and (15) are preserved by continuous maps.

::: pf-proof

::: {.pf-step #pos-1}
(1) Connectedness: the continuous image of a connected space is connected (Theorem 23.5).
:::

::: {.pf-step #pos-2}
(2) Path connectedness: if $g:X\to Y$ is continuous and $f:[0,1]\to X$ is a path from $x$ to $x'$, then $g\circ f$ is a path from $g(x)$ to $g(x')$ (the remark after Example 5 of §24).
:::

::: {.pf-step #pos-5}
(5) Compactness: the continuous image of a compact space is compact (Theorem 26.5).
:::

::: {.pf-step #pos-14}
(14) Lindelöfness: if $f:X\to Y$ is continuous and $X$ is Lindelöf, pull an open cover of $f(X)$ back to $X$, take a countable subcover and push it forward.
:::

::: {.pf-step #pos-15}
(15) Countable dense subset: if $D\subset X$ is countable and dense then $f(D)$ is countable and dense in $f(X)$, since $f(\overline{D})\subset\overline{f(D)}$ for continuous $f$.
:::

:::

:::

::: {.pf-step #negative}
Each of the other twelve properties fails to be preserved: for each there is a continuous surjection whose domain has the property and whose image does not.

::: pf-proof

::: {.pf-step #neg-6}
(6) Limit point compactness: the projection $\ZZ_{+}\times Y\to\ZZ_{+}$, $(n,y)\mapsto n$, where $Y$ is the two-point space whose only open sets are $Y$ and $\varnothing$.

::: pf-proof
The space $\ZZ_{+}\times Y$ is limit point compact and not compact (Example 1 of §28), and every infinite subset of it has a limit point. The projection is continuous, the preimage of $\{n\}$ being the open set $\{n\}\times Y$, and it is onto. The target $\ZZ_{+}$ is discrete, hence not limit point compact: every singleton is open, so an infinite subset has no limit point. This answers Exercise 28.3(a) in the negative.
:::

:::

::: {.pf-step #neg-3}
(3) Local connectedness and (4) local path connectedness: a bijection from $\NN$ with its discrete topology onto $\QQ$ with its usual topology.

::: pf-proof
$\NN$ and $\QQ$ are both countably infinite, so such a bijection exists, and it is continuous because every subset of a discrete space is open. The rationals are not locally connected (Example 3 of §25). A locally path connected space is locally connected, so $\QQ$ is not locally path connected either and one map refutes both entries.
:::

:::

::: {.pf-step #neg-7}
(7) Local compactness: the same bijection onto $\QQ$.

::: pf-proof
It is continuous as above; $\QQ$ is not locally compact (Example 1 of §29), though it is Hausdorff.
:::

:::

::: {.pf-step #neg-8}
(8) Hausdorffness: the identity from $\NN$ with the discrete topology onto $\NN$ with the finite complement topology.

::: pf-proof
Any two nonempty open sets of the finite complement topology meet, their complements being finite; so that space is not Hausdorff, while the identity out of a discrete space is continuous.
:::

:::

::: {.pf-step #neg-9}
(9) Regularity and (10) complete regularity: the identity from $\RR$ with the discrete topology onto $\RR_{K}$.

::: pf-proof
The identity is continuous, and $\RR_{K}$ is Hausdorff and not regular (Example 1 of §31). A completely regular space is regular, since the preimages of $[0,\tfrac12)$ and $(\tfrac12,1]$ under a separating function are disjoint open sets around a point and a closed set not containing it; so $\RR_{K}$ is not completely regular either.
:::

:::

::: {.pf-step #neg-11}
(11) Normality: a bijection from $\RR$ with the discrete topology onto the Sorgenfrey plane $\RR_{\ell}^{2}$.

::: pf-proof
Both sets have the cardinality of the continuum, since $\abs{\RR_{\ell}^{2}}=\abs{\RR^{2}}=\abs{\RR}$, so such a bijection exists and is continuous out of a discrete space. The Sorgenfrey plane is not normal (Example 3 of §31).
:::

:::

::: {.pf-step #neg-12}
(12) First countability: the identity from $\RR$ with the discrete topology onto $\RR$ with the finite complement topology.

::: pf-proof
The identity is continuous and onto. The target is not first countable: given countably many open neighbourhoods $U_{n}=\RR\setminus F_{n}$ of $x$, the set $F=\bigcup_{n}F_{n}$ is countable, so there is $y\ne x$ outside $F$; then $\RR\setminus\{y\}$ is a neighbourhood of $x$ containing none of the $U_{n}$, since $y\in U_{n}$ for every $n$.
:::

:::

::: {.pf-step #neg-13}
(13) Second countability: the identity from $\RR$ with its usual topology onto $\RR$ with the finite complement topology.

::: pf-proof
The finite complement topology is contained in the usual one, since finite sets are closed in $\RR$, so the identity is continuous. A discrete domain is not available here: a discrete space is second countable only if it is countable, while the target's underlying set is $\RR$. And the target has no countable basis: if $\{B_{n}\}$ were one, each nonempty $B_{n}$ would have finite complement, so the union of the sets $\RR\setminus B_{n}$ over the nonempty $B_{n}$ would be countable, giving a point $y$ with $y\in B_{n}$ for every nonempty $n$; then $\RR\setminus\{y\}$ is a nonempty open set containing none of them.
:::

:::

::: {.pf-step #neg-16}
(16) Local metrizability and (17) metrizability: the identity from $\RR$ with the discrete topology onto the Sorgenfrey line $\RR_{\ell}$.

::: pf-proof
The identity is continuous and onto. The Sorgenfrey line is regular and Lindelöf (Examples 2 of §31 and 3 of §30), so by Exercise 34.8 a locally metrizable such space would be metrizable; but $\RR_{\ell}$ is not metrizable (Exercise 30.6). So it is neither locally metrizable nor metrizable, and one map refutes both entries.
:::

:::

::: {.pf-qed}
For the twelve negative entries, the witnesses above are continuous surjections whose domains have the property and whose images do not, so no one of those properties is preserved. For the five positive entries, step [](#positive){.pf-ref} gives preservation. Hence exactly
$$
\boxed{(1),\ (2),\ (5),\ (14),\ (15)}
$$
are preserved by continuous maps.
:::

:::

:::

:::
:::
