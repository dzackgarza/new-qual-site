---
schema: qual/card@1
id: P-7ITXP
kind: problem
title: Approximating a bounded set by open and closed sets, equivalent to measurability
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source condition 2 omitted H ⊆ E ⊆ V, so it held for every E with V = H = ∅; the statement now requires H ⊆ E ⊆ V.'
---

::: {.problem}
Let $E \subseteq \RR^n$ be bounded.
Prove the following are equivalent: 

1. For any $\varepsilon>0$ there exists an open set $G$ and a closed set $F$ such that
$$
F \subseteq E \subseteq G \quad\text{and}\quad m(G\sm F) < \varepsilon.
$$

2. There exists a $G_\delta$ set $V$ and an $F_\sigma$ set $H$ such that
$$
H \subseteq E \subseteq V \quad\text{and}\quad m(V\sm H) = 0.
$$
:::

::: {.solution}
Fix an open ball $B \supseteq E$.

::: pf

::: {.pf-step #s1}

(1) implies (2).

::: pf-proof

For each $k$, (1) with $\eps = 1/k$ gives open $G_k$ and closed $F_k$ with $F_k \subseteq E \subseteq G_k$ and $m(G_k \setminus F_k) < 1/k$. Put $V = \bigcap_k G_k$, a $G_\delta$ set, and $H = \bigcup_k F_k$, an $F_\sigma$ set. Then $H \subseteq E \subseteq V$, and $V \setminus H \subseteq G_k \setminus F_k$ for each $k$, so $m(V \setminus H) < 1/k$ for every $k$, and $m(V \setminus H) = 0$.

:::

:::

::: {.pf-step #s2}

(2) implies (1).

::: pf-proof

::: pf-step

There are open $G_1 \supseteq G_2 \supseteq \cdots$ with $\bigcap_m G_m = V \cap B$ and $m(G_1) < \infty$, and closed $F_1 \subseteq F_2 \subseteq \cdots$ with $\bigcup_m F_m = H$.

::: pf-proof

Write $V = \bigcap_j U_j$ with $U_j$ open and $H = \bigcup_j K_j$ with $K_j$ closed, and put $G_m = B \cap U_1 \cap \cdots \cap U_m$ and $F_m = K_1 \cup \cdots \cup K_m$. Then $G_1 \subseteq B$ has finite measure. Since $E \subseteq B$, $E \subseteq V \cap B$.

:::

:::

::: {.pf-step #s2-2}

$m(G_m \setminus (V \cap B)) \to 0$ and $m(H \setminus F_m) \to 0$.

::: pf-proof

The first is continuity from above for $G_m \downarrow V \cap B$, valid because $m(G_1) < \infty$. The second is continuity from below for $F_m \uparrow H$, with $m(H) \le m(B) < \infty$ because $H \subseteq E$.

:::

:::

::: pf-qed

Given $\eps > 0$, step [](#s2-2){.pf-ref} gives $m$ with $m(G_m \setminus (V\cap B)) < \eps/2$ and $m(H \setminus F_m) < \eps/2$. Put $G = G_m$ and $F = F_m$. Then $F \subseteq H \subseteq E \subseteq V \cap B \subseteq G$, and
$$
m(G \setminus F) \le m(G \setminus (V\cap B)) + m(V \setminus H) + m(H \setminus F) < \eps.
$$

:::

:::

:::

:::

:::
