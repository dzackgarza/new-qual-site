---
schema: qual/card@1
id: E-EHQWZ
kind: problem
title: $X$ is connected if and only if its only clopen subsets are $\emptyset$ and
  $X$
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
---

::: {.exercise}
Prove that $X$ is connected iff the only clopen subsets are $\emptyset, X$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $X$ is disconnected, then $X=U\sqcup V$ for nonempty disjoint open sets $U,V$.

::: pf-proof

This is the definition of disconnectedness.

:::

:::

::: {.pf-step #s2}

Then $U$ is a nontrivial clopen subset.

::: pf-proof

It is open, and its complement $V$ is open, so $U$ is closed; it is neither empty nor all of $X$.

:::

:::

::: {.pf-step #s3}

Conversely, if $A\subset X$ is nontrivial and clopen, then $X=A\sqcup(X\setminus A)$ is a separation.

::: pf-proof

Both pieces are nonempty, disjoint, and open because $A$ is both open and closed.

:::

:::

::: pf-step

Hence $X$ is connected iff its only clopen subsets are $\varnothing$ and $X$.

::: pf-proof

Combine steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
