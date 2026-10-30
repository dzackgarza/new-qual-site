---
schema: qual/card@1
id: P-UCLAB14S-07
kind: problem
title: Absolutely convergent rows and columns without absolute double summability
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2014.
---

::: {.problem}
Find a doubly infinite sequence $\{a_{n,m}:n,m\in\ZZ\}$ such that for every $m$,
$$
\sum_n a_{n,m}=0,
$$
and for every $n$,
$$
\sum_m a_{n,m}=0,
$$
with all these series converging absolutely, but such that
$$
\sum_n\sum_m \abs{a_{n,m}}=\infty.
$$
:::

::: {.solution}

Use disjoint $2\times2$ blocks whose four entries sum to zero in each row and column, with block masses forming a divergent series.

::: pf

::: {.pf-step #s1-1}

For each integer $k\geq1$, set
$$
c_k=\frac1k
$$
and define four entries by
$$
a_{2k,2k}=c_k,
\qquad
a_{2k,2k+1}=-c_k,
$$
$$
a_{2k+1,2k}=-c_k,
\qquad
a_{2k+1,2k+1}=c_k.
$$
Set
$$
a_{n,m}=0
$$
for every other pair $(n,m)\in\ZZ^2$.


::: pf-proof

This explicitly defines a doubly infinite array. The nonzero entries occur in pairwise disjoint $2\times2$ blocks indexed by $k\geq1$.

:::

:::

::: {.pf-step #s1-2}

Every fixed row has at most two nonzero entries.


::: pf-proof

If $n=2k$ for some $k\geq1$, the only nonzero entries in row $n$ are
$$
a_{2k,2k}=c_k,
\qquad
a_{2k,2k+1}=-c_k.
$$
If $n=2k+1$, the only nonzero entries are
$$
a_{2k+1,2k}=-c_k,
\qquad
a_{2k+1,2k+1}=c_k.
$$
All remaining rows are zero.

:::

:::

::: {.pf-step #s1-3}

Consequently, for every $n\in\ZZ$,
$$
\sum_m a_{n,m}=0,
$$
and this series converges absolutely.


::: pf-proof

By step [](#s1-2){.pf-ref}, a nonzero row consists of either $(c_k,-c_k)$ or $(-c_k,c_k)$, so its sum is zero and its absolute sum is $2c_k<\infty$. A zero row has both sums zero.

:::

:::

::: {.pf-step #s1-4}

Every fixed column likewise has at most two nonzero entries, of opposite signs and equal magnitude.


::: pf-proof

For column $m=2k$, the only nonzero entries are
$$
a_{2k,2k}=c_k,
\qquad
a_{2k+1,2k}=-c_k.
$$
For column $m=2k+1$, they are
$$
a_{2k,2k+1}=-c_k,
\qquad
a_{2k+1,2k+1}=c_k.
$$
Every other column is zero.

:::

:::

::: {.pf-step #s1-5}

Therefore, for every $m\in\ZZ$,
$$
\sum_n a_{n,m}=0,
$$
and this series converges absolutely.


::: pf-proof

The two possible nonzero terms described in step [](#s1-4){.pf-ref} cancel, and their absolute sum is $2c_k<\infty$.

:::

:::

::: {.pf-step #s1-6}

The total absolute mass of the $k$th block is
$$
4c_k=\frac4k.
$$


::: pf-proof

The block has four entries, each of absolute value $c_k=1/k$.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\sum_n\sum_m\abs{a_{n,m}}
=\sum_{k=1}^{\infty}\frac4k
=\infty.
$$


::: pf-proof

The blocks are disjoint, so the iterated absolute sum is the sum of their absolute masses from step [](#s1-6){.pf-ref}. The harmonic series diverges.

:::

:::

::: {.pf-step #s1-8}

Thus the array in step [](#s1-1){.pf-ref} satisfies all the required properties.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-5){.pf-ref} give absolutely convergent row and column sums equal to zero, while step [](#s1-7){.pf-ref} gives divergent total absolute sum.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} verifies the construction completely.

:::

:::

:::
