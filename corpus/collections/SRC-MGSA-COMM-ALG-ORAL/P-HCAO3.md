---
schema: qual/card@1
id: P-HCAO3
kind: problem
title: Prime ideals need not be maximal
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Maximal Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found. Two valid examples: (0) in Z is prime because Z is a domain and is not
    maximal because Z is not a field; (x) in k[x,y] is prime because the quotient is k[y], a domain,
    and not maximal because k[y] is not a field, with (x) contained properly in (x,y). Checked that
    both rings carry an identity, which the question requires, and that each non-maximality is
    exhibited by a strictly intermediate ideal and not only by the failure of a field quotient. Not
    checked: the oral examination itself, which is not a printed source in the checkout.
---

::: {.problem}
Give an example of a commutative ring with identity that has a prime ideal which is not maximal.
:::

::: {.solution}

::: pf

::: pf-step
In $\ZZ$, the zero ideal is prime and not maximal.

::: pf-proof
The quotient $\ZZ/\langle0\rangle\cong\ZZ$ is an integral domain, because the
product of two nonzero integers is nonzero, so $\langle0\rangle$ is prime. The
chain $\langle0\rangle\subsetneq\langle2\rangle\subsetneq\ZZ$ shows that
$\langle0\rangle$ is not maximal; equivalently, $2$ is not invertible in the
quotient $\ZZ$, which is therefore not a field.
:::

:::

::: pf-step
For a field $k$, the ideal $\langle x\rangle\subseteq k[x,y]$ is prime
and not maximal.

::: pf-proof
The quotient $k[x,y]/\langle x\rangle\cong k[y]$ is an integral domain, so
$\langle x\rangle$ is prime. In $k[y]$ the nonzero element $y$ is not a unit,
so $k[y]$ is not a field. Equivalently,
$$
\langle x\rangle\subsetneq\langle x,y\rangle\subsetneq k[x,y],
$$
where $\langle x,y\rangle$ is maximal because
$k[x,y]/\langle x,y\rangle\cong k$.
:::

:::

:::
:::
