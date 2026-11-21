---
schema: qual/card@1
id: P-APASP08A
kind: problem
title: "Group of order 121 is Abelian"
classification:
  areas:
  - applied-algebra
  topics:
  - Group Theory
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Show that a group of order 121 is Abelian.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the centre, the two cases and the cyclic-quotient lemma as separate steps.

Let $G$ be a group of order $121=11^{2}$.

::: pf

::: {.pf-step #centre}
$Z(G)$ is nontrivial, so $\cardinality{Z(G)}\in\theset{11,121}$.

::: pf-proof
$G$ is a nontrivial finite $11$-group, and a nontrivial finite $p$-group has nontrivial centre: the class equation $\cardinality{G}=\cardinality{Z(G)}+\sum_{i}\cardinality{G:C_{G}(x_{i})}$ has every index $\cardinality{G:C_{G}(x_{i})}$ divisible by $11$, so $11$ divides $\cardinality{Z(G)}$, which is nonzero. A subgroup of order dividing $121$ and a multiple of $11$ has order $11$ or $121$.
:::

:::

::: {.pf-step #cyclic-quotient}
If $G/Z(G)$ is cyclic then $G$ is abelian.

::: pf-proof
If $G/Z(G)=\langle gZ(G)\rangle$, then any $x,y\in G$ are $x=g^{a}z_{1}$ and $y=g^{b}z_{2}$ with $z_{1},z_{2}\in Z(G)$, so $xy=g^{a+b}z_{1}z_{2}=g^{a+b}z_{2}z_{1}=yx$ because $z_{1},z_{2}$ are central and powers of $g$ commute.
:::

:::

::: {.pf-step #exclude}
$\cardinality{Z(G)}=11$ is impossible.

::: pf-proof
If $\cardinality{Z(G)}=11$ then $\cardinality{G/Z(G)}=121/11=11$, and a group of prime order is cyclic, so $G/Z(G)$ is cyclic; by step [](#cyclic-quotient){.pf-ref} $G$ is then abelian, which forces $Z(G)=G$ and $\cardinality{Z(G)}=121$, a contradiction.
:::

:::

::: {.pf-qed}
By step [](#centre){.pf-ref} the order of $Z(G)$ is $11$ or $121$, and step [](#exclude){.pf-ref} rules out $11$; so $Z(G)=G$ and $G$ is abelian.
:::

:::

:::
