---
schema: qual/card@1
id: P-KSRING17-085
kind: problem
title: '$\mathbb Z[\sqrt{13}]$ is not a UFD: irreducibility of $x^2+3x-1$'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 85 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D = \mathbb { Z } ( { \sqrt { 1 3 } } ) = \{ m + n { \sqrt { 1 3 } } \mid m , n \in \mathbb { Z } \}$ and $F = \mathbb { Q } ( { \sqrt { 1 3 } } )$ its field of fractions.
Show the following:

(a) $x ^ { 2 } + 3 x - 1$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.
:::

Set
$$
f(x)
\coloneqq
x^2+3x-1.
$$

::: pf

::: pf-step

The roots of $f$ in
$$
F=\QQ(\sqrt{13})
$$
are
$$
\alpha
\coloneqq
\frac{-3+\sqrt{13}}2,
\qquad
\beta
\coloneqq
\frac{-3-\sqrt{13}}2.
$$


::: pf-proof

The discriminant of
$$
x^2+3x-1
$$
is
$$
3^2-4(1)(-1)
=
13.
$$
The quadratic formula gives the displayed roots.

:::

:::

::: pf-step

Hence
$$
\boxed{
f(x)
=(x-\alpha)(x-\beta)
}
$$
in
$$
F[x].
$$


::: pf-proof

This is the factorization determined by the two roots from step <1>1.
Thus $f$ is reducible over $F$.

:::

:::

::: pf-step

Neither $\alpha$ nor $\beta$ belongs to
$$
D=\ZZ[\sqrt{13}].
$$


::: pf-proof

Suppose
$$
\alpha
=
m+n\sqrt{13}
$$
with
$$
m,n\in\ZZ.
$$
Then
$$
-\frac32
+
\frac12\sqrt{13}
=
m+n\sqrt{13}.
$$
Since
$$
\sqrt{13}\notin\QQ,
$$
comparison of the coefficients of
$$
1
\qquad\text{and}\qquad
\sqrt{13}
$$
gives
$$
m=-\frac32,
\qquad
n=\frac12,
$$
contradicting
$$
m,n\in\ZZ.
$$
Thus
$$
\alpha\notin D.
$$

The same argument for
$$
\beta
=
-\frac32
-
\frac12\sqrt{13}
$$
gives
$$
\beta\notin D.
$$

:::

:::

::: pf-step

A monic quadratic over an integral domain is reducible only if it has a root in that domain.


::: pf-proof

Let
$$
A
$$
be an integral domain and suppose the monic quadratic
$$
g(x)
$$
has a nontrivial factorization
$$
g(x)
=(ux+a)(vx+b).
$$
Since the leading coefficient of $g$ is $1$,
$$
uv=1,
$$
so $u$ and $v$ are units.
Therefore
$$
g(x)
=(x+u^{-1}a)(x+v^{-1}b),
$$
and
$$
-u^{-1}a
\in A
$$
is a root.

:::

:::

::: pf-step

The polynomial
$$
x^2+3x-1
$$
is irreducible in
$$
D[x].
$$


::: pf-proof

The ring $D$ is an integral domain by hypothesis.
If $f$ were reducible in $D[x]$, step <1>4 would give a root of $f$ in $D$.
Its only roots in the fraction field are $\alpha$ and $\beta$, and step <1>3 shows neither lies in $D$.
Hence $f$ is irreducible over $D$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
x^2+3x-1
\text{ is irreducible in }D[x]
\text{ but reducible in }F[x].
}
$$


::: pf-proof

Combine steps <1>2 and <1>5.

:::

:::

::: pf-step

The element
$$
\alpha
=
\frac{-3+\sqrt{13}}2
$$
is integral over $D$ but does not belong to $D$.


::: pf-proof

By step <1>1,
$$
f(\alpha)=0,
$$
where
$$
f(x)=x^2+3x-1
$$
is monic with coefficients in
$$
\ZZ\subseteq D.
$$
Thus $\alpha$ is integral over $D$.
Step <1>3 gives
$$
\alpha\notin D.
$$

:::

:::

::: pf-step

Every UFD is integrally closed in its field of fractions.


::: pf-proof

Let
$$
A
$$
be a UFD and let
$$
z=\frac ab
\in
\operatorname{Frac}(A)
$$
be integral over $A$, with $a,b$ chosen to have no common irreducible factor.
If
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_0=0
$$
is a monic equation over $A$, then multiplying by
$$
b^n
$$
gives
$$
a^n
=
-b
\left(
c_{n-1}a^{n-1}
+
\cdots
+
c_0b^{n-1}
\right).
$$
Thus
$$
b\mid a^n.
$$
If $b$ were not a unit, some irreducible
$$
\pi
$$
would divide $b$.
In a UFD irreducibles are prime, so
$$
\pi\mid a^n
$$
would imply
$$
\pi\mid a,
$$
contradicting the choice of $a,b$.
Therefore $b$ is a unit and
$$
z\in A.
$$
Hence $A$ is integrally closed.

:::

:::

::: pf-step

The ring $D$ is not a UFD.


::: pf-proof

Step <1>7 exhibits an element of
$$
\operatorname{Frac}(D)=F
$$
that is integral over $D$ but not in $D$.
Thus $D$ is not integrally closed.
Step <1>8 shows that every UFD is integrally closed.
Therefore
$$
\boxed{
D
\text{ is not a unique factorization domain}.
}
$$

:::

:::

::: pf-qed

Step <1>6 proves part (a), and step <1>9 proves part (b).

:::

:::
