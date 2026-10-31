---
schema: qual/card@1
id: E-HAT-1.3-17
kind: problem
title: Normal covering spaces from group extensions
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Given a group $G$ and a normal subgroup $N$, show that there exists a normal covering space $\tilde{X} \to X$ with $\pi_1(X) \approx G$, $\pi_1(\tilde{X}) \approx N$, and deck transformation group $G(\tilde{X}) \approx G/N$.
:::

::: {.solution}

::: pf

::: pf-step
There is a connected CW complex $X$ with $\pi_1(X)\cong G$.

::: pf-proof
Choose a presentation of $G$. Form a CW complex with one vertex, one $1$-cell for each generator, and one $2$-cell attached along each relator. Van Kampen identifies its fundamental group with the presented group $G$. A CW complex is locally path connected and semilocally simply connected, so the covering classification applies.
:::

:::

::: pf-step
The connected covering of $X$ corresponding to $N\leq G$ has fundamental group isomorphic to $N$ and deck group isomorphic to $G/N$.

::: pf-proof
Choose an isomorphism $\pi_1(X)\cong G$ and use the covering-space classification for the subgroup corresponding to $N$. The covering map injects its fundamental group with image $N$, giving $\pi_1(\widetilde X)\cong N$. Since $N$ is normal, the covering is normal, and the deck transformation group is $\pi_1(X)/N\cong G/N$.
:::

:::

:::

:::
