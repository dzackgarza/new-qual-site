---
schema: qual/card@1
id: E-7ML5F
kind: problem
title: Separation axioms under refinement of topologies
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: Ana Emilia de Orellana, "Solutions -
    Topology Munkres", Section 31 Exercise 4, printed p. 32
    (tmp/sources/munkres-solutions-anadeore.pdf), and "Doug's World", "Munkres - Topology -
    Chapter 4 Solutions" (30 August 2017), Problem 31.4, printed pp. 4-5
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf); checked against Munkres, Topology (2000),
    Section 31 Exercise 4, printed p. 199, Example 31.1 (printed p. 197: R_K is Hausdorff and not
    regular) and Example 31.2 (printed p. 198: R_l is normal). The six answers are those of the two
    sets: a finer topology inherits Hausdorffness from a coarser one and nothing else transfers in
    either direction. What was corrected: Orellana's R_K example for the failure of normality under
    passing to a finer topology reads "the K-topology is neither regular nor normal", which is
    correct but is asserted without the implication normal => regular that makes R_K a witness;
    the card states that implication (a normal space is regular because its one-point sets are
    closed). Doug's World's normal case is stated for R rather than argued; the card keeps the
    example and the reason.
---

::: {.exercise}

Let $X$ and $X'$ denote a single set under two topologies $\mathcal{T}$ and $\mathcal{T}'$, respectively; assume that $\mathcal{T}' \supset \mathcal{T}$.
If one of the spaces is Hausdorff (or regular, or normal), what does that imply about the other?
:::

::: {.solution}

::: pf

::: pf-step
Hausdorff property ($T_2$):
- If $(X, \mathcal{T})$ is Hausdorff, then $(X, \mathcal{T}')$ is Hausdorff.
- If $(X, \mathcal{T}')$ is Hausdorff, $(X, \mathcal{T})$ need not be Hausdorff.

::: pf-proof

::: pf-step
**Forward preservation:** Suppose $(X, \mathcal{T})$ is Hausdorff. For any distinct $x \neq y \in X$, there exist disjoint open sets $U, V \in \mathcal{T}$ with $x \in U$ and $y \in V$. Since $\mathcal{T} \subset \mathcal{T}'$, $U, V \in \mathcal{T}'$, so $(X, \mathcal{T}')$ is Hausdorff.
:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is Hausdorff, but the coarser cofinite topology $\mathcal{T}$ on $X$ is not Hausdorff.
:::

:::

:::

::: pf-step
Regular property ($T_3$):
Neither direction holds:
- $(X, \mathcal{T})$ regular does NOT imply $(X, \mathcal{T}')$ is regular.
- $(X, \mathcal{T}')$ regular does NOT imply $(X, \mathcal{T})$ is regular.

::: pf-proof

::: pf-step
**Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\RR$ is regular (and metric). The $K$-topology $\mathcal{T}' = \mathcal{T}_K$ is strictly finer than $\mathcal{T}$, but $(\RR, \mathcal{T}_K)$ is not regular because the closed set $K = \{1/n \mid n \in \ZZ_+\}$ and the point $0 \notin K$ cannot be separated by disjoint open sets in $\mathcal{T}_K$.
:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is regular, but the coarser cofinite topology $\mathcal{T}$ is not regular.
:::

:::

:::

::: pf-step
Normal property ($T_4$):
Neither direction holds:
- $(X, \mathcal{T})$ normal does NOT imply $(X, \mathcal{T}')$ is normal.
- $(X, \mathcal{T}')$ normal does NOT imply $(X, \mathcal{T})$ is normal.

::: pf-proof

::: pf-step
**Forward failure:** The standard Euclidean topology $\mathcal{T}$ on $\RR$ is normal, but the strictly finer $K$-topology $\mathcal{T}_K$ is not even regular, and therefore not normal.
:::

::: pf-step
**Backward failure:** The discrete topology $\mathcal{T}'$ on an infinite set $X$ is normal, but the coarser cofinite topology $\mathcal{T}$ is not normal (it is not even Hausdorff).
:::

:::

:::

::: pf-step
Summary Table of Implications:
- **Hausdorff:** Coarser $\implies$ Finer (yes); Finer $\implies$ Coarser (no).
- **Regular:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).
- **Normal:** Coarser $\implies$ Finer (no); Finer $\implies$ Coarser (no).
:::

:::

:::
