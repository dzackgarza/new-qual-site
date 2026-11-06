---
schema: qual/card@1
id: P-WESRA04-P3
kind: problem
title: Absolutely continuous functions map null sets to null sets
classification:
  areas: [real-analysis]
  topics: [Absolute Continuity, Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.3 problem 3 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed problem supposes g: [0,1] -> R
    absolutely continuous and E a subset of [0,1] of Lebesgue measure zero, and
    asks for a proof that g(E) is a set of Lebesgue measure zero. The card states
    exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The proof is
    derived here, from the epsilon-delta form of absolute continuity applied to
    the intervals of an open cover of E of small measure, with continuity
    supplying that g of an interval stays an interval.
---

::: {.problem}
Let $g:[0,1]\to\RR$ be absolutely continuous and let $E\subset[0,1]$ have Lebesgue measure zero.
Prove that $g(E)$ has Lebesgue measure zero.
:::

::: {.solution}

Let $g\colon[0,1]\to\RR$ be absolutely continuous and let $E\subseteq[0,1]$
with $m(E)=0$, where $m$ is Lebesgue measure. Absolute continuity means that
for every $\varepsilon>0$ there is $\delta>0$ such that
$\sum_j\abs{g(b_j)-g(a_j)}<\varepsilon$ for every finite family of pairwise
disjoint intervals $(a_j,b_j)\subseteq[0,1]$ with $\sum_j(b_j-a_j)<\delta$.

::: pf

::: {.pf-step #continuity}

$g$ is continuous, and for an interval $I\subseteq[0,1]$ the set $g(I)$ is an
interval with $m^*(g(I))\le V(g;I)$, where $V(g;I)$ is the total variation of
$g$ on $I$.

::: pf-proof

Absolute continuity implies continuity: taking the single interval $(a,b)$ in
the definition gives $\abs{g(b)-g(a)}<\varepsilon$ whenever $b-a<\delta$,
which is uniform continuity. A continuous image of an interval is an interval,
so $m^*(g(I))$ equals its diameter. For any two points $p<q$ of $I$,
$\abs{g(q)-g(p)}\le V(g;I)$ because the two-point partition is one of those
over which the variation is taken; hence the diameter, being a supremum of
such differences, is at most $V(g;I)$.

:::

:::

::: {.pf-step #cover}

There is an open $U\subseteq\RR$ with $E\subseteq U$ and
$m(U\cap[0,1])<\delta$, and $U\cap[0,1]$ is a countable disjoint union of open
intervals $I_k$.

::: pf-proof

$m(E)=0$ and Lebesgue measure is outer regular, so there is open $U\supseteq
E$ with $m(U)<\delta$; intersecting with $[0,1]$ and using subadditivity gives
$m(U\cap[0,1])<\delta$. An open subset of $\RR$ is a countable disjoint union
of open intervals, and intersecting with $[0,1]$ gives a countable disjoint
family of intervals, possibly with $0$ or $1$ as an endpoint, whose total
length is $m(U\cap[0,1])<\delta$.

:::

:::

::: {.pf-step #variation}

$\sum_kV(g;I_k)\le\varepsilon$.

::: pf-proof

Let $J$ be a finite set of indices and, for each $k\in J$, a finite partition
of $I_k$ into consecutive subintervals. These subintervals are pairwise
disjoint, being contained in the disjoint $I_k$, and their total length is at
most the total length of the $I_k$ for $k\in J$, which is at most
$m(U\cap[0,1])<\delta$. So the absolute continuity of $g$ gives $\sum_{k\in
J}V_{\text{part}}(g;I_k)<\varepsilon$, where the left side is the variation
sum of that choice of partitions. Taking the supremum over the partitions of
each $I_k$ and then over the finite $J$ gives $\sum_kV(g;I_k)\le\varepsilon$.

:::

:::

::: {.pf-step #null}

$m^*(g(E))=0$, hence $g(E)$ is Lebesgue measurable with $m(g(E))=0$.

::: pf-proof

$E\subseteq\bigcup_kI_k$ gives $g(E)\subseteq\bigcup_kg(I_k)$, so by countable
subadditivity of outer measure
$m^*(g(E))\le\sum_km^*(g(I_k))\le\sum_kV(g;I_k)\le\varepsilon$ by steps
[](#continuity){.pf-ref} and [](#variation){.pf-ref}. Since $\varepsilon>0$
was arbitrary, $m^*(g(E))=0$; a set of outer measure zero is Lebesgue
measurable with measure zero.

:::

:::

:::


:::
