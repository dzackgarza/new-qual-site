---
schema: qual/card@1
id: P-YZBES
kind: problem
title: Zeros of $z^4-6z+3$ in the unit disk and an annulus
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the polynomial, both regions and multiplicity convention with May 2013 problem 2 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both strict boundary inequalities and exclusion of unit-circle zeros before subtracting the disk counts."
---

::: {.problem}
Prove that there is only one solution in the unit disc $\{z : |z| < 1\}$ and there are three solutions on the annulus $\{z : 1 < |z| < 2\}$ (counting multiplicities) for the equation $z^4 - 6z + 3 = 0$.
:::

::: {.solution}
Put $p(z)=z^4-6z+3$.

<1>1. There is exactly one zero in $|z|<1$, counted with multiplicity.

::: {.proof}
On $|z|=1$,
$$
|z^4+3|\leq1+3=4<6=|-6z|.
$$
Both $p$ and $-6z$ are holomorphic on a neighborhood of
the closed disk. Rouché's theorem therefore gives the same
number of interior zeros, counted with multiplicity, for
these two functions [@SS03]. The polynomial $-6z$ has
exactly one simple zero. Thus the count for $p$ is one.
Moreover, $|p(z)|\geq6-4>0$ on $|z|=1$, so this circle
contains no zero of $p$.
:::

<1>2. There are exactly three zeros in $1<|z|<2$, counted with multiplicity.

::: {.proof}
On $|z|=2$,
$$
|-6z+3|\leq12+3=15<16=|z^4|.
$$
Rouché's theorem, now comparing $p$ with $z^4$, gives
four zeros in $|z|<2$, counted with multiplicity [@SS03].
The strict inequality also excludes zeros on $|z|=2$.
Step <1>1 accounts for one of these four zeros in the unit
disk and excludes zeros on the intervening unit circle.
Consequently the open annulus contains exactly $4-1=3$
zeros, counted with multiplicity, as required.
:::
:::
