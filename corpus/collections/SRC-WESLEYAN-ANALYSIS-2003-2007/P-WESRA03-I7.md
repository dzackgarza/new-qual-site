---
schema: qual/card@1
id: P-WESRA03-I7
kind: problem
title: Define absolute continuity of one measure with respect to another
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 7 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 7 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "Define what it means for a measure mu to be
    absolutely continuous with respect to a measure nu on (X, tau(X))." The card
    gives the definition, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definition is
    the answer; the proof block records what follows from it and points to the
    card on which the epsilon-delta characterisation is proved.
---

::: {.problem}
Define what it means for a measure $\mu$ to be absolutely continuous with respect to a measure $\nu$ on $(X,\tau(X))$.
:::

::: {.solution}

Let $\mu$ and $\nu$ be measures on the measurable space $(X,\tau(X))$. Then
$\mu$ is absolutely continuous with respect to $\nu$, written $\mu\ll\nu$, if
$$
\boxed{\nu(E)=0\ \Longrightarrow\ \mu(E)=0\qquad\text{for every }E\in\tau(X).}
$$

::: pf

::: {.pf-step #consequences}

$\mu\ll\nu$ holds if and only if $\mu$ is concentrated wherever $\nu$ is:
$\mu(E)=0$ for every $E$ with $\nu(E)=0$, so $\mu$ vanishes on every set that
$\nu$ ignores.

::: pf-proof

The condition is exactly the statement that $\nu$-null sets are $\mu$-null. It
is not symmetric: counting measure on $\RR$ is absolutely continuous with
respect to neither Lebesgue measure nor its reverse, since it charges the null
singleton $\{0\}$ while Lebesgue measure vanishes on every countable set, and
Lebesgue measure charges a null set of counting measure.

:::

:::

::: {.pf-step #epsilon-delta}

For finite $\mu$ and $\nu$, $\mu\ll\nu$ if and only if for every
$\varepsilon>0$ there is $\delta>0$ with $\nu(E)<\delta$ implying
$\mu(E)<\varepsilon$.

::: pf-proof

This equivalence, with both directions, is proved on [[P-WESRA07-I5]]; the
argument on the one hand notes that a null set has measure below every
$\delta$, and on the other builds, from the failure of the
$\varepsilon$-$\delta$ condition, sets $E_n$ with $\nu(E_n)<2^{-n}$ and
$\mu(E_n)\ge\varepsilon$ whose limsup is $\nu$-null and $\mu$-large. Both
proofs use only the finiteness of the two measures, which is why the
definition above is the general one and the $\varepsilon$-$\delta$ form a
theorem about finite measures.

:::

:::

:::


:::
