---
schema: qual/card@1
id: E-2HSGM
kind: problem
title: $[0,1]$ is compact
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Euclidean Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that $[0, 1]$ is compact.
:::

::: {.solution}

Let $\mathcal{U}$ be a cover of $[0, 1]$ by open subsets of $\RR$, and let
$$
S = \{x \in [0, 1] \mid [0, x] \text{ is covered by finitely many members of } \mathcal{U}\}.
$$

::: pf

::: pf-step

$S$ has a supremum $c \in [0,1]$.

::: pf-proof

Some $U_0 \in \mathcal{U}$ contains $0$, so $[0,0] \subseteq U_0$ and $0 \in S$. Also $S \subseteq [0,1]$ is bounded above by $1$, so the least upper bound property of $\RR$ gives $c = \sup S$ with $0 \le c \le 1$.

:::

:::

::: {.pf-step #c-in-S}

$c \in S$.

::: pf-proof

Choose $U_c \in \mathcal{U}$ containing $c$ and $\varepsilon > 0$ with $(c - \varepsilon, c + \varepsilon) \subseteq U_c$. By definition of the supremum there is $x_0 \in S$ with $c - \varepsilon < x_0 \le c$, and finitely many members of $\mathcal{U}$ cover $[0, x_0]$. Together with $U_c \supseteq [x_0, c]$ they cover $[0, c]$.

:::

:::

::: pf-step

$c = 1$, so $[0,1]$ is covered by finitely many members of $\mathcal{U}$.

::: pf-proof

Suppose $c < 1$, and take $U_c$, $\varepsilon$ as in step [](#c-in-S){.pf-ref} and $x_1 \in (c, \min(c + \varepsilon, 1))$. The finite cover of $[0,c]$ from step [](#c-in-S){.pf-ref} together with $U_c \supseteq [c, x_1]$ covers $[0, x_1]$, so $x_1 \in S$, contradicting $x_1 > c = \sup S$. Hence $c = 1$, and $1 \in S$ by step [](#c-in-S){.pf-ref}.

:::

:::

:::

:::
