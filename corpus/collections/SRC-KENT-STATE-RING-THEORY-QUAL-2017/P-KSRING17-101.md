---
schema: qual/card@1
id: P-KSRING17-101
kind: problem
title: Irreducibility of $x^4+5x^2+3x+2$ over $\QQ$
classification:
  areas: [algebra]
  topics:
  - Irreducible Polynomials
  - Reduction Mod p
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 101 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that the polynomial $f(x) = x^{4} + 5x^{2} + 3x + 2$ is irreducible over the field of rational numbers.
:::

::: {.solution}

Set
$$
f(x)
\coloneqq
x^4+5x^2+3x+2
\in
\ZZ[x].
$$

::: pf

::: {.pf-step #s1-1}

The polynomial $f$ is primitive.


::: pf-proof

The coefficients are
$$
1,0,5,3,2.
$$
Their greatest common divisor is $1$ because the leading coefficient is $1$.
Thus $f$ is primitive.

:::

:::

::: pf-step

Reduce $f$ modulo $3$:
$$
\overline f(x)
=
x^4+2x^2+2
\in
\FF_3[x].
$$


::: pf-proof

Modulo $3$,
$$
5\equiv2,
\qquad
3\equiv0,
\qquad
2\equiv2.
$$
Substitution gives the displayed reduction.

:::

:::

::: {.pf-step #s1-3}

The polynomial $\overline f$ has no root in $\FF_3$.


::: pf-proof

Evaluate at the three elements:
$$
\overline f(0)=2.
$$
Also,
$$
\overline f(1)
=
1+2+2
=
5
\equiv
2
\pmod3.
$$
Finally,
$$
\overline f(2)
=
2^4+2\cdot2^2+2
=
16+8+2
=
26
\equiv
2
\pmod3.
$$
Thus none of
$$
0,1,2
$$
is a root.

:::

:::

::: {.pf-step #s1-4}

If $\overline f$ is reducible in $\FF_3[x]$, then it factors as a product of two monic quadratics.


::: pf-proof

The polynomial $\overline f$ has degree $4$ and no linear factor by step [](#s1-3){.pf-ref}.
A nontrivial factorization over a field must therefore have factor degrees
$$
2
\qquad\text{and}\qquad
2.
$$
Since $\overline f$ is monic, the two quadratic factors may be taken monic.

:::

:::

::: {.pf-step #s1-5}

Suppose
$$
\overline f(x)
=
(x^2+ax+b)(x^2+cx+d)
$$
with
$$
a,b,c,d\in\FF_3.
$$
Then
$$
c=-a,
\qquad
bd=2,
$$
and
$$
ac+b+d=2.
$$


::: pf-proof

Expanding,
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
Comparison with
$$
x^4+2x^2+2
$$
gives the displayed equations.

:::

:::

::: {.pf-step #s1-6}

The condition
$$
bd=2
$$
forces
$$
\{b,d\}=\{1,2\}.
$$


::: pf-proof

The nonzero elements of $\FF_3$ are $1$ and $2$.
Their products are
$$
1\cdot1=1,
\qquad
1\cdot2=2,
\qquad
2\cdot2=4\equiv1.
$$
Thus the only ordered pairs with product $2$ are
$$
(b,d)=(1,2)
\quad\text{or}\quad
(2,1).
$$

:::

:::

::: {.pf-step #s1-7}

In either case,
$$
b+d=0
$$
in $\FF_3$.
Hence
$$
ac=2.
$$


::: pf-proof

For
$$
\{b,d\}=\{1,2\},
$$
one has
$$
b+d=3\equiv0.
$$
The relation
$$
ac+b+d=2
$$
from step [](#s1-5){.pf-ref} therefore becomes
$$
ac=2.
$$

:::

:::

::: {.pf-step #s1-8}

Since
$$
c=-a,
$$
the equation
$$
ac=2
$$
forces
$$
a^2=1.
$$


::: pf-proof

Substitute
$$
c=-a
$$
into
$$
ac=2:
$$
$$
-a^2=2.
$$
In $\FF_3$,
$$
-2=1,
$$
so
$$
a^2=1.
$$
Thus
$$
a\ne0.
$$

:::

:::

::: {.pf-step #s1-9}

The coefficient of $x$ cannot vanish.


::: pf-proof

The $x$-coefficient in the hypothetical factorization is
$$
ad+bc.
$$
Using
$$
c=-a,
$$
this becomes
$$
a(d-b).
$$
By step [](#s1-6){.pf-ref},
$$
b\ne d,
$$
so
$$
d-b\ne0.
$$
By step [](#s1-8){.pf-ref},
$$
a\ne0.
$$
Since $\FF_3$ is a field,
$$
a(d-b)\ne0.
$$
But the $x$-coefficient of
$$
\overline f(x)=x^4+2x^2+2
$$
is $0$, a contradiction.

:::

:::

::: {.pf-step #s1-10}

Therefore $\overline f$ is irreducible in $\FF_3[x]$.


::: pf-proof

Step [](#s1-3){.pf-ref} rules out linear factors, and steps [](#s1-4){.pf-ref} through [](#s1-9){.pf-ref} rule out a factorization into two quadratics.
These are all possible nontrivial factorizations of a quartic over a field.
Hence
$$
\overline f
$$
is irreducible.

:::

:::

::: {.pf-step #s1-11}

The polynomial $f$ is irreducible in $\QQ[x]$.


::: pf-proof

The polynomial $f$ is primitive by step [](#s1-1){.pf-ref}.
If it were reducible in $\QQ[x]$, Gauss's lemma would make it reducible in $\ZZ[x]$.
Reducing a primitive factorization modulo $3$ would then give a nontrivial factorization of
$$
\overline f
\in
\FF_3[x],
$$
contradicting step [](#s1-10){.pf-ref}.
Therefore
$$
\boxed{
x^4+5x^2+3x+2
\text{ is irreducible over }\QQ.
}
$$

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the required conclusion.

:::

:::

:::
