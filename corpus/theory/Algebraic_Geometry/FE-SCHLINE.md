---
schema: qual/card@1
id: FE-SCHLINE
kind: example
title: The line with a doubled origin
classification:
  areas:
  - algebraic-geometry
  topics:
  - Schemes
  - Separatedness
  - Gluing
relations:
- kind: uses
  target: D-SCHGLUE
review: draft
prompts:
- Give a scheme that is not separated.
- Why is the diagonal used to define separatedness?
---

::: {.example}
Glue two copies of $\AA^1\slice k$ along $\AA^1 \sm \ts{0}$ by the identity.
The result $X$ is a scheme with two points $0_1, 0_2$ whose every neighbourhood meets every neighbourhood of the other.
:::

::: {.remark}
$X$ is the standard answer to "give a non-separated scheme", and the follow-up is always why the Hausdorff condition was replaced by the diagonal.
The Zariski topology is never Hausdorff, so the topological condition is useless; the workable replacement asks that
\[
\Delta: X \to \fiberprod{X}{S}{X}
\]
be a closed immersion, which for topological spaces with the product topology recovers Hausdorff exactly.

On $X$ the diagonal is not closed: its closure contains $(0_1, 0_2)$.
The visible symptom is a failure of uniqueness — the two morphisms $\AA^1 \to X$ picking out the two origins agree on $\AA^1 \sm \ts{0}$ but not on $\AA^1$ — and non-separatedness is exactly the statement that a morphism is not determined by its restriction to a dense open.
:::
