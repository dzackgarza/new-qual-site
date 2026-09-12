---
schema: qual/card@1
id: P-JTLTW
kind: problem
title: Nontrivial centre of a group of order $p^3$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Centralizers and Normalizers
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Let $G$ be a group of order $p^3$, where $p$ is prime. Show that $Z(G)$ is nontrivial, and hence that $G$ has a nontrivial normal subgroup.
:::

::: {.solution}
Let $G$ act on itself by conjugation. The class equation is
\[
|G|=|Z(G)|+\sum_i [G:C_G(x_i)],
\]
where the $x_i$ represent the noncentral conjugacy classes.

For noncentral $x_i$, the centralizer $C_G(x_i)$ is a proper subgroup of the $p$-group $G$, so
\[
[G:C_G(x_i)]
\]
is divisible by $p$. Hence every term in the sum is divisible by $p$. Since $|G|=p^3$ is divisible by $p$, the class equation gives
\[
|Z(G)|\equiv0\pmod p.
\]
But the identity lies in $Z(G)$, so $|Z(G)|\ge1$. Therefore $|Z(G)|\ge p$, and $Z(G)$ is nontrivial.

The center is characteristic in $G$, hence normal. Thus $G$ has a nontrivial normal subgroup.
:::
