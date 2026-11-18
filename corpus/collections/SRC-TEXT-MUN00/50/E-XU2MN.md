---
schema: qual/card@1
id: E-XU2MN
kind: problem
title: Hausdorff equals completely regular for locally euclidean spaces
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Separation Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), supplementary Exercise 7 of §50, printed p. 318, with the definition
    of complete regularity in §33 and Theorem 29.1 for the one-point compactification. A completely regular space
    is T1 and separates points from closed sets, hence Hausdorff. Conversely a Hausdorff locally euclidean space
    is locally compact, being covered by the interiors of compact coordinate balls, so it imbeds in its
    compact Hausdorff one-point compactification, which is normal and hence completely regular by Theorem 33.1,
    and complete regularity passes to subspaces. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves supplementary Exercise 7 of §50 (printed
    p. 318). Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of
    Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8
    | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost.
    The Stack Exchange queries of this pass, listed in the COMPLAINTS.md entry for §43--§50, returned no
    question on the equivalence. The card's two steps are its own: complete regularity gives Hausdorff because
    it includes $T_1$ and separates a point from a singleton, and conversely a locally $m$-euclidean Hausdorff
    space is locally compact by a closed ball inside a chart, hence completely regular through its one-point
    compactification. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the card's own argument. The step the earlier prose described in a
    phrase is now constructed: from a chart phi: U -> W about a point x, a closed ball of radius eps/2
    about phi(x) lies in W, and its preimage C is a compact subspace of X --- homeomorphic to that closed
    ball, which is compact in R^m by Theorem 27.3 --- containing the neighbourhood V = phi^{-1}(B(phi(x),
    eps/2)) of x, which is open in X because U is. That is what Munkres' definition of local compactness
    asks for, and the earlier wording, "a neighbourhood whose closure in the chart is compact", supplied
    neither the compact subspace nor the membership V in C. The passage to complete regularity now runs
    through Theorem 29.1, Theorem 32.3, Theorem 33.1 and Theorem 33.2 with their pages. No published
    solution located; the card keeps its own argument and says so. Checked against Munkres, Topology
    (2000), supplementary Exercise 7 of Section 50, printed p. 318.
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that $X$ is Hausdorff if and only if $X$ is completely regular.
:::

::: {.solution}

