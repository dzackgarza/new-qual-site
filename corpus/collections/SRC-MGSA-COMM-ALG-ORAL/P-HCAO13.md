---
schema: qual/card@1
id: P-HCAO13
kind: problem
title: An ideal maximal among those disjoint from a multiplicative set is prime
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Localization
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $R$ be a commutative ring with $1 \ne 0$, and let $S \subseteq R$ be a multiplicative set with $0 \notin S$.
Consider the set of ideals of $R$ which are disjoint from $S$.
Show that every maximal element of this set is a prime ideal.
:::

::: {.solution}

::: pf

::: pf-step
Let $I$ be maximal among ideals disjoint from $S$.

::: pf-proof
by hypothesis.
:::

:::

::: pf-step
Suppose $ab \in I$ with $a, b \notin I$.

::: pf-proof
assume for contradiction that $I$ is not prime.
:::

:::

::: pf-step
The ideals $I + (a)$ and $I + (b)$ are strictly larger than $I$.

::: pf-proof
they contain $a$ and $b$ respectively, which are not in $I$.
:::

:::

::: {.pf-step #each-meets-s}
Hence each meets $S$.

::: pf-proof
by maximality of $I$, any strictly larger ideal is not disjoint from $S$.
:::

:::

::: pf-step
So there are $s_1 \in (I + (a)) \cap S$ and $s_2 \in (I + (b)) \cap S$.

::: pf-proof
by step [](#each-meets-s){.pf-ref}.
:::

:::

::: pf-step
Write $s_1 = i_1 + r_1 a$ and $s_2 = i_2 + r_2 b$ with $i_1, i_2 \in I$ and $r_1, r_2 \in R$.

::: pf-proof
elements of $I + (a)$ and $I + (b)$ have this form.
:::

:::

::: pf-step
$s_1 s_2 = (i_1 + r_1 a)(i_2 + r_2 b) = i_1 i_2 + i_1 r_2 b + r_1 a i_2 + r_1 r_2 ab \in I$.

::: pf-proof
each term lies in $I$ (the first three contain a factor in $I$, and the last contains $ab \in I$).
:::

:::

::: {.pf-step #s1s2-in-intersection}
But $s_1 s_2 \in S$ (since $S$ is multiplicative), so $s_1 s_2 \in I \cap S$, contradicting $I \cap S = \emptyset$.

::: pf-proof
$S$ is closed under multiplication, and $I$ is disjoint from $S$.
:::

:::

::: pf-qed
the contradiction in step [](#s1s2-in-intersection){.pf-ref} shows $I$ is prime.
:::

:::
:::
