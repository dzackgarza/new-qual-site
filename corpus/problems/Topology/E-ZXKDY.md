---
schema: qual/card@1
id: E-ZXKDY
kind: problem
title: Degree of a non-surjective map $S^n\to S^n$ is zero
classification:
  areas:
  - topology
  topics:
  - Degree
  - Homology
relations: []
review: draft
audit:
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source does not declare f; the statement now names f as a continuous map S^n -> S^n with n >= 1."
---

::: {.exercise}
Let $f\colon S^n\to S^n$ be continuous, $n\ge1$. Show that if $f$ is not surjective then $\deg f = 0$.
:::

::: {.solution}

Choose $p\in S^n\setminus f(S^n)$.

::: pf

::: {.pf-step #factor}

$f$ factors as $S^n \mapsvia{f_1} S^n\smts{p}\mapsvia{j} S^n$, where $j$ is the inclusion.

::: pf-proof

The image of $f$ lies in $S^n\smts{p}$; let $f_1$ be the corestriction.

:::

:::

::: {.pf-step #zero-group}

$H_n(S^n\smts{p})=0$.

::: pf-proof

Stereographic projection gives $S^n\smts{p}\cong\RR^n$, which is contractible, and $n\ge1$.

:::

:::

::: pf-step

$\deg f=\boxed{0}$.

::: pf-proof

By step [](#factor){.pf-ref}, $f_*=j_*\circ(f_1)_*$ on $H_n(S^n)\cong\ZZ$, and this composite factors through $H_n(S^n\smts{p})$, which is $0$ by step [](#zero-group){.pf-ref}. So $f_*=0$, which is multiplication by $0$.

:::

:::

:::

:::
