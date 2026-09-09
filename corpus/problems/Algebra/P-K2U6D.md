---
schema: qual/card@1
id: P-K2U6D
kind: problem
title: A group of order $231$ has a normal Sylow $7$-subgroup and a central Sylow $11$-subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Centralizers and Normalizers
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

::: problem
Let $G$ be a group of order
\[
231=3\cdot7\cdot11.
\]
Show that $G$ has a normal Sylow $7$-subgroup and that its Sylow $11$-subgroup is central.
:::

::: {.solution}
<1>1. The Sylow $7$-subgroup is normal.
::: {.proof}
Let $n_7$ be the number of Sylow $7$-subgroups. Sylow gives
\[
n_7\equiv1\pmod7,
\qquad
n_7\mid 33.
\]
The divisors of $33$ are $1,3,11,33$, and only $1$ is congruent to $1$ modulo $7$. Hence
\[
n_7=1.
\]
So the Sylow $7$-subgroup is unique and therefore normal.
:::

<1>2. The Sylow $11$-subgroup is unique.
::: {.proof}
Similarly,
\[
n_{11}\equiv1\pmod{11},
\qquad
n_{11}\mid21.
\]
Among $1,3,7,21$, only $1$ is congruent to $1$ modulo $11$. Thus $n_{11}=1$. Let $Q$ denote this unique Sylow $11$-subgroup; then $Q\trianglelefteq G$ and $Q\cong C_{11}$.
:::

<1>3. The subgroup $Q$ is central.
::: {.proof}
Conjugation gives a homomorphism
\[
G\longrightarrow\Aut(Q)\cong C_{10}.
\]
Because $Q$ is abelian, $Q$ lies in the kernel, so the image has order dividing
\[
|G/Q|=21.
\]
It also has order dividing $|\Aut(Q)|=10$. Since
\[
\gcd(21,10)=1,
\]
the image is trivial. Thus every element of $G$ centralizes every element of $Q$, so
\[
Q\subseteq Z(G).
\]
:::
:::
