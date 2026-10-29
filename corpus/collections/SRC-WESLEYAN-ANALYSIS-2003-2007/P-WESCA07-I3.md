---
schema: qual/card@1
id: P-WESCA07-I3
kind: problem
title: "State the local Cauchy Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section I, item 3 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the local Cauchy Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Local Cauchy Theorem.** Let $U\subseteq\CC$ be open and let $f:U\to\CC$ be analytic. For every $z_0\in U$, there exists $r>0$ such that
$$
\overline{B(z_0,r)}\subseteq U
$$
and
$$
\boxed{\int_\gamma f(z)\,dz=0}
$$
for every closed piecewise $C^1$ path $\gamma$ contained in $B(z_0,r)$.


::: pf-proof

This is the local form of Cauchy's theorem: on a sufficiently small disk contained in the domain, a holomorphic function has zero integral around every closed path.

:::

:::

::: {.pf-step #s1-2}

Equivalently, for every $z_0\in U$ there is a neighborhood $V\subseteq U$ of $z_0$ on which $f$ has a holomorphic primitive $F$, so that
$$
F'=f\quad\text{on }V.
$$


::: pf-proof

Vanishing of all closed-path integrals on a connected open set is equivalent to path independence of the integral from a base point, which defines a primitive. Conversely, the integral of a derivative over every closed path is zero.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the requested theorem statement; step [](#s1-2){.pf-ref} gives its standard equivalent formulation.

:::

:::

:::
