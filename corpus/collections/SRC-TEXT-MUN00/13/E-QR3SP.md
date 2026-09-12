---
schema: qual/card@1
id: E-QR3SP
kind: problem
title: The countable complement topology and an infinite complement collection
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
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

Show that the collection $\mathcal{T}_c$ given in Example 4 of §12 is a topology on the set $X$.
Is the collection

$$
\mathcal{T}_\infty = \ts{U \mid X - U \text{ is infinite or empty or all of } X}
$$

a topology on $X$?
:::

::: {.solution}
Let
\[
\mathcal T_c=\{\varnothing\}\cup\{U\subseteq X: X-U\text{ is countable}\}.
\]
Certainly $\varnothing,X\in\mathcal T_c$. If $\{U_\alpha\}$ is a family in $\mathcal T_c$ and all $U_\alpha$ are empty there is nothing to prove. Otherwise choose one nonempty $U_\beta$. Then
\[
X-\bigcup_\alpha U_\alpha=\bigcap_\alpha(X-U_\alpha)\subseteq X-U_\beta,
\]
so the complement of the union is countable. For finitely many nonempty $U_1,\dots,U_n$,
\[
X-\bigcap_{i=1}^nU_i=\bigcup_{i=1}^n(X-U_i),
\]
a finite union of countable sets. Hence $\mathcal T_c$ is a topology.

The analogous collection $\mathcal T_\infty$ is not a topology in general. Take $X=\mathbb Z_+$,
\[
U=\{2,4,6,\dots\},\qquad V=\{3,5,7,\dots\}.
\]
Both complements are infinite, so $U,V\in\mathcal T_\infty$, but
\[
U\cup V=X-\{1\},
\]
whose complement is the nonempty finite set $\{1\}$. Thus $U\cup V\notin\mathcal T_\infty$.
:::
