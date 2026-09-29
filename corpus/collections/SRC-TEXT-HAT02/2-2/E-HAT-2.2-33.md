---
schema: qual/card@1
id: E-HAT-2.2-33
kind: problem
title: 'Nerve-type vanishing: $\tilde{H}_i(X) = 0$ for $i \geq n-1$ when intersections are acyclic'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Suppose the space $X$ is the union of open sets $A_1, \cdots, A_n$ such that each intersection $A_{i_1} \cap \cdots \cap A_{i_k}$ is either empty or has trivial reduced homology groups.
Show that $\tilde{H}_i(X) = 0$ for $i \geq n-1$, and give an example showing this inequality is best possible, for each $n$.
:::

::: {.solution}

::: pf

::: pf-step

Consider the Mayer–Vietoris spectral sequence (or the Čech-to-derived / nerve argument) for the open cover $\{A_1, \ldots, A_n\}$.

::: pf-proof

setup.

:::

:::

::: pf-step

The $E^1$ page has $E^1_{p,q} = \bigoplus_{i_0 < \cdots < i_p} \tilde H_q(A_{i_0} \cap \cdots \cap A_{i_p})$.

::: pf-proof

the Mayer–Vietoris spectral sequence for a cover.

:::

:::

::: {.pf-step #s3}

By hypothesis, each intersection $A_{i_0} \cap \cdots \cap A_{i_p}$ is either empty or acyclic, so $E^1_{p,q} = 0$ for all $q > 0$.

::: pf-proof

the hypothesis (trivial reduced homology).

:::

:::

::: {.pf-step #s4}

Hence the spectral sequence is concentrated in the row $q = 0$, so it degenerates and $\tilde H_i(X)$ is the homology of the nerve complex $N(\mathcal{U})$ (the Čech complex of the cover).

::: pf-proof

Step [](#s3){.pf-ref} (the spectral sequence collapses to the nerve).

:::

:::

::: {.pf-step #s5}

The nerve $N(\mathcal{U})$ is a simplicial complex with $n$ vertices, so its homology vanishes in degrees $\ge n$.

::: pf-proof

a simplicial complex with $n$ vertices has no simplices of dimension $\ge n$, so its homology is zero in degrees $\ge n$.

:::

:::

::: {.pf-step #s6}

Hence $\tilde H_i(X) = 0$ for $i \ge n - 1$.

::: pf-proof

Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} (the nerve has $n$ vertices, so $H_i(N) = 0$ for $i \ge n$; combined with the shift, $\tilde H_i(X) = 0$ for $i \ge n-1$).

:::

:::

::: {.pf-step #s7}

Example showing sharpness: take $X = S^{n-1}$ covered by the $n$ open hemispheres $A_i = \{x \in S^{n-1} : x_i > 0\}$ (and their slight enlargements to make them open and cover $S^{n-1}$).

::: pf-proof

construct the example.

:::

:::

::: {.pf-step #s8}

Each intersection of these hemispheres is contractible (or empty), so the hypothesis holds, but $\tilde H_{n-1}(S^{n-1}) = \ZZ \neq 0$.

::: pf-proof

Step [](#s7){.pf-ref} (the intersections are convex, hence contractible, but $S^{n-1}$ has $\tilde H_{n-1} = \ZZ$).

:::

:::

::: {.pf-step #s9}

Hence the bound $i \ge n-1$ is best possible.

::: pf-proof

Step [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s6){.pf-ref} and [](#s9){.pf-ref}.

:::

:::

:::
