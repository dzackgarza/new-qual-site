---
schema: qual/card@1
id: P-N4ABN
kind: problem
title: If $A$ and $B$ are normal and $G/A$, $G/B$ are abelian then $G/(A \cap B)$
  is abelian
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Abelian Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
If $A$ and $B$ are normal in $G$, and $G/A$ and $G/B$ are abelian, show that $G/(A \cap B)$ is also abelian.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For a normal subgroup $N\lhd G$, the quotient $G/N$ is abelian if and only if $[G,G]\subseteq N$.

::: pf-proof

$G/N$ is abelian exactly when $xyx^{-1}y^{-1}N=N$ for all $x,y\in G$, that is, when every commutator lies in $N$; since $N$ is a subgroup, this is equivalent to $[G,G]\subseteq N$.

:::

:::

::: {.pf-step #s2}

$[G,G]\subseteq A\cap B$.

::: pf-proof

Step [](#s1){.pf-ref} applied to $A$ and to $B$ gives $[G,G]\subseteq A$ and $[G,G]\subseteq B$.

:::

:::

::: pf-qed

The intersection $A\cap B$ of normal subgroups is normal, so step [](#s1){.pf-ref} applied to $N=A\cap B$, together with step [](#s2){.pf-ref}, shows that $G/(A\cap B)$ is abelian.

:::

:::

:::
