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
---

::: {.exercise}

After studying Chapters 6 and 7, repeat Exercises 1–6 of the Supplementary Exercises (Review of the Basics) for the following properties:

(18) paracompact

(19) topologically complete

You should be able to answer all but one of the 340 questions involved in Exercises 1–6, and all but one of the 40 questions involved in Exercise 7. These two are unsolved; see the remark in Exercise 5 of §32.
:::

::: {.solution}
Exercises 1–6 classified properties (1)–(17). The tables below supply properties (18) paracompact and (19) topologically complete in the same order, and name for each entry the result that decides it. “Topologically complete” means that some metric for the topology makes the space complete, §43 Exercise 6; such a metric is a metric for the topology, so a topologically complete space is metrizable.

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

**Paracompactness, column one.** Every compact space is paracompact, so (b) and (d) are paracompact, the ordered square being compact by Theorem 27.1. Every metrizable space is paracompact, Theorem 41.4, so (g) and (h) are, by Theorem 20.5 and by the uniform metric. Every regular Lindelöf space is paracompact, Theorem 41.5, so (e) is, by Example 3 of §30 and Example 2 of §31. A paracompact Hausdorff space is normal, Theorem 41.1, so the three spaces already known to be nonnormal are not paracompact: (c) by Example 2 of §32, (f) by Example 3 of §31, and (j), since an uncountable product of copies of $\RR$ is not normal, Exercise 32.9. The space $\RR_K$ is Hausdorff but not regular, Example 1 of §31, so it is not paracompact by the same theorem, which is (k). That leaves (a): $S_\Omega$ is not paracompact, and there are two routes in the book. The product of a paracompact space with the compact $\overline S_\Omega$ would be paracompact, Exercise 41.2(a), but it is not, Exercise 41.2(b), the space $S_\Omega\times\overline S_\Omega$ being nonnormal. Alternatively $S_\Omega$ is countably compact and not compact, and a countably compact paracompact space is compact: a locally finite family of nonempty open sets in a countably compact space is finite, so a locally finite open refinement of an open cover is already a finite subcover. The box entry is the open question recorded in Example 5 of §41, that is, the same one as the normality entry of Exercise 1(i).

**Topological completeness, column two.** A topologically complete space is metrizable, so every space known not to be metrizable is out: (a) and (b) by Example 3 of §28, (c) because it contains the closed subspace $S_\Omega\times\{\Omega\}$ and metrizability passes to subspaces, Exercise 21.1, (d) and (e) by Exercise 30.6, (f) because it contains the closed subspace $\RR_\ell\times\{0\}$, (i) because the box topology on $\RR^\omega$ is not first countable, (j) by Example 2 of §21, and (k) because a metrizable space is regular, Theorem 32.2, while $\RR_K$ is not. That leaves (g) and (h), which are the two positive entries. For (g): $\RR$ is topologically complete, and a countable product of topologically complete spaces is topologically complete in the product topology, Exercise 43.6(b). For (h): the uniform metric $\bar\rho$ is complete on $\RR^\omega$, a $\bar\rho$-Cauchy sequence being uniformly Cauchy in every coordinate and hence convergent coordinatewise, and uniformly so.

**Exercises 2–6 for the two properties.** The answers are these, and each is decided by the same results.

| Operation or class | Paracompact (18) | Topologically complete (19) |
| --- | --- | --- |
| Arbitrary subspace | No | No |
| Closed subspace | Yes | Yes |
| Open subspace | No | Yes |
| Finite product | No | Yes |
| Countable product | No | Yes |
| Arbitrary product | No | No |
| Continuous image | No | No |
| Every metric space | Yes | No |
| Every compact Hausdorff space | Yes | No |

Paracompactness is not hereditary: $S_\Omega$ is a subspace of the compact, hence paracompact, $\overline S_\Omega$ and is not paracompact. It passes to closed subspaces (§41) and not to open ones, $S_\Omega$ again being open in $\overline S_\Omega$. It is not preserved by finite products, $\RR_\ell\times\RR_\ell$ being paracompact in each factor, Example 4 of §41, and not paracompact; padding a finite counterexample with one-point factors gives the countable and arbitrary columns, and the uncountable product $\RR^J$ is not paracompact for a second reason, being Hausdorff and nonnormal, Example 6 of §41. Continuous images fail by Exercise 41.4(b). Every metrizable space is paracompact, Theorem 41.4, and every compact space is paracompact, so the last two rows are Yes.

Topological completeness passes to closed subspaces, Exercise 43.6(a), to open subspaces, Exercise 43.6(c), and to countable products in the product topology, Exercise 43.6(b), which also covers finite products after padding with one-point spaces. It does not pass to arbitrary subspaces: $\QQ$ is a subspace of the complete space $\RR$ and is not topologically complete, since a topologically complete space is a Baire space (the remark at the start of §48) and $\QQ$ is a countable union of nowhere dense singletons. It does not pass to arbitrary products, since $\RR^J$ is not even metrizable for uncountable $J$, Example 2 of §21; and it is not preserved by continuous images, since the identity from a set with the discrete topology onto a non-metrizable space of the same cardinality is continuous, while a discrete space is complete in the discrete metric. The last two rows are No: $\QQ$ is a metric space that is not topologically complete, and $\overline S_\Omega$ is a compact Hausdorff space that is not, being nonmetrizable.
:::
