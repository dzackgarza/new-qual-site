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
---

::: {.problem}
Give an example of a commutative ring with identity that has a prime ideal which is not maximal.
:::

::: {.solution}
<1>1. In $\ZZ$, the zero ideal is prime and not maximal.

::: {.proof}
The quotient $\ZZ/\langle0\rangle\cong\ZZ$ is an integral domain, because the
product of two nonzero integers is nonzero, so $\langle0\rangle$ is prime. The
chain $\langle0\rangle\subsetneq\langle2\rangle\subsetneq\ZZ$ shows that
$\langle0\rangle$ is not maximal; equivalently, $2$ is not invertible in the
quotient $\ZZ$, which is therefore not a field.
:::

<1>2. For a field $k$, the ideal $\langle x\rangle\subseteq k[x,y]$ is prime
and not maximal.

::: {.proof}
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
