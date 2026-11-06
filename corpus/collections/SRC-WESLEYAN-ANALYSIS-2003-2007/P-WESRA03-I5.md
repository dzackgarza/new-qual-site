---
schema: qual/card@1
id: P-WESRA03-I5
kind: problem
title: Uniformly bounded pointwise convergence on a finite-measure set
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 5 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item supposes E Lebesgue measurable with m(E) <
    infinity, a uniformly bounded sequence of real-valued measurable functions
    on E converging pointwise to f, and asks whether there is a relationship
    between the integrals, and if so what. The card states this and answers with
    the limit relation, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The answer is
    derived here, as an application of dominated convergence with the constant
    bound, which is integrable only because m(E) is finite.
---

::: {.problem}
Let $E\subset\RR$ be Lebesgue measurable with $m(E)<\infty$.
Suppose $(f_n)$ is a uniformly bounded sequence of real-valued measurable functions on $E$ and $f_n(x)\to f(x)$ for every $x\in E$.
What relationship holds between $\int_Ef_n\,dm$ and $\int_Ef\,dm$?
:::

::: {.solution}

Let $E\subseteq\RR$ be Lebesgue measurable with $m(E)<\infty$, let $f_n\colon
E\to\RR$ be measurable and uniformly bounded, say $\abs{f_n(x)}\le M$ for all
$n$ and all $x\in E$, and let $f_n\to f$ pointwise on $E$. Then
$$
\boxed{\lim_{n\to\infty}\int_Ef_n\,dm=\int_Ef\,dm.}
$$

::: pf

::: {.pf-step #domination}

$f$ is measurable with $\abs f\le M$ on $E$, and $M\mathbf 1_E\in L^1(\RR)$.

::: pf-proof

$f$ is a pointwise limit of measurable functions, hence measurable, and
$\abs{f(x)}=\lim_n\abs{f_n(x)}\le M$ at each $x\in E$. Since $m(E)<\infty$,
$\int_\RR M\mathbf 1_E\,dm=M\,m(E)<\infty$, so the constant bound is an
integrable dominating function; this is exactly where the hypothesis
$m(E)<\infty$ is used, and on a set of infinite measure the conclusion fails,
as $f_n=\mathbf 1_{[n,n+1]}$ on $\RR$ shows.

:::

:::

::: {.pf-step #interchange}

$\lim_n\int_Ef_n\,dm=\int_Ef\,dm$.

::: pf-proof

Extend $f_n$ and $f$ by $0$ off $E$; the extensions are measurable, converge
pointwise on $\RR$ (at points outside $E$ all terms vanish), and satisfy
$\abs{f_n}\le M\mathbf 1_E$ everywhere. The dominated convergence theorem with
dominating function $M\mathbf 1_E$, which is integrable by step
[](#domination){.pf-ref}, gives $\int_\RR f_n\,dm\to\int_\RR f\,dm$; the
integrals over $\RR$ of the extensions are the integrals over $E$ of the
original functions, so the stated relation holds.

:::

:::

:::


:::
