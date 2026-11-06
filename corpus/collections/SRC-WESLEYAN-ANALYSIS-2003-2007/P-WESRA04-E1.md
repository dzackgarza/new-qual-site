---
schema: qual/card@1
id: P-WESRA04-E1
kind: problem
title: A positive-measure subset of $[0,1]$ with empty interior
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.2, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.2 item 1 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item asks for "an example of a subset
    of [0,1] with positive Lebesgue measure, whose closure contains no non-empty
    open intervals", and the section's instruction says the required examples
    may be presented without proof that they have the desired properties. The
    card gives the Smith-Volterra-Cantor set, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The example is
    named on the card and its three properties are verified in the proof block,
    which is more than the printed instruction requires.
---

::: {.problem}
Give an example of a subset of $[0,1]$ with positive Lebesgue measure whose closure contains no nonempty open interval.
:::

::: {.solution}

Take the Smith-Volterra-Cantor set $S\subset[0,1]$: from $[0,1]$ remove at
stage $n\ge1$ a central open interval of length $4^{-n}$ from each of the
$2^{n-1}$ closed intervals left after stage $n-1$, and let
$S=\bigcap_{n\ge0}S_n$, where $S_n$ is the union of the $2^n$ closed intervals
remaining after stage $n$ and $S_0=[0,1]$.

::: pf

::: {.pf-step #measure}

$S$ is closed and $m(S)=\frac12$.

::: pf-proof

Each $S_n$ is a finite union of closed intervals and $S_n\subseteq S_{n-1}$,
so $S=\bigcap_nS_n$ is closed. The open set removed at stage $n$ has measure
$2^{n-1}4^{-n}=2^{-n-1}$, so the total removed has measure
$\sum_{n\ge1}2^{-n-1}=\frac12$, and $m(S)=1-\frac12=\frac12$; equivalently
$m(S)=\lim_nm(S_n)$ by continuity from above for the finite measure $m$ and
the decreasing sequence $S_n$.

:::

:::

::: {.pf-step #nowheredense}

$S$ contains no nonempty open interval.

::: pf-proof

After stage $n$ we have $S\subseteq S_n$, a union of $2^n$ closed intervals of
total length $m(S_n)=1-\sum_{k\le n}2^{-k-1}=\frac12+2^{-n-1}$, so each has
length below $2^{-n}$. If $S$ contained an interval of length $L>0$, that
interval would lie in $S_n$ for every $n$; an interval contained in a finite
union of intervals each of length below $2^{-n}$ has length below $2^{-n}$, so
$L\le2^{-n}$ for all $n$ and $L=0$, a contradiction.

:::

:::

::: {.pf-step #example}

$S$ is a subset of $[0,1]$ of positive measure whose closure contains no
nonempty open interval.

::: pf-proof

$S\subseteq[0,1]$ by construction, $m(S)=\frac12>0$ by step
[](#measure){.pf-ref}, and $\overline S=S$ because $S$ is closed, so by step
[](#nowheredense){.pf-ref} no nonempty open set, hence no nonempty open
interval, is contained in $\overline S$. That is the required example.

:::

:::

:::


:::
