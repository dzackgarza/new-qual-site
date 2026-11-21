---
schema: qual/card@1
id: P-WESRA07-I6
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
  note: Checked against Part I, item 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
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
    2007, Part I item 6 (assets/attachments/analysis_2003-2007.pdf, PDF page 1),
    from the checked-in MinerU extraction and a 300 dpi render of the page. The
    printed item is "The Radon-Nikodym theorem", under "Give precise statements
    of the following". The card states it for sigma-finite positive measures
    with the density unique up to a.e. equality, which is the standard form, so
    no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    No published solution set is retained for this examination. The statement is
    the answer; the proof block proves the uniqueness clause, which is part of
    the theorem and is what the word "the" density rests on.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The uniqueness step wrote 0 = integral over D_k of (h' - h) dnu, which subtracts two
    integrals that may both be infinite. It now restricts to measurable subsets of D_k on
    which both measures are finite, possible by sigma-finiteness, integrates h' >= h + 1/k
    there without subtracting, and exhausts D_k by countably many such sets. The theorem
    and its conclusion are unchanged.

---

::: {.problem}
Give a precise statement of the Radon--Nikodym theorem.
:::

::: {.solution}

Let $(X,\mathcal A)$ be a measurable space and let $\mu,\nu$ be
$\sigma$-finite positive measures with $\mu\ll\nu$. Then there is a measurable
$h\colon X\to[0,\infty]$ with
$$
\mu(E)=\int_Eh\,d\nu\qquad\text{for all }E\in\mathcal A,
$$
and $h$ is unique up to $\nu$-almost-everywhere equality; it is written
$h=\frac{d\mu}{d\nu}$.

::: pf

::: {.pf-step #uniqueness}

If $h,h'$ are measurable, $[0,\infty]$-valued, and
$\int_Eh\,d\nu=\int_Eh'\,d\nu$ for every $E\in\mathcal A$, then $h=h'$
$\nu$-almost everywhere.

::: pf-proof

Let $D=\{h'>h\}=\bigcup_{k\ge1}D_k$ where $D_k=\{h'>h+1/k\}$, each measurable.
On $D_k$ we have $h<\infty$, so the difference $h'-h$ is defined there and exceeds
$1/k$. Fix a measurable $E\subseteq D_k$ with $\mu(E)<\infty$ and $\nu(E)<\infty$;
such sets exhaust $D_k$, because both measures are $\sigma$-finite. Integrating
the inequality over $E$ subtracts no infinite quantities and gives
$$
\mu(E)=\int_Eh'\ \ge\ \int_Eh+\tfrac1k\,\nu(E)=\mu(E)+\tfrac1k\,\nu(E),
$$
hence $\nu(E)=0$, and a countable exhaustion gives $\nu(D_k)=0$ for each $k$, so
$\nu(D)=\sum_k\nu(D_k)=0$. Exchanging $h$
and $h'$ gives $\nu(\{h>h'\})=0$, so $h=h'$ off the null set
$\{h>h'\}\cup\{h'>h\}$.

:::

:::

::: {.pf-step #statement}

Under $\mu\ll\nu$ and $\sigma$-finiteness, such an $h$ exists, so the pair
(existence, uniqueness) is the theorem as stated; and $h$ is determined on the
set where $\nu$ is concentrated.

::: pf-proof

Existence is the substance of the Radon-Nikodym theorem and is not proved
here: it is what the printed item asks the candidate to state. The uniqueness
proved in step [](#uniqueness){.pf-ref} says two densities differ only on a
$\nu$-null set, so the class of $h$ in $L^1(\nu)$ is determined by $\mu$, and
$\mu(E)=\int_Eh\,d\nu$ then holds for every measurable $E$, which is the
assertion of the theorem together with the notation $\frac{d\mu}{d\nu}$. The
$\sigma$-finite hypothesis is what makes the passage from finite measure to
general measure available through a countable partition of $X$ into sets of
finite $\nu$-measure.

:::

:::

:::


:::
