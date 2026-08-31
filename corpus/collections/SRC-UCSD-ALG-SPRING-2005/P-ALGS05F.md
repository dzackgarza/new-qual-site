---
schema: qual/card@1
id: P-ALGS05F
kind: problem
title: "Conjugacy classes in a group are bounded by the index of the center"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a group whose center has index $n$.
Show that every conjugacy class in $G$ has at most $n$ elements.
:::

::: {.solution}
<1>1. Let $g \in G$, and let $C(g) = \{x g x^{-1} : x \in G\}$ be its conjugacy class.
::: {.proof}
setup.
:::

<1>2. The size of the conjugacy class is $|C(g)| = [G : C_G(g)]$, where $C_G(g)$ is the centralizer of $g$.
::: {.proof}
orbit–stabilizer theorem applied to the conjugation action.
:::

<1>3. $Z(G) \subseteq C_G(g)$.
::: {.proof}
every element of the center commutes with $g$, hence centralizes $g$.
:::

<1>4. Hence $[G : C_G(g)] \le [G : Z(G)] = n$.
::: {.proof}
$C_G(g) \supseteq Z(G)$, so the index of $C_G(g)$ is at most the index of $Z(G)$.
:::

<1>5. Therefore $|C(g)| \le n$.
::: {.proof}
<1>2 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
