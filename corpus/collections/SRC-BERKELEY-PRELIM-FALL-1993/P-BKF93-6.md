---
schema: qual/card@1
id: P-BKF93-6
kind: problem
title: Cancellation for direct products of finite abelian groups
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Applied uniqueness of the elementary-divisor decomposition of finite
    abelian groups and cancelled the cyclic p-power multiplicities contributed
    by A.
---

::: {.problem}
Let $A,B,C$ be finite abelian groups. Prove that if
\[
A\times B\cong A\times C,
\]
then
\[
B\cong C.
\]
:::

::: {.solution}

::: pf

::: pf-step

Write the elementary-divisor decompositions
$$
A\cong\prod_{p,k}(\ZZ/p^k\ZZ)^{a_{p,k}},
\qquad
B\cong\prod_{p,k}(\ZZ/p^k\ZZ)^{b_{p,k}},
\qquad
C\cong\prod_{p,k}(\ZZ/p^k\ZZ)^{c_{p,k}},
$$
where the products range over primes $p$ and integers $k\geq1$, and all but
finitely many multiplicities are zero.

::: pf-proof

This is the elementary-divisor form of the fundamental theorem of finite
abelian groups.

:::

:::

::: {.pf-step #s2}

For every prime $p$ and every $k\geq1$,
$$
a_{p,k}+b_{p,k}
=
a_{p,k}+c_{p,k}.
$$

::: pf-proof

Taking direct products adds the multiplicities of each cyclic factor
$\ZZ/p^k\ZZ$. Hence
$$
A\times B
\cong
\prod_{p,k}(\ZZ/p^k\ZZ)^{a_{p,k}+b_{p,k}},
$$
while
$$
A\times C
\cong
\prod_{p,k}(\ZZ/p^k\ZZ)^{a_{p,k}+c_{p,k}}.
$$
The assumed isomorphism $A\times B\cong A\times C$ and uniqueness of the
elementary-divisor decomposition force the displayed multiplicities to agree.

:::

:::

::: {.pf-step #s3}

For every prime $p$ and every $k\geq1$,
$$
b_{p,k}=c_{p,k}.
$$

::: pf-proof

Cancel $a_{p,k}$ from the equality in step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

One has
$$
B\cong C.
$$

::: pf-proof

By step [](#s3){.pf-ref}, the elementary-divisor decompositions of $B$ and $C$ contain
exactly the same cyclic $p$-power factors with the same multiplicities.
Therefore the fundamental theorem of finite abelian groups gives
$B\cong C$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
