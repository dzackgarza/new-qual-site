---
schema: qual/card@1
id: P-BKF83-6
kind: problem
title: Count zeros of $z^5+z^3+5z^2+2$ in $1<|z|<2$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked both strict Rouche inequalities, the corresponding disk zero counts, and subtraction across the annulus.
---

::: {.problem}
How many zeros, counted with multiplicity, does
\[
p(z)=z^5+z^3+5z^2+2
\]
have in the annulus
\[
1<|z|<2?
\]
:::

::: {.solution}
<1>1. The polynomial $p$ has exactly five zeros in
$$
\abs{z}<2,
$$
counted with multiplicity.

::: {.proof}
On the circle $\abs{z}=2$,
$$
\abs{z^5}=32,
$$
while
$$
\abs{z^3+5z^2+2}
\le
8+20+2
=30.
$$
Thus
$$
\abs{z^3+5z^2+2}<\abs{z^5}
$$
on the whole circle. By Rouché's theorem, $p$ and $z^5$ have the same
number of zeros in $\abs{z}<2$. Hence $p$ has five there.
:::

<1>2. The polynomial $p$ has exactly two zeros in
$$
\abs{z}<1,
$$
counted with multiplicity.

::: {.proof}
On the circle $\abs{z}=1$,
$$
\abs{5z^2}=5,
$$
while
$$
\abs{z^5+z^3+2}
\le
1+1+2
=4.
$$
Therefore
$$
\abs{z^5+z^3+2}<\abs{5z^2}
$$
on the whole circle. Rouché's theorem shows that $p$ and $5z^2$ have the
same number of zeros in $\abs{z}<1$, namely two.
:::

<1>3. The annulus
$$
1<\abs{z}<2
$$
contains exactly
$$
\boxed{3}
$$
zeros of $p$, counted with multiplicity.

::: {.proof}
The strict inequalities in steps <1>1 and <1>2 also show that $p$ has no
zeros on either boundary circle. Thus the zeros in $\abs{z}<2$ split into
those in $\abs{z}<1$ and those in the annulus. Their multiplicities give
$$
5-2=3.
$$
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the requested count.
:::
:::
