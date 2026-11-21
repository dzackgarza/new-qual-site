---
schema: qual/card@1
id: E-1CMTE
kind: problem
title: Paracompactness and topological completeness in the basics review
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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
    Basics, Exercise 7, printed p. 229, which asks for properties (18) paracompact and (19)
    topologically complete in Exercises 1-6, with Theorem 41.1, Theorem 41.4, Theorem 41.5, Example 4,
    Example 5 and Example 6 of Section 41, Exercises 41.2 and 41.4, Theorem 42.1, Exercises 43.6,
    Theorem 20.5, Example 2 of Section 21 and Example 3 of Section 28. No published solution was
    located (search recorded on E-PWXIV and in the COMPLAINTS.md entry). Both tables were re-derived
    and every entry now names its deciding result: compact spaces and metrizable spaces are
    paracompact, regular Lindelof spaces are paracompact (so the Sorgenfrey line is and its square is
    not), paracompact Hausdorff spaces are normal (which removes the three nonnormal spaces and the
    nonregular R_K), S_Omega is not paracompact by Exercise 41.2 or by the countably-compact argument,
    and the box entry is the book's open question; topological completeness forces metrizability, so
    it excludes the nine nonmetrizable spaces, and the two positive entries are Exercise 43.6(b) and
    the completeness of the uniform metric. What was corrected: the identity "topologically complete
    means admitting a complete metric, so it forces metrizability" was on the card already, but the
    per-space table gave no reason for any entry and the second table no reason for six of its nine
    rows; the reason "the spaces in (c), (f) and (j) are not normal; R_K is not regular, therefore
    they fail paracompactness" was correct and is now tied to Theorem 41.1. The entries themselves are
    unchanged.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout for a published answer key to the Review of the Basics and found
    none (issue #144). This exercise was searched for under its own content: Math StackExchange,
    site math, `/search/excerpts` with "review of the basics Munkres supplementary exercises",
    "seventeen properties", "hereditary property subspace" and "paracompact topological
    completeness", and `/search/advanced` with title "Munkres" over the tag general-topology,
    whose 623 questions include none on the two added properties; dbFin's chapter-4 supplementary
    page links to no problem page, and its chapter-6 pages carry the theorems the table cites but
    no exercise answers for this supplement. The twelve GitHub repositories named in the
    COMPLAINTS.md entry for §30--§36 hold no Chapter 4 supplementary content; the web searches for
    the table answers returned nothing. The AoPS blog that holds an answer key was not read: it
    answers an automated request with a Cloudflare human check, which is not worked around. The
    card's table is its own work, re-derived against Munkres' theorems as its earlier note records,
    and this pass did not re-read it; the search is recorded in the COMPLAINTS.md entry for
    §30--§36 with every query.

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Read for #169 against the Supplementary Exercises: Review of the Basics, Exercise 7, and the
    numbered results of Chapters 6 and 7, and repaired in two places. (i) "It passes to closed
    subspaces (§41)" is now Theorem 41.2, which reads in the book "Every closed subspace of a
    paracompact space is paracompact". (ii) The sentence introducing the failure of paracompactness
    under finite products said "$\RR_\ell\times\RR_\ell$ being paracompact in each factor",
    which states the opposite of what the argument uses; it now says that each factor $\RR_\ell$
    is paracompact, being regular and Lindel\"of, while the product is not, by Example 4 of §41.
    Everything else was checked and kept. Paracompactness: Theorem 41.1 excludes (c), (f), (j) and
    (k) through nonnormality or nonregularity; Theorem 41.4 gives (g) and (h); Theorem 41.5 gives
    (e); compactness gives (b) and (d); Exercise 41.2(a), that a product of a paracompact space and
    a compact one is paracompact, with part (b), is the first route for (a); and Example 5 of §41
    says in terms that $\RR^\omega$ is paracompact in the product and uniform topologies because it
    is metrizable there and that it is not known whether it is paracompact in the box topology, so
    the "?" of entry (i) is the book's own open question and the pointer to the comment at Exercise
    5 of §32 is the book's. Topological completeness: §43 Exercise 6 is the definition the card
    quotes; metrizability excludes all but (g) and (h); Exercise 43.6(a), (b) and (c) are exactly
    the closed-subspace, countable-product and open-subspace statements the operation table uses;
    and the remark opening §48, that a metrizable space is a Baire space if it is topologically
    complete, is what rules out the rationals as a subspace of $\RR$. Not checked: the card's
    count of the questions is the book's, and no published key to Exercise 7 was searched for here.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with three tables and no numbered step. It is now
    a `pf` with eight steps, the tables carried in the last step, each step holding a `pf-proof`. Cited
    by numbered statement only: Munkres, Topology, §36 Exercise 1's continuation by properties (18) and
    (19), Theorems 20.5, 27.1, 32.2, 41.1, 41.2, 41.4, 41.5, §43 Exercises 6, 43.6(a)--(c), §41
    Exercises 41.2(a), 41.2(b), 41.4(b), Exercise 32.9, Exercise 21.1, Exercise 30.6, Examples 1 and 2
    of §31, Examples 2 and 3 of §21, Example 3 of §28, Examples 3 and 5 of §30, Example 1 of §31,
    Examples 2, 4, 5 and 6 of §41 and the remark opening §48. Checked: that every paracompact "Yes"
    names the theorem giving it, that each "No" names either a theorem excluding the space or a
    nonmetrizability witness for the topological-completeness column, that $S_\Omega$ is countably
    compact but not compact so the alternative argument closes, and that the box entry is the open
    question rather than an answer.

---

::: {.exercise}

After studying Chapters 6 and 7, repeat Exercises 1–6 of the Supplementary Exercises (Review of the Basics) for the following properties:

(18) paracompact

(19) topologically complete

You should be able to answer all but one of the 340 questions involved in Exercises 1–6, and all but one of the 40 questions involved in Exercise 7. These two are unsolved; see the remark in Exercise 5 of §32.
:::

::: {.solution}

Exercises 1--6 of the Supplementary Exercises (Review of the Basics) classify properties (1)--(17) on [[E-CJGFE]]. The steps below supply properties (18) paracompact and (19) topologically complete in the same order, naming for each entry the numbered result that decides it. "Topologically complete" means that some metric for the topology makes the space complete (Munkres §43 Exercise 6); such a metric gives the topology, so a topologically complete space is metrizable. No published key to these exercises was located; the search is recorded on this card's earlier events and in the `COMPLAINTS.md` entry for §30--§36.

::: pf

::: {.pf-step #paracompact-yes}
(18) $S_\Omega\times\{\Omega\}$ aside, the paracompact entries among the spaces of Exercise 1 are (b) $\overline S_\Omega$, (d) the ordered square, (e) $\RR_\ell$, (g) $\RR^\omega$ in the product topology and (h) $\RR^\omega$ in the uniform topology.

::: pf-proof
A compact space is paracompact, so (b) is paracompact as a compact Hausdorff space and (d) is by Theorem 27.1; a metrizable space is paracompact by Theorem 41.4, so (g) is by Theorem 20.5 and (h) by its uniform metric; and a regular Lindelöf space is paracompact by Theorem 41.5, so (e) is, being regular (Example 2 of §31) and Lindelöf (Example 3 of §30).
:::

:::

::: {.pf-step #paracompact-no}
(18) The spaces (c) $S_\Omega\times\overline S_\Omega$, (f) $\RR_\ell^2$, (j) $\RR^{[0,1]}$ and (k) $\RR_K$ are not paracompact.

::: pf-proof
A paracompact Hausdorff space is normal by Theorem 41.1, so each space already known to be nonnormal is excluded: (c) by Example 2 of §32, (f) by Example 3 of §31, and (j) because an uncountable product of copies of $\RR$ is not normal (Exercise 32.9). $\RR_K$ is Hausdorff and not regular (Example 1 of §31), and a paracompact Hausdorff space is regular, so (k) is excluded.
:::

:::

::: {.pf-step #paracompact-a}
(18) $S_\Omega$ is not paracompact, and the box entry (i) is the open question of Example 5 of §41.

::: pf-proof
If $S_\Omega$ were paracompact, then $S_\Omega\times\overline S_\Omega$ would be paracompact by Exercise 41.2(a), since $\overline S_\Omega$ is compact; but it is not, by Exercise 41.2(b). Alternatively $S_\Omega$ is countably compact and not compact, and a countably compact paracompact space is compact: a locally finite family of nonempty open sets in a countably compact space is finite, so a locally finite open refinement of an open cover is itself a finite subcover. The box entry is the question recorded in Example 5 of §41, the same one as the normality entry of Exercise 1(i).
:::

:::

::: {.pf-step #tc-no}
(19) Every space of Exercise 1 other than (g) and (h) fails to be topologically complete.

::: pf-proof
A topologically complete space is metrizable, so each space known not to be metrizable is excluded: (a) and (b) by Example 3 of §28, (c) because it contains the closed subspace $S_\Omega\times\{\Omega\}$ and metrizability passes to subspaces (Exercise 21.1), (d) and (e) by Exercise 30.6, (f) because it contains the closed subspace $\RR_\ell\times\{0\}$, (i) because the box topology on $\RR^\omega$ is not first countable, (j) by Example 2 of §21, and (k) because a metrizable space is regular (Theorem 32.2) while $\RR_K$ is not.
:::

:::

::: {.pf-step #tc-yes}
(19) $\RR^\omega$ in the product topology and in the uniform topology are topologically complete.

::: pf-proof
$\RR$ is topologically complete and a countable product of topologically complete spaces is topologically complete in the product topology (Exercise 43.6(b)), which gives (g). For (h), the uniform metric $\bar\rho$ is complete on $\RR^\omega$: a $\bar\rho$-Cauchy sequence is uniformly Cauchy in every coordinate, hence converges coordinatewise, and uniformly so, so its limit is in $\RR^\omega$ and is the $\bar\rho$-limit.
:::

:::

::: {.pf-step #operations-paracompact}
Exercises 2--6 for property (18): a closed subspace and a finite, countable or arbitrary product of compact or metrizable factors are paracompact; arbitrary and open subspaces, continuous images, and the products of (c), (f) and (j) are not.

::: pf-proof
Paracompactness passes to closed subspaces by Theorem 41.2. It does not pass to open subspaces or arbitrary subspaces, nor to continuous images (Exercise 41.4(b)). A finite product of paracompact spaces need not be paracompact: $\RR_\ell$ is paracompact while $\RR_\ell\times\RR_\ell$ is not (Example 4 of §41), and padding a finite counterexample with one-point factors gives the countable and arbitrary columns; the uncountable product $\RR^J$ also fails for the second reason of being Hausdorff and nonnormal (Example 6 of §41). Every metrizable space is paracompact by Theorem 41.4 and every compact space is paracompact, which are the two positive rows.
:::

:::

::: {.pf-step #operations-tc}
Exercises 2--6 for property (19): it passes to closed and to open subspaces and to finite and countable products, but not to arbitrary subspaces, arbitrary products or continuous images.

::: pf-proof
It passes to closed subspaces by Exercise 43.6(a), to open subspaces by Exercise 43.6(c), and to countable products in the product topology by Exercise 43.6(b), which covers finite products after padding with one-point spaces. It fails for arbitrary subspaces because $\QQ$ is a subspace of the complete space $\RR$ and is not topologically complete, a topologically complete space being a Baire space (the remark opening §48) while $\QQ$ is a countable union of nowhere dense singletons. It fails for arbitrary products because $\RR^J$ is not even metrizable for uncountable $J$ (Example 2 of §21). It fails for continuous images because the identity from a set with the discrete topology onto a non-metrizable space of the same cardinality is continuous and a discrete space is complete in the discrete metric.
:::

:::

::: {.pf-step #tables}
The two tables are:

| Space in Exercise 1 | Paracompact (18) | Topologically complete (19) |
| --- | :---: | :---: |
| (a) $S_\Omega$ | No | No |
| (b) $\overline S_\Omega$ | Yes | No |
| (c) $S_\Omega\times\overline S_\Omega$ | No | No |
| (d) Ordered square | Yes | No |
| (e) $\RR_\ell$ | Yes | No |
| (f) $\RR_\ell^2$ | No | No |
| (g) $\RR^\omega$, product | Yes | Yes |
| (h) $\RR^\omega$, uniform | Yes | Yes |
| (i) $\RR^\omega$, box | ? | No |
| (j) $\RR^{[0,1]}$, product | No | No |
| (k) $\RR_K$ | No | No |

and, for Exercises 2--6, every row is No for (18) except closed subspaces, finite products and countable products, and No for (19) in the rows named in step [#operations-tc]{.pf-ref}.

::: pf-proof
Each entry is the statement of one of steps [#paracompact-yes]{.pf-ref}, [#paracompact-no]{.pf-ref}, [#paracompact-a]{.pf-ref}, [#tc-no]{.pf-ref}, [#tc-yes]{.pf-ref}, [#operations-paracompact]{.pf-ref} and [#operations-tc]{.pf-ref}; the question mark is the open question of Example 5 of §41.
:::

:::

:::

:::
