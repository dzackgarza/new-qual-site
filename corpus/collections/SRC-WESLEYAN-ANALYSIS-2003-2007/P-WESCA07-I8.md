---
schema: qual/card@1
id: P-WESCA07-I8
kind: problem
title: "Define the arc length of a path"
classification:
  areas: [complex-analysis]
  topics:
  - Arc Length
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 8 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 7 (printed p. 2 of the 2007 complex-analysis paper). The card had cited neither the
    examination nor a page; it now names both, and the statement was compared with the
    printed item and left unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had answered
    the question, which STYLE-08 forbids; it is dropped, and the step that carries the
    result is now the QED step. No argument or statement changes.

- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The definition given is the standard one: the supremum of the sums of chord
    lengths over partitions of the interval, with the path called rectifiable when
    that supremum is finite, and the piecewise continuously differentiable case
    identified with the integral of the speed. Both statements are correct.
---

::: {.problem}
Define the arc length of a path $\gamma:[a,b]\to\CC$.
:::

::: {.solution}
The item is Section 1 item 8 of the Complex Analysis section of the Analysis Qualifier, Wesleyan University, Summer 2007 (the definition of the arc length of a path), in the retained scan `assets/attachments/analysis_2003-2007.pdf`.


::: pf

::: {.pf-step #s1-1}

The **arc length** of a continuous path $\gamma:[a,b]\to\CC$ is
$$
\boxed{
L(\gamma)
\coloneqq
\sup_P
\sum_{j=1}^m
\abs{\gamma(t_j)-\gamma(t_{j-1})},}
$$
where the supremum is taken over all partitions
$$
P:\quad a=t_0<t_1<\cdots<t_m=b.
$$


::: pf-proof

This is the definition of the length, or total variation, of the path. If the supremum is finite, the path is called rectifiable.

:::

:::

::: {.pf-step #s1-2}

If $\gamma$ is piecewise $C^1$, then
$$
\boxed{L(\gamma)=\int_a^b\abs{\gamma'(t)}\,dt.}
$$


::: pf-proof

For a piecewise $C^1$ path, the standard arc-length theorem identifies the partition-supremum definition in step [](#s1-1){.pf-ref} with the integral of the speed.

:::

:::


:::

:::
