---
schema: qual/card@1
id: PR-C9ZEK
kind: proposition
title: Exactness is checked on stalks, and global sections are only left exact
classification:
  areas:
  - algebraic-geometry
  topics:
  - Stalks
  - Exact Sequences
  - Cohomology
relations:
- kind: uses
  target: T-3VX80
review: draft
prompts:
- How do you check that a sequence of sheaves is exact?
- Is a surjection of sheaves surjective on sections?
- Where does the failure of right exactness go?
---

::: {.proposition}
A sequence of sheaves $\mathcal{F} \to \mathcal{G} \to \mathcal{H}$ is exact exactly when
\[
\mathcal{F}_p \to \mathcal{G}_p \to \mathcal{H}_p
\]
is exact for every $p \in X$.
For $0 \to \mathcal{F} \to \mathcal{G} \to \mathcal{H} \to 0$ exact, the sequence of global sections
\[
0 \to \mathcal{F}(X) \to \mathcal{G}(X) \to \mathcal{H}(X)
\]
is exact, but the last map need not be surjective.
:::

::: {.remark}
Surjectivity of $\mathcal{G} \to \mathcal{H}$ means every germ lifts, which is a statement about some neighbourhood of each point.
A global section of $\mathcal{H}$ therefore lifts over each member of some cover, and the lifts need not agree on overlaps.
The obstruction to correcting them is a Čech $1$-cocycle, and it is $H^1(X, \mathcal{F})$ that measures whether it can be corrected.

This is the whole motivation for sheaf cohomology, and the correct answer to "where exactly does that fail" is: at the overlaps, and the failure is measured by $H^1$ of the kernel.
:::
