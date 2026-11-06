---
schema: qual/card@1
id: P-WESRA07-II1
kind: problem
title: Continuity from below and failure of continuity from above without finiteness
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Read against the Wesleyan analysis qualifier, Real Analysis section, Summer
    2007, Part II problem 1 (assets/attachments/analysis_2003-2007.pdf, PDF page
    1), from the checked-in MinerU extraction and a 300 dpi render of the page.
    The printed problem supposes an increasing sequence of measurable sets and
    asks for the continuity-from-below identity plus an example showing the
    decreasing analogue fails. The card states both parts, so no repair was
    needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination; the proof is
    derived here, by the disjoint-difference decomposition and a counterexample
    with a set of infinite measure.
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a measure space and let $A_1\subseteq A_2\subseteq\cdots$ be measurable.
Prove that
$$
\mu\!\left(\bigcup_{n=1}^\infty A_n\right)=\lim_{n\to\infty}\mu(A_n).
$$
Give an example showing that the corresponding statement for decreasing sequences is false in general.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and $A_1\subseteq
A_2\subseteq\cdots$ measurable sets.

::: pf

::: {.pf-step #disjoint}

With $B_1=A_1$ and $B_n=A_n\setminus A_{n-1}$ for $n\ge2$, the sets $B_n$ are
measurable and pairwise disjoint, $A_n=\bigcup_{k\le n}B_k$, and
$\bigcup_nA_n=\bigcup_kB_k$.

::: pf-proof

Measurability is clear from measurability of the $A_n$. If $m<n$ and $x\in
B_m\subseteq A_m\subseteq A_{n-1}$, then $x\notin A_n\setminus A_{n-1}=B_n$,
so the $B_n$ are disjoint. For the unions: $B_k\subseteq A_k\subseteq A_n$ for
$k\le n$, giving one inclusion, and conversely $x\in A_n$ lies in
$A_k\setminus A_{k-1}$ for the least $k$ with $x\in A_k$, or in $A_1$; so
$A_n=\bigcup_{k\le n}B_k$. Taking unions over $n$ gives the second identity.

:::

:::

::: {.pf-step #continuous}

$\mu\bigl(\bigcup_{n=1}^\infty A_n\bigr)=\lim_{n\to\infty}\mu(A_n)$.

::: pf-proof

By step [](#disjoint){.pf-ref} and countable additivity,
$\mu\bigl(\bigcup_nA_n\bigr)=\sum_{k\ge1}\mu(B_k)$, and by finite additivity
$\mu(A_n)=\sum_{k\le n}\mu(B_k)$. The latter are the partial sums of a series
of nonnegative terms, so they converge to the sum, which is the former. No
finiteness hypothesis is needed for an increasing sequence, and the limit is
taken in $[0,\infty]$.

:::

:::

::: {.pf-step #counterexample}

The decreasing analogue fails in general: with Lebesgue measure on $\RR$ and
$E_n=[n,\infty)$, the sets decrease, $\bigcap_nE_n=\emptyset$, and yet
$\mu(E_n)=\infty$ for every $n$, so
$\lim_n\mu(E_n)=\infty\ne0=\mu(\bigcap_nE_n)$.

::: pf-proof

$[n+1,\infty)\subseteq[n,\infty)$ gives the decrease, and a real number $x$
lies in $\bigcap_n[n,\infty)$ only if $x\ge n$ for all $n$, which is
impossible; so the intersection is empty. Each $E_n$ is a half-line, hence of
infinite Lebesgue measure. So the identity fails, and the reason is the
absence of a finiteness hypothesis: the standard continuity-from-above
statement requires $\mu(E_1)<\infty$ so that the decreasing differences
$\mu(E_1)-\mu(E_n)$ may be subtracted.

:::

:::

:::


:::
