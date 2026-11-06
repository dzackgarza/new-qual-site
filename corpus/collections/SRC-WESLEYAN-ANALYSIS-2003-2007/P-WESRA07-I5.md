---
schema: qual/card@1
id: P-WESRA07-I5
kind: problem
title: Define absolute continuity of measures
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part I item 5 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "The definition of absolute continuity for one measure with
    respect to another", under "Give precise statements of the following". The
    card gives the definition, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definition
    is the answer; the proof block establishes that for finite measures it is
    equivalent to the epsilon-delta condition that the subsequent theorems use.
---

::: {.problem}
Give the definition of absolute continuity for one measure with respect to another.
:::

::: {.solution}

Let $\mu$ and $\nu$ be measures on the same measurable space $(X,\mathcal A)$.
Then $\mu$ is absolutely continuous with respect to $\nu$, written
$\mu\ll\nu$, if
$$
\boxed{\nu(E)=0\ \Longrightarrow\ \mu(E)=0\qquad\text{for every }E\in\mathcal A.}
$$

::: pf

::: {.pf-step #epsilon-delta}

If $\mu$ and $\nu$ are finite, then $\mu\ll\nu$ if and only if for every
$\varepsilon>0$ there is $\delta>0$ such that $\nu(E)<\delta$ implies
$\mu(E)<\varepsilon$.

::: pf-proof

If the $\varepsilon$-$\delta$ condition holds and $\nu(E)=0$, then
$\nu(E)<\delta$ for every $\delta>0$, so $\mu(E)<\varepsilon$ for every
$\varepsilon>0$ and $\mu(E)=0$; this direction needs no finiteness. Conversely
suppose $\mu\ll\nu$ and the condition fails for some $\varepsilon>0$. Then for
every $n$ there is $E_n\in\mathcal A$ with $\nu(E_n)<2^{-n}$ and
$\mu(E_n)\ge\varepsilon$. Put $F=\limsup_nE_n=\bigcap_N\bigcup_{n\ge N}E_n$;
then $\nu(F)\le\sum_{n\ge N}\nu(E_n)<2^{1-N}$ for every $N$, so $\nu(F)=0$,
and by continuity of the finite measure $\mu$ from above applied to the
decreasing sets $\bigcup_{n\ge N}E_n\supseteq E_N$,
$\mu(F)=\lim_N\mu(\bigcup_{n\ge N}E_n)\ge\limsup_N\mu(E_N)\ge\varepsilon>0$.
So $\nu(F)=0<\mu(F)$, contradicting $\mu\ll\nu$.

:::

:::

::: {.pf-step #density}

If $\nu$ is $\sigma$-finite and $\mu\ll\nu$, then $\mu$ has no atoms off the
support of $\nu$: any $E$ with $\nu(E)=0$ satisfies $\mu(E)=0$, and in
particular $\mu$ is concentrated on any set carrying $\nu$.

::: pf-proof

The first clause is the definition. For the second, if $\nu(X\setminus S)=0$
then $\mu(X\setminus S)=0$ by absolute continuity, so $\mu(E)=\mu(E\cap S)$
for every $E$; this is what lets an integral against $\nu$ represent $\mu$,
since integrals against $\nu$ cannot see sets of $\nu$-measure zero.

:::

:::

:::


:::
