---
schema: qual/card@1
id: P-TRIV-CA05
kind: problem
title: Laurent series of $1/(z-3)^3$ about $z=i$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the Laurent series of $f ( z ) = { \frac { 1 } { ( z - 3 ) ^ { 3 } } }$ around $z _ { 0 } = i ;$ give the region of convergence.
:::

::: {.solution}
Set
$$
w=z-i.
$$
Then
$$
z-3
=
w-(3-i).
$$

<1>1. One has
$$
\frac1{(z-3)^3}
=
-\frac1{(3-i)^3}
\left(
1-\frac{w}{3-i}
\right)^{-3}.
$$

::: {.proof}
Factor
$$
z-3
=
-(3-i)
\left(
1-\frac{w}{3-i}
\right).
$$
Cubing introduces a factor $-1$, and then taking reciprocals gives the
displayed identity.
:::

<1>2. For $|u|<1$,
$$
(1-u)^{-3}
=
\sum_{n=0}^{\infty}
\binom{n+2}{2}u^n.
$$

::: {.proof}
Differentiate the geometric series twice:
$$
\frac1{1-u}
=
\sum_{n=0}^{\infty}u^n.
$$
The standard binomial-series coefficient for exponent $-3$ is
$$
\binom{n+2}{2}.
$$
:::

<1>3. Therefore
$$
\boxed{
\frac1{(z-3)^3}
=
-\sum_{n=0}^{\infty}
\binom{n+2}{2}
\frac{(z-i)^n}{(3-i)^{n+3}}.
}
$$

::: {.proof}
Substitute
$$
u=\frac{w}{3-i}
$$
into step <1>2 and use step <1>1.
:::

<1>4. The series converges when
$$
|z-i|
<
|3-i|
=
\sqrt{10}.
$$

::: {.proof}
The binomial series in step <1>2 requires
$$
\left|
\frac{z-i}{3-i}
\right|
<1.
$$
Since
$$
|3-i|
=
\sqrt{3^2+(-1)^2}
=
\sqrt{10},
$$
this is exactly the stated disk.
:::

<1>5. The radius $\sqrt{10}$ is maximal.

::: {.proof}
The function
$$
\frac1{(z-3)^3}
$$
has its nearest singularity to the center $i$ at $z=3$, whose distance from
$i$ is $\sqrt{10}$. A Taylor series about $i$ cannot converge through that
singularity.
:::

<1>6. Thus the Laurent series about $i$ has region of convergence
$$
\boxed{|z-i|<\sqrt{10}}.
$$

::: {.proof}
The center $z=i$ is not singular, so the Laurent series has no negative-power
terms and is an ordinary Taylor series. Steps <1>4--<1>5 give its exact disk
of convergence.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>3 and <1>6 give the requested series and its region of convergence.
:::
:::
