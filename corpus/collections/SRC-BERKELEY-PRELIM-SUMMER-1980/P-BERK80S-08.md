---
schema: qual/card@1
id: P-BERK80S-08
kind: problem
title: Uncountably many connected components in a subset of the real line
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the Cantor-set example, singleton components, and the countability argument for components of open subsets of the real line.
---

::: {.problem}
Give an example of a subset of $\RR$ having uncountably many connected components. Can such a subset be open? Closed?
:::

::: {.solution}
Let $C\subset\RR$ be the middle-thirds Cantor set.

::: pf

::: {.pf-step #s1}

The Cantor set $C$ has uncountably many connected components.

::: pf-proof

The Cantor set is uncountable. It is also totally disconnected: if $x<y$
are distinct points of $C$, then at some finite stage of the Cantor
construction they lie in two different surviving closed intervals,
separated by one of the deleted open middle thirds. Hence no connected
subset of $C$ contains both $x$ and $y$.

Therefore every connected component of $C$ is a singleton. Since $C$ is
uncountable, it has uncountably many connected components.

:::

:::

::: {.pf-step #s2}

Such a subset can be closed.

::: pf-proof

The Cantor set $C$ is an intersection of finite unions of closed intervals,
hence closed in $\RR$, and step [](#s1){.pf-ref} shows that it has uncountably many
connected components.

:::

:::

::: {.pf-step #s3}

Such a subset cannot be open.

::: pf-proof

Every connected component of an open subset $U\subseteq\RR$ is an open
interval, possibly unbounded, and distinct components are disjoint. Each
nonempty open interval contains a rational number. Choosing one rational
from each component gives an injection from the set of connected
components of $U$ into $\QQ$. Since $\QQ$ is countable, $U$ has at most
countably many connected components.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} gives the example $C$. Step [](#s3){.pf-ref} shows that such a subset cannot
be open, and step [](#s2){.pf-ref} shows that it can be closed.

:::

:::

:::
