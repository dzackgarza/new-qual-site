---
schema: qual/card@1
id: E-AMD-OQDKJ6H2
kind: exercise
title: $Z(G)=\bigcap_{a\in G}C_G(a)$
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}
Show that $Z(G) = \bigcap_{a\in G} C_G(a)$.
:::

::: {.solution}
**Goal.** Show $Z(G) = \bigcap_{a \in G} C_G(a)$.

<1>1. $Z(G) \subseteq \bigcap_{a \in G} C_G(a)$.
<2>1. If $z \in Z(G)$, then $za = az$ for all $a \in G$.
::: {.proof}
definition of the center.
:::
<2>2. Hence $z \in C_G(a)$ for every $a \in G$.
::: {.proof}
$C_G(a) = \theset{g : ga = ag}$.
:::
<2>3. Hence $z \in \bigcap_{a \in G} C_G(a)$.
::: {.proof}
$z$ is in every centralizer.
:::

<1>2. $\bigcap_{a \in G} C_G(a) \subseteq Z(G)$.
<2>1. If $z \in \bigcap_{a \in G} C_G(a)$, then $z \in C_G(a)$ for every $a$.
::: {.proof}
definition of intersection.
:::
<2>2. Hence $za = az$ for every $a \in G$.
::: {.proof}
definition of $C_G(a)$.
:::
<2>3. Hence $z \in Z(G)$.
::: {.proof}
definition of the center.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2 give both inclusions.
:::
:::
