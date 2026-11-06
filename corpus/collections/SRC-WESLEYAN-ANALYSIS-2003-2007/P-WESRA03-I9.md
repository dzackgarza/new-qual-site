---
schema: qual/card@1
id: P-WESRA03-I9
kind: problem
title: Uniform convergence on the real line need not imply convergence of integrals
classification:
  areas: [real-analysis]
  topics: [Integration, Uniform Convergence]
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
    Read against the Wesleyan Preliminary Examination, Analysis, August 4, 2003,
    section I, item 9 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render,
    then re-read at 300 dpi because the printed symbol is defective: the page
    prints "implies the integral of f_n dm = 0" with a handwritten
    "lim n -> infinity" inserted under the integral sign, which is the intended
    reading lim_n integral f_n dm = 0. The card asks "Must the integral tend to
    0?", which is that reading; it is not a repair of the printed words but a
    resolution of a handwritten annotation on the scan, and it is recorded here
    as such.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The
    counterexample is derived here, a uniformly small tall-enough bump whose
    integral does not go to zero because the domain has infinite measure.
---

::: {.problem}
Suppose $f_n:\RR\to\RR$ are integrable and $f_n\to0$ uniformly on $\RR$.
Must
$$
\int_{\RR}f_n\,dm\longrightarrow0?
$$
:::

::: {.solution}

No: uniform convergence to $0$ on a set of infinite measure does not force the
integrals to tend to $0$.

::: pf

::: {.pf-step #example}

$f_n=\frac1n\mathbf 1_{[0,n]}$ is integrable, $\norm{f_n}_\infty=\frac1n\to0$,
and $\int_\RR f_n\,dm=1$ for every $n$.

::: pf-proof

$f_n$ is a bounded measurable function supported on the finite-measure set
$[0,n]$, so it lies in $L^1(\RR)$; its supremum is $\frac1n$, attained on
$[0,n]$; and $\int_\RR f_n\,dm=\frac1n\cdot m([0,n])=\frac1n\cdot n=1$.

:::

:::

::: {.pf-step #uniform}

$f_n\to0$ uniformly on $\RR$, so the hypotheses of the printed question are
met.

::: pf-proof

$\sup_{x\in\RR}\abs{f_n(x)-0}=\frac1n\to0$, which is precisely uniform
convergence to the zero function. So a sequence of integrable functions
converging uniformly to $0$ has integrals identically $1$, and $\lim_n\int_\RR
f_n\,dm=1\ne0$.

:::

:::

::: {.pf-step #answer}

The answer is no, and the missing hypothesis is integrability of a dominating
function or finiteness of the measure of the domain.

::: pf-proof

Steps [](#example){.pf-ref} and [](#uniform){.pf-ref} exhibit the failure. On
a set of finite measure, uniform convergence to $0$ does give $\int f_n\to0$,
since $\abs{f_n}\le\varepsilon_n$ with $\varepsilon_n\to0$ and
$\int\abs{f_n}\le\varepsilon_n\mu(X)$; on $\RR$ the same bound is useless
because $\mu(X)=\infty$. This is why the dominated convergence theorem
requires a fixed integrable dominating function and not merely a bound tending
to zero.

:::

:::

:::


:::
