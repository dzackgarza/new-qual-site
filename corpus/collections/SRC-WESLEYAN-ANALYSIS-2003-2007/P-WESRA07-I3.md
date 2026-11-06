---
schema: qual/card@1
id: P-WESRA07-I3
kind: problem
title: Define almost uniform convergence
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part I item 3 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "The definition of almost uniform convergence for a sequence
    of functions", and the card asks for the definition, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definition
    is the answer; the proof block proves that the two formulations the card
    gives, an exceptional set of small measure off which the convergence is
    uniform and a uniform distance tending to zero, are equivalent.
---

::: {.problem}
Give the definition of almost uniform convergence for a sequence of functions.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and $f_n,f$ measurable functions
on $X$. The sequence converges to $f$ almost uniformly if for every
$\varepsilon>0$ there is $E\in\mathcal A$ with $\mu(E)<\varepsilon$ such that
$f_n\to f$ uniformly on $X\setminus E$.

::: pf

::: {.pf-step #equivalent}

This is equivalent to: for every $\varepsilon>0$ there is $E\in\mathcal A$
with $\mu(E)<\varepsilon$ and $\sup_{x\in X\setminus E}\abs{f_n(x)-f(x)}\to0$.

::: pf-proof

Suppose $f_n\to f$ uniformly on $X\setminus E$, and fix $\delta>0$. By
definition of uniform convergence there is $N$ with $\abs{f_n(x)-f(x)}<\delta$
for all $n\ge N$ and all $x\in X\setminus E$, so $\sup_{x\in X\setminus
E}\abs{f_n-f}\le\delta$ for $n\ge N$; as $\delta$ was arbitrary, the supremum
tends to $0$. Conversely, if the supremum tends to $0$ then for every
$\delta>0$ there is $N$ with the supremum below $\delta$ from $N$ on, which is
uniform convergence on $X\setminus E$. The exceptional set $E$ is the same in
both formulations, so the two conditions have the same content.

:::

:::

::: {.pf-step #monotone}

The exceptional sets may be taken decreasing, and the definition is unchanged
if "for every $\varepsilon>0$" is replaced by "for every $\varepsilon>0$ there
is a set of measure at most $\varepsilon$".

::: pf-proof

If $E$ works for $\varepsilon$ and $E'\supset E$ has $\mu(E')<\varepsilon$,
then $E'$ works too, since a subset of $X\setminus E'$ is a subset of
$X\setminus E$ and uniformity passes to subsets; this gives monotonicity in
$\varepsilon$, and it shows that "$\mu(E)<\varepsilon$" and
"$\mu(E)\le\varepsilon$" define the same notion, because one may pass to a
smaller threshold. So the definition is stable under the harmless variations
in the literature.

:::

:::

:::


:::
