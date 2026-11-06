---
schema: qual/card@1
id: P-7QSIF
kind: problem
title: Normal $p$-subgroups lie in every Sylow $p$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of Hungerford II.5.6.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section II.5,
    exercise 6, book page 96: "If H is a normal subgroup of order p^k of a
    finite group G, then H is contained in every Sylow p-subgroup of G." The
    card states exactly this. The proof was checked: H is a p-subgroup, so it
    lies in some Sylow p-subgroup Q, and every Sylow p-subgroup is conjugate to
    the given P, say Q = gPg^{-1}; conjugating H ≤ gPg^{-1} by g^{-1} gives
    g^{-1}Hg ≤ P, and normality of H makes g^{-1}Hg = H, so H ≤ P. Both halves
    of the Sylow theory used (existence of a containing Sylow subgroup, and
    conjugacy of Sylow subgroups) are theorems of the same section, and the
    argument concludes for an arbitrary P. Complete; no defect.
---

::: {.problem}
Let $p$ be a prime, $G$ a finite group and $H \trianglelefteq G$ a normal subgroup of order $p^k$.
Show that $H$ is contained in every Sylow $p$-subgroup of $G$.
:::

::: {.solution}
Let $P$ be an arbitrary Sylow $p$-subgroup of $G$.

::: pf

::: {.pf-step #s1}

There exists $g\in G$ such that $H\le gPg^{-1}$.

::: pf-proof

The subgroup $H$ is a $p$-subgroup. By Sylow's containment theorem, every
$p$-subgroup of $G$ is contained in a conjugate of a Sylow $p$-subgroup. Hence
$H\le gPg^{-1}$ for some $g\in G$.

:::

:::

::: pf-step

One has $H\le P$.

::: pf-proof

Conjugating the inclusion in step [](#s1){.pf-ref} by $g^{-1}$ gives
$$
g^{-1}Hg\le P.
$$
Since $H\trianglelefteq G$, normality gives $g^{-1}Hg=H$. Therefore $H\le P$.

:::

:::

::: pf-step

Thus $H$ is contained in every Sylow $p$-subgroup of $G$.

::: pf-proof

The Sylow subgroup $P$ was arbitrary.

:::

:::

:::

:::
