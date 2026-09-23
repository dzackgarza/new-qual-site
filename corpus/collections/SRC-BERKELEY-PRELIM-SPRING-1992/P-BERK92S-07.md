---
schema: qual/card@1
id: P-BERK92S-07
kind: problem
title: Ten integers between one and twenty-five are multiplicatively dependent
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $a_1,\dots,a_{10}$ be integers with
\[
1\le a_i\le25.
\]
Prove that there are integers $n_1,\dots,n_{10}$, not all zero, such that
\[
\prod_{i=1}^{10}a_i^{n_i}=1.
\]
:::

::: {.solution}
Let
$$
p_1,\ldots,p_9=2,3,5,7,11,13,17,19,23
$$
be the primes at most $25$.

<1>1. Each $a_i$ determines a vector $v_i\in\ZZ^9$ such that
$$
a_i=\prod_{j=1}^9p_j^{(v_i)_j}.
$$

::: {.proof}
Every prime divisor of an integer between $1$ and $25$ is one of the
nine displayed primes. The fundamental theorem of arithmetic therefore
gives a unique exponent vector
$$
v_i=
(\nu_{p_1}(a_i),\ldots,\nu_{p_9}(a_i))\in\ZZ_{\ge0}^9
$$
with the stated factorization.
:::

<1>2. There are integers $n_1,\ldots,n_{10}$, not all zero, such that
$$
\sum_{i=1}^{10}n_iv_i=0.
$$

::: {.proof}
The ten vectors $v_1,\ldots,v_{10}$ lie in the nine-dimensional
$\QQ$-vector space $\QQ^9$, so they are linearly dependent over
$\QQ$. Thus there are rational numbers $q_i$, not all zero, with
$$
\sum_{i=1}^{10}q_iv_i=0.
$$
Multiplying by a common positive denominator of the $q_i$ produces
integers $n_i$, not all zero, satisfying the claimed relation.
:::

<1>3. $\prod_{i=1}^{10}a_i^{n_i}=\boxed{1}$.

::: {.proof}
Using step <1>1 and collecting the exponent of each prime,
$$
\prod_{i=1}^{10}a_i^{n_i}
=
\prod_{j=1}^9
p_j^{\sum_{i=1}^{10}n_i(v_i)_j}.
$$
Every exponent on the right is zero by step <1>2, so the product is
$1$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give the required nonzero integer relation.
:::
:::
