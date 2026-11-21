---
schema: qual/card@1
id: P-WESRA08-II1
kind: problem
title: The nonzero set of an integrable function is sigma-finite
classification:
  areas: [real-analysis]
  topics: [Measure Theory, L1 Spaces]
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
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Re-read the problem in the collection's checked-in extraction of the examination,
    assets/attachments/analysis_2008-2013_extracted.md, under "Real Analysis Preliminary Examination
    July 8, 2008", section 2, problem 1, which reads: "Let (X, B, mu) be a measure space and f: X -> R
    an integrable function. Prove that {x in X | f(x) != 0} is a countable union of sets of finite
    measure." The stored statement is that, with the set displayed. The collection's provenance is the
    examination paper alone, so no retained solution set covers the problem and the argument is the
    card's own.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the prose solution into a Lamport proof. The prose chained three inequalities in one
    display and asserted measurability without comment; the steps now record that f is measurable
    because it is integrable so the level sets are measurable, that the two ends of the display are
    the two sides of the Markov estimate, and both inclusions of the set identity, the one that fails
    for a fixed threshold being supplied by choosing n above 1/|f(x)|. The boxed conclusion is
    unchanged.
---

::: {.problem}
Let $(X,\mathcal B,\mu)$ be a measure space and let $f:X\to\RR$ be integrable.
Prove that
$$
\{x\in X:f(x)\ne0\}
$$
is a countable union of sets of finite measure.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this problem; the argument is the card's own. Write $\norm{f}_{1}=\int_{X}\abs{f}\,d\mu$ and $E_{n}=\theset{x\in X:\abs{f(x)}\ge 1/n}$ for $n\ge1$.

::: pf

::: {.pf-step #measurable}
Each $E_{n}$ is measurable.

::: pf-proof
An integrable function is measurable, so $\abs{f}$ is measurable, and $E_{n}$ is the preimage under $\abs{f}$ of the closed set $[1/n,\infty)$.
:::

:::

::: {.pf-step #finite-measure}
$\mu(E_{n})\le n\norm{f}_{1}<\infty$.

::: pf-proof
On $E_{n}$ the integrand satisfies $\abs{f}\ge 1/n$, so $\frac{1}{n}\mu(E_{n})=\int_{E_{n}}\frac{1}{n}\,d\mu\le\int_{E_{n}}\abs{f}\,d\mu$; monotonicity of the integral then gives $\int_{E_{n}}\abs{f}\,d\mu\le\int_{X}\abs{f}\,d\mu=\norm{f}_{1}$. Combining, $\mu(E_{n})\le n\norm{f}_{1}$, which is finite because $f$ is integrable.
:::

:::

::: {.pf-step #union}
$\theset{x\in X:f(x)\ne0}=\bigcup_{n\ge1}E_{n}$.

::: pf-proof
If $f(x)\ne0$ then $\abs{f(x)}>0$, and choosing $n>1/\abs{f(x)}$ gives $\abs{f(x)}>1/n$, so $x\in E_{n}$; hence the left side lies in the union. Conversely $x\in E_{n}$ means $\abs{f(x)}\ge1/n>0$, so $f(x)\ne0$ and the union lies in the left side.
:::

:::

::: {.pf-step #answer}
$\boxed{\theset{x\in X:f(x)\ne0}=\bigcup_{n\ge1}E_{n}}$ is a countable union of sets of finite measure.

::: pf-proof
Step [](#union){.pf-ref} is the set identity, step [](#measurable){.pf-ref} makes each member a measurable set and step [](#finite-measure){.pf-ref} gives $\mu(E_{n})<\infty$; the index set is the positive integers, so this is a countable union of sets of finite measure, as the problem asks.
:::

:::

:::
:::
