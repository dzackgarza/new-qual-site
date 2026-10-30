---
schema: qual/card@1
id: P-DBY54
kind: problem
title: Maximal ideals disjoint from a multiplicative set exist and are prime
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
  - Zorn's Lemma
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring, and $S\subset R$ be a nonempty subset that does not contain 0 such that for all $x, y\in S$ we have $xy\in S$.
Let $\mci$ be the set of all ideals $I\normal R$ such that $I\intersect S = \emptyset$.

Show that for every ideal $I\in \mci$, there is an ideal $J\in \mci$ such that $I\subset J$ and $J$ is not properly contained in any other ideal in $\mci$.

Prove that every such ideal $J$ is prime.
:::

::: {.solution}

::: pf

::: {.pf-step #zorn}

For every $I\in\mci$ there is a maximal element $J$ of $\mci$ with $I\subseteq J$.

::: pf-proof

Let $\mathcal P=\{K\in\mci: I\subseteq K\}$, ordered by inclusion; it contains $I$. Let $\mathcal C\subseteq\mathcal P$ be a nonempty chain and $U=\bigcup_{K\in\mathcal C}K$. Any two elements of $U$ lie in a common member of the chain, so $U$ is an ideal, and $U\supseteq I$. If $s\in U\cap S$, then $s\in K\cap S$ for some $K\in\mathcal C$, which is impossible. So $U\in\mathcal P$ is an upper bound. Zorn's lemma gives a maximal element $J$ of $\mathcal P$. A member of $\mci$ that contains $J$ contains $I$, so it lies in $\mathcal P$ and equals $J$.

:::

:::

::: {.pf-step #proper}

Every $J\in\mci$ is proper.

::: pf-proof

$S$ is nonempty and $J\cap S=\emptyset$, so $J\neq R$.

:::

:::

::: {.pf-step #prime}

A maximal element $J$ of $\mci$ is prime.

::: pf-proof

Let $ab\in J$ and suppose $a\notin J$ and $b\notin J$. The ideals $J+Ra$ and $J+Rb$ strictly contain $J$, so by maximality they are not in $\mci$. Choose $x=p_1+r_1a\in S$ and $y=p_2+r_2b\in S$ with $p_1,p_2\in J$ and $r_1,r_2\in R$. Then
$$
xy=p_1p_2+p_1r_2b+p_2r_1a+r_1r_2ab\in J,
$$
since each term contains a factor $p_1$, $p_2$ or $ab$ from $J$. But $xy\in S$, so $xy\in J\cap S=\emptyset$, a contradiction.

:::

:::

::: pf-qed

Step [](#zorn){.pf-ref} gives the ideal $J$, and Steps [](#proper){.pf-ref} and [](#prime){.pf-ref} show that $J$ is prime.

:::

:::

:::
