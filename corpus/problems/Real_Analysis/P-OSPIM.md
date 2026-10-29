---
schema: qual/card@1
id: P-OSPIM
kind: problem
title: Approximating bounded sets by open and closed sets, measurability of $\inf_k f_k$ and $\sup_k f_k$,
  Fatou's lemma, and the monotone
  convergence theorem from Fatou
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Measure Theory
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source part (a) condition 2 omitted H ⊆ E ⊆ V, so it held for every E with V = H = ∅; the statement now requires H ⊆ E ⊆ V.'
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source reads 'measurable function' for the plural and 'Monotone Converge Theorem', and prints the hint inside part (b)(i); the statement corrects both typos and moves the hint to a hint block. The title now also names part (a)."
---

::: {.problem}
(a) Let $E \subseteq \RR^n$ be bounded.
Prove that the following are equivalent:

(i) For any $\varepsilon>0$ there exist an open set $G$ and a closed set $F$ such that $F \subseteq E \subseteq G$ and $m(G\sm F) < \varepsilon$.

(ii) There exist a $G_\delta$ set $V$ and an $F_\sigma$ set $H$ such that $H \subseteq E \subseteq V$ and $m(V\sm H) = 0$.

(b) Let $f_k$ be a sequence of extended real-valued Lebesgue measurable functions.

(i) Prove that $\inf_k f_k, \sup_k f_k$ are both Lebesgue measurable functions.

(ii) Carefully state Fatou's Lemma and deduce the Monotone Convergence Theorem from it.
:::

::: {.hint}
For (b)(i), argue that
$$
\theset{x \st \inf_k f_k(x) < a} = \Union_k \theset{x \st f_k(x) < a}.
$$
:::

::: {.solution}

::: pf

::: pf-step

Statements (a)(i) and (a)(ii) are equivalent.

::: pf-proof

Fix an open ball $B \supseteq E$.

::: pf-step

(i) implies (ii).

::: pf-proof

For each $k$, (i) with $\eps = 1/k$ gives open $G_k$ and closed $F_k$ with $F_k \subseteq E \subseteq G_k$ and $m(G_k \setminus F_k) < 1/k$. Put $V = \bigcap_k G_k$, a $G_\delta$ set, and $H = \bigcup_k F_k$, an $F_\sigma$ set. Then $H \subseteq E \subseteq V$, and $V \setminus H \subseteq G_k \setminus F_k$ for each $k$, so $m(V \setminus H) < 1/k$ for every $k$, and $m(V \setminus H) = 0$.

:::

:::

::: pf-step

(ii) implies (i).

::: pf-proof

::: pf-step

There are open $G_1 \supseteq G_2 \supseteq \cdots$ with $\bigcap_m G_m = V \cap B$ and $m(G_1) < \infty$, and closed $F_1 \subseteq F_2 \subseteq \cdots$ with $\bigcup_m F_m = H$.

::: pf-proof

Write $V = \bigcap_j U_j$ with $U_j$ open and $H = \bigcup_j K_j$ with $K_j$ closed, and put $G_m = B \cap U_1 \cap \cdots \cap U_m$ and $F_m = K_1 \cup \cdots \cup K_m$. Then $G_1 \subseteq B$ has finite measure. Since $E \subseteq B$, $E \subseteq V \cap B$.

:::

:::

::: {.pf-step #a-limits}

$m(G_m \setminus (V \cap B)) \to 0$ and $m(H \setminus F_m) \to 0$.

::: pf-proof

The first is continuity from above for $G_m \downarrow V \cap B$, valid because $m(G_1) < \infty$. The second is continuity from below for $F_m \uparrow H$, with $m(H) \le m(B) < \infty$ because $H \subseteq E$.

:::

:::

::: pf-qed

Given $\eps > 0$, step [](#a-limits){.pf-ref} gives $m$ with $m(G_m \setminus (V\cap B)) < \eps/2$ and $m(H \setminus F_m) < \eps/2$. Put $G = G_m$ and $F = F_m$. Then $F \subseteq H \subseteq E \subseteq V \cap B \subseteq G$, and
$$
m(G \setminus F) \le m(G \setminus (V\cap B)) + m(V \setminus H) + m(H \setminus F) < \eps.
$$

:::

:::

:::

:::

:::

::: pf-step

For measurable $f_k$ with values in $[-\infty, \infty]$, $\sup_k f_k$ and $\inf_k f_k$ are measurable.

::: pf-proof

For every $a \in \RR$, $\theset{\sup_k f_k \le a} = \bigcap_k\theset{f_k \le a}$ and $\theset{\inf_k f_k < a} = \bigcup_k\theset{f_k < a}$ are countable intersections and unions of measurable sets.

:::

:::

::: pf-step

Fatou's lemma: for measurable $f_n \ge 0$, $\int \liminf_n f_n \le \liminf_n \int f_n$.

:::

::: pf-step

If $0 \le f_1 \le f_2 \le \cdots$ are measurable and $f_n \to f$ pointwise, then $\int f_n \to \int f$.

::: pf-proof

$\int f_n$ is nondecreasing, so $\lim_n\int f_n$ exists in $[0,\infty]$. Since $f_n \le f$, $\lim_n \int f_n \le \int f$. Since $f = \liminf_n f_n$, Fatou's lemma gives $\int f \le \liminf_n \int f_n = \lim_n \int f_n$.

:::

:::

:::

:::
