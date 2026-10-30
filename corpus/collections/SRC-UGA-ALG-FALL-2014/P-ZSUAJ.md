---
schema: qual/card@1
id: P-ZSUAJ
kind: problem
title: $xR$ is proper in a nonzero commutative ring without unit and with no proper
  maximal ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a nonzero commutative ring without unit such that $R$ does not contain a proper maximal ideal.
Prove that for all $x\in R$, the ideal $xR$ is proper.

> You may assume the axiom of choice.
:::

::: {.solution}

::: pf

::: {.pf-step #assume}

Suppose for contradiction that $xR=R$ for some $x\in R$. Then the family $\mathcal S$ of ideals of $R$ that do not contain $x$ is nonempty and every member of $\mathcal S$ is proper.

::: pf-proof

$R$ is nonzero, so $x$ can be taken with $R=xR\neq0$; the zero ideal does not contain $x$ unless $x=0$, and $x=0$ would give $R=0R=0$. An ideal containing all of $R$ contains $x$.

:::

:::

::: {.pf-step #zorn}

$\mathcal S$ has a maximal element $M$ under inclusion.

::: pf-proof

The union of a chain in $\mathcal S$ is an ideal and does not contain $x$, so it is an upper bound in $\mathcal S$. Apply Zorn's lemma.

:::

:::

::: {.pf-step #maximal}

$M$ is a proper maximal ideal of $R$.

::: pf-proof

$M$ is proper by Step [](#assume){.pf-ref}. Let $M\subsetneq N$ be an ideal. By maximality of $M$ in $\mathcal S$, $x\in N$, so $R=xR\subseteq N$.

:::

:::

::: pf-qed

Step [](#maximal){.pf-ref} contradicts the hypothesis that $R$ has no proper maximal ideal. Hence $xR\neq R$ for every $x\in R$.

:::

:::

:::
