---
schema: qual/card@1
id: S-4WQ1R
kind: solution
title: Normal p-subgroups lie in every Sylow — part (a)
classification:
  areas:
  - algebra
  topics:
  - groups
relations:
- kind: solves
  target: P-P2UAH
- kind: uses
  target: D-7TQ2M
review: draft
---

::: {.solution}
Let $S$ be a Sylow $p\dash$subgroup of $G$, so $\abs S = p^a$ is the full $p\dash$part of $\abs G$.

Because $P \normal G$, the product $PS$ is a subgroup of $G$, and
$$
\abs{PS} = \frac{\abs P \cdot \abs S}{\abs{P \intersect S}}
$$
is a quotient of powers of $p$, hence itself a power of $p$. So $PS$ is a $p\dash$subgroup of
$G$ containing $S$. Since $S$ is maximal among $p\dash$subgroups, $\abs{PS} = \abs S$ and
therefore $PS = S$. As $P \subseteq PS$, we conclude $P \subseteq S$.

Since $S$ was an arbitrary Sylow $p\dash$subgroup, $P$ lies in all of them.
:::

::: {.remark}
Part (b) is not written up yet, which is why this card is marked `draft` rather
than split into a second solution card.
:::
