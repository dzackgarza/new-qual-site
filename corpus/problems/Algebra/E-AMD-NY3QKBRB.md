---
schema: qual/card@1
id: E-AMD-NY3QKBRB
kind: exercise
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
Show that the kernel of the map $G\to \aut(G)$ given by $g\mapsto (h\mapsto ghg\inv)$ is $Z(G)$.
:::

::: solution
**Goal:** show that $g$ acts trivially by conjugation exactly when $g$ commutes with every element of $G$.

<1>1. Write $\varphi: G \to \aut(G)$ for the map $\varphi(g) = c_g$, where $c_g(h) = ghg\inv$.

<1>2. $g \in \ker \varphi$ if and only if $g \in Z(G)$.
::: {.proof}
<2>1. $\ker \varphi = \ts{ g \in G \st c_g = \id_G }$, since the identity of $\aut(G)$ is the identity automorphism.
<2>2. $c_g = \id_G$ says $ghg\inv = h$ for every $h \in G$.
<2>3. Multiplying on the right by $g$, this is equivalent to $gh = hg$ for every $h \in G$.
<2>4. That is the defining condition for $g \in Z(G)$.

:::
<1>3. Q.E.D. *Proof:* Step <1>2 is the equality $\ker \varphi = Z(G)$ of subsets, and both sides are subgroups of $G$.
:::
