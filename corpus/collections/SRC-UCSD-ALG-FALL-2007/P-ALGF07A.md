---
schema: qual/card@1
id: P-ALGF07A
kind: problem
title: "Sylow subgroups of a group of order 240 and elements of order 15"
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
Let $G$ be a group of order $240 = 2^4 \cdot 3 \cdot 5$.

(a) How many $p$-Sylow subgroups might $G$ have, for $p = 2, 3, 5$?

(b) If $G$ has a subgroup of order 15, show that it has an element of order 15.
:::

::: {.solution}
**Part (a).**

<1>1. $n_2 \equiv 1 \pmod 2$ and $n_2 \mid 15$, so $n_2 \in \{1, 3, 5, 15\}$.
::: {.proof}
Sylow's third theorem; the odd divisors of $15$ are $1, 3, 5, 15$.
:::

<1>2. $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 80$, so $n_3 \in \{1, 4, 10, 16, 40\}$.
::: {.proof}
the divisors of $80 = 2^4 \cdot 5$ that are $\equiv 1 \pmod 3$ are $1, 4, 10, 16, 40$.
:::

<1>3. $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 48$, so $n_5 \in \{1, 6, 16\}$.
::: {.proof}
the divisors of $48 = 2^4 \cdot 3$ that are $\equiv 1 \pmod 5$ are $1, 6, 16$.
:::

**Part (b).**

<1>1. Let $H \le G$ be a subgroup of order $15 = 3 \cdot 5$.
::: {.proof}
hypothesis.
:::

<1>2. $H$ has a normal Sylow $5$-subgroup.
::: {.proof}
$n_5(H) \equiv 1 \pmod 5$ and $n_5(H) \mid 3$, so $n_5(H) = 1$.
:::

<1>3. $H$ has a normal Sylow $3$-subgroup.
::: {.proof}
$n_3(H) \equiv 1 \pmod 3$ and $n_3(H) \mid 5$, so $n_3(H) = 1$.
:::

<1>4. Hence $H \cong \ZZ/3 \times \ZZ/5 \cong \ZZ/15$.
::: {.proof}
both Sylow subgroups are normal and intersect trivially, so $H$ is their direct product, which is cyclic of order $15$.
:::

<1>5. Therefore $H$ (and hence $G$) has an element of order $15$.
::: {.proof}
a cyclic group of order $15$ has a generator of order $15$.
:::

<1>6. Q.E.D.
::: {.proof}
<1>3 (a) and <1>5 (b).
:::
:::
