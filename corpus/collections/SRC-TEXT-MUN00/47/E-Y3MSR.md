---
schema: qual/card@1
id: E-Y3MSR
kind: problem
title: Compact closures in the topology of compact convergence
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 2 (printed p. 293) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against the book's Theorem 46.7, Theorem 29.2,
    Lemma 45.2, Theorem 45.4, Theorem 37.3 and Lemma 46.4. What was corrected: the "only if" direction had
    proved equicontinuity with nets, a technique the book does not use and does not define; it now restricts
    the compact family to a compact neighbourhood K of the point (Theorem 29.2), where compact convergence is
    the uniform topology (Theorem 46.7), and applies Lemma 45.2 to get equicontinuity on K, hence at the point.
    The "converse" embeds C(X,R^n) by restriction into the product over the compact subspaces of X, applies
    Ascoli (Theorem 45.4) in each factor, Tychonoff (Theorem 37.3) to the product of the closures, and Lemma
    46.4 for the continuity of the compatible function, with every point of X having a compact neighbourhood by
    Theorem 29.2. The last sentence records that the square and euclidean metrics on R^n are uniformly
    equivalent, so neither boundedness nor equicontinuity depends on which is used.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 2 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass for compact closure under pointwise boundedness and equicontinuity,
    recorded in the COMPLAINTS.md entry for §43--§50, returned nothing on the theorem. The card
    keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct in
    outline and in its citations (Theorem 29.2 for compact neighbourhoods, Theorem 46.7 for the
    topology of compact convergence, Lemma 45.2 for totally bounded families being
    equicontinuous, Ascoli and Tychonoff). Added: the continuity of restriction as its own step,
    the reason the compact-neighbourhood set U is a neighbourhood in X, the net characterisation
    that identifies the topology of compact convergence with the initial topology of the
    restrictions, the closedness of the compatibility conditions via agreement of continuous
    maps into a Hausdorff space, and the gluing step in which local compactness is what makes
    the glued function continuous. No statement was changed. Not claimed: a retained solution
    set; the collection's provenance is the Munkres textbook, whose text is not retained here.

- event: solution-written
  by: GPT-6.2
  date: 2026-11-25
  note: >-
    Issue #169. Located Yang Di's Chapter 7 solution, §47 Exercise 2,
    and checked Munkres's printed Exercise 2 on p. 293 and general Ascoli
    Theorem 47.1 on p. 290. The earlier proof cited Theorem 46.7 for an
    initial-topology description which that theorem does not state.
    Use the actual general Ascoli theorem in both directions, with the
    compact-convergence Hausdorff argument and Heine-Borel. The two
    standard metrics are uniformly equivalent. The statement and prior
    audit records are unchanged.

---

::: {.exercise}

Prove the following.

Theorem.
If $X$ is a locally compact Hausdorff space, then a subspace $\mathcal{F}$ of $\mathcal{C}(X, \RR^n)$ in the topology of compact convergence has compact closure if and only if $\mathcal{F}$ is pointwise bounded and equicontinuous under either of the standard metrics on $\RR^n$.
:::

::: {.solution}
The exercise is Munkres, *Topology* (2000), Section 47, Exercise 2. See [Yang Di's solution, §47, Exercise 2](https://hexo.yougi.top/2025/01/15/Munkres-Topology-Solution-Chapter-7/#Ex-47-2), using the general Ascoli theorem (Munkres, Theorem 47.1).

Write $\mathcal F_x=\{f(x):f\in\mathcal F\}$ for each $x\in X$. For either standard metric on $\RR^n$, Heine--Borel (Munkres, Theorem 27.3) gives
$$
\mathcal F_x\text{ is bounded}\iff \overline{\mathcal F_x}\text{ is compact in }\RR^n.
$$
Moreover, the compact-convergence topology on $\mathcal C(X,\RR^n)$ is Hausdorff: for distinct functions $f,g$, choose a point at which they differ, and separate their values by disjoint metric neighbourhoods. Evaluation there is continuous since a singleton is compact. Thus a subset of $\mathcal C(X,\RR^n)$ has compact closure precisely when it is contained in a compact subspace: the reverse implication holds because that compact subspace is closed.

If $\mathcal F$ is pointwise bounded and equicontinuous, its pointwise value sets have compact closure by Heine--Borel. Theorem 47.1(a) places $\mathcal F$ in a compact subspace, hence its closure is compact. Conversely, if $\mathcal F$ has compact closure, it is contained in a compact subspace; since $X$ is locally compact Hausdorff, Theorem 47.1(b) implies equicontinuity and compact closure of each $\mathcal F_x$, hence pointwise boundedness.

Finally, writing $d_\infty$ and $d_2$ for the square and Euclidean metrics, respectively,
$$
d_\infty(u,v)\le d_2(u,v)\le\sqrt n\,d_\infty(u,v).
$$
These inequalities give both the same bounded subsets and the same equicontinuous families, and also the same compact-convergence topology. The asserted equivalence is therefore independent of the chosen standard metric.
:::
