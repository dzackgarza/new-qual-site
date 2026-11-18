---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-GW2
kind: problem
title: Nonhomeomorphic spaces with isomorphic nontrivial fundamental groups
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homeomorphisms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the two spaces named, their common fundamental group
    computed, and their separation by $H_{2}$. No retained solution set covers this exercise (the
    collection retains the problem packets, not solutions), so the argument is the card's own; it was
    re-read for this pass.
---

::: {.problem}
Find two spaces $X$ and $Y$ such that $\pi_1(X)\cong\pi_1(Y)$ and are non-trivial, and are NOT homeomorphic.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The example is $X=S^{1}$ and $Y=S^{1}\vee S^{2}$.

::: pf

::: {.pf-step #pi1}
$\pi_{1}(S^{1}\vee S^{2})\cong\ZZ\cong\pi_{1}(S^{1})$, and the group is nontrivial.

::: pf-proof
$S^{1}\vee S^{2}$ is the union of two path connected spaces meeting in a single point, which is a deformation retract of an open neighbourhood in each, so van Kampen applies and gives $\pi_{1}(S^{1}\vee S^{2})\cong\pi_{1}(S^{1})*\pi_{1}(S^{2})$. Now $\pi_{1}(S^{2})=1$ because $S^{2}$ is simply connected, so the free product is $\pi_{1}(S^{1})\cong\ZZ$, which is nontrivial.
:::

:::

::: {.pf-step #homology}
$H_{2}(S^{1})=0$ and $H_{2}(S^{1}\vee S^{2})\cong\ZZ$.

::: pf-proof
$S^{1}$ is a one-dimensional space, so its degree-two homology vanishes. For the wedge, reduced homology is additive over a wedge of path connected spaces, so $\tilde H_{2}(S^{1}\vee S^{2})\cong\tilde H_{2}(S^{1})\oplus\tilde H_{2}(S^{2})\cong0\oplus\ZZ$, and the unreduced group is $\ZZ$ as the space is path connected.
:::

:::

::: {.pf-step}
$S^{1}$ and $S^{1}\vee S^{2}$ are not homeomorphic.

::: pf-proof
A homeomorphism induces isomorphisms on singular homology in every degree. By step [](#homology){.pf-ref} the second homology groups are $0$ and $\ZZ$, which are not isomorphic, so no homeomorphism exists. With step [](#pi1){.pf-ref} the two spaces have the same nontrivial fundamental group $\ZZ$ and are not homeomorphic, which is the requested pair.
:::

:::

:::
:::
