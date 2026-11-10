---
schema: qual/card@1
id: E-RIGIX
kind: problem
title: Complete normality of standard spaces and constructions
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Checked against Munkres, Topology (2000), Section 32 Exercise 7, printed pp. 205-206, with the
    answers of "Doug's World", "Munkres - Topology - Chapter 4 Solutions" (30 August 2017; the file
    names no author), Problem 32.7, printed p. 7 (tmp/sources/munkres-solutions-dougsworld-ch4.pdf),
    which are Yes, No, Yes, Yes, No, Yes, Yes. Corrections: (b) is now the source's own example --
    S_Omega and S_bar_Omega are completely normal by Theorem 32.4, while S_Omega x S_bar_Omega is not
    normal by Example 2 of Section 32 (printed p. 203) -- instead of the Sorgenfrey plane, which
    would use part (g) of the same exercise; (c) was a citation to "linearly ordered topological
    spaces are hereditarily normal" with no argument, and now proves that a subspace of a
    well-ordered set carries the order topology of its induced well-order and applies Theorem 32.4
    (printed p. 202); (e) was quoted from Stone's theorem on R^J for uncountable J, which needs
    Tychonoff for the compactness of [0,1]^J, and is now the book's own witness
    S_bar_Omega x S_bar_Omega, compact by Theorem 26.7 (printed p. 167) and Hausdorff by Theorem
    19.4 (printed p. 116), containing the non-normal subspace S_Omega x S_bar_Omega. The source's
    own answers to (c) and (e) are the bare sentences "Remember that in fact every set in the order
    topology is completely normal!" and "No, but I haven't been able to find a counterexample I
    understand", so no complete published argument exists for those two parts; the search is
    recorded in the COMPLAINTS.md entry for this batch.
---

::: {.exercise}

Which of the following spaces are completely normal?
Justify your answers.

(a) A subspace of a completely normal space.

(b) The product of two completely normal spaces.

(c) A well-ordered set in the order topology.

(d) A metrizable space.

(e) A compact Hausdorff space.

(f) A regular space with a countable basis.

(g) The space $\RR_\ell$.
:::

::: {.solution}
(a) Yes. Every subspace of a subspace of a completely normal space is a subspace of the original space, hence normal.

(b) No. A well-ordered set in the order topology is normal by Theorem 32.4, and every subspace of a well-ordered set is again a well-ordered set in its order topology, as part (c) below spells out, so $S_\Omega$ and $\overline{S}_\Omega$ are completely normal; but their product $S_\Omega\times\overline{S}_\Omega$ is not normal, as Example 2 of §32 shows. The same example shows that the product of two normal spaces need not be normal.

(c) Yes. Let $W$ be a well-ordered set and $A\subseteq W$ a subspace with the induced order. The order topology of $A$ coincides with the subspace topology: a ray of $A$ is the trace of a ray of $W$, an interval of $A$ is the trace of an interval of $W$, and conversely a basis element of $W$ meets $A$ in a ray or an interval of $A$. So $A$ is a well-ordered set in the order topology and is normal by Theorem 32.4. Hence every subspace of $W$ is normal.

(d) Yes. Every subspace of a metrizable space is metrizable, hence normal.

(e) No. The space $\overline{S}_\Omega\times\overline{S}_\Omega$ is compact (Theorem 26.7) and Hausdorff (Theorem 19.4), hence normal (Theorem 32.3); but it contains the subspace $S_\Omega\times\overline{S}_\Omega$, which is not normal by Example 2 of §32. Complete normality of the product would make that subspace normal, so the product is not completely normal.

(f) Yes. Every subspace of a regular second-countable space is regular and second countable. Second-countable spaces are Lindelöf, so every subspace is regular Lindelöf and hence normal by the preceding exercise. Thus the original space is completely normal.

(g) Yes. First, every subspace $A\subset\RR_\ell$ is Lindelöf. Given an open cover of $A$, refine it so that for each $x\in A$ one chosen member contains a basic interval $[x,b_x)\cap A$. The ordinary open intervals $(x,b_x)$ have union $O\subset\RR$. Since the usual real line is second countable, $O$ is Lindelöf, so countably many of these ordinary intervals cover $O$. The exceptional set
$$
D=A\setminus O
$$
is countable: if $d<d'$ are in $D$, then $d'\notin(d,b_d)$, hence $d'\ge b_d$; therefore the intervals $(d,b_d)$, $d\in D$, are pairwise disjoint, and assigning a rational point to each gives an injection $D\hookrightarrow\QQ$. Adding one chosen cover member for each point of the countable set $D$ gives a countable subcover of $A$.

The Sorgenfrey line is regular, and regularity is hereditary to subspaces. Hence every subspace is regular Lindelöf and therefore normal by the preceding exercise. Thus $\RR_\ell$ is completely normal.
:::
