---
schema: qual/card@1
id: P-WESRA04-P5
kind: problem
title: Equality of all restricted integrals forces equality almost everywhere
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Integration]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.3, problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.3 problem 5 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 35, printed page 3), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed problem supposes f and g integrable
    with equal integrals over every measurable A and asks for f = g mu-a.e. The
    card states exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The proof is
    derived here, by applying the hypothesis to the level sets of the difference.
---

::: {.problem}
Let $f,g$ be integrable functions on a measure space $(X,\mathcal B,\mu)$.
Suppose that
$$
\int_A f\,d\mu=\int_A g\,d\mu
$$
for every $A\in\mathcal B$.
Prove that $f=g$ almost everywhere.
:::

::: {.solution}

Let $f,g\in L^1(X,\mathcal B,\mu)$ with $\int_Af\,d\mu=\int_Ag\,d\mu$ for
every $A\in\mathcal B$.

::: pf

::: {.pf-step #difference}

$h=f-g$ lies in $L^1(\mu)$ and $\int_Ah\,d\mu=0$ for every $A\in\mathcal B$.

::: pf-proof

$h$ is measurable and $\abs h\le\abs f+\abs g$ with the right side integrable,
so $h\in L^1$; and $\int_Ah=\int_Af-\int_Ag=0$ by linearity of the integral
for integrable functions, the two integrals being finite.

:::

:::

::: {.pf-step #levelsets}

$\mu\{h>0\}=0$ and $\mu\{h<0\}=0$.

::: pf-proof

For $n\ge1$ let $E_n=\{h>1/n\}$, measurable. On $E_n$ the integrand $h$
exceeds $1/n$, so $0=\int_{E_n}h\,d\mu\ge\frac1n\mu(E_n)$, forcing
$\mu(E_n)=0$. Since $\{h>0\}=\bigcup_nE_n$, countable subadditivity gives
$\mu\{h>0\}=0$. Applying the same argument to $-h$, which also has vanishing
integrals over every $A$, gives $\mu\{h<0\}=0$.

:::

:::

::: {.pf-step #conclusion}

$f=g$ $\mu$-almost everywhere.

::: pf-proof

$\{h\ne0\}=\{h>0\}\cup\{h<0\}$ is a union of two null sets by step
[](#levelsets){.pf-ref}, hence null, so $f(x)=g(x)$ off a null set. For
complex-valued $f,g$ the same argument applied to $\operatorname{Re}h$ and
$\operatorname{Im}h$ separately, each of which has vanishing integrals over
every $A$ by linearity, gives the same conclusion.

:::

:::

:::


:::
