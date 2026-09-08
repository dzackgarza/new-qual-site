---
schema: qual/card@1
id: P-ALGS11C
kind: problem
title: Unique prime ideal equivalent to units-or-nilpotents and $A/\mathfrak{n}$ a field
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 3 of the official UCSD Spring 2011 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Verified the equivalence using maximal ideals, the nilradical as the intersection of prime ideals, and the prime correspondence for A/n.
---

::: problem
Consider a commutative ring $A$ with unity and let $\mathfrak{n}$ be its nilradical.
Show that the following statements are equivalent:

(i) $A$ has only one prime ideal

(ii) every element in $A$ is either a unit or nilpotent

(iii) $A/\mathfrak{n}$ is a field.
:::

::: {.solution}
<1>1. Assume that $A$ has exactly one prime ideal.
Then every element of $A$ is either a unit or nilpotent.
::: {.proof}
Let $\mathfrak p$ be the unique prime ideal of $A$.
The nilradical is the intersection of all prime ideals, hence
\[
\mathfrak n=\mathfrak p.
\]
Every maximal ideal is prime, so $\mathfrak p$ is also the unique maximal ideal.
If $a\in A$ is not a unit, then the proper ideal $(a)$ is contained in some maximal ideal; therefore
\[
a\in\mathfrak p=\mathfrak n.
\]
Membership in the nilradical means that $a$ is nilpotent.
Thus every element is a unit or nilpotent.
:::

<1>2. Assume that every element of $A$ is either a unit or nilpotent.
Then $A/\mathfrak n$ is a field.
::: {.proof}
Let $a+\mathfrak n$ be a nonzero element of $A/\mathfrak n$.
Then $a\notin\mathfrak n$, so $a$ is not nilpotent.
By hypothesis, $a$ is therefore a unit in $A$.
If $ab=1$, then
\[
(a+\mathfrak n)(b+\mathfrak n)=1+\mathfrak n,
\]
so $a+\mathfrak n$ is a unit in the quotient.
Every nonzero element of $A/\mathfrak n$ is therefore invertible, hence $A/\mathfrak n$ is a field.
:::

<1>3. Assume that $A/\mathfrak n$ is a field.
Then $A$ has exactly one prime ideal.
::: {.proof}
Every prime ideal $\mathfrak p$ of $A$ contains the nilradical $\mathfrak n$.
Prime ideals of $A$ containing $\mathfrak n$ correspond bijectively to prime ideals of $A/\mathfrak n$ via
\[
\mathfrak p\longmapsto \mathfrak p/\mathfrak n.
\]
Since $A/\mathfrak n$ is a field, its only prime ideal is $(0)$.
Consequently the only prime ideal of $A$ is $\mathfrak n$.
:::

<1>4. Therefore conditions (i), (ii), and (iii) are equivalent.
::: {.proof}
Steps <1>1, <1>2, and <1>3 prove
\[
\text{(i)}\Longrightarrow\text{(ii)}\Longrightarrow\text{(iii)}\Longrightarrow\text{(i)}.
\]
:::
:::