No complete published solution was located; the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`, and the argument is the card's own. Two steps of it are written out here rather than described: the transfer of the compact ball of a chart into a compact subspace of $X$, and the passage from local compactness to complete regularity through the one-point compactification. The earlier prose said that shrinking inside a chart gives "a neighbourhood whose closure in the chart is compact", which names neither the compact subspace of $X$ that Munkres' definition needs nor the neighbourhood inside it; the card now produces both.

The statement was checked against Munkres, *Topology* (2000), the supplementary Exercise 7 of §50, printed p. 318, with the definition of locally $m$-euclidean printed on p. 316, that of local compactness printed on p. 182, Theorem 29.1 on printed p. 183, Theorem 32.3 on printed p. 202, the Urysohn lemma (Theorem 33.1) on printed p. 207 and Theorem 33.2 on printed p. 211. Throughout, $X$ is locally $m$-euclidean: each $x\in X$ has a neighbourhood homeomorphic to an open set of $\RR^{m}$ (printed p. 316), a condition that already gives the $T_{1}$ axiom but not the Hausdorff axiom, which is the hypothesis the exercise varies. Complete regularity is as defined on printed p. 211: one-point sets are closed, and each point can be separated from a closed set not containing it by a continuous map to $[0,1]$ taking the value $1$ at the point and $0$ on the set.

::: pf

::: {.pf-step #cr-to-haus}

If $X$ is completely regular, then $X$ is Hausdorff.

::: pf-proof

Complete regularity includes the $T_{1}$ axiom, so one-point sets are closed (printed p. 211). Given distinct $x,y\in X$, the set $\theset{y}$ is closed and does not contain $x$, so there is a continuous $f\colon X\to[0,1]$ with $f(x)=1$ and $f(y)=0$. The sets $f^{-1}\big((\tfrac12,1]\big)$ and $f^{-1}\big([0,\tfrac12)\big)$ are disjoint, and both are open in $X$ because $(1/2,1]$ and $[0,1/2)$ are open in $[0,1]$ and $f$ is continuous. So $x$ and $y$ have disjoint neighbourhoods.

:::

:::

::: {.pf-step #locally-compact}

$X$ is locally compact; the Hausdorff hypothesis plays no part in this step.

:::: pf-proof

Let $x\in X$. The chart at $x$, which local $m$-euclidean-ness supplies, gives the compact subspace and the neighbourhood of $x$ inside it that the definition of local compactness requires.

::: {.pf-step #chart}

For $x\in X$ there are a neighbourhood $U$ of $x$, an open $W\subset\RR^{m}$ and a homeomorphism $\varphi\colon U\to W$.

::: pf-proof

This is the definition of locally $m$-euclidean (printed p. 316), applied to $x$.

:::

:::

::: {.pf-step #ball}

There is $\varepsilon>0$ with $\overline{B}\big(\varphi(x),\varepsilon/2\big)\subset W$.

::: pf-proof

$W$ is open and $\varphi(x)\in W$, so some ball $B(\varphi(x),\varepsilon)$ about $\varphi(x)$ lies in $W$; the closed ball of half that radius lies in the open ball, hence in $W$.

:::

:::

::: {.pf-step #compact-subspace}

$C\coloneqq\varphi^{-1}\big(\overline{B}(\varphi(x),\varepsilon/2)\big)$ is a compact subspace of $X$, and $V\coloneqq\varphi^{-1}\big(B(\varphi(x),\varepsilon/2)\big)$ is a neighbourhood of $x$ with $V\subset C$.

::: pf-proof

$\overline{B}(\varphi(x),\varepsilon/2)$ is closed and bounded in $\RR^{m}$, hence compact (Theorem 27.3, printed p. 173). The restriction of $\varphi$ is a homeomorphism of $C$ onto that closed ball, since a homeomorphism carries a subset onto its image homeomorphically; so $C$ is compact as a subspace of $X$. The set $V$ is the image under $\varphi^{-1}$ of an open subset of $W$, hence is open in $U$ and therefore in $X$, because $U$ is open in $X$; and $x\in V$ because $0<\varepsilon/2$. Finally $V\subset C$, since the open ball lies in the closed one of the same radius.

:::

:::

::: pf-step

$X$ is locally compact.

::: pf-proof

At each $x$ step [](#compact-subspace){.pf-ref} produces a compact subspace $C$ of $X$ containing the neighbourhood $V$ of $x$; that is the definition of local compactness at $x$ (printed p. 182).

:::

:::

::::

:::

::: {.pf-step #lc-to-cr}

If $X$ is locally compact Hausdorff, then $X$ is completely regular.

::: pf-proof

By Theorem 29.1 (printed p. 183) the space $X$ has a one-point compactification $X^{*}$, which contains $X$ as a subspace and is compact Hausdorff. A compact Hausdorff space is normal (Theorem 32.3, printed p. 202), and a normal space is completely regular by the Urysohn lemma (Theorem 33.1, printed p. 207); a subspace of a completely regular space is completely regular (Theorem 33.2, printed p. 211). Hence $X$ is completely regular.

:::

:::

::: pf-step

Therefore a locally $m$-euclidean space is Hausdorff if and only if it is completely regular.

::: pf-proof

Step [](#cr-to-haus){.pf-ref} gives the implication from complete regularity to the Hausdorff axiom, for every space. Conversely, if $X$ is Hausdorff then it is locally compact by step [](#locally-compact){.pf-ref} --- which uses only local $m$-euclidean-ness --- hence locally compact Hausdorff, hence completely regular by step [](#lc-to-cr){.pf-ref}. The two implications together are the equivalence the exercise asks for, and the $T_{1}$ axiom needed for complete regularity is supplied by local $m$-euclidean-ness itself (printed p. 316).

:::

:::

:::

:::
