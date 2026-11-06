---
schema: qual/card@1
id: P-WESRA04-E2
kind: problem
title: A continuous bounded-variation function that is not absolutely continuous
classification:
  areas: [real-analysis]
  topics: [Absolute Continuity, Bounded Variation]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.2, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the Wesleyan Preliminary Examination, Analysis, August 2, 2004,
    Real Analysis section 2.2 item 2 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item asks for "an example of a
    continuous function of bounded variation that is not absolutely continuous",
    and the section waives proof that the example has the properties. The card
    gives the Cantor-Lebesgue function, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The example is
    named on the card and the proof block verifies continuity, bounded variation,
    and the failure of absolute continuity, citing the standard Lusin condition
    that absolutely continuous functions carry null sets to null sets.
---

::: {.problem}
Give an example of a continuous function of bounded variation that is not absolutely continuous.
:::

::: {.solution}

Let $F\colon[0,1]\to[0,1]$ be the Cantor-Lebesgue function, and $C$ the
middle-thirds Cantor set.

::: pf

::: {.pf-step #properties}

$F$ is continuous, nondecreasing, $F(0)=0$, $F(1)=1$, and $F(C)=[0,1]$.

::: pf-proof

$F$ is defined as the uniform limit of the continuous piecewise linear
functions that are constant on the complementary intervals of the $n$-th stage
of the construction of $C$ and increase linearly across the remaining $2^n$
intervals, so it is continuous; each approximant is nondecreasing and so is
the limit; and the values at the endpoints are $0$ and $1$. On the Cantor set
$F$ is onto $[0,1]$ because every $y\in[0,1]$ has a ternary expansion in
digits $0$ and $2$, whose corresponding point of $C$ is mapped to $y$; and $F$
is constant on each complementary interval, so the image of $C$ is the whole
interval.

:::

:::

::: {.pf-step #bv}

$F$ has bounded variation, with $V_0^1(F)=1$.

::: pf-proof

For a nondecreasing function and any partition $0=x_0<\dots<x_N=1$, the
variation sum is $\sum_j(F(x_j)-F(x_{j-1}))=F(1)-F(0)=1$ by telescoping, so
the total variation is $1$; in particular $F$ has bounded variation on
$[0,1]$.

:::

:::

::: {.pf-step #notac}

$F$ is not absolutely continuous.

::: pf-proof

An absolutely continuous $g$ on $[0,1]$ satisfies Lusin's condition: $m(E)=0$
implies $m(g(E))=0$. Indeed such a $g$ is differentiable a.e. with $g'\in L^1$
and $g(y)-g(x)=\int_x^yg'\,dm$, and the one-dimensional change of variables
inequality gives $m(g(E))\le\int_E\abs{g'}\,dm=0$ for a null set $E$. Here $C$
is null while $F(C)=[0,1]$ has measure $1$, so $F$ cannot be absolutely
continuous; the verification is more than the printed instruction requires,
which waives proof of the example's properties.

:::

:::

:::


:::
