---
schema: qual/card@1
id: P-IK7LQ
kind: problem
title: Free groups are torsion-free
classification:
  areas:
  - algebra
  topics:
  - Free Groups
  - Torsion
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the Hungerford I.9 exercise statement reproduced in a Modern Algebra assignment keyed to Hungerford 1.9.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that every non-identity element in a free group $F$ has infinite order.
:::

::: solution
Let $F=F(X)$ be free on $X$, and let $1\ne g\in F$. We show that $g^m\ne1$
for every integer $m\ne0$.

<1>1. There exist reduced words $u$ and $v$ such that
\[
g=uvu^{-1},
\]
where $v$ is nonempty and cyclically reduced.
::: proof
Start with the reduced word for $g$. If its first letter is inverse to its last
letter, remove those two letters and record the first letter in $u$. Repeating
this operation must terminate because the word is finite. The remaining word
$v$ is nonempty, since otherwise the original reduced word would represent the
identity, and its first and last letters are not inverse. Thus $v$ is cyclically
reduced and $g=uvu^{-1}$.
:::

<1>2. For every integer $m\ge1$, the word $v^m$ is reduced and nonempty.
::: proof
Each copy of $v$ is reduced. At a junction between two consecutive copies, the
last letter of one copy is followed by the first letter of the next. Since $v$
is cyclically reduced, these letters are not inverse, so no cancellation occurs
at any junction. Hence $v^m$ is a reduced word of positive length.
:::

<1>3. For every integer $m\ge1$, one has $g^m\ne1$.
::: proof
Using <1>1,
\[
g^m=(uvu^{-1})^m=uv^m u^{-1}.
\]
If $g^m=1$, conjugating by $u^{-1}$ and $u$ would give $v^m=1$, contradicting
<1>2 because a nonempty reduced word in a free group does not represent the
identity.
:::

<1>4. Therefore $g$ has infinite order.
::: proof
If $g$ had finite order, then $g^m=1$ for some $m\ge1$, contradicting <1>3.
Negative exponents add no further possibility since $g^m=1$ with $m<0$ implies
$g^{-m}=1$.
:::
:::
