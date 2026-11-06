---
schema: qual/card@1
id: P-WESRA07-I2
kind: problem
title: Define convergence in measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part I item 2 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "The definition of convergence in measure for a sequence of
    functions", and the card asks for the definition, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The definition
    is the answer to the question; the proof block establishes what a definition
    needs to be usable, namely that the sets involved are measurable and that
    the notion depends only on the almost-everywhere classes of the functions.
---

::: {.problem}
Give the definition of convergence in measure for a sequence of functions.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and let $f_n,f$ be measurable
functions on $X$, real- or complex-valued. The sequence $(f_n)$ converges to
$f$ in measure if for every $\varepsilon>0$,
$$
\boxed{\mu\bigl(\{x\in X:\abs{f_n(x)-f(x)}>\varepsilon\}\bigr)\longrightarrow0\quad(n\to\infty).}
$$

::: pf

::: {.pf-step #measurable}

For each $n$ and $\varepsilon>0$ the set $\{x:\abs{f_n(x)-f(x)}>\varepsilon\}$
is measurable, so its measure is defined.

::: pf-proof

$f_n-f$ is measurable because sums of measurable functions are measurable;
$\abs{f_n-f}$ is measurable because the absolute value is continuous; and the
superlevel set $\{x:\abs{f_n-f}>\varepsilon\}$ is the preimage of the open set
$(\varepsilon,\infty)$ under a measurable function, hence measurable. So each
term of the sequence whose limit is taken is a well-defined element of
$[0,\mu(X)]$.

:::

:::

::: {.pf-step #classes}

Convergence in measure depends only on the almost-everywhere classes of the
functions: if $g_n=f_n$ a.e. and $g=f$ a.e. for all $n$, then $f_n\to f$ in
measure if and only if $g_n\to g$ in measure.

::: pf-proof

Let $N_0$ be a null set off which $g=f$ and $N_n$ null sets off which
$g_n=f_n$, and put $N=\bigcup_{n\ge0}N_n$, a null set as a countable union of
null sets. On $X\setminus N$ we have $g_n=f_n$ and $g=f$ for every $n$, so
$\{\abs{g_n-g}>\varepsilon\}\cap(X\setminus
N)=\{\abs{f_n-f}>\varepsilon\}\cap(X\setminus N)$, and therefore
$\mu(\abs{g_n-g}>\varepsilon)$ and $\mu(\abs{f_n-f}>\varepsilon)$ differ by at
most $\mu(N)=0$. Hence the two sequences of measures have the same limit
behaviour, which is the claim.

:::

:::

:::


:::
