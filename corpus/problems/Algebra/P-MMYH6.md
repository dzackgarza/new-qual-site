---
schema: qual/card@1
id: P-MMYH6
kind: problem
title: $S_3$ is not nilpotent
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Permutations
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that $S_3$ is not nilpotent.
:::

::: {.solution}
A finite nilpotent group has all Sylow subgroups normal.

In $S_3$, the Sylow $2$-subgroups are
\[
\langle(12)\rangle,
\qquad
\langle(13)\rangle,
\qquad
\langle(23)\rangle.
\]
Thus there are three Sylow $2$-subgroups, so none is normal.

Therefore $S_3$ is not nilpotent.

Equivalently, its lower central series does not terminate at the identity: since
\[
[S_3,S_3]=A_3
\]
and $[A_3,S_3]=A_3$, the lower central series stabilizes at $A_3\ne1$.
:::
