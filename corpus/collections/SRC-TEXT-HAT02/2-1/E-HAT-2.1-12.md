---
schema: qual/card@1
id: E-HAT-2.1-12
kind: problem
title: Chain homotopy is an equivalence relation
classification:
  areas:
  - topology
  topics:
  - Homology
  - Chain Complexes
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that chain homotopy of chain maps is an equivalence relation.
:::

::: {.solution}
Fix chain complexes $(C_*,d_C)$ and $(D_*,d_D)$. A chain homotopy from $f$ to $g$ is a degree-one family $P_n:C_n\to D_{n+1}$ satisfying
$$
f_n-g_n=d_D P_n+P_{n-1}d_C
$$
in every degree.

::: pf

::: {.pf-step #s1}

Chain homotopy is reflexive.

::: pf-proof

For any chain map $f$, take $P_n=0$ in every degree. Then $f_n-f_n=d_D P_n+P_{n-1}d_C=0$.

:::

:::

::: {.pf-step #s2}

Chain homotopy is symmetric.

::: pf-proof

If $P$ is a chain homotopy from $f$ to $g$, then
$$
g_n-f_n=d_D(-P_n)+(-P_{n-1})d_C.
$$
Thus $-P$ is a chain homotopy from $g$ to $f$.

:::

:::

::: {.pf-step #s3}

Chain homotopy is transitive.

::: pf-proof

If $P$ is a chain homotopy from $f$ to $g$ and $Q$ is one from $g$ to $h$, add their defining identities:
$$
f_n-h_n=d_D(P_n+Q_n)+(P_{n-1}+Q_{n-1})d_C.
$$
Thus $P+Q$ is a chain homotopy from $f$ to $h$.

:::

:::

::: pf-step

Hence chain homotopy is an equivalence relation on the chain maps $C_*\to D_*$.

::: pf-proof

This follows from steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref}.

:::

:::

:::
:::
