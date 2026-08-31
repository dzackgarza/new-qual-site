---
schema: qual/card@1
id: P-ALGF18A
kind: problem
title: Group of order $2pq$ has normal subgroups of orders $pq$ and $q$
classification:
  areas:
  - algebra
  topics:
  - Group Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Suppose $p < q$ are two odd primes.
Suppose $G$ is a group of order $2pq$.
Prove that $G$ has normal subgroups $N_1$ and $N_2$ such that $|N_1| = pq$, $|N_2| = q$, and $N_2 \subseteq N_1$.
:::

::: {.solution}
**Goal.** For $G$ of order $2pq$ with odd primes $p < q$, find normal subgroups $N_1, N_2$ with $|N_1| = pq$, $|N_2| = q$, $N_2 \subseteq N_1$.

<1>1. $G$ has a normal Sylow $q$-subgroup $N_2$ of order $q$.
<2>1. The number $n_q$ of Sylow $q$-subgroups satisfies $n_q \equiv 1 \pmod q$ and $n_q \mid 2p$.
::: {.proof}
Sylow's theorem.
:::
<2>2. The divisors of $2p$ are $1, 2, p, 2p$; among these only $1$ is $\equiv 1 \pmod q$.
::: {.proof}
$q > p > 2$, so $2, p, 2p < q$ and none is $\equiv 1 \pmod q$ (they are all $< q$ and $> 1$).
:::
<2>3. Hence $n_q = 1$, so the Sylow $q$-subgroup $N_2$ is normal.
::: {.proof}
a Sylow subgroup is normal iff it is unique.
:::

<1>2. $G$ has a normal subgroup $N_1$ of order $pq$.
<2>1. $G/N_2$ has order $2p$.
::: {.proof}
$|G/N_2| = 2pq/q = 2p$.
:::
<2>2. $G/N_2$ has a normal subgroup of order $p$.
::: {.proof}
by Sylow, the number of Sylow $p$-subgroups of $G/N_2$ divides $2$ and is $\equiv 1 \pmod p$; since $p > 2$, the only such divisor is $1$, so the Sylow $p$-subgroup is normal.
:::
<2>3. Its preimage $N_1$ in $G$ is normal of order $pq$.
::: {.proof}
the preimage of a normal subgroup under the quotient map is normal, and $|N_1| = p \cdot q = pq$.
:::
<2>4. $N_2 \subseteq N_1$.
::: {.proof}
$N_1$ is the preimage of a subgroup of $G/N_2$, so it contains the kernel $N_2$.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 gives $N_2$; <1>2 gives $N_1$ with $N_2 \subseteq N_1$.
:::
:::
