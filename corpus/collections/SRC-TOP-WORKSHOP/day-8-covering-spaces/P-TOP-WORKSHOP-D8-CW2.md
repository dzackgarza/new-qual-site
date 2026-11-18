---
schema: qual/card@1
id: P-TOP-WORKSHOP-D8-CW2
kind: problem
title: $S^2\vee S^2$ does not cover $S^2$
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
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
    Restructured into numbered steps for issue #2: the triviality of connected coverings of a simply
    connected space, the obstruction from $H_{2}$, and the conclusion. No retained solution set covers
    this exercise (the collection retains the problem packets, not solutions), so the argument is the
    card's own; it was re-read for this pass.
---

::: {.problem}
Prove or disprove: $S^2\vee S^2$ is a covering space of $S^2$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. The claim to be disproved is that $S^{2}\vee S^{2}$ is a covering space of $S^{2}$; a covering map is required to be surjective, so a nowhere-defined covering needs no separate treatment.

::: pf

::: {.pf-step #trivial}
Every connected covering space of a simply connected space is a homeomorphism onto its base.

::: pf-proof
Let $p:\tilde X\to S^{2}$ be a covering with $\tilde X$ connected. For any covering, $p_{*}\pi_{1}(\tilde X)$ is a subgroup of $\pi_{1}(S^{2})$, which is trivial because $S^{2}$ is simply connected; so $\tilde X$ is simply connected and the number of sheets of $p$ is the index $[\pi_{1}(S^{2}):p_{*}\pi_{1}(\tilde X)]=1$. A one-sheeted covering is a bijective local homeomorphism, hence a homeomorphism.
:::

:::

::: {.pf-step #spheres}
$H_{2}(S^{2}\vee S^{2})\cong\ZZ\oplus\ZZ$ and $H_{2}(S^{2})\cong\ZZ$.

::: pf-proof
$S^{2}\vee S^{2}$ is the union of two copies of $S^{2}$ meeting in a single point, and reduced homology is additive over a wedge: $\tilde H_{2}(S^{2}\vee S^{2})\cong\tilde H_{2}(S^{2})\oplus\tilde H_{2}(S^{2})\cong\ZZ\oplus\ZZ$, so the unreduced group is $\ZZ\oplus\ZZ$ as well because the wedge is path connected. For the sphere, $H_{2}(S^{2})\cong\ZZ$ and the higher groups vanish.
:::

:::

::: {.pf-step}
$S^{2}\vee S^{2}$ is not a covering space of $S^{2}$.

::: pf-proof
Suppose it were, with covering map $p:S^{2}\vee S^{2}\to S^{2}$. The total space is path connected, so by step [](#trivial){.pf-ref} $p$ would be a homeomorphism onto $S^{2}$. A homeomorphism induces isomorphisms on all homology groups, so $H_{2}$ of the total space would be isomorphic to $H_{2}(S^{2})$; but by step [](#spheres){.pf-ref} these are $\ZZ\oplus\ZZ$ and $\ZZ$, which are not isomorphic groups. Hence no such covering exists and the statement is false.
:::

:::

:::
:::
