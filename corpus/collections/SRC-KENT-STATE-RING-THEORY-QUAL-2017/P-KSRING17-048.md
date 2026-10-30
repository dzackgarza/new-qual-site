---
schema: qual/card@1
id: P-KSRING17-048
kind: problem
title: Values of $a$ making $\ZZ_5[x]/(x^3+2x^2+ax+3)$ a field
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
Find all values of $a$ in $\ZZ_{5}$ such that the quotient ring
$$
\ZZ_{5}[x]/(x^{3} + 2x^{2} + ax + 3)
$$
is a field. Justify your answer.
:::

::: {.solution}

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

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

Because $f_a$ has degree $3$, it is irreducible if and only if it has no root in $\FF_5$.


::: pf-proof

If a cubic over a field is reducible, one factor in a nontrivial factorization has degree $1$, giving a root. Conversely, a root yields a linear factor by the factor theorem.

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

If
$$
a=3,
$$
then $f_a$ is reducible.


::: pf-proof

By step [](#s1-3){.pf-ref},
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

::: {.pf-step #s1-5}

If
$$
a=4,
$$
then $f_a$ is reducible.


::: pf-proof

By step [](#s1-3){.pf-ref},
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

::: {.pf-step #s1-6}

If
$$
a\in\{0,1,2\},
$$
then $f_a$ has no root in $\FF_5$.


::: pf-proof

Use step [](#s1-3){.pf-ref}.

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

::: {.pf-step #s1-7}

Therefore the quotient is a field exactly for
$$
\boxed{
a\in\{0,1,2\}.
}
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} exclude
$$
a=3,4.
$$
Step [](#s1-6){.pf-ref} and step [](#s1-2){.pf-ref} show that $f_a$ is irreducible for
$$
a=0,1,2.
$$
Step [](#s1-1){.pf-ref} then gives the corresponding field quotients.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} gives the complete list.

:::

:::

:::
