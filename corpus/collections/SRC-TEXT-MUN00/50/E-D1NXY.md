---
schema: qual/card@1
id: E-D1NXY
kind: problem
title: The line is a manifold that is not compact
classification:
  areas:
  - topology
  topics:
  - Manifolds
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
    Checked against Munkres, Topology (2000), supplementary Exercise 3 of §50, printed p. 317, together with the
    card of supplementary Exercise 2 for the labels of the conditions: R is locally 1-euclidean, Hausdorff and
    second countable (the intervals with rational endpoints), so it satisfies (ii); the cover by the intervals
    (-n,n) has no finite subcover, so it fails (i). Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located treats supplementary Exercise 3 of §50 (printed
    p. 317); the example is a two-line matter of the countable basis of intervals with rational endpoints and
    the cover by $(-n,n)$, and the card gives it. Murayama's selection has no Chapter 8, dbFin has no
    chapter-8 page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36,
    and the AoPS post *Topology by Munkres Chapter 8 | Day 18*
    (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The Stack
    Exchange queries of this pass are listed in the COMPLAINTS.md entry for §43--§50. Nothing needed
    correction.
---

::: {.exercise}

Show that $\RR$ is locally 1-euclidean and satisfies (ii) but not (i) of Exercise 2.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the two conditions of Exercise 2 (card [[E-OYPV7]]) checked separately.

::: pf

::: {.pf-step #locally-euclidean}
$\RR$ is locally $1$-euclidean.

::: pf-proof
Given $x\in\RR$ and a neighbourhood $U$ of $x$, choose $\varepsilon>0$ with $(x-\varepsilon,x+\varepsilon)\subseteq U$. The map $t\mapsto x+t$ carries $(-1,1)$ homeomorphically onto $(x-\varepsilon,x+\varepsilon)$ when composed with $t\mapsto\varepsilon t$, so $U$ contains an open neighbourhood of $x$ homeomorphic to an open subset of $\RR^{1}$; this is the definition of locally $1$-euclidean.
:::

:::

::: {.pf-step #condition-two}
$\RR$ satisfies condition (ii) of Exercise 2.

::: pf-proof
Condition (ii) asks for a Hausdorff space with a countable basis. Distinct reals $x<y$ have the disjoint open neighbourhoods $(x-1,x+(y-x)/2)$ and $(x+(y-x)/2,y+1)$, so $\RR$ is Hausdorff. The intervals $(p,q)$ with $p<q$ rational form a basis: given a point $x$ of an open set $U$, choose $a<b$ with $x\in(a,b)\subseteq U$, then by density of $\QQ$ choose rationals $p,q$ with $a<p<x<q<b$, and $(p,q)$ is a basis element with $x\in(p,q)\subseteq U$. That basis is indexed by the countable set $\QQ\times\QQ$, so $\RR$ is second countable.
:::

:::

::: {.pf-step #not-condition-one}
$\RR$ does not satisfy condition (i) of Exercise 2, which requires compactness.

::: pf-proof
The cover $\theset{(-n,n)\mid n\in\ZZ_{+}}$ of $\RR$ by open sets has no finite subcover: a finite subcollection has a largest index $N$ and its union is $(-N,N)$, a proper subset of $\RR$.
:::

:::

::: {.pf-qed}
$\RR$ is locally $1$-euclidean by step [](#locally-euclidean){.pf-ref}, satisfies (ii) by step [](#condition-two){.pf-ref}, and fails (i) by step [](#not-condition-one){.pf-ref}.
:::

:::

:::
