---
schema: qual/card@1
id: P-TO35W
kind: problem
title: Example of an Artinian ring
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Rings
relations: []
review: draft
---

::: {.problem}
Give an example of an Artinian ring.
:::

::: {.solution}
For any integer $n\ge2$, the ring
\[
\ZZ/n\ZZ
\]
is Artinian.

Indeed, it is finite. Any descending chain of ideals
\[
I_1\supseteq I_2\supseteq I_3\supseteq\cdots
\]
is therefore a descending chain of subsets of a finite set, so there can be only finitely many strict inclusions. Hence the chain stabilizes.

Thus every finite ring is Artinian, and $\ZZ/n\ZZ$ is a basic example.
:::
