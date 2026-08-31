---
schema: qual/card@1
id: P-HFGO24
kind: problem
title: Galois group of x to the eighth minus one
classification:
  areas: [algebra]
  topics: [Galois Theory]
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Determine the Galois group of $x^8-1$ over $\mathbb Q$.
:::

::: {.solution}
<1>1. Roots of $x^8-1$ are $8$th roots of unity $\zeta_8^k$, $k=0..7$.
::: {.proof}
$x^8=1$.
:::

<1>2. Splitting field is $\Q(\zeta_8)=\Q(i,\sqrt2)$.
::: {.proof}
$\zeta_8=(1+i)/\sqrt2$.
:::

<1>3. $[\Q(\zeta_8):\Q]=\varphi(8)=4$.
::: {.proof}
$m=8$ even >2.
:::

<1>4. $\Gal(\Q(\zeta_8)/\Q)\cong(\Z/8)^\times=\{1,3,5,7\}\cong C_2\times C_2$.
::: {.proof}
cyclotomic.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.
:::
:::
