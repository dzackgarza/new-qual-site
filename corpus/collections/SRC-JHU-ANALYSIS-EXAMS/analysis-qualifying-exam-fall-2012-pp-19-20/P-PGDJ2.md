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

1. How many zeros does the polynomial

$$
z^9 + z^6 + 30 z^5 - 3z + 2
$$

have in the annulus $\{ 1 \leq | z | \leq 3 \}$ . Justify your answer.

::: solution
**Goal:** Show the polynomial has $4$ zeros in $1\le|z|\le3$.

<1> Count zeros in $|z|<3$.
    *Proof:*
    <2>1. For $|z|=3$,
        $$
        |z^9| = 19683,\qquad
        |z^6+30z^5-3z+2| \le 3^6 + 30\cdot3^5 + 3 + 2 = 8030 < 19683.
        $$
    <2>2. So $|z^6+30z^5-3z+2|<|z^9|$.
    <2>3. Rouché gives that $p(z)$ and $z^9$ have the same number of zeros in $|z|<3$.
    <2>4. Therefore $N(3)=9$.

<1> Count zeros in $|z|<1$.
    *Proof:*
    <2>1. For $|z|=1$,
        $$
        |30z^5|=30,\qquad
        |z^9+z^6-3z+2| \le 1+1+3+2 = 7 < 30.
        $$
    <2>2. Rouché gives that $p(z)$ and $30z^5$ have the same number of zeros in $|z|<1$.
    <2>3. Therefore $N(1)=5$.

<1> Conclude the annulus count.
    *Proof:*
    <2>1. No zero can lie on $\{|z|=1\}$ or $\{|z|=3\}$ by strict inequalities above.
    <2>2. Hence the number in $1\le|z|\le3$ is
        $$
        N(3)-N(1)=9-5=4.
        $$
    <2>3. Therefore the polynomial has exactly $4$ zeros in $\{1\le|z|\le3\}$.

Authored by **Codex 5.3 Spark Extra High**.
:::
