---
schema: qual/card@1
id: P-WESRA06-1
kind: problem
title: Cauchy sequences, completeness, and Baire category
classification:
  areas: [real-analysis]
  topics: [Metric Spaces, Baire Category]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 17: the Real Analysis Preliminary
    Examination, 2006, item 1. The page had cited only the extraction; it now names the
    examination, its item and the page of the scan. The statement is unchanged.

---

::: {.problem}
Let $(X,d)$ be a metric space.

1. Define a Cauchy sequence in $(X,d)$.

2. Prove that every convergent sequence in $(X,d)$ is Cauchy.

3. Define completeness of $(X,d)$.

4. State one form of Baire's category theorem.
:::

::: {.solution}
The item is item 1 of the Real Analysis Preliminary Examination, 2006 (On a metric space: Cauchy sequence, convergent implies Cauchy, completeness, Baire), on the first page
of that paper, PDF p. 17 of the retained scan assets/attachments/analysis_2003-2007.pdf.


::: pf

::: pf-step

Cauchy sequences.

::: pf-proof

A sequence $(x_n)$ in $X$ is Cauchy if for every $\varepsilon>0$ there exists $N$ such that
$$
m,n\ge N\quad\Longrightarrow\quad d(x_m,x_n)<\varepsilon.
$$

:::

:::

::: pf-step

Every convergent sequence is Cauchy.

::: pf-proof

Suppose $x_n\to x\in X$.
Given $\varepsilon>0$, choose $N$ such that
$$
n\ge N\quad\Longrightarrow\quad d(x_n,x)<\frac\varepsilon2.
$$
Then for $m,n\ge N$, the triangle inequality gives
$$
d(x_m,x_n)\le d(x_m,x)+d(x,x_n)<\varepsilon.
$$
Hence $(x_n)$ is Cauchy.

:::

:::

::: pf-step

Completeness.

::: pf-proof

The metric space $(X,d)$ is complete if every Cauchy sequence in $X$ converges to a point of $X$.

:::

:::

::: pf-step

Baire category theorem.

::: pf-proof

One standard form is: if $(X,d)$ is a nonempty complete metric space and $U_1,U_2,\ldots$ are open dense subsets of $X$, then
$$
\bigcap_{n=1}^\infty U_n
$$
is dense in $X$.

Equivalently, a nonempty complete metric space cannot be written as a countable union of closed sets with empty interior.

:::

:::

:::

:::
