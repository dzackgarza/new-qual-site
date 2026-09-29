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

::: {.problem}
Let $G$ be a group whose center has index $n$.
Show that every conjugacy class in $G$ has at most $n$ elements.
:::

::: {.solution}

::: pf

::: pf-step

Let $g \in G$, and let $C(g) = \{x g x^{-1} : x \in G\}$ be its conjugacy class.

::: pf-proof

setup.

:::

:::

::: {.pf-step #s2}

The size of the conjugacy class is $|C(g)| = [G : C_G(g)]$, where $C_G(g)$ is the centralizer of $g$.

::: pf-proof

orbit–stabilizer theorem applied to the conjugation action.

:::

:::

::: pf-step

$Z(G) \subseteq C_G(g)$.

::: pf-proof

every element of the center commutes with $g$, hence centralizes $g$.

:::

:::

::: {.pf-step #s4}

Hence $[G : C_G(g)] \le [G : Z(G)] = n$.

::: pf-proof

$C_G(g) \supseteq Z(G)$, so the index of $C_G(g)$ is at most the index of $Z(G)$.

:::

:::

::: {.pf-step #s5}

Therefore $|C(g)| \le n$.

::: pf-proof

Steps [](#s2){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref}.

:::

:::

:::
