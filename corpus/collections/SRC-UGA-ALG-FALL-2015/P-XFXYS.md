---
schema: qual/card@1
id: P-XFXYS
kind: problem
title: A rng with a surjective right-multiplication map has a maximal left ideal
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
---
::: {.problem}
Let $R$ be a rng (a ring not assumed to have an identity $1$) with $R \ne \{0\}$, and suppose $R$ contains an element $u \in R$ such that for all $y \in R$, there exists an $x \in R$ with $x u = y$ (that is, $R u = R$).

Prove that $R$ contains a maximal left ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Any left ideal containing $u$ equals $R$.

::: pf-proof

If $u\in I$ for a left ideal $I$, then $Ru\subseteq I$ by closure under left multiplication. The hypothesis $Ru=R$ therefore implies $I=R$.

:::

:::

::: pf-step

The partially ordered set $\mathcal P$ of left ideals not containing $u$ has a maximal element.

::: pf-proof

Since $R\neq0$ and $Ru=R$, one has $u\neq0$, so the zero left ideal belongs to $\mathcal P$. The union of any nonempty chain of left ideals in $\mathcal P$ is again a left ideal, because two of its elements lie together in a member of the chain, and is still disjoint from $\{u\}$. The empty chain has the zero ideal as an upper bound. Zorn's lemma thus gives a maximal member $M\in\mathcal P$.

:::

:::

::: {.pf-step #s3}

The left ideal $M$ is maximal among all proper left ideals of $R$.

::: pf-proof

Since $u\notin M$, it is proper. Suppose $M\subsetneq L$ for another left ideal $L$. By maximality in $\mathcal P$, the ideal $L$ must contain $u$; by step [](#s1){.pf-ref} this forces $L=R$. Thus no proper left ideal strictly contains $M$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} establishes the existence of a maximal left ideal.

:::

:::

:::
