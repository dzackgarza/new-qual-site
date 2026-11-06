---
schema: qual/card@1
id: P-WESRA04-E3
kind: problem
title: Functions separating $L^2(\RR)$ and $L^3(\RR)$
classification:
  areas: [real-analysis]
  topics: [Function Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.2, item 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.2 item 3 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item 3 has two parts, (a) a function
    in L^2(R) but not in L^3(R) and (b) a function in L^3(R) but not in L^2(R),
    and the section waives proof that the examples have the properties. The card
    states both parts, in the same order, so no repair was needed; the extraction
    loses the (a)/(b) labels, which the render supplies.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The two examples
    are given with the power computations that verify their integrability and
    non-integrability, which is more than the printed instruction requires.
---

::: {.problem}
Give examples of

1. a real-valued function in $L^2(\RR)$ but not in $L^3(\RR)$;

2. a real-valued function in $L^3(\RR)$ but not in $L^2(\RR)$.
:::

::: {.solution}

Write $\mathbf 1_E$ for the indicator of a set $E$; in both examples the
function is supported on a set of infinite measure or has a singularity, and
the two behaviours are separated by the convergence of $\int x^{-p}$ at $0$
and at $\infty$.

::: pf

::: {.pf-step #l2notl3}

$f(x)=x^{-2/5}\mathbf 1_{(0,1)}(x)$ satisfies $f\in L^2(\RR)\setminus
L^3(\RR)$.

::: pf-proof

$\int_\RR\abs f^2=\int_0^1x^{-4/5}\,dx=\left[5x^{1/5}\right]_0^1=5<\infty$,
since the exponent $-4/5$ exceeds $-1$. And $\int_\RR\abs
f^3=\int_0^1x^{-6/5}\,dx=\left[-5x^{-1/5}\right]_{0}^{1}$, which diverges,
since the exponent $-6/5$ is at most $-1$ and the integral near $0$ of
$x^{-6/5}$ is infinite. So $f$ is square integrable and not cube integrable.

:::

:::

::: {.pf-step #l3notl2}

$g(x)=x^{-2/5}\mathbf 1_{[1,\infty)}(x)$ satisfies $g\in L^3(\RR)\setminus
L^2(\RR)$.

::: pf-proof

$\int_\RR\abs g^3=\int_1^\infty
x^{-6/5}\,dx=\left[-5x^{-1/5}\right]_1^\infty=5<\infty$, since the exponent
$-6/5$ is below $-1$ and the integral converges at infinity. And $\int_\RR\abs
g^2=\int_1^\infty x^{-4/5}\,dx$, which diverges because $-4/5$ is above $-1$.
So $g$ is cube integrable and not square integrable.

:::

:::

::: {.pf-step #both}

The two examples answer (a) and (b) respectively.

::: pf-proof

$f$ is real-valued and measurable, lies in $L^2(\RR)$ and not in $L^3(\RR)$,
which is (a); $g$ is real-valued and measurable, lies in $L^3(\RR)$ and not in
$L^2(\RR)$, which is (b). No single function can serve for both, since $L^2$
and $L^3$ on a space of finite measure are not comparable in general; here the
finite measure is concentrated near $0$ for $f$ and near infinity for $g$,
which is exactly why the two examples differ in their supports.

:::

:::

:::


:::
