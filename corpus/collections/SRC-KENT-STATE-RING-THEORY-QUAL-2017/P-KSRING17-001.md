---
schema: qual/card@1
id: P-KSRING17-001
kind: problem
title: 'Examples of rings: irreducible polynomials, non-UFD domains, non-Euclidean PIDs, local rings'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Give an example of each of the following.

(a) An irreducible polynomial of degree $3$ in $\ZZ_{3}[x]$.

(b) A polynomial in $\ZZ[x]$ that is not irreducible in $\ZZ[x]$ but is irreducible in $\QQ[x]$.

(c) A non-commutative ring of characteristic $p$, $p$ a prime.

(d) A ring with exactly $6$ invertible elements.

(e) An infinite non-commutative ring with only finitely many ideals.

(f) An infinite non-commutative ring with non-zero characteristic.

(g) An integral domain which is not a unique factorization domain.

(h) A unique factorization domain that is not a principal ideal domain.

(i) A principal ideal domain that is not a Euclidean domain.

(j) A Euclidean domain other than the ring of integers or a field.

(k) A finite non-commutative ring.

(l) A commutative ring with a sequence $\{P_{n}\}_{n=1}^{\infty}$ of prime ideals such that $P_{n}$ is properly contained in $P_{n+1}$ for all $n$.

(m) A non-zero prime ideal of a commutative ring that is not a maximal ideal.

(n) An irreducible element of a commutative ring that is not a prime element.

(o) An irreducible element of an integral domain that is not a prime element.

(p) A commutative ring that has exactly one maximal ideal and is not a field.

(q) A non-commutative ring with exactly two maximal ideals.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For part (a), take
$$
\boxed{x^3-x+1\in\FF_3[x].}
$$


::: pf-proof

A cubic over a field is reducible if and only if it has a root in that field. At the three elements of $\FF_3$,
$$
f(0)=1,
\qquad
f(1)=1,
\qquad
f(2)=8-2+1=7\equiv1\pmod3.
$$
Thus $f$ has no root in $\FF_3$ and is irreducible.

:::

:::

