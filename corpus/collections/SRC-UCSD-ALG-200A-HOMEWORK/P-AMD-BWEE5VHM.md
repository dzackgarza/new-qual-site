---
schema: qual/card@1
id: P-AMD-BWEE5VHM
kind: problem
title: A group of squarefree order $pqr$ has a normal Sylow subgroup
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Given: $|G| = pqr, p < q < r$

Show: $\exists P_i \in \text{Syl}_i(G) \normal G$
:::

::: {.solution}
<1>1. $|G| = pqr$ with $p < q < r$ primes.
::: {.proof}
hypothesis.
:::

<1>2. $n_r \equiv 1 \pmod r$ and $n_r \mid pq$, so $n_r \in \{1, pq\}$.
::: {.proof}
Sylow's third theorem; the divisors of $pq$ are $1, p, q, pq$, and since $p, q < r$, neither $p$ nor $q$ is $\equiv 1 \pmod r$.
:::

<1>3. If $n_r = 1$, then the Sylow $r$-subgroup is normal, and we are done.
::: {.proof}
a Sylow subgroup is normal iff it is unique.
:::

<1>4. Suppose $n_r = pq$; we show the Sylow $q$-subgroup is normal.
<2>1. Then $pq \equiv 1 \pmod r$, so $pq \ge r + 1$.
::: {.proof}
$pq = 1 + kr$ for some $k \ge 1$.
:::
<2>2. The number of elements of order $r$ is $pq(r-1)$.
::: {.proof}
$pq$ Sylow $r$-subgroups, each with $r-1$ non-identity elements, pairwise disjoint.
:::
<2>3. Hence the number of elements not of order $r$ is $pqr - pq(r-1) = pq$.
::: {.proof}
<2>2. <2>4. $n_q \equiv 1 \pmod q$ and $n_q \mid pr$, so $n_q \in \{1, r, pr\}$ (since $p < q$ rules out $p$).
::: {.proof}
Sylow's third theorem.
:::
:::
<2>5. If $n_q \neq 1$, then $n_q \ge r \ge q + 1$, so the number of elements of order $q$ is at least $r(q-1) \ge (q+1)(q-1) = q^2 - 1$.
::: {.proof}
$n_q \ge r$ Sylow $q$-subgroups, each with $q-1$ non-identity elements.
:::
<2>6. But $q^2 - 1 > pq$ (since $q^2 - pq - 1 = q(q-p) - 1 \ge q - 1 > 0$, as $q - p \ge 1$ and $q \ge 3$).
::: {.proof}
$q > p \ge 2$, so $q - p \ge 1$ and $q(q-p) \ge q \ge 3 > 1$.
:::
<2>7. This contradicts <2>3 (there are only $pq$ elements not of order $r$, but $q^2 - 1 > pq$ elements of order $q$).
::: {.proof}
<2>5 and <2>6. <2>8. Hence $n_q = 1$, so the Sylow $q$-subgroup is normal.
:::
::: {.proof}
<2>7.
:::

<1>5. Therefore $G$ has a normal Sylow subgroup (either the Sylow $r$-subgroup or the Sylow $q$-subgroup).
::: {.proof}
<1>3 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>5.
:::
:::
