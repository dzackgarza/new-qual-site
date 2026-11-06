---
schema: qual/card@1
id: P-RBKAW
kind: problem
title: A radical extension is radical over every intermediate field
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Solvable Groups
  - Galois Theory
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section V.9,
    exercise 1, book page 309: "If F is a radical extension field of K and E is an
    intermediate field, then F is a radical extension of E." The card states
    exactly this. The proof was checked against the section's definition of a
    radical extension as a tower K = E_0 ⊂ ... with E_i = E_{i-1}(u_i) and
    u_i^{m_i} ∈ E_{i-1}: writing F = K(α_1, ..., α_n) with α_i^{n_i} in the
    preceding step field, the same list generates F over E and each α_i^{n_i} lies
    in the corresponding step field over E because K ⊆ E, so the tower can be
    re-based at E. Complete; no defect.
---
review: draft
---

::: {.problem}
If $F$ is a radical extension field of $K$ and $E$ is an intermediate field, then $F$ is a radical extension of $E$.
:::

::: {.solution}
Since $F/K$ is radical, $F=K(\alpha_1,\ldots,\alpha_n)$, where for each $i$ there is $n_i>0$ with $\alpha_i^{n_i}\in K(\alpha_1,\ldots,\alpha_{i-1})$.

::: pf

::: {.pf-step #s1}

$F=E(\alpha_1,\ldots,\alpha_n)$.

::: pf-proof

Since $K\subseteq E\subseteq F$, we have $F=K(\alpha_1,\ldots,\alpha_n)\subseteq E(\alpha_1,\ldots,\alpha_n)\subseteq F$.

:::

:::

::: {.pf-step #s2}

For each $i$, $\alpha_i^{n_i}\in E(\alpha_1,\ldots,\alpha_{i-1})$.

::: pf-proof

$\alpha_i^{n_i}\in K(\alpha_1,\ldots,\alpha_{i-1})\subseteq E(\alpha_1,\ldots,\alpha_{i-1})$ because $K\subseteq E$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} exhibit $F$ as $E(\alpha_1,\ldots,\alpha_n)$ with $\alpha_i^{n_i}\in E(\alpha_1,\ldots,\alpha_{i-1})$ for every $i$, which is the definition of a radical extension of $E$.

:::

:::

:::
