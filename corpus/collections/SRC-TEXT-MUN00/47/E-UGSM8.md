---
schema: qual/card@1
id: E-UGSM8
kind: problem
title: The general Ascoli theorem implies the classical version
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §47 Exercise 3 (printed p. 293) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Theorem 47.1 (the general Ascoli
    theorem as the book states it, printed p. 290), Theorem 45.4 (the classical version), Theorem 46.7 (compact
    convergence equals uniform convergence on a compact space) and Theorem 27.3 plus Theorem 26.3. The argument
    is: on a compact space the two topologies agree and the space of functions is metrizable, hence Hausdorff;
    in R^n a set has compact closure iff it is bounded; so pointwise boundedness of F is pointwise relative
    compactness of the closures F_a, and part (a) of Theorem 47.1 puts F inside a compact subspace, which is
    closed in the Hausdorff function space, so the closure of F is compact; conversely if the closure of F is
    compact then F is contained in a compact subspace and part (b) of Theorem 47.1, whose hypothesis of local
    compactness holds for the compact Hausdorff X, gives equicontinuity and compact closures of the F_a. Nothing
    needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 3 of
    §47, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange
    searches of this pass, recorded in the COMPLAINTS.md entry for §43--§50, returned nothing on the
    passage from the general Ascoli theorem to Theorem 45.4. The card keeps its own proof.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The printed exercise was re-read at section 47 Exercise 3, printed p. 293
    (PDF p. 308): "Show that the general version of Ascoli's theorem implies
    the classical version (Theorem 45.4) when X is Hausdorff", which is what
    the card states. Both implications are correct. For the direct one, on a
    compact X the topology of compact convergence is the uniform topology, which
    is metrizable, hence Hausdorff; pointwise boundedness in R^n makes each
    F_a relatively compact by Heine-Borel, so part (a) of Theorem 47.1 puts F
    inside a compact subspace, which is closed in the Hausdorff function space,
    so the closure of F is compact. For the converse, the closure of F is a
    compact subspace containing F; X is compact Hausdorff and therefore locally
    compact Hausdorff, so part (b) of Theorem 47.1 gives equicontinuity and
    compact closures of the F_a, and Heine-Borel turns those into boundedness.
    Nothing was changed.
---

::: {.exercise}

Show that the general version of Ascoli's theorem implies the classical version (Theorem 45.4) when $X$ is Hausdorff.
:::

::: {.solution}
The classical version (Theorem 45.4) states: for $X$ compact and $\mathcal C(X, \RR^n)$ in the uniform topology, a subset $\mathcal F$ has compact closure if and only if $\mathcal F$ is equicontinuous and pointwise bounded.

The general version states: for a space $X$, a metric space $(Y, d)$, and $\mathcal C(X, Y)$ in the topology of compact convergence, if $\mathcal F \subseteq \mathcal C(X, Y)$ is equicontinuous and each set $\mathcal F_a = \{f(a) : f \in \mathcal F\}$ has compact closure, then $\mathcal F$ is contained in a compact subspace of $\mathcal C(X, Y)$; the converse holds if $X$ is locally compact Hausdorff.

Let $X$ be compact Hausdorff and $Y = \RR^n$.

::: pf

::: {.pf-step #s1}

On $\mathcal C(X, \RR^n)$, the topology of compact convergence equals the uniform topology, and it is Hausdorff.

::: pf-proof

$X$ is compact, so the two topologies coincide by [[E-2AWO8]]. The uniform topology is induced by a metric.

:::

:::

::: {.pf-step #s2}

For $a \in X$, $\mathcal F_a$ has compact closure in $\RR^n$ if and only if $\mathcal F_a$ is bounded.

::: pf-proof

The closure of a bounded subset of $\RR^n$ is closed and bounded, hence compact by the Heine--Borel theorem; a set with compact closure is bounded.

:::

:::

::: {.pf-step #s3}

If $\mathcal F$ is equicontinuous and pointwise bounded, then $\overline{\mathcal F}$ is compact.

::: pf-proof

By step [](#s2){.pf-ref} each $\mathcal F_a$ has compact closure, so the general version puts $\mathcal F$ inside a compact subspace $K$. By step [](#s1){.pf-ref}, $K$ is closed in the Hausdorff space $\mathcal C(X, \RR^n)$, so $\overline{\mathcal F} \subseteq K$ is a closed subset of a compact space, hence compact.

:::

:::

::: {.pf-step #s4}

If $\overline{\mathcal F}$ is compact, then $\mathcal F$ is equicontinuous and pointwise bounded.

::: pf-proof

$\mathcal F$ is contained in the compact subspace $\overline{\mathcal F}$. A compact Hausdorff space is locally compact Hausdorff, so the converse in the general version shows that $\mathcal F$ is equicontinuous and each $\mathcal F_a$ has compact closure; by step [](#s2){.pf-ref}, each $\mathcal F_a$ is bounded.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} are the two implications of the classical version.

:::

:::

:::
