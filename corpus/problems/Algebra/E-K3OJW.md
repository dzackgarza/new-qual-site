---
schema: qual/card@1
id: E-K3OJW
kind: problem
title: Normal Sylow $p$-subgroup when $|G|=p^{e}v$ with $p>v$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
\envlist

- Let $G$ be a finite group of order $p^e v$, where $e$ and $v$ are positive integers, $p$ is prime, $p>v$, and $p\nmid v$.
  Show that $G$ has a normal Sylow p-subgroup.
:::

::: {.solution}
Let $n_p$ denote the number of Sylow $p$-subgroups of $G$.

<1>1. Sylow's theorem gives
\[
n_p\mid v,
\qquad
n_p\equiv1\pmod p.
\]
::: {.proof}
Since
\[
|G|=p^e v
\]
with $p\nmid v$, a Sylow $p$-subgroup has order $p^e$. The third Sylow theorem says that the number of such subgroups divides the complementary factor $v$ and is congruent to $1$ modulo $p$.
:::

<1>2. One has $n_p=1$.
::: {.proof}
Because $n_p\mid v$, we have
\[
1\le n_p\le v<p.
\]
The only positive integer strictly less than $p$ that is congruent to $1$ modulo $p$ is $1$. Thus $n_p=1$.
:::

<1>3. Therefore the Sylow $p$-subgroup is normal.
::: {.proof}
All Sylow $p$-subgroups are conjugate. Since there is exactly one, it is fixed by conjugation by every element of $G$, hence is normal.
:::
:::
