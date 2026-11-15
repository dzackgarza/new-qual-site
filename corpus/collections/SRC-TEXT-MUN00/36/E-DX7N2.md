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

---

::: {.exercise}

Consider the seventeen properties listed in Exercise 1 of the Supplementary Exercises (Review of the Basics).

Which of these properties are preserved by continuous maps?
:::

::: {.solution}
Exactly the following five properties of the list are preserved by continuous maps:
$$
\boxed{(1),\ (2),\ (5),\ (14),\ (15).}
$$
That is: connectedness, path connectedness, compactness, Lindelöfness, and the existence of a countable dense subset. None of the other twelve is preserved, and a witness is given for each below, limit point compactness among them.

**The five positive entries.**
(1) The continuous image of a connected space is connected, Theorem 23.5.
(2) The continuous image of a path connected space is path connected: if $g: X \to Y$ is continuous and $f: [0,1] \to X$ is a path from $x$ to $x'$, then $g \circ f$ is a path from $g(x)$ to $g(x')$. This is the remark after Example 5 of §24.
(5) The continuous image of a compact space is compact, Theorem 26.5.
(14) If $f: X \to Y$ is continuous and $X$ is Lindelöf, pull an open cover of $f(X)$ back to $X$, take a countable subcover, and push it forward: $f(X)$ is Lindelöf.
(15) If $D \subseteq X$ is a countable dense subset then $f(D)$ is a countable dense subset of $f(X)$, since $f(\bar D) \subseteq \overline{f(D)}$.

**The twelve negative entries.** Each witness is a continuous surjection whose domain has the property and whose image does not. Except in entry (6) the domain is a discrete space, which is the finest topology on its underlying set, so every map out of it is continuous; where the target carries a different underlying set the map is a bijection, and one exists because the two sets have the same cardinality. Discreteness gives Hausdorffness, regularity, normality, first countability, local compactness, local connectedness, local path connectedness and local metrizability, so the domain is never the obstruction. The targets are spaces of this chapter.

- (6) Limit point compact: the projection $\ZZ_+ \times Y \to \ZZ_+$, $(n, y) \mapsto n$, where $Y$ is the two-point space whose only open sets are $Y$ and $\varnothing$. That product with the product topology is limit point compact and not compact, Example 1 of §28, and every nonempty subset of it has a limit point. The map is continuous, the preimage of $\{n\}$ being the open set $\{n\} \times Y$, and it is onto; the target is $\ZZ_+$ with the discrete topology, which is not limit point compact, its infinite subsets having no limit point, every singleton being open. Munkres' Exercise 28.3(a) asks whether a continuous image of a limit point compact space is limit point compact, and this is a negative answer to it.

- (3) Locally connected: a bijection from $\NN$ with the discrete topology onto $\QQ$ with its usual topology, which exists because $\NN$ and $\QQ$ are both countably infinite. The rationals are neither connected nor locally connected, Example 3 of §25. The same map refutes (4) local path connectedness, a path connected neighbourhood being connected.
- (7) Locally compact Hausdorff: the same bijection onto $\QQ$. The rationals are not locally compact, Example 1 of §29, though $\QQ$ is Hausdorff.
- (8) Hausdorff: the identity from $\NN$ with the discrete topology onto $\NN$ with the finite complement topology. Any two nonempty open sets of that topology meet, since their complements are finite, so the space is not Hausdorff.
- (9) Regular: the identity from $\RR$ with the discrete topology onto $\RR_K$. The space $\RR_K$ is Hausdorff and not regular, Example 1 of §31.
- (10) Completely regular: the same map onto $\RR_K$. A completely regular space is regular, since the preimages of $[0,\frac{1}{2})$ and $(\frac{1}{2},1]$ under a separating function are disjoint open sets, so $\RR_K$ is not completely regular either.
- (11) Normal: a bijection from $\RR$ with the discrete topology onto the Sorgenfrey plane $\RR_\ell^2$, which exists because both sets have the cardinality of the continuum, $\abs{\RR_\ell^2} = \abs{\RR^2} = \abs{\RR}$. The Sorgenfrey plane is not normal, Example 3 of §31.
- (12) First countable: the identity from $\RR$ with its usual topology onto $\RR$ with the finite complement topology, in which the open sets are $\varnothing$ and the sets with finite complement. That identity is continuous, the closed sets of the target being finite and hence closed in the domain, and it is onto. The target is not first countable: given countably many open neighbourhoods $U_n = \RR - F_n$ of a point $x$, a local base being extractable from the open sets, the set $F = \bigcup_n F_n$ is countable, so there is a point $y \neq x$ outside $F$; then $\RR - \theset{y}$ is a neighbourhood of $x$, its complement being a singleton, and it contains none of the $U_n$, since $y \in U_n$ for every $n$ and $y \notin \RR - \theset{y}$. So no countable family of neighbourhoods of $x$ is a local base.
- (13) Second countable: the same map onto $\RR$ with the finite complement topology. That space has no countable basis: were $\theset{B_n}$ one, each $B_n$ would have finite complement, so $\bigcup_n (\RR - B_n)$ would be countable and there would be a point $y$ outside it, that is, $y \in B_n$ for every $n$; then $\RR - \theset{y}$ is a nonempty open set containing no $B_n$, a contradiction. This also follows from (12), a second countable space being first countable.
- (16) Locally metrizable: the identity from $\RR$ with the discrete topology onto $\RR_\ell$. The Sorgenfrey line is regular and Lindelöf, Examples 2 of §31 and 3 of §30, so by Exercise 34.8 it would be metrizable if it were locally metrizable, and it is not metrizable, Exercise 30.6.
- (17) Metrizable: the same map onto $\RR_\ell$, which is not metrizable, Exercise 30.6.

A remark on the device. A finer topology inherits from a coarser one its closed sets, hence Hausdorffness, regularity and normality; that is why the domain of all the witnesses above but the one for (6) can be taken discrete, which is the finest topology on a set. It inherits neither countability axiom, nor compactness, nor local compactness, so a witness for one of those needs either a discrete domain, out of which every map is continuous, which is what entries (8) to (11) use, or a target whose topology is contained in one the set already carries, which is what (12) and (13) use. There that target cannot be the co-countable topology: $\RR - \theset{1/n \mid n \in \ZZ_+}$ is co-countable, and it is not open in $\RR$, its complement accumulating at $0$, so the identity from the usual topology onto the co-countable one is not continuous. The finite complement topology is contained in the usual one, its closed sets being finite.
:::
