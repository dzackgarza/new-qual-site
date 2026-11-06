---
schema: qual/card@1
id: P-WESRA04-T3
kind: problem
title: State Lusin's theorem on continuous approximation of measurable functions
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.1, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.1 item 3 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 34, printed page 2), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item is "State a theorem which
    describes how Lebesgue measurable functions on [0,1] can be approximated by
    continuous functions." The card answers with Lusin's theorem and with the
    equivalent form asserting approximation in measure by a continuous function,
    either of which is an answer to the printed item, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The statement is
    the answer; the proof block derives the continuous-function form from
    Lusin's theorem by Tietze extension, and derives the density of the
    continuous functions in L^1, which is the quantitative form of the same
    approximation.
---

::: {.problem}
State a theorem describing how Lebesgue measurable functions on $[0,1]$ can be approximated by continuous functions.
:::

::: {.solution}

Lusin's theorem: if $f\colon[0,1]\to\RR$ is Lebesgue measurable and finite
almost everywhere, then for every $\varepsilon>0$ there is a compact
$K\subset[0,1]$ with $m([0,1]\setminus K)<\varepsilon$ such that $f$
restricted to $K$ is continuous.

::: pf

::: {.pf-step #continuousform}

For every $\varepsilon>0$ there is $g\in C([0,1])$ with $m\{x:f(x)\ne
g(x)\}<\varepsilon$.

::: pf-proof

Given $\varepsilon$, Lusin's theorem gives compact $K$ with $m([0,1]\setminus
K)<\varepsilon$ and $f|_K$ continuous; discarding a further null subset we may
suppose $f$ is finite and bounded on $K$, since $f$ is finite a.e. and a
continuous function on a compact set is bounded. By the Tietze extension
theorem $f|_K$, a continuous real function on the closed subset $K$ of the
normal space $[0,1]$, extends to $g\in C([0,1])$ with $\sup_{[0,1]}\abs
g=\sup_K\abs{f}$. Then $\{x:f(x)\ne g(x)\}\subseteq[0,1]\setminus K$, which
has measure $<\varepsilon$.

:::

:::

::: {.pf-step #density}

For $f\in L^1([0,1])$ and $\varepsilon>0$ there is $g\in C([0,1])$ with
$\int_0^1\abs{f-g}\,dm<\varepsilon$; hence $C([0,1])$ is dense in $L^1[0,1]$.

::: pf-proof

First replace $f$ by the bounded $f_N=f\mathbf 1_{\{\abs f\le N\}}$, which
satisfies $\int\abs{f-f_N}\le\int_{\{\abs f>N\}}\abs f\to0$ by dominated
convergence with dominating function $\abs f$, and choose $N$ so that
$\int\abs{f-f_N}<\varepsilon/2$. By step [](#continuousform){.pf-ref} applied
to $f_N$ there is $g\in C([0,1])$ with $f_N=g$ off a set of measure less than
$\varepsilon/(4(N+1))$; then $\int\abs{f_N-g}\le2N\cdot m\{f_N\ne
g\}<\varepsilon/2$. So $\int\abs{f-g}<\varepsilon$ by the triangle inequality
for the integral, which is the assertion that continuous functions approximate
any integrable function in $L^1$.

:::

:::

:::


:::
