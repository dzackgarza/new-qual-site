---
schema: qual/card@1
id: P-PGDJ2
kind: problem
title: "Zeros of a polynomial in the annulus from one to three"
classification:
  areas:
  - real-analysis
  topics:
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
1. How many zeros does the polynomial

$$
z^9 + z^6 + 30 z^5 - 3z + 2
$$

have in the annulus $\{ 1 \leq | z | \leq 3 \}$ . Justify your answer.
:::

::: {.solution}
Let $P(z)=z^9+z^6+30z^5-3z+2$, and count zeros with multiplicity.

<1>1. $P$ has $9$ zeros in $\abs z<3$ and none on $\abs z=3$.

::: {.proof}
On $\abs z=3$, $\abs{z^9}=3^9=19683$, while $\abs{z^6+30z^5-3z+2}\le 3^6+30\cdot3^5+3\cdot3+2=8030$. By Rouché's theorem $P$ has as many zeros in $\abs z<3$ as $z^9$, namely $9$, and $\abs P\ge19683-8030>0$ on the circle.
:::

<1>2. $P$ has $5$ zeros in $\abs z<1$ and none on $\abs z=1$.

::: {.proof}
On $\abs z=1$, $\abs{30z^5}=30$, while $\abs{z^9+z^6-3z+2}\le1+1+3+2=7$. By Rouché's theorem $P$ has as many zeros in $\abs z<1$ as $30z^5$, namely $5$, and $\abs P\ge30-7>0$ on the circle.
:::

<1>3. Q.E.D.

::: {.proof}
By steps <1>1 and <1>2, the annulus $1\le\abs z\le3$ contains $9-5=\boxed{4}$ zeros.
:::
:::
