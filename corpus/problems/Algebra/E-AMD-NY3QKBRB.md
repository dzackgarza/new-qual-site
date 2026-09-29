---
schema: qual/card@1
id: E-AMD-NY3QKBRB
kind: problem
title: Kernel of conjugation $G\to\Aut(G)$ is $Z(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Centralizers and Normalizers
  - Homomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that the kernel of the map $G\to \aut(G)$ given by $g\mapsto (h\mapsto gh\inverseof{g})$ is $Z(G)$.
:::

::: {.solution}

::: pf

::: pf-step
Write $\varphi: G \to \aut(G)$ for the map $\varphi(g) = c_g$, where $c_g(h) = gh\inverseof{g}$.
:::

::: {.pf-step #kernel-iff-center}
$g \in \ker \varphi$ if and only if $g \in Z(G)$.

::: pf-proof

::: pf-step
$\ker \varphi = \ts{ g \in G \st c_g = \id_G }$, since the identity of $\aut(G)$ is the identity automorphism.
:::

::: pf-step
$c_g = \id_G$ says $gh\inverseof{g} = h$ for every $h \in G$.
:::

::: pf-step
Multiplying on the right by $g$, this is equivalent to $gh = hg$ for every $h \in G$.
:::

::: pf-step
That is the defining condition for $g \in Z(G)$.
:::

:::

:::

::: pf-qed
Step [](#kernel-iff-center){.pf-ref} is the equality $\ker \varphi = Z(G)$ of subsets, and both sides are subgroups of $G$.
:::

:::

:::
