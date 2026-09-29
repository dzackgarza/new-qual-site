---
schema: qual/card@1
id: E-0S3OA
kind: problem
title: Subgroups and closures of subgroups are topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $H$ be a subspace of the topological group $G$.
Show that if $H$ is also a subgroup of $G$, then both $H$ and $\overline{H}$ are topological groups.
:::

::: {.solution}
Let $m\colon G\times G\to G$ and $i\colon G\to G$ be multiplication and inversion, which are continuous.

::: pf

::: {.pf-step #subgroup-is-topological-group}
If $K\subseteq G$ is a subgroup, then $K$ with the subspace topology is a topological group.

::: pf-proof
By [[E-R3NOE]], the product topology on $K\times K$ is the subspace topology from $G\times G$.
The maps $m|_{K\times K}$ and $i|_K$ are restrictions of continuous maps to subspaces, and they take values in the subspace $K$ because $K$ is a subgroup; a continuous map with image in a subspace is continuous into that subspace.
:::

:::

::: {.pf-step #closure-closed-under-inversion}
$\overline H$ is closed under inversion.

::: pf-proof
$i$ is continuous and $i\circ i=\operatorname{id}_G$, so $i$ is a homeomorphism and $i(\overline H)=\overline{i(H)}=\overline H$.
:::

:::

::: {.pf-step #closure-closed-under-multiplication}
$\overline H$ is closed under multiplication.

::: pf-proof
Let $x,y\in\overline H$ and let $W$ be an open neighborhood of $xy$.
By continuity of $m$ at $(x,y)$ there are open $U\ni x$ and $V\ni y$ with $UV\subseteq W$.
Choose $h_1\in U\cap H$ and $h_2\in V\cap H$; then $h_1h_2\in W\cap H$.
Hence every neighborhood of $xy$ meets $H$, and $xy\in\overline H$.
:::

:::

::: pf-qed
Step [](#subgroup-is-topological-group){.pf-ref} applies to $H$.
The identity lies in $H\subseteq\overline H$, so by steps [](#closure-closed-under-inversion){.pf-ref} and [](#closure-closed-under-multiplication){.pf-ref} $\overline H$ is a subgroup, and step [](#subgroup-is-topological-group){.pf-ref} applies to $\overline H$.
:::

:::

:::
