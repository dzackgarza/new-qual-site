---
schema: qual/card@1
id: P-HCAO13
kind: problem
title: An ideal maximal among those disjoint from a multiplicative set is prime
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $R$ be a commutative ring with $1 \ne 0$, and let $S \subseteq R$ be a multiplicative set with $0 \notin S$.
Consider the set of ideals of $R$ which are disjoint from $S$.
Show that every maximal element of this set is a prime ideal.
:::

::: {.solution}
**Goal.** Show an ideal maximal among those disjoint from a multiplicative set $S$ is prime.

<1>1. Let $I$ be maximal among ideals disjoint from $S$.
Proof: by hypothesis.

<1>2. Suppose $ab \in I$ with $a, b \notin I$.
Proof: assume for contradiction that $I$ is not prime.

<1>3. The ideals $I + (a)$ and $I + (b)$ are strictly larger than $I$.
Proof: they contain $a$ and $b$ respectively, which are not in $I$.

<1>4. Hence each meets $S$.
Proof: by maximality of $I$, any strictly larger ideal is not disjoint from $S$.

<1>5. So there are $s_1 \in (I + (a)) \cap S$ and $s_2 \in (I + (b)) \cap S$.
Proof: by <1>4.

<1>6. Write $s_1 = i_1 + r_1 a$ and $s_2 = i_2 + r_2 b$ with $i_1, i_2 \in I$ and $r_1, r_2 \in R$.
Proof: elements of $I + (a)$ and $I + (b)$ have this form.

<1>7. $s_1 s_2 = (i_1 + r_1 a)(i_2 + r_2 b) = i_1 i_2 + i_1 r_2 b + r_1 a i_2 + r_1 r_2 ab \in I$.
Proof: each term lies in $I$ (the first three contain a factor in $I$, and the last contains $ab \in I$).

<1>8. But $s_1 s_2 \in S$ (since $S$ is multiplicative), so $s_1 s_2 \in I \cap S$, contradicting $I \cap S = \emptyset$.
Proof: $S$ is closed under multiplication, and $I$ is disjoint from $S$.

<1>9. Q.E.D. Proof: the contradiction in <1>8 shows $I$ is prime.
:::
