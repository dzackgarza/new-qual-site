---
schema: qual/card@1
id: P-KSRING17-108
kind: problem
title: Irreducibility of $x^4+x^3+x^2+x+1$ and reducibility of $x^4+1$ over $\ZZ_3$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 108 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
(a) Show that $x^{4} + x^{3} + x^{2} + x + 1$ is irreducible in $\ZZ_{3}[x]$.

(b) Show that $x^{4} + 1$ is not irreducible in $\ZZ_{3}[x]$.
:::

::: {.solution}

Set
$$
f(x)
\coloneqq
x^4+x^3+x^2+x+1
\in
\FF_3[x].
$$

::: pf

::: {.pf-step #s1-1}

The polynomial $f$ has no root in $\FF_3$.


::: pf-proof

Evaluate at
$$
0,1,2.
$$
One has
$$
f(0)=1.
$$
Also,
$$
f(1)
=
1+1+1+1+1
=
5
\equiv
2
\pmod3.
$$
Finally,
$$
\begin{aligned}
f(2)
&=
2^4+2^3+2^2+2+1\\
&=
16+8+4+2+1\\
&=
31\\
&\equiv
1
\pmod3.
\end{aligned}
$$
Thus $f$ has no root in $\FF_3$.

:::

:::

::: {.pf-step #s1-2}

If $f$ is reducible, then it factors as a product of two monic quadratics.


::: pf-proof

The polynomial $f$ has degree $4$.
By step [](#s1-1){.pf-ref} it has no linear factor.
Hence any nontrivial factorization over the field $\FF_3$ must have factor degrees
$$
2
\qquad\text{and}\qquad
2.
$$
Because $f$ is monic, the two factors may be chosen monic.

:::

:::

::: {.pf-step #s1-3}

Suppose
$$
f(x)
=
(x^2+ax+b)(x^2+cx+d).
$$
Then
$$
a+c=1,
$$
$$
ac+b+d=1,
$$
$$
ad+bc=1,
$$
and
$$
bd=1.
$$


::: pf-proof

Expand:
$$
\begin{aligned}
(x^2+ax+b)(x^2+cx+d)
&=
x^4
+(a+c)x^3\\
&\quad+
(ac+b+d)x^2\\
&\quad+
(ad+bc)x
+bd.
\end{aligned}
$$
Compare coefficients with
$$
x^4+x^3+x^2+x+1.
$$

:::

:::

::: {.pf-step #s1-4}

The equation
$$
bd=1
$$
forces either
$$
(b,d)=(1,1)
$$
or
$$
(b,d)=(2,2).
$$


::: pf-proof

The nonzero elements of $\FF_3$ are $1$ and $2$.
The products equal to $1$ are
$$
1\cdot1=1
$$
and
$$
2\cdot2=4\equiv1.
$$

:::

:::

::: {.pf-step #s1-5}

The case
$$
b=d=1
$$
is impossible.


::: pf-proof

The equations from step [](#s1-3){.pf-ref} become
$$
a+c=1
$$
and
$$
ac+2=1,
$$
so
$$
ac=2.
$$
Thus $a$ and $c$ would be roots of
$$
t^2-t+2.
$$
Its discriminant is
$$
1-8
=
-7
\equiv
2
\pmod3.
$$
But the squares in $\FF_3$ are only
$$
0
\qquad\text{and}\qquad
1.
$$
Hence this quadratic has no roots in $\FF_3$, contradiction.

:::

:::

::: {.pf-step #s1-6}

The case
$$
b=d=2
$$
is impossible.


::: pf-proof

The $x^2$-coefficient equation gives
$$
ac+2+2
=
1,
$$
so
$$
ac=0.
$$
The $x^3$-coefficient equation still gives
$$
a+c=1.
$$
But the $x$-coefficient becomes
$$
ad+bc
=
2a+2c
=
2(a+c)
=
2,
$$
whereas step [](#s1-3){.pf-ref} requires it to equal $1$.
This is a contradiction.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
x^4+x^3+x^2+x+1
\text{ is irreducible in }\FF_3[x].
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} rules out linear factors.
Steps [](#s1-2){.pf-ref} through [](#s1-6){.pf-ref} rule out every possible quadratic-by-quadratic factorization.
Thus no nontrivial factorization exists.

:::

:::

::: {.pf-step #s1-8}

In $\FF_3[x]$,
$$
\boxed{
x^4+1
=
(x^2+x+2)(x^2+2x+2).
}
$$


::: pf-proof

Multiply:
$$
\begin{aligned}
(x^2+x+2)(x^2+2x+2)
&=
x^4
+3x^3
+6x^2
+6x
+4\\
&=
x^4+1
\end{aligned}
$$
in characteristic $3$.
Both factors have positive degree.

:::

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{
x^4+1
\text{ is reducible in }\FF_3[x].
}
$$


::: pf-proof

Step [](#s1-8){.pf-ref} gives a nontrivial factorization.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
