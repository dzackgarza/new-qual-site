---
schema: qual/card@1
id: E-MH2FB
kind: exercise
title: Continuity of x times y inverse characterizes topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.exercise}

Let $H$ denote a group that is also a topological space satisfying the $T_1$ axiom.
Show that $H$ is a topological group if and only if the map of $H \times H$ into $H$ sending $x \times y$ into $x \cdot y^{-1}$ is continuous.
:::

::: solution
**Goal:** Show continuity of inversion and multiplication are equivalent to continuity of
$$m(x,y)=xy^{-1}.$$

<1> Assume $H$ is a topological group.
    *Proof:* By definition, inversion and multiplication are continuous.
    The map $m$ is the composite
    $$
    H\times H \xrightarrow{(\id,\operatorname{inv})} H\times H \xrightarrow{\mu} H,
    $$
    where $\mu$ is multiplication, so $m$ is continuous.

<1> Assume $m$ is continuous.
    *Proof:* We recover inversion and multiplication from $m$.
    <2>1. For inversion, for any $x\in H$,
        $$x^{-1}=m(e,x).$$
        So $\operatorname{inv}$ is continuous as $x\mapsto(e,x)$ followed by $m$.
    <2>2. For multiplication, for $x,y\in H$,
        $$
        xy = m(x,y^{-1}).
        $$
        Since inversion is continuous, so is $(x,y)\mapsto(x,y^{-1})$, hence
        $(x,y)\mapsto xy$ is continuous as a composition with $m$.

<1> Therefore continuity of $m$ is equivalent to $H$ being a topological group.

Authored by **Codex 5.3 Spark Extra High**.
:::
