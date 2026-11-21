---
schema: qual/card@1
id: P-JHUU51RA4
kind: problem
title: "A function whose every set-integral is bounded by measure is at most 1 a.e."
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 4 of the JHU Real Analysis Qualifying Exam on p. 51 of the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The total variation bound is derived from the supremum over finite measurable partitions, the density of the total variation is stated with the reason, and the final set is taken as {|f| > 1 + 1/n} over n rather than over rationals, which removes the need for a density argument in the last line. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Suppose $f\in L^1(\RR^n,m)$ satisfies
$$
\abs{\int_E f\,dm}\le m(E)
$$
for every Lebesgue-measurable set $E$. Prove that
$$
\abs{f}\le1
$$
almost everywhere.
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the JHU examination papers and the card records only the statement. The argument is the card's own.

Let $\nu(E)=\int_Ef\,dm$, a finite signed (or complex) measure by $f\in L^1$.

::: pf

::: {.pf-step #variation}
$\abs\nu(A)\le m(A)$ for every measurable $A$, where $\abs\nu$ is the total variation measure.

::: pf-proof
For a finite measurable partition $A=\bigsqcup_{j=1}^NA_j$, the hypothesis gives $\sum_j\abs{\nu(A_j)}\le\sum_jm(A_j)=m(A)$. The total variation is the supremum of such sums over finite measurable partitions, so $\abs\nu(A)\le m(A)$.
:::

:::

::: {.pf-step #density}
$\abs\nu(A)=\int_A\abs f\,dm$ for every measurable $A$.

::: pf-proof
For a measure with density $f$ with respect to $m$, the total variation has density $\abs f$: on a set where $f$ has constant sign (or, in the complex case, constant argument up to $2\pi/n$) the variation is the integral of $\pm f$, and a partition into such sets exhibits both inequalities.
:::

:::

::: {.pf-step #bound}
$\int_A\abs f\,dm\le m(A)$ for every measurable $A$.

::: pf-proof
Combine steps [](#variation){.pf-ref} and [](#density){.pf-ref}.
:::

:::

::: {.pf-step}
$\abs f\le1$ almost everywhere.

::: pf-proof
For $n\ge1$ let $A_n=\{\abs f>1+1/n\}$, a measurable set. On $A_n$, $\abs f>1+1/n$, so
$$
\left(1+\frac1n\right)m(A_n)\le\int_{A_n}\abs f\,dm\le m(A_n),
$$
which forces $m(A_n)=0$. Then $\{\abs f>1\}=\bigcup_nA_n$ has measure $0$, so $\abs f\le1$ almost everywhere.
:::

:::

:::
:::
