---
schema: qual/card@1
id: E-CFH1Q
kind: problem
title: Closed sets satisfy the topology axioms
classification:
  areas:
  - topology
  topics:
  - Closed Sets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $\mathcal{C}$ be a collection of subsets of the set $X$.
Suppose that $\varnothing$ and $X$ are in $\mathcal{C}$, and that finite unions and arbitrary intersections of elements of $\mathcal{C}$ are in $\mathcal{C}$.
Show that the collection

$$
\mathcal{T} = \ts{X - C \mid C \in \mathcal{C}}
$$

is a topology on $X$.
:::

::: {.solution}
We verify the topology axioms for
\[
\mathcal T=\{X-C:C\in\mathcal C\}.
\]
Since $X,\varnothing\in\mathcal C$, their complements show that $\varnothing,X\in\mathcal T$.

If $U_\alpha=X-C_\alpha\in\mathcal T$, then by De Morgan,
\[
\bigcup_\alpha U_\alpha
=X-\bigcap_\alpha C_\alpha.
\]
The arbitrary intersection $\bigcap_\alpha C_\alpha$ belongs to $\mathcal C$, so the union belongs to $\mathcal T$.

For finitely many $U_i=X-C_i$,
\[
\bigcap_{i=1}^nU_i=X-\bigcup_{i=1}^nC_i,
\]
and the finite union on the right belongs to $\mathcal C$. Hence $\mathcal T$ is a topology.
:::
