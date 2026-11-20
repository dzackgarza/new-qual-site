---
schema: qual/card@1
id: P-WESCA05-I4
kind: problem
title: "Define uniform continuity on an open set"
classification:
  areas: [complex-analysis]
  topics:
  - Uniform Continuity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1, item 4 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 25: the Complex Analysis Section of
    the Analysis Qualifier, Wesleyan University, Summer 2005, Section 1 item 4. The page had cited
    only the extraction; it now names the examination, its item and the page of the
    scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had
    answered the question, which STYLE-08 forbids; it is dropped, and the step that
    carries the result is now the QED step. No argument or statement changes.

---

::: {.problem}
Let $U\subseteq\CC$ be open.
Define what it means for a function $f:U\to\CC$ to be uniformly continuous on $U$.
:::

::: {.solution}
The item is Section 1 item 4 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (uniform continuity on an open set), in the retained scan `assets/attachments/analysis_2003-2007.pdf`.


::: pf

::: {.pf-step #s1-1}

The function $f:U\to\CC$ is **uniformly continuous on $U$** if for every $\varepsilon>0$ there exists $\delta>0$ such that for all $z,w\in U$,
$$
\abs{z-w}<\delta
\quad\Longrightarrow\quad
\abs{f(z)-f(w)}<\varepsilon.
$$


::: pf-proof

This is the definition of uniform continuity for the Euclidean metric on $U\subseteq\CC$ and the Euclidean metric on $\CC$.

:::

:::

::: pf-step

The essential distinction from ordinary continuity is that, once $\varepsilon$ is fixed, the same number $\delta$ must work simultaneously for every pair $z,w\in U$.


::: pf-proof

In pointwise continuity the permissible $\delta$ may depend on the base point. Uniform continuity requires a single $\delta=\delta(\varepsilon)$ independent of the point.

:::

:::


:::

:::
