---
schema: qual/card@1
id: P-UCTOP-SU14-6
kind: problem
title: '$\RP^2\vee S^3$ and $\RP^3$ are not homotopy equivalent'
classification:
  areas:
    - topology
  topics:
    - Homotopy
relations: []
review: draft
---

::: {.problem}
Prove that $\RP^2 \vee S^3$ and $\RP^3$ are not homotopy-equivalent.
:::

::: {.solution}

::: pf

::: {.pf-step #same-homology}

The two spaces have isomorphic integral homology, so homology does not distinguish them: both have $H_0 \cong \ZZ$, $H_1 \cong \ZZ/2$, $H_2 = 0$, $H_3 \cong \ZZ$, and vanishing higher homology.

::: pf-proof

Reduced homology of a wedge is the direct sum of the reduced homologies of the summands, and $\RP^2$ contributes $\ZZ/2$ in degree $1$ while $S^3$ contributes $\ZZ$ in degree $3$. The cellular chain complex $\ZZ \xrightarrow{0} \ZZ \xrightarrow{2} \ZZ \xrightarrow{0} \ZZ$ of $\RP^3$ gives the same groups.

:::

:::

::: {.pf-step #pi2-rp3}

$\pi_2(\RP^3) = 0$.

::: pf-proof

The universal cover of $\RP^3$ is $S^3$, a covering map induces isomorphisms on $\pi_n$ for $n \ge 2$, and $\pi_2(S^3) = 0$.

:::

:::

::: {.pf-step #pi2-wedge}

$\pi_2(\RP^2 \vee S^3) \cong \ZZ$.

::: pf-proof

$\pi_1(\RP^2 \vee S^3) \cong \ZZ/2$ by van Kampen, since $S^3$ is simply connected.
The universal cover is $S^2$ with one copy of $S^3$ attached at each of the two lifts of the wedge point; contracting an arc in $S^2$ joining the two attachment points shows that it is homotopy equivalent to $S^2 \vee S^3 \vee S^3$.
This space is simply connected with $H_2 \cong \ZZ$, so by Hurewicz its $\pi_2$ is $\ZZ$, and the covering map identifies it with $\pi_2(\RP^2 \vee S^3)$.

:::

:::

::: pf-qed

A homotopy equivalence induces isomorphisms on all homotopy groups, and Steps [](#pi2-rp3){.pf-ref} and [](#pi2-wedge){.pf-ref} give different $\pi_2$. So the spaces are not homotopy equivalent, although Step [](#same-homology){.pf-ref} shows that their homology groups agree.

:::

:::

:::
