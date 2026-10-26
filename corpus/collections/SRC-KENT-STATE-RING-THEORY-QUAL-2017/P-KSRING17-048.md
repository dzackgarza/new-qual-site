---
schema: qual/card@1
id: P-KSRING17-048
kind: problem
title: Values of $a$ making $\mathbb Z_5[x]/(x^3+2x^2+ax+3)$ a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 48 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Find all values of a in $\mathbb { Z } _ { 5 }$ such that the quotient ring

$$
\mathbb { Z } _ { 5 } [ x ] / ( x ^ { 3 } + 2 x ^ { 2 } + a x + 3 )
$$

is a field.
Justify your answer.
:::

For
$$
a\in\FF_5,
$$
set
$$
f_a(x)
\coloneqq
x^3+2x^2+ax+3.
$$

::: pf

::: pf-step

The quotient
$$
\FF_5[x]/(f_a)
$$
is a field if and only if
$$
f_a
$$
is irreducible in
$$
\FF_5[x].
$$


::: pf-proof

Since
$$
\FF_5[x]
$$
is a PID, the principal ideal
$$
(f_a)
$$
is maximal exactly when $f_a$ is irreducible. The quotient by $(f_a)$ is a field exactly when $(f_a)$ is maximal.

:::

:::

::: pf-step

Because $f_a$ has degree $3$, it is irreducible if and only if it has no root in $\FF_5$.


::: pf-proof

If a cubic over a field is reducible, one factor in a nontrivial factorization has degree $1$, giving a root. Conversely, a root yields a linear factor by the factor theorem.

:::

:::

::: pf-step

The values of $f_a$ at the five elements of $\FF_5$ are
$$
\begin{aligned}
f_a(0)&=3,\\
f_a(1)&=1+a,\\
f_a(2)&=4+2a,\\
f_a(3)&=3+3a,\\
f_a(4)&=4+4a.
\end{aligned}
$$


::: pf-proof

These follow by direct substitution and reduction modulo $5$:
$$
\begin{aligned}
f_a(1)
&=
1+2+a+3
\equiv
1+a,\\
f_a(2)
&=
8+8+2a+3
=
19+2a
\equiv
4+2a,\\
f_a(3)
&=
27+18+3a+3
=
48+3a
\equiv
3+3a,\\
f_a(4)
&=
64+32+4a+3
=
99+4a
\equiv
4+4a.
\end{aligned}
$$

:::

:::

::: pf-step

If
$$
a=3,
$$
then $f_a$ is reducible.


::: pf-proof

By step <1>3,
$$
f_3(2)
=
4+2\cdot3
=
10
\equiv
0
\pmod5.
$$
Thus $2$ is a root.

:::

:::

::: pf-step

If
$$
a=4,
$$
then $f_a$ is reducible.


::: pf-proof

By step <1>3,
$$
f_4(1)
=
1+4
=
0
$$
in $\FF_5$. Thus $1$ is a root.

:::

:::

::: pf-step

If
$$
a\in\{0,1,2\},
$$
then $f_a$ has no root in $\FF_5$.


::: pf-proof

Use step <1>3.

For
$$
a=0,
$$
the five values are
$$
3,1,4,3,4,
$$
all nonzero.

For
$$
a=1,
$$
the five values are
$$
3,2,1,1,3,
$$
all nonzero.

For
$$
a=2,
$$
the five values are
$$
3,3,3,4,2,
$$
all nonzero.
Thus none of these three polynomials has a root in $\FF_5$.

:::

:::

::: pf-step

Therefore the quotient is a field exactly for
$$
\boxed{
a\in\{0,1,2\}.
}
$$


::: pf-proof

Steps <1>4--<1>5 exclude
$$
a=3,4.
$$
Step <1>6 and step <1>2 show that $f_a$ is irreducible for
$$
a=0,1,2.
$$
Step <1>1 then gives the corresponding field quotients.

:::

:::

::: pf-qed

Step <1>7 gives the complete list.

:::

:::
