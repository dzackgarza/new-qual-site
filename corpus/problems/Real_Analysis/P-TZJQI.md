---
schema: qual/card@1
id: P-TZJQI
kind: problem
title: $E$ is measurable if and only if $E$ is regular
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
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: 'The source wrote only "Show that E is measurable iff E is regular", with E and regularity undefined; the statement now takes E in R^n with finite outer measure and defines regularity as equality of inner and outer measure, which fails as a criterion for sets of infinite outer measure.'
---

::: {.problem}

Let $\mu$ be Lebesgue measure on $\RR^n$, $\mu^*$ Lebesgue outer measure, and $E \subseteq \RR^n$ a set with $\mu^*(E) < \infty$. Call $E$ regular if its inner measure $\mu_*(E) \coloneqq \sup\theset{\mu(F) : F \subseteq E,\ F \text{ compact}}$ equals $\mu^*(E)$. Show that $E$ is measurable iff $E$ is regular.

:::

::: {.solution}

Outer measure is outer regular: $\mu^*(E) = \inf\theset{\mu(G) : G \supseteq E,\ G \text{ open}}$ for every $E \subseteq \RR^n$.

::: pf

::: {.pf-step #s1}

If $A$ is measurable and $\eps > 0$, there is an open $G \supseteq A$ with $\mu(G \setminus A) < \eps$.

::: pf-proof

Write $A = \bigcup_k A_k$ with $A_k = A \cap B(0,k)$, so $\mu(A_k) < \infty$. Outer regularity gives open $G_k \supseteq A_k$ with $\mu(G_k) < \mu(A_k) + \eps 2^{-k}$, so $\mu(G_k \setminus A_k) < \eps 2^{-k}$. Then $G = \bigcup_k G_k$ is open, contains $A$, and $G \setminus A \subseteq \bigcup_k (G_k \setminus A_k)$ has measure less than $\eps$.

:::

:::

::: pf-step

Measurable $\Rightarrow$ regular.

::: pf-proof

Let $\eps > 0$. $E^c$ is measurable, so step [](#s1){.pf-ref} gives an open $G \supseteq E^c$ with $\mu(G \setminus E^c) < \eps$, and the closed set $F = G^c \subseteq E$ satisfies $\mu(E \setminus F) = \mu(G \setminus E^c) < \eps$.
The compact sets $F \cap \overline{B(0,k)}$ increase to $F$, so $\mu(F \cap \overline{B(0,k)}) > \mu(E) - 2\eps$ for large $k$.
Hence $\mu_*(E) = \mu(E) = \mu^*(E)$.

:::

:::

::: pf-step

Regular $\Rightarrow$ measurable.

::: pf-proof

Outer regularity gives open $G_k \supseteq E$ with $\mu(G_k) \le \mu^*(E) + 1/k$; let $V = \cap_k G_k$, a $G_\delta$ containing $E$, with $\mu(V) = \mu^*(E)$.

The definition of $\mu_*$ gives compact $F_k \subseteq E$ with $\mu(F_k) \ge \mu_*(E) - 1/k$; let $H = \cup_k F_k$, an $F_\sigma$ inside $E$, with $\mu(H) = \mu_*(E)$.
Since $\mu^*(E) = \mu_*(E) < \infty$, $\mu(V \setminus H) = \mu(V) - \mu(H) = 0$. Then $E = H \cup (E \setminus H)$ with $H$ measurable and $E \setminus H \subseteq V \setminus H$ null, hence measurable because Lebesgue measure is complete; so $E$ is measurable.

:::

:::

:::

:::
