---
schema: qual/card@1
id: P-KSRING17-101
kind: problem
title: Irreducibility of $x^4+5x^2+3x+2$ over $\mathbb Q$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 101 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that the polynomial $f ( x ) = x ^ { 4 } + 5 x ^ { 2 } + 3 x + 2$ is irreducible over the field of rational numbers.
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

<1>1. The polynomial $f$ is primitive.

::: {.proof}
The coefficients are
$$
1,0,5,3,2.
$$
Their greatest common divisor is $1$ because the leading coefficient is $1$.
Thus $f$ is primitive.
:::

<1>2. Reduce $f$ modulo $3$:
$$
\overline f(x)
=
x^4+2x^2+2
\in
\FF_3[x].
$$

::: {.proof}
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

<1>3. The polynomial $\overline f$ has no root in $\FF_3$.

::: {.proof}
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

<1>4. If $\overline f$ is reducible in $\FF_3[x]$, then it factors as a product of two monic quadratics.

::: {.proof}
The polynomial $\overline f$ has degree $4$ and no linear factor by step <1>3.
A nontrivial factorization over a field must therefore have factor degrees
$$
2
\qquad\text{and}\qquad
2.
$$
Since $\overline f$ is monic, the two quadratic factors may be taken monic.
:::

<1>5. Suppose
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

::: {.proof}
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

<1>6. The condition
$$
bd=2
$$
forces
$$
\{b,d\}=\{1,2\}.
$$

::: {.proof}
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

<1>7. In either case,
$$
b+d=0
$$
in $\FF_3$.
Hence
$$
ac=2.
$$

::: {.proof}
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
from step <1>5 therefore becomes
$$
ac=2.
$$
:::

<1>8. Since
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

::: {.proof}
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

<1>9. The coefficient of $x$ cannot vanish.

::: {.proof}
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
By step <1>6,
$$
b\ne d,
$$
so
$$
d-b\ne0.
$$
By step <1>8,
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

<1>10. Therefore $\overline f$ is irreducible in $\FF_3[x]$.

::: {.proof}
Step <1>3 rules out linear factors, and steps <1>4--<1>9 rule out a factorization into two quadratics.
These are all possible nontrivial factorizations of a quartic over a field.
Hence
$$
\overline f
$$
is irreducible.
:::

<1>11. The polynomial $f$ is irreducible in $\QQ[x]$.

::: {.proof}
The polynomial $f$ is primitive by step <1>1.
If it were reducible in $\QQ[x]$, Gauss's lemma would make it reducible in $\ZZ[x]$.
Reducing a primitive factorization modulo $3$ would then give a nontrivial factorization of
$$
\overline f
\in
\FF_3[x],
$$
contradicting step <1>10.
Therefore
$$
\boxed{
x^4+5x^2+3x+2
\text{ is irreducible over }\QQ.
}
$$
:::

<1>12. Q.E.D.

::: {.proof}
Step <1>11 is the required conclusion.
:::
:::
