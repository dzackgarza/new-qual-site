---
schema: qual/card@1
id: P-URS24
kind: problem
title: Open subsets of the quotient space $\RR/\QQ$
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
Define an equivalence relation $\sim$ on $\RR$ by $x \sim y$ if and only if $x - y \in \QQ$.
Let $X$ be the set of equivalence classes, endowed with the quotient topology induced by the canonical projection $\pi : \RR \to X$.

Describe, with proof, all open subsets of $X$ with respect to this topology.
:::

::: {.solution}
<1>1. $U \subseteq X$ is open iff $\pi^{-1}(U)$ is open in $\mathbb{R}$.
::: {.proof}
definition of the quotient topology.
:::

<1>2. $\pi^{-1}(U)$ is a union of equivalence classes, i.e. a union of cosets of $\mathbb{Q}$ in $\mathbb{R}$.
::: {.proof}
the equivalence classes are exactly the cosets $x + \mathbb{Q}$.
:::

<1>3. A union of cosets of $\mathbb{Q}$ is open in $\mathbb{R}$ iff it is either empty or all of $\mathbb{R}$.
::: {.proof}
if $\pi^{-1}(U)$ is a nonempty open set, it contains an open interval $(a, b)$; but every coset of $\mathbb{Q}$ meets $(a, b)$ (since $\mathbb{Q}$ is dense), so $\pi^{-1}(U)$ contains every coset, hence equals $\mathbb{R}$.
:::

<1>4. Hence the only open subsets of $X$ are $\varnothing$ and $X$.
::: {.proof}
<1>1 and <1>3.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
