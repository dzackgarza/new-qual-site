---
schema: qual/card@1
id: P-ARTALG-AL04-7
kind: problem
title: Local rings characterized by their nonunits
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both directions and the condition a not in M with PDF page 33 (printed page 5), Rings 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the maximal-ideal existence argument and proved separately that the nonunit ideal is proper, maximal, and the only maximal ideal."
---

::: problem
A commutative ring $R$ is called a local ring if it has a unique maximal ideal.
Prove that if $R$ is a local ring with maximal ideal $M$ then an element $a \in R$ is a unit if and only if $a \notin M$.
Conversely, prove that if $R$ is a commutative ring in which the set of non-units forms an ideal, then $R$ is a local ring.
:::

::: solution
Rings are understood to have an identity, and maximal ideals are proper.

<1>1. Every nonunit belongs to a maximal ideal, and no proper ideal
contains a unit.

::: proof
If an ideal contains a unit $u$, it contains $u^{-1}u=1$ and
therefore the whole ring. If $a$ is a nonunit, its principal ideal
$(a)$ is proper, since $1=ra$ would make $a$ invertible.

For completeness, consider the partially ordered set of proper
ideals containing $(a)$. It is nonempty. The union of any nonempty
chain is an ideal containing $(a)$, and is proper: if it contained
$1$, one ideal in the chain would already contain $1$.
The empty chain has $(a)$ as an upper bound. Zorn's lemma gives
a maximal member, which is a maximal ideal of $R$ containing $a$.
:::

<1>2. If $R$ has a unique maximal ideal $M$, its units are exactly
the elements outside $M$.

::: proof
No unit lies in $M$ because $M$ is proper. Conversely every
nonunit lies in some maximal ideal by step <1>1, and that ideal
must be $M$. Thus $a$ is a unit if and only if $a\notin M$.
:::

<1>3. If the set $I$ of nonunits is an ideal, it is the unique
maximal ideal of $R$.

::: proof
The identity $1$ is a unit, so $1\notin I$ and $I$ is proper.
Any ideal strictly containing $I$ contains an element outside
$I$, hence a unit, and must equal $R$ by step <1>1. Thus $I$
is maximal.

Every maximal ideal $M$ is proper and so contains no units.
Consequently $M\subseteq I$. Since $M$ is maximal and $I$
is proper, $M=I$. This proves uniqueness and hence locality.
:::
:::