::: {.pf-step #s1-2}

For part (b), take
$$
\boxed{2x+2\in\ZZ[x].}
$$


::: pf-proof

In $\ZZ[x]$,
$$
2x+2
=
2(x+1),
$$
and neither factor is a unit, so the polynomial is reducible. In $\QQ[x]$, the constant $2$ is a unit and $2x+2$ has degree $1$, so it is irreducible.

:::

:::

::: {.pf-step #s1-3}

For part (c), take
$$
\boxed{M_2(\FF_p).}
$$


::: pf-proof

Its characteristic is $p$ because scalar addition is entrywise over $\FF_p$. It is noncommutative for $2\times2$ matrices; for example,
$$
E_{12}E_{21}
=
E_{11}
\ne
E_{22}
=
E_{21}E_{12}.
$$

:::

:::

::: {.pf-step #s1-4}

For part (d), take
$$
\boxed{\ZZ/9\ZZ.}
$$


::: pf-proof

The units modulo $9$ are exactly the residue classes relatively prime to $9$:
$$
1,2,4,5,7,8.
$$
Thus the ring has exactly
$$
\varphi(9)=6
$$
units.

:::

:::

::: {.pf-step #s1-5}

For part (e), take
$$
\boxed{M_2(\QQ).}
$$


::: pf-proof

The ring is infinite and noncommutative. A full matrix ring over a field is simple: any nonzero two-sided ideal containing a nonzero matrix contains a matrix unit after multiplication on the left and right by suitable matrix units, and hence contains every matrix unit. Therefore its only two-sided ideals are
$$
0
\qquad\text{and}\qquad
M_2(\QQ).
$$
Thus it has finitely many ideals.

:::

:::

::: {.pf-step #s1-6}

For part (f), take
$$
\boxed{M_2(\FF_p(t)).}
$$


::: pf-proof

The rational-function field $\FF_p(t)$ is infinite and has characteristic $p$. Hence its $2\times2$ matrix ring is infinite, has characteristic $p$, and is noncommutative.

:::

:::

::: {.pf-step #s1-7}

For part (g), take
$$
\boxed{\ZZ[\sqrt{-5}].}
$$


::: pf-proof

This is an integral domain because it is a subring of the field $\QQ(\sqrt{-5})$.
Use the multiplicative norm
$$
N(a+b\sqrt{-5})
\coloneqq
a^2+5b^2.
$$
There are no elements of norm $2$ or $3$. Hence:

- $2$ is irreducible, since a nontrivial factorization would force an element of norm $2$;
- $3$ is irreducible, since a nontrivial factorization would force an element of norm $3$;
- $1\pm\sqrt{-5}$ are irreducible, since their norm is $6$, and a nontrivial factorization would require factors of norms $2$ and $3$.

But
$$
6
=
2\cdot3
=
(1+\sqrt{-5})(1-\sqrt{-5}).
$$
The only units have norm $1$, hence are $\pm1$. The irreducibles in the two factorizations are therefore not associates. Thus factorization is not unique, so the domain is not a UFD.

:::

:::

::: {.pf-step #s1-8}

For part (h), take
$$
\boxed{\QQ[x,y].}
$$


::: pf-proof

A polynomial ring over a field is a UFD, and adjoining another indeterminate preserves the UFD property, so $\QQ[x,y]$ is a UFD.

It is not a PID. Indeed, if
$$
(x,y)=(f)
$$
were principal, then $f$ would divide both $x$ and $y$. Since $x$ and $y$ are relatively prime in the UFD $\QQ[x,y]$, $f$ would be a unit. That would give
$$
(x,y)=\QQ[x,y],
$$
contrary to the fact that every element of $(x,y)$ has zero constant term.

:::

:::

::: {.pf-step #s1-9}

For part (i), let
$$
\boxed{
R
\coloneqq
\ZZ\left[\frac{1+\sqrt{-19}}2\right].
}
$$
Then $R$ is a PID but is not a Euclidean domain.


::: pf-proof

Set
$$
\omega
\coloneqq
\frac{1+\sqrt{-19}}2.
$$
This is the ring of integers of the imaginary quadratic field
$$
K=\QQ(\sqrt{-19}),
$$
whose discriminant is $-19$.

First, $R$ is a PID. The Minkowski bound for an imaginary quadratic field says that every ideal class contains an integral ideal $I$ with
$$
N(I)
\le
\frac2\pi\sqrt{19}
<3.
$$
Thus
$$
N(I)\in\{1,2\}.
$$
There is no ideal of norm $2$: such an ideal would give a quotient map
$$
R\longrightarrow\FF_2,
$$
so the image of $\omega$ would be a root in $\FF_2$ of its minimal polynomial
$$
x^2-x+5.
$$
Modulo $2$ this is
$$
x^2+x+1,
$$
which has no root in $\FF_2$. Hence every ideal class contains an ideal of norm $1$, so every ideal class is trivial. Therefore $R$ is a PID.

Now suppose $R$ were Euclidean with respect to some Euclidean function $\delta$. Choose a nonzero nonunit $b$ with $\delta(b)$ minimal among all nonunits. Euclidean division says that every $a\in R$ can be written
$$
a=qb+r,
$$
where either $r=0$ or
$$
\delta(r)<\delta(b).
$$
By minimality, every nonzero remainder must be a unit. Thus every residue class modulo $(b)$ has a representative among
$$
0
\quad\text{and the units of }R.
$$

The norm form is
$$
N(a+c\omega)
=
a^2+ac+5c^2.
$$
The equation $N(u)=1$ has only $u=\pm1$, so the only units are $\pm1$. Therefore
$$
\abs{R/(b)}
\le3.
$$
But
$$
\abs{R/(b)}
=
\abs{N(b)}.
$$
Since $b$ is a nonunit, this norm is greater than $1$. On the other hand,
$$
a^2+ac+5c^2
=
\left(a+\frac c2\right)^2
+
\frac{19}{4}c^2,
$$
so it never takes the values $2$ or $3$: if $c=0$ it is a square, and if $c\ne0$ it is at least $19/4$. This contradicts
$$
2
\le
\abs{N(b)}
\le
3.
$$
Hence $R$ is not Euclidean.

:::

:::

::: {.pf-step #s1-10}

For part (j), take
$$
\boxed{\FF_2[x].}
$$


::: pf-proof

For nonzero polynomials $f,g\in\FF_2[x]$, polynomial division gives
$$
f=qg+r,
\qquad
r=0
\quad\text{or}\quad
\deg r<\deg g.
$$
Thus degree is a Euclidean function. The ring is neither a field nor the ring of integers.

:::

:::

::: {.pf-step #s1-11}

For part (k), take
$$
\boxed{M_2(\FF_2).}
$$


::: pf-proof

The ring has
$$
2^4=16
$$
elements and is noncommutative by the matrix-unit computation in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

For part (l), take
$$
\boxed{
R
\coloneqq
k[x_1,x_2,x_3,\ldots]
}
$$
for any field $k$, with
$$
P_n
\coloneqq
(x_1,\ldots,x_n).
$$


::: pf-proof

The quotient is
$$
R/P_n
\cong
k[x_{n+1},x_{n+2},\ldots],
$$
which is an integral domain. Hence each $P_n$ is prime.

Moreover,
$$
x_{n+1}\in P_{n+1}
$$
but
$$
x_{n+1}\notin P_n,
$$
so
$$
P_n
\subsetneq
P_{n+1}
$$
for every $n$.

:::

:::

::: {.pf-step #s1-13}

For part (m), take
$$
\boxed{
(x)
\subset
\QQ[x,y].
}
$$


::: pf-proof

The ideal is nonzero. Moreover,
$$
\QQ[x,y]/(x)
\cong
\QQ[y],
$$
which is an integral domain, so $(x)$ is prime. The quotient is not a field, so $(x)$ is not maximal.

:::

:::

::: {.pf-step #s1-14}

For part (n), take the element
$$
\boxed{
2\in\ZZ[\sqrt{-5}].
}
$$


::: pf-proof

By step [](#s1-7){.pf-ref}, $2$ is irreducible. It is not prime because
$$
2
\mid
(1+\sqrt{-5})(1-\sqrt{-5})
=
6,
$$
but $2$ divides neither factor: an equality
$$
1\pm\sqrt{-5}
=
2(a+b\sqrt{-5})
$$
would force the integer coefficient $1$ to be even. Thus $2$ is irreducible but not prime in this commutative ring.

:::

:::

::: {.pf-step #s1-15}

The same example answers part (o):
$$
\boxed{
2\in\ZZ[\sqrt{-5}].
}
$$


::: pf-proof

The ring $\ZZ[\sqrt{-5}]$ is an integral domain, and step [](#s1-14){.pf-ref} proves that $2$ is irreducible but not prime.

:::

:::

::: {.pf-step #s1-16}

For part (p), take
$$
\boxed{\ZZ/4\ZZ.}
$$


::: pf-proof

Its ideals are
$$
(0),
\qquad
(2),
\qquad
\ZZ/4\ZZ.
$$
Thus $(2)$ is its unique maximal ideal. The ring is not a field because the nonzero class of $2$ is not invertible.

:::

:::

::: {.pf-step #s1-17}

For part (q), take
$$
\boxed{
M_2(\FF_2)
\times
M_2(\FF_2).
}
$$


::: pf-proof

Let
$$
A=M_2(\FF_2).
$$
The ring $A$ is simple and noncommutative. Every two-sided ideal of
$$
A\times A
$$
is a product
$$
I_1\times I_2
$$
with $I_1,I_2$ ideals of $A$: multiplication by the central idempotents
$$
(1,0),
\qquad
(0,1)
$$
splits any ideal into its two coordinate parts.

Since $A$ has only the ideals $0$ and $A$, the proper ideals of $A\times A$ are
$$
0\times0,
\qquad
A\times0,
\qquad
0\times A.
$$
The last two are maximal because the corresponding quotients are each isomorphic to the simple ring $A$. Thus the ring has exactly two maximal two-sided ideals.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-17){.pf-ref} provide and justify examples for parts (a)--(q), respectively.

:::

:::

:::
