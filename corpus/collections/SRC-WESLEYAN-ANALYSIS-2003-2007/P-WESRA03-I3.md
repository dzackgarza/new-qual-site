---
schema: qual/card@1
id: P-WESRA03-I3
kind: problem
title: A positive-measure compact set containing no rational numbers
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Read against the Wesleyan Preliminary Examination, Analysis, August 4, 2003,
    section I, item 3 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "Is there a compact subset of [0,1] \\ Q
    with positive Lebesgue measure?" and the printed instructions ask for a
    brief explanation or counterexample as appropriate. The card asks the same
    question and answers it, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The construction
    is derived here, by covering the rationals with open intervals of total
    length below 1/4 and taking the compact complement in [0,1].
---

::: {.problem}
Is there a compact subset of $[0,1]\setminus\QQ$ with positive Lebesgue measure?
:::

::: {.solution}

Let $m$ be Lebesgue measure on $\RR$. The answer is yes: there is a compact
$K\subseteq[0,1]\setminus\QQ$ with $m(K)>0$.

::: pf

::: {.pf-step #cover}

Enumerate $\QQ\cap[0,1]$ as $(q_n)_{n\ge1}$ and choose around $q_n$ an open
interval $I_n$ with $m(I_n)<2^{-n-2}$; then $U=\bigcup_nI_n$ is open, contains
$\QQ\cap[0,1]$, and $m(U)\le\frac14$.

::: pf-proof

The rationals in $[0,1]$ are countable, so such an enumeration and such
intervals exist, since an interval of arbitrarily small length can be centred
at $q_n$. Then $m(U)\le\sum_nm(I_n)<\sum_n2^{-n-2}=\frac14$ by countable
subadditivity, the geometric series being $\frac14$.

:::

:::

::: {.pf-step #compact}

$K=[0,1]\setminus U$ is compact, is contained in $[0,1]\setminus\QQ$, and has
$m(K)\ge\frac34>0$.

::: pf-proof

$K$ is closed in $\RR$, being the complement of the open $U$, and lies in the
compact interval $[0,1]$, so it is compact; a closed subset of a compact space
is compact. Every rational of $[0,1]$ lies in $U$, so $K$ contains none.
Finally $m(K)=m([0,1])-m(U\cap[0,1])\ge1-\frac14=\frac34$, using additivity
for the measurable set $U$ and step [](#cover){.pf-ref}.

:::

:::

::: {.pf-step #answer}

A compact subset of $[0,1]\setminus\QQ$ of positive Lebesgue measure exists,
namely $K$.

::: pf-proof

Steps [](#cover){.pf-ref} and [](#compact){.pf-ref} exhibit $K$ with all the
stated properties. The point is that a set of full measure need not contain an
interval of irrationals: the complement of a dense open set of small measure
is a large compact set of irrationals, so nothing prevents it from carrying
most of the measure of $[0,1]$.

:::

:::

:::


:::
