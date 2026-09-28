---
schema: qual/card@1
id: D-BIVAU
kind: definition
title: The Zariski topology
classification:
  areas:
  - algebraic-geometry
  topics:
  - Varieties
  - Zariski Topology
relations: []
review: draft
prompts:
- What are the closed subsets of $\AA^n$?
- What is a distinguished open set?
- What is the Zariski topology on $\AA^1$?
- Show that the Zariski topology on $\AA^1$ is not Hausdorff.
- Show that $\AA^1$ is irreducible without using the Nullstellensatz.
- Show that $\AA^n$ is irreducible.
- Show that $\dim \AA^1 = 1$ and $\dim \AA^n = n$.
---

::: {.definition title="Zariski topology"}
The \dfn{Zariski topology} on $\AA^n$ has as its closed sets the vanishing loci
\[
V(J) \da \ts{ p \in \AA^n \st f(p) = 0 \text{ for all } f \in J }
\]
of ideals $J \subseteq k[x_1,\ldots,x_n]$.
The **distinguished open set** attached to $f$ is $D_f \da \AA^n \sm V(f)$, and these form a basis.
:::

::: {.remark}
On $\AA^1$, and on any irreducible curve, the proper closed sets are the finite sets, so the Zariski topology is the cofinite topology.
For $\AA^1$ over $k = \bar{k}$: since $k[x]$ is a PID, every ideal is $(f)$, and factoring $f$ into linear factors gives $V(f) = \ts{a_1, \ldots, a_r}$ when $f \neq 0$.
This is the source of most of the topology's strangeness: any two nonempty opens meet, so the space is irreducible and very far from Hausdorff, and a continuity argument borrowed from the analytic topology will not survive.
:::
