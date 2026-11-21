---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS4A-HW2
kind: problem
title: A $\Delta$-complex structure and homology of $S^1$
classification:
  areas:
  - topology
  topics:
  - Cell Complexes
  - Homology
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
    Restructured into numbered steps for issue #2: the $\Delta$-complex structure, the boundary
    computation, and the two homology groups with the vanishing above degree one. No retained solution set
    covers this exercise (the collection retains the worksheets, not solutions), so the argument is the
    card's own; the chain groups and the boundary were checked for this pass.
---

::: {.problem}
Give a $\Delta$-complex structure for $S^1$, and use that to compute the homology groups for $S^1$.
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own. For a $\Delta$-complex structure on a space the simplicial chain groups are $C_{n}=\ZZ^{\#\{n\text{-simplices}\}}$ with the boundary $\partial_{n}$ sending an $n$-simplex to the alternating sum of its faces.

::: pf

::: {.pf-step #structure}
$S^{1}$ has the $\Delta$-complex structure with one vertex $v$ and one $1$-simplex $e$ whose two faces are both identified with $v$.

::: pf-proof
Take the standard $1$-simplex $\Delta^{1}=[0,1]$ and the map sending every point to $S^{1}$ by $t\mapsto e^{2\pi i t}$; its two faces $0$ and $1$ both go to the point $1\in S^{1}$, and the interior maps homeomorphically onto $S^{1}\setminus\{1\}$. So $S^{1}$ is the quotient of one $1$-simplex with its two endpoints identified once, which is a $\Delta$-complex structure with a single vertex and a single edge.
:::

:::

::: {.pf-step #chains}
$C_{1}=\ZZ e$, $C_{0}=\ZZ v$, $C_{n}=0$ for $n\ge2$, and $\partial_{1}e=v-v=0$.

::: pf-proof
There is exactly one simplex in each of the degrees $0$ and $1$ and none in higher degrees, so the chain groups are as displayed. The boundary of $e$ is the alternating sum of its two faces: with both faces equal to $v$, $\partial_{1}e=v-v=0$.
:::

:::

::: {.pf-step}
$H_{1}(S^{1})\cong\ZZ$, $H_{0}(S^{1})\cong\ZZ$, and $H_{n}(S^{1})=0$ for $n\ge2$.

::: pf-proof
By definition $H_{1}=\ker\partial_{1}/\operatorname{im}\partial_{2}$; step [](#chains){.pf-ref} gives $\partial_{1}=0$ and $C_{2}=0$, so $H_{1}=\ZZ e\cong\ZZ$. Likewise $H_{0}=C_{0}/\operatorname{im}\partial_{1}=\ZZ v/\{0\}\cong\ZZ$. For $n\ge2$ both $C_{n}$ and $C_{n+1}$ vanish, so $H_{n}=0$. This is the computation of the homology of $S^{1}$ required.
:::

:::

:::
:::
