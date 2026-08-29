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

::: problem
Let $R$ be a nonzero commutative ring without unit such that $R$ does not contain a proper maximal ideal.
Prove that for all $x\in R$, the ideal $xR$ is proper.

> You may assume the axiom of choice.
:::

::: {.solution}
<1>1. Suppose for contradiction that $xR = R$ for some $x \in R$.
Proof: assume the contrary.

<1>2. Then $x \in xR = R$, so there is $y \in R$ with $x = xy$.
Proof: since $xR = R$, the element $x$ lies in $xR$, so $x = xy$ for some $y \in R$.

<1>3. Consider the ideal $J = \{r \in R : r = ry\}$.
<2>1. $J$ is an ideal.
Proof: $0 = 0y$; if $r = ry$ and $s = sy$, then $r + s = ry + sy = (r+s)y$; and for $t \in R$, $tr = t(ry) = (tr)y$ (using commutativity).
<2>2. $J$ is proper.
Proof: if $J = R$, then $r = ry$ for all $r \in R$, so $y$ is a right identity; since $R$ is commutative, $y$ is a two-sided identity (a unit), contradicting that $R$ has no unit. Hence $J \neq R$.

<1>4. By Zorn's lemma, $J$ is contained in a maximal ideal $M$.
<2>1. Consider the poset of proper ideals of $R$ containing $J$, ordered by inclusion.
Proof: setup.
<2>2. Every chain has an upper bound (the union of the chain), and this union is proper.
Proof: the union of a chain of ideals is an ideal; if the union were $R$, then $x$ would lie in some member $K$ of the chain, and since $xR = R$ (<1>1), we would get $R = xR \subseteq K$, contradicting that $K$ is proper.
<2>3. Hence by Zorn's lemma there is a maximal proper ideal $M$ containing $J$.
Proof: <2>1 and <2>2.

<1>5. This contradicts the hypothesis that $R$ has no proper maximal ideal.
Proof: <1>4 produces a maximal ideal $M$.

<1>6. Therefore $xR \neq R$, i.e. $xR$ is proper, for every $x \in R$.
Proof: <1>1–<1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
