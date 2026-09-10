---
schema: qual/card@1
id: E-VXB5V
kind: problem
title: Discrete spaces have dimension zero
classification:
  areas:
  - topology
  topics:
  - Dimension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Show that any discrete space has dimension 0.
:::

::: {.solution}
Let \(\mathcal U\) be an open cover of a discrete space \(X\). The family of singletons
\[
\mathcal V=\{\{x\}:x\in X\}
\]
is an open cover refining \(\mathcal U\): for each \(x\), choose \(U_x\in\mathcal U\) containing \(x\), and then \(\{x\}\subset U_x\). No point belongs to more than one member of \(\mathcal V\), so \(\mathcal V\) has order \(1\). Thus \(\dim X\le0\). For a nonempty space the dimension cannot be less than \(0\), hence \(\dim X=0\). (The empty space has the conventional dimension \(-1\).)
:::
