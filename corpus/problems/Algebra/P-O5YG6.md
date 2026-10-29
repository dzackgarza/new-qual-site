---
schema: qual/card@1
id: P-O5YG6
kind: problem
title: Distinct Sylow subgroups intersect trivially; normal subgroups of $p$-groups
  meet the center
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - p-Groups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: Part (a) of the source names no ambient group; the statement places both Sylow subgroups in one finite group.
---

::: {.problem}
(a) Show that a Sylow $p_1$-subgroup and a Sylow $p_2$-subgroup of a finite group intersect trivially when $p_1\ne p_2$.

(b) Show that every nontrivial normal subgroup of a finite $p$-group intersects the center nontrivially.
:::

::: {.solution}

::: pf

::: pf-step

(a) If $P_1$ is a $p_1$-subgroup and $P_2$ a $p_2$-subgroup of a finite group $G$ with $p_1\ne p_2$, then $P_1\cap P_2=\{e\}$.

::: pf-proof

The order of $P_1\cap P_2$ divides both $\abs{P_1}$, a power of $p_1$, and $\abs{P_2}$, a power of $p_2$. Hence
$$
\abs{P_1\cap P_2}=1,
$$
so $P_1\cap P_2=\{e\}$.

:::

:::

::: pf-step

(b) If $G$ is a finite $p$-group and $1\ne N\trianglelefteq G$, then $N\cap Z(G)\ne1$.

::: pf-proof

Let $G$ act on $N$ by conjugation. Because $N$ is normal, this action is well-defined. Its fixed points are exactly
$$
N\cap Z(G).
$$
Every non-fixed orbit has size
$$
[G:C_G(x)],
$$
a positive power of $p$, hence is divisible by $p$. Therefore the class equation for this action gives
$$
\abs{N}\equiv \abs{N\cap Z(G)}\pmod p.
$$
Since $N$ is a nontrivial subgroup of a $p$-group, $p\mid \abs{N}$. Hence
$$
p\mid \abs{N\cap Z(G)}.
$$
Thus $N\cap Z(G)$ contains more than the identity.

:::

:::

:::

:::
