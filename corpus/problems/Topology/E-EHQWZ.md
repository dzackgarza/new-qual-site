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

::: exercise
Prove that $X$ is connected iff the only clopen subsets are $\emptyset, X$.
:::

::: {.solution}
<1>1. If $X$ is disconnected, then $X=U\sqcup V$ for nonempty disjoint open sets $U,V$.
::: {.proof}
This is the definition of disconnectedness.
:::

<1>2. Then $U$ is a nontrivial clopen subset.
::: {.proof}
It is open, and its complement $V$ is open, so $U$ is closed; it is neither empty nor all of $X$.
:::

<1>3. Conversely, if $A\subset X$ is nontrivial and clopen, then $X=A\sqcup(X\setminus A)$ is a separation.
::: {.proof}
Both pieces are nonempty, disjoint, and open because $A$ is both open and closed.
:::

<1>4. Hence $X$ is connected iff its only clopen subsets are $\varnothing$ and $X$.
::: {.proof}
Combine <1>1--<1>3.
:::
:::
