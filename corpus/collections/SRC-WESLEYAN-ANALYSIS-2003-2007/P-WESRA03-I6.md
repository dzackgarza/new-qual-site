---
schema: qual/card@1
id: P-WESRA03-I6
kind: problem
title: Lebesgue integrability does not imply Riemann integrability
classification:
  areas: [real-analysis]
  topics: [Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Short Answer Question 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    section I, item 6 (assets/attachments/analysis_2003-2007.pdf, PDF page 37,
    printed page 1), from the checked-in MinerU extraction and a 100 dpi render
    of the page. The printed item is "Is every bounded real-valued function on
    [0,1] which is Lebesgue integrable also Riemann integrable?" The card asks
    the same question and answers no, with the Dirichlet function, so no repair
    was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The example and
    both verifications, of Lebesgue integrability and of the failure of Riemann
    integrability through the Darboux sums of every subinterval, are derived here.
---

::: {.problem}
Is every bounded real-valued function on $[0,1]$ that is Lebesgue integrable also Riemann integrable?
:::

::: {.solution}

No: boundedness and Lebesgue integrability on $[0,1]$ do not imply Riemann
integrability.

::: pf

::: {.pf-step #lebesgue}

The Dirichlet function $f=\mathbf 1_{\QQ\cap[0,1]}$ is bounded and Lebesgue
integrable, with $\int_0^1f\,dm=0$.

::: pf-proof

$f$ is bounded by $1$ and measurable, since $\QQ\cap[0,1]$ is countable and
hence a Borel set. A countable set has Lebesgue measure zero, being a
countable union of singletons, so $f=0$ almost everywhere and its integral is
$0$; being measurable and bounded on a finite measure space, $f$ lies in
$L^1$.

:::

:::

::: {.pf-step #riemann}

$f$ is not Riemann integrable.

::: pf-proof

Let $[c,d]\subseteq[0,1]$ with $c<d$. Every nonempty open interval contains a
rational and an irrational, so $f$ takes both values $1$ and $0$ on $[c,d]$;
hence $\sup_{[c,d]}f=1$ and $\inf_{[c,d]}f=0$. For any partition the upper
Darboux sum is therefore $\sum_j1\cdot(x_j-x_{j-1})=1$ and the lower Darboux
sum is $0$, so the upper and lower integrals are $1$ and $0$; they differ, and
$f$ is not Riemann integrable.

:::

:::

::: {.pf-step #answer}

The answer to the printed question is no.

::: pf-proof

Step [](#lebesgue){.pf-ref} gives a bounded Lebesgue integrable function on
$[0,1]$, and step [](#riemann){.pf-ref} shows it is not Riemann integrable, so
the implication fails. The obstruction is precisely that the function is
discontinuous everywhere, which is the content of Lebesgue's criterion: a
bounded function on an interval is Riemann integrable exactly when its set of
discontinuities has measure zero.

:::

:::

:::


:::
