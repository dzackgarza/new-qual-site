---
schema: qual/card@1
id: P-BKS84-7
kind: problem
title: Count roots of $z^7-4z^3-11$ in the annulus $1<|z|<2$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Checked the two Rouché comparisons on the unit circle and the circle of radius two.
---

::: {.problem}
Find the number of roots of
\[
z^7-4z^3-11=0
\]
that lie between the circles
\[
|z|=1
\qquad\text{and}\qquad
|z|=2.
\]
:::

::: {.solution}
Let
$$
p(z)=z^7-4z^3-11.
$$

<1>1. The polynomial $p$ has no zero in the closed unit disk.

::: {.proof}
On $\abs z=1$,
$$
\abs{z^7-4z^3}
\leq
\abs{z}^7+4\abs{z}^3
=
5
<
11
=
\abs{-11}.
$$
By Rouché's theorem, $p(z)=-11+(z^7-4z^3)$ and the constant function
$-11$ have the same number of zeros in $\abs z<1$, namely none.
The strict inequality also shows that $p$ has no zero on $\abs z=1$.
:::

<1>2. The polynomial $p$ has seven zeros in the disk $\abs z<2$,
counted with multiplicity.

::: {.proof}
On $\abs z=2$,
$$
\abs{-4z^3-11}
\leq
4\abs z^3+11
=
43
<
128
=
\abs{z^7}.
$$
By Rouché's theorem, $p(z)=z^7+(-4z^3-11)$ and $z^7$ have the same
number of zeros in $\abs z<2$. Thus $p$ has seven zeros there, counted
with multiplicity. Again, the strict inequality excludes zeros on
$\abs z=2$.
:::

<1>3. The number of roots in
$$
1<\abs z<2
$$
is
$$
\boxed{7},
$$
counted with multiplicity.

::: {.proof}
Step <1>2 counts seven zeros inside the outer circle, while step <1>1
counts zero zeros on or inside the inner circle. Therefore all seven zeros
inside $\abs z<2$ lie in the stated annulus.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested root count.
:::
:::
