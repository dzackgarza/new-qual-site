---
schema: qual/card@1
id: E-NNTQB
kind: problem
title: 'Lagrange''s theorem: $|G|/|H|=[G:H]$ for finite $G$'
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
Show that if $G$ is finite then $\abs{G}/\abs{H} = [G: H]$.
:::

::: {.solution}
<1>1. The left cosets of $H$ in $G$ partition $G$ into $[G : H]$ disjoint sets.
::: {.proof}
the cosets $gH$ are the equivalence classes of the relation $g_1 \sim g_2 \iff g_1^{-1}g_2 \in H$.
:::

<1>2. Each coset $gH$ has exactly $|H|$ elements.
::: {.proof}
the map $H \to gH$, $h \mapsto gh$, is a bijection.
:::

<1>3. Hence $|G| = [G : H] \cdot |H|$.
::: {.proof}
<1>1 and <1>2 (the total number of elements is the number of cosets times the size of each coset).
:::

<1>4. Therefore $|G|/|H| = [G : H]$.
::: {.proof}
<1>3, dividing by $|H|$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
