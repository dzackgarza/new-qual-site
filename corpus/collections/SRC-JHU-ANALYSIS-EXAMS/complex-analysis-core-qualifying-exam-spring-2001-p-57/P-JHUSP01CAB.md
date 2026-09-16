---
schema: qual/card@1
id: P-JHUSP01CAB
kind: problem
title: Zeros of $2z^5+8z-1$ in $1<|z|<2$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the polynomial and open annulus with both recorded appearances: the undated six-question exam and Spring 2001 Complex Analysis question 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Used strict Rouche estimates on both boundary circles, excluded boundary zeros, and subtracted the multiplicity counts."
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Verified the two disk counts and proved that the polynomial and its derivative have no common zero, so the answer also counts distinct roots."
---

::: {.problem}
Question 2. Find the number of zeros of the function $f ( z ) = 2 z ^ { 5 } + 8 z - 1$ in the annulus $1 < | z | < 2$
:::

::: solution
There are exactly $\boxed{4}$ zeros in the annulus, and all are simple.

<1>1. There is exactly one zero in $|z|<1$.
::: proof
Let
$$
p(z)=2z^5+8z-1.
$$
On $|z|=1$,
$$
|2z^5-1|\le 3<8=|8z|.
$$
Rouché's theorem [@SS03] therefore gives the same number of zeros in the unit disk for
$p$ and $8z$, namely one, counted with multiplicity. The strict inequality also
shows that $p$ has no zero on $|z|=1$.
:::

<1>2. There are exactly five zeros in $|z|<2$.
::: proof
On $|z|=2$,
$$
|8z-1|\le17<64=|2z^5|.
$$
A second application of Rouché's theorem gives the same number of zeros in
$|z|<2$ for $p$ and $2z^5$, namely five, counted with multiplicity. Again the
strict inequality excludes zeros from the boundary circle.
:::

<1>3. Subtracting the two disk counts gives the annular count.
::: proof
Because neither boundary circle contains a zero, every zero in $|z|<2$ lies
either in $|z|<1$ or in $1<|z|<2$. Hence the annulus contains
$$
5-1=4
$$
zeros, counted with multiplicity.
:::

<1>4. Every root is simple, so there are four distinct annular roots.
::: proof
A multiple root $a$ would satisfy $p(a)=p'(a)=0$.
The derivative equation $10a^4+8=0$ gives $a^4=-4/5$.
Substitution in the polynomial equation gives
$$
0=2a\left(-\frac45\right)+8a-1
=\frac{32}{5}a-1,
$$
so $a=5/32$ is positive real. This contradicts its
negative fourth power. Therefore no multiple root
exists, and the preceding count is also a count of
distinct zeros.
:::
:::
