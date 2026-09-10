---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS2A-HW3
kind: problem
title: Identify hypotheses relating compact and closed sets (warm-up)
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
What property on a space guarantees that compact sets are closed?
What property on a space guarantees that closed sets are compact?
:::

::: {.solution}
If a space is **Hausdorff**, every compact subset is closed.

If a space is **compact**, every closed subset is compact: if \(F\subseteq X\) is closed and \(\{U_\alpha\}\) covers \(F\), then
\[
\{U_\alpha\}\cup\{X\setminus F\}
\]
is an open cover of \(X\); a finite subcover of \(X\) restricts to a finite subcover of \(F\).

Thus Hausdorffness guarantees “compact \(\Rightarrow\) closed,” while compactness guarantees “closed \(\Rightarrow\) compact.”
:::
