---
schema: qual/card@1
id: E-LZX97
kind: problem
title: Smirnov metrization versus the local metrizability exercises of section 34
classification:
  areas:
  - topology
  topics:
  - Metrizability
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Compare Theorem 42.1 (the Smirnov metrization theorem) with Exercises 7 and 8 of §34.
:::

::: {.solution}
The Smirnov metrization theorem says
\[
X\text{ metrizable}
\quad\Longleftrightarrow\quad
X\text{ paracompact and locally metrizable}.
\]
It subsumes the two local-metrizability criteria from §34 once their hypotheses are used to obtain paracompactness.

For Exercise 7 of §34, if \(X\) is compact Hausdorff and locally metrizable, then \(X\) is paracompact because every compact Hausdorff space is paracompact. Smirnov therefore gives metrizability immediately.

For Exercise 8 of §34, if \(X\) is regular, Lindelöf, and locally metrizable, then \(X\) is paracompact: the standard regular-Lindelöf argument produces a locally finite refinement of every open cover. Smirnov again yields metrizability.

Thus the two earlier exercises are special cases of Smirnov's theorem. Conversely, they illustrate two common sufficient hypotheses—compact Hausdorff, or regular Lindelöf—that guarantee the paracompactness condition appearing in Smirnov's characterization.
:::
