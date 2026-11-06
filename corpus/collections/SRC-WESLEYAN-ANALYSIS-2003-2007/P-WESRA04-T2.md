---
schema: qual/card@1
id: P-WESRA04-T2
kind: problem
title: State the Radon--Nikodym theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis section 2.1, item 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    Real Analysis section 2.1 item 2 (assets/attachments/analysis_2003-2007.pdf,
    PDF page 34, printed page 2), from the checked-in MinerU extraction and a
    100 dpi render of the page. The printed item is "State the Radon-Nikodym
    theorem." The card states it for sigma-finite positive measures with the
    density unique up to a.e. equality, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The statement is
    the answer to the printed item; the proof block proves the well-posedness of
    the integral formula and the uniqueness half, which is part of the theorem.
---

::: {.problem}
State the Radon--Nikodym theorem.
:::

::: {.solution}

Let $(X,\mathcal A)$ be a measurable space and let $\mu,\nu$ be
$\sigma$-finite positive measures on it with $\mu\ll\nu$. The Radon-Nikodym
theorem asserts that there is a measurable $h\colon X\to[0,\infty]$ with
$$
\mu(E)=\int_Eh\,d\nu\qquad(E\in\mathcal A),
$$
unique up to $\nu$-almost-everywhere equality and written
$h=\frac{d\mu}{d\nu}$.

::: pf

::: {.pf-step #wellformed}

For fixed measurable $h\ge0$ the formula $E\mapsto\int_Eh\,d\nu$ defines a
measure, and two functions equal $\nu$-almost everywhere give the same
integrals over every $E$.

::: pf-proof

$E\mapsto\int_Eh\,d\nu$ is countably additive by monotone convergence applied
to the partial unions of a disjoint sequence, and vanishes on $\emptyset$, so
it is a measure. If $h=h'$ off a $\nu$-null set $N$ then
$\int_Eh=\int_{E\setminus N}h+\int_{E\cap N}h$ with $\nu(E\cap N)=0$ and $h$
finite $\nu$-a.e. on it, so the second term is $0$; the same computation for
$h'$ and the agreement on $E\setminus N$ give $\int_Eh=\int_Eh'$.

:::

:::

::: {.pf-step #uniqueness}

If $\int_Eh\,d\nu=\int_Eh'\,d\nu$ for every $E$, then $h=h'$ $\nu$-almost
everywhere, so a density is unique.

::: pf-proof

For $k\ge1$ let $D_k=\{h'>h+1/k\}$. On $D_k$ the integrand $h'-h$ exceeds
$1/k$, so $0=\int_{D_k}(h'-h)\,d\nu\ge\frac1k\nu(D_k)$ and $\nu(D_k)=0$. Hence
$\nu(\{h'>h\})=\nu(\bigcup_kD_k)=0$, and exchanging the roles of $h$ and $h'$
gives $\nu(\{h>h'\})=0$; off the union of those null sets the two functions
agree. Any two candidate densities satisfy the hypothesis by the theorem's
equation, so they agree a.e. and the class of $h$ is determined by $\mu$.

:::

:::

::: {.pf-step #existence}

Existence of $h$ under $\sigma$-finiteness and $\mu\ll\nu$ is the substance of
the theorem and is the assertion being stated.

::: pf-proof

The printed item asks the candidate to state the theorem, so existence is
recorded rather than re-proved here; what the two preceding steps establish is
that the assertion is well posed and sharp, the measure being recovered by
integration against $h$ and $h$ being determined only as a $\nu$-a.e. class,
which is the content of the notation $\frac{d\mu}{d\nu}$ and of calling $h$
the Radon-Nikodym derivative.

:::

:::

:::


:::
