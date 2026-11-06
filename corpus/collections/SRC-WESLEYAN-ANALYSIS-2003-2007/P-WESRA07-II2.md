---
schema: qual/card@1
id: P-WESRA07-II2
kind: problem
title: L1 convergence implies convergence in measure
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
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
    2007, Part II problem 2 (assets/attachments/analysis_2003-2007.pdf, PDF page
    1), from the checked-in MinerU extraction and a 300 dpi render of the page.
    The printed problem supposes f_n, f in L^1 with the L^1 distance tending to
    zero and asks for convergence in measure, for all a > 0. The card states
    exactly this, so no repair was needed. The printed extraction garbles the
    quantifier over a as "pmb a" and the limit sign; the render shows a > 0 and
    the limit as n tends to infinity.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination; the proof is
    derived here, from the elementary inequality a mu(E_n) <= the tail integral.
---

::: {.problem}
Let $(X,\mathcal A,\mu)$ be a measure space.
Suppose $f_n,f\in L^1(X,\mu)$ and
$$
\int_X\abs{f_n-f}\,d\mu\longrightarrow0.
$$
Prove that for every $a>0$,
$$
\mu\{x:\abs{f_n(x)-f(x)}>a\}\longrightarrow0.
$$
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and $f_n,f\in L^1(X,\mu)$ with
$\int_X\abs{f_n-f}\,d\mu\to0$.

::: pf

::: {.pf-step #markov}

For $a>0$ and $E_n=\{x:\abs{f_n(x)-f(x)}>a\}$, one has
$a\,\mu(E_n)\le\int_X\abs{f_n-f}\,d\mu$.

::: pf-proof

$E_n$ is measurable because $\abs{f_n-f}$ is measurable and $(a,\infty)$ is
open. On $E_n$ the integrand $\abs{f_n-f}$ exceeds $a$, so
$$
\int_{E_n}\abs{f_n-f}\,d\mu\ \ge\ a\,\mu(E_n),
$$
using monotonicity of the integral and the fact that the constant $a$
integrates to $a\mu(E_n)$ over a set of finite measure, which $E_n$ has since
$a\mu(E_n)\le\int_X\abs{f_n-f}<0+\infty$. Adding the integral over $X\setminus
E_n$, which is $\ge0$, gives the stated inequality.

:::

:::

::: {.pf-step #inmeasure}

$\mu(E_n)\to0$ as $n\to\infty$, so $f_n\to f$ in measure.

::: pf-proof

Rearranging step [](#markov){.pf-ref} gives
$\mu(E_n)\le\frac1a\int_X\abs{f_n-f}\,d\mu$, and the right-hand side tends to
$0$ because $\int_X\abs{f_n-f}$ does and $1/a$ is fixed. As $a>0$ was
arbitrary, the superlevel sets of the difference have measures tending to
zero, which is convergence in measure.

:::

:::

:::


:::
