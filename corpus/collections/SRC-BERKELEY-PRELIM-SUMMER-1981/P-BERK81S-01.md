---
schema: qual/card@1
id: P-BERK81S-01
kind: problem
title: Asymptotics of $2/(1+\sqrt{1-y})$ along $y=1-2\sin^2(2\pi h)$
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Since 1-y(h)=2 sin^2(2 pi h), one has
    sqrt(1-y(h))=sqrt(2)|sin(2 pi h)|. Writing
    a=sqrt(2)|sin(2 pi h)| and using the exact identity
    2/(1+a)=2-2a+2a^2/(1+a), together with
    ||sin u|-|u||<=|sin u-u|<=|u|^3/6, gives the linear
    -4 sqrt(2) pi |h| term and an explicitly O(h^2) remainder.
---

::: {.problem}
Let
\[
y(h)=1-2\sin^2(2\pi h),
\qquad
f(y)=\frac{2}{1+\sqrt{1-y}}.
\]
Justify the asymptotic formula
\[
f(y(h))=2-4\sqrt2\,\pi |h|+O(h^2)
\qquad(h\to0),
\]
with a remainder bounded in absolute value by a constant multiple of $h^2$ near $0$.
:::

::: {.solution}
Set
$$
u=2\pi h
$$
and
$$
a=\sqrt2\,\abs{\sin u}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
\sqrt{1-y(h)}
=
\sqrt2\,\abs{\sin(2\pi h)}
=
a.
$$

::: pf-proof

By definition,
$$
1-y(h)
=
2\sin^2(2\pi h).
$$
Taking the nonnegative square root gives
$$
\sqrt{1-y(h)}
=
\sqrt2\,\sqrt{\sin^2(2\pi h)}
=
\sqrt2\,\abs{\sin(2\pi h)}.
$$

:::

:::

::: {.pf-step #s2}

Hence
$$
f(y(h))
=
\frac{2}{1+a}
=
2-2a+\frac{2a^2}{1+a}.
$$

::: pf-proof

Step [](#s1){.pf-ref} gives the first equality. For the second,
$$
\begin{aligned}
\frac2{1+a}-(2-2a)
&=
\frac{2-2(1-a)(1+a)}{1+a}\\
&=
\frac{2a^2}{1+a}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

For every real $u$,
$$
\abs{
\abs{\sin u}-\abs u
}
\leq
\frac{\abs u^3}{6}.
$$

::: pf-proof

The reverse triangle inequality gives
$$
\abs{
\abs{\sin u}-\abs u
}
\leq
\abs{\sin u-u}.
$$
Taylor's theorem at $0$ gives
$$
\abs{\sin u-u}
\leq
\frac{\abs u^3}{6},
$$
because the third derivative of $\sin$ has absolute value at most $1$.

:::

:::

::: {.pf-step #s4}

One has
$$
-2a
=
-4\sqrt2\,\pi\abs h
+
R_1(h),
$$
where
$$
\abs{R_1(h)}
\leq
\frac{\sqrt2}{3}(2\pi)^3\abs h^3.
$$

::: pf-proof

Since
$$
a=\sqrt2\,\abs{\sin u},
$$
one has
$$
\begin{aligned}
-2a
&=
-2\sqrt2\,\abs u
-2\sqrt2
\left(
\abs{\sin u}-\abs u
\right)\\
&=
-4\sqrt2\,\pi\abs h
+
R_1(h),
\end{aligned}
$$
where
$$
R_1(h)
=
-2\sqrt2
\left(
\abs{\sin u}-\abs u
\right).
$$
Step [](#s3){.pf-ref} gives
$$
\abs{R_1(h)}
\leq
\frac{\sqrt2}{3}\abs u^3
=
\frac{\sqrt2}{3}(2\pi)^3\abs h^3.
$$

:::

:::

::: {.pf-step #s5}

The second remainder term in step [](#s2){.pf-ref} satisfies
$$
0
\leq
\frac{2a^2}{1+a}
\leq
16\pi^2 h^2.
$$

::: pf-proof

Since $a\geq0$,
$$
\frac{2a^2}{1+a}
\leq
2a^2
=
4\sin^2u.
$$
The elementary bound
$$
\abs{\sin u}\leq\abs u
$$
gives
$$
4\sin^2u
\leq
4u^2
=
16\pi^2h^2.
$$

:::

:::

::: {.pf-step #s6}

There is a constant $C>0$ such that for all sufficiently small
$h$,
$$
\abs{
f(y(h))
-
\left(
2-4\sqrt2\,\pi\abs h
\right)
}
\leq
Ch^2.
$$

::: pf-proof

Combining steps [](#s2){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} gives
$$
f(y(h))
-
\left(
2-4\sqrt2\,\pi\abs h
\right)
=
R_1(h)
+
\frac{2a^2}{1+a}.
$$
For $\abs h\leq1$, step [](#s4){.pf-ref} gives
$$
\abs{R_1(h)}
\leq
\frac{\sqrt2}{3}(2\pi)^3h^2,
$$
and step [](#s5){.pf-ref} gives
$$
\frac{2a^2}{1+a}
\leq
16\pi^2h^2.
$$
Thus the desired bound holds with, for example,
$$
C
=
\frac{\sqrt2}{3}(2\pi)^3
+
16\pi^2.
$$

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
f(y(h))
=
2-4\sqrt2\,\pi\abs h
+
O(h^2)
}
$$
as $h\to0$.

::: pf-proof

Step [](#s6){.pf-ref} is exactly the stated $O(h^2)$ estimate, with an explicit
constant bounding the remainder divided by $h^2$ near $0$.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the required asymptotic formula.

:::

:::

:::
