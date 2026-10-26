---
schema: qual/card@1
id: P-KSRING17-047
kind: problem
title: Values of $a$ making $\mathbb Z_3[x]/(x^3+x^2+ax+1)$ a field
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 47 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Find all values of a in $\mathbb { Z } _ { 3 }$ such that the quotient ring

$$
\mathbb { Z } _ { 3 } [ x ] / ( x ^ { 3 } + x ^ { 2 } + a x + 1 )
$$

is a field.
Justify your answer.
:::

For
$$
a\in\FF_3,
$$
set
$$
f_a(x)
\coloneqq
x^3+x^2+ax+1.
$$

::: pf

::: pf-step

The quotient
$$
\FF_3[x]/(f_a)
$$
is a field if and only if
$$
f_a
$$
is irreducible in
$$
\FF_3[x].
$$


::: pf-proof

The ring
$$
\FF_3[x]
$$
is a principal ideal domain. In a PID, the quotient by a nonzero principal ideal
$$
(f_a)
$$
is a field if and only if
$$
(f_a)
$$
is maximal, which is equivalent to $f_a$ being irreducible.

:::

:::

::: pf-step

Since $f_a$ has degree $3$, it is irreducible if and only if it has no root in $\FF_3$.


::: pf-proof

If a cubic is reducible over a field, one factor in a nontrivial factorization must have degree $1$, hence gives a root.
Conversely, a root gives a linear factor by the factor theorem.

:::

:::

::: pf-step

One has
$$
f_a(0)=1.
$$


::: pf-proof

Substitution gives
$$
f_a(0)
=
0+0+0+1
=
1.
$$
Thus $0$ is never a root.

:::

:::

::: pf-step

One has
$$
f_a(1)=a
$$
in $\FF_3$.


::: pf-proof

Compute
$$
\begin{aligned}
f_a(1)
&=
1+1+a+1\\
&=
3+a\\
&=
a
\end{aligned}
$$
in characteristic $3$.

:::

:::

::: pf-step

One has
$$
f_a(2)=1+2a
$$
in $\FF_3$.


::: pf-proof

Compute modulo $3$:
$$
\begin{aligned}
f_a(2)
&=
2^3+2^2+2a+1\\
&=
8+4+2a+1\\
&=
13+2a\\
&\equiv
1+2a
\pmod3.
\end{aligned}
$$

:::

:::

::: pf-step

For
$$
a=0,
$$
the polynomial $f_a$ is reducible.


::: pf-proof

By step <1>4,
$$
f_0(1)=0.
$$
Thus $1$ is a root, so $f_0$ is reducible by step <1>2.

:::

:::

::: pf-step

For
$$
a=1,
$$
the polynomial $f_a$ is reducible.


::: pf-proof

By step <1>5,
$$
f_1(2)
=
1+2
=
0
$$
in $\FF_3$.
Thus $2$ is a root, so $f_1$ is reducible.

:::

:::

::: pf-step

For
$$
a=2,
$$
the polynomial $f_a$ has no root in $\FF_3$.


::: pf-proof

By steps <1>3--<1>5,
$$
f_2(0)=1,
$$
$$
f_2(1)=2,
$$
and
$$
f_2(2)
=
1+4
=
5
\equiv
2
\pmod3.
$$
None of these values is zero.

:::

:::

::: pf-step

Therefore
$$
\boxed{a=2}
$$
is the unique value for which
$$
\FF_3[x]/(x^3+x^2+ax+1)
$$
is a field.


::: pf-proof

Steps <1>6--<1>7 exclude $a=0,1$. Step <1>8 and step <1>2 show that $f_2$ is irreducible, and step <1>1 then implies the corresponding quotient is a field.

:::

:::

::: pf-qed

Step <1>9 gives the complete list.

:::

:::
