---
schema: qual/card@1
id: E-LZX97
kind: problem
title: Local metrizability criteria as cases of the Smirnov metrization theorem
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
X\text{ paracompact Hausdorff and locally metrizable}.
\]
Both criteria of §34 follow from it, because each hypothesis implies paracompactness.

In [[E-MQTBP]], \(X\) is compact Hausdorff and locally metrizable. Every compact Hausdorff space is paracompact, so the Smirnov theorem gives metrizability.

In [[E-KK77N]], \(X\) is regular, Lindelöf, and locally metrizable. Every regular Lindelöf space is paracompact: the construction in [[E-KVFCT]](a) gives a locally finite open refinement of every open cover. So the Smirnov theorem gives metrizability.

Conversely, compactness with the Hausdorff property and regularity with the Lindelöf property are two sufficient conditions for the paracompactness hypothesis of the Smirnov theorem.
:::
