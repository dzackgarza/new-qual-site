---
schema: qual/card@1
id: P-WESRA04-T1
kind: problem
title: State the Lebesgue monotone convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.1, item 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.1 item 1 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 34, printed page 2), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item is "State the Lebesgue monotone
    convergence theorem." The card states it for a nondecreasing sequence of
    nonnegative measurable functions with both sides allowed to be infinite,
    which is the standard statement, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. Beyond the
    statement, the proof block proves the theorem from the simple-function case,
    so the card carries the argument and not only the assertion.
---

::: {.problem}
State the Lebesgue monotone convergence theorem.
:::

::: {.solution}

Let $(X,\mathcal A,\mu)$ be a measure space and $0\le f_1\le f_2\le\cdots$
measurable with $f=\lim_nf_n$ pointwise, values in $[0,\infty]$. The monotone
convergence theorem asserts
$$
\boxed{\int_Xf\,d\mu=\lim_{n\to\infty}\int_Xf_n\,d\mu,}
$$
both sides allowed to be $+\infty$.

::: pf

::: {.pf-step #measurable}

$f$ is measurable and $\int f_n$ is a nondecreasing sequence with a limit in
$[0,\infty]$.

::: pf-proof

$f(x)=\sup_nf_n(x)$ and a countable supremum of measurable functions is
measurable, since $\{f\le c\}=\bigcap_n\{f_n\le c\}$ for each real $c$. Since
$f_n\le f_{n+1}$ pointwise, monotonicity of the integral gives $\int
f_n\le\int f_{n+1}$, so the sequence of integrals increases and has a limit in
$[0,\infty]$; and $\int f_n\le\int f$ for every $n$ by $f_n\le f$, so the
limit is at most $\int f$.

:::

:::

::: {.pf-step #simple}

For a simple $\varphi=\sum_{i=1}^ma_i\mathbf 1_{A_i}\ge0$ with $\varphi\le f$
and a constant $0<c<1$, one has
$c\int_X\varphi\,d\mu\le\liminf_n\int_Xf_n\,d\mu$.

::: pf-proof

The sets $A_{i,n}=A_i\cap\{f_n\ge ca_i\}$ are measurable and increase with $n$
to $A_i$, because on $A_i$ we have $ca_i\le cf\le f$ (as $c<1$ and $f\ge a_i$
there) and $f_n\uparrow f$. So $\mu(A_{i,n})\to\mu(A_i)$ by continuity from
below, whence $\sum_ia_i\mu(A_{i,n})\to\sum_ia_i\mu(A_i)=\int\varphi\,d\mu$,
that is $c\int\varphi\,d\mu=\lim_n\sum_ica_i\mu(A_{i,n})$. On $A_{i,n}$ we
have $ca_i\le f_n$, so $\sum_ica_i\mathbf 1_{A_{i,n}}\le f_n$ pointwise, and
integrating gives $\sum_ica_i\mu(A_{i,n})\le\int_Xf_n\,d\mu$ for every $n$.
Taking $\liminf$ proves the claim.

:::

:::

::: {.pf-step #theorem}

$\int_Xf\,d\mu=\lim_n\int_Xf_n\,d\mu$.

::: pf-proof

Let $\varphi\le f$ be simple and $c<1$; step [](#simple){.pf-ref} gives
$c\int\varphi\le\liminf_n\int f_n$ for every such $c$, so letting $c\uparrow1$
gives $\int\varphi\le\liminf_n\int f_n$, and then taking the supremum over all
simple $0\le\varphi\le f$, which by definition of the integral equals $\int
f$, gives $\int f\le\liminf_n\int f_n$. Step [](#measurable){.pf-ref} gives
$\limsup_n\int f_n\le\int f$ and also that the limit exists. Combining, $\int
f\le\liminf\le\limsup\le\int f$, so all are equal.

:::

:::

:::


:::
