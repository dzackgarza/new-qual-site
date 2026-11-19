---
schema: qual/card@1
id: P-WESRA08-I5
kind: problem
title: State the Radon-Nikodym theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Radon-Nikodym Theorem]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The exercise asks for a statement, not a proof, so the structure is a decomposition of the
    statement: setting, hypotheses, the existence clause, the uniqueness clause, and the
    demonstration that neither hypothesis can be dropped. Statement checked against the
    retained extraction of the Wesleyan Real Analysis Preliminary Examination of June 2013,
    Part I item 2, line 105 of assets/attachments/analysis_2008-2013_extracted.md, which reads
    "State the Radon-Nikodym theorem."; the extraction gives no page numbers, so the line is
    the locator. Added to the card's answer: the integrability of the density when nu is
    finite, uniqueness up to mu-almost-everywhere equality stated as a separate clause with
    its reason, and two witnesses — counting measure on [0,1] for sigma-finiteness and a point
    mass for absolute continuity — that the hypotheses are not redundant. No repair to the
    printed statement.
---

::: {.problem}
State the Radon-Nikodym theorem.
:::

::: {.solution}
The exercise asks for a statement rather than a proof, so what follows is the theorem decomposed into its parts, with a witness for each hypothesis showing that it cannot be dropped. The card's own objection to be met is that a bare display of a formula is not a statement: its hypotheses, its uniqueness clause, and the role of each hypothesis are separated below.

Throughout, $(X,\mathcal M)$ is a measurable space, $\mu$ and $\nu$ are positive measures on $\mathcal M$, $\sigma$-finite means $X=\bigcup_{n}X_n$ with $\mu(X_n)<\infty$ and likewise for $\nu$, and $\nu\ll\mu$ means $\mu(E)=0$ implies $\nu(E)=0$ for $E\in\mathcal M$.

::: pf

::: {.pf-step #hypotheses}
The theorem is stated for a measurable space with two positive measures, both $\sigma$-finite, the second absolutely continuous with respect to the first.

::: pf-proof
The hypotheses are: (i) $\mu$ and $\nu$ are positive measures on the same $\sigma$-algebra $\mathcal M$ of subsets of $X$; (ii) $\mu$ and $\nu$ are both $\sigma$-finite; (iii) $\nu\ll\mu$. Steps [](#existence){.pf-ref}, [](#uniqueness){.pf-ref} and [](#sharp){.pf-ref} show that (i) is the framework, that (ii) and (iii) are each needed, and that under all three the conclusion below holds.
:::

:::

::: {.pf-step #existence}
Under these hypotheses there is a measurable $f:X\to[0,\infty)$ with $\nu(E)=\int_{E}f\,d\mu$ for every $E\in\mathcal M$; if $\nu$ is finite then $f\in L^{1}(\mu)$. This $f$ is written $\frac{d\nu}{d\mu}$ and called the Radon-Nikodym derivative of $\nu$ with respect to $\mu$.

::: pf-proof
This is the existence clause of the theorem. The integrability claim is part of the statement rather than an extra hypothesis: taking $E=X$ in the displayed identity gives $\int_{X}f\,d\mu=\nu(X)<\infty$ when $\nu$ is finite, and $f\ge0$ makes the integral of $f$ well defined in $[0,\infty]$. For $\nu$ only $\sigma$-finite, $f$ is finite $\mu$-almost everywhere and integrable on each $X_n$ of a $\sigma$-finite exhaustion.
:::

:::

::: {.pf-step #uniqueness}
If $f$ and $g$ both satisfy $\nu(E)=\int_{E}f\,d\mu=\int_{E}g\,d\mu$ for all $E\in\mathcal M$, then $f=g$ $\mu$-almost everywhere.

::: pf-proof
Let $h=f-g$, which is measurable. The hypothesis gives $\int_{E}h\,d\mu=0$ for every measurable $E$. Taking $E=\{h>0\}$ and $E=\{h<0\}$ — measurable sets — shows $\int_{E}h^{+}=0$ and $\int_{E}h^{-}=0$, and a nonnegative measurable function with zero integral vanishes almost everywhere, so $h=0$ $\mu$-a.e.
:::

:::

::: {.pf-step #sharp}
Neither hypothesis (ii) nor (iii) can be dropped.

::: pf-proof
$\sigma$-finiteness: let $X=[0,1]$ with the Borel $\sigma$-algebra, $\mu$ Lebesgue measure and $\nu$ counting measure. Then $\mu(E)=0$ forces $E=\emptyset$, so $\nu\ll\mu$ holds; but $\nu$ is not $\sigma$-finite on $[0,1]$, and no density exists, since $\nu(\{t\})=1$ for each $t$ while $\int_{\{t\}}f\,d\mu=0$ for every measurable $f$.

Absolute continuity: let $X=[0,1]$, $\mu$ Lebesgue measure and $\nu=\delta_{0}$ the point mass at $0$. Then $\nu(\{0\})=1$ while $\mu(\{0\})=0$, so $\nu\ll\mu$ fails, and again no density exists: $\int_{\{0\}}f\,d\mu=0\neq1=\nu(\{0\})$. In both examples $\nu$ is a positive measure and $\mu$ is $\sigma$-finite, so the failure is attributable to the hypothesis named.
:::

:::

::: {.pf-step #statement}
The Radon-Nikodym theorem: for positive $\sigma$-finite $\mu,\nu$ on $(X,\mathcal M)$ with $\nu\ll\mu$, there is a measurable $f\ge0$ with $\nu(E)=\int_{E}f\,d\mu$ for all $E\in\mathcal M$, unique up to $\mu$-a.e. equality, denoted $d\nu/d\mu$.

::: pf-proof
Steps [](#hypotheses){.pf-ref}, [](#existence){.pf-ref} and [](#uniqueness){.pf-ref} give the statement with its hypotheses and its uniqueness clause, and step [](#sharp){.pf-ref} records that the hypotheses are exactly what the conclusion needs. That is the theorem as the exercise asks it to be stated.
:::

:::

:::
:::
