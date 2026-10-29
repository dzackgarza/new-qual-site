---
schema: qual/card@1
id: P-KSRING17-084
kind: problem
title: '$\ZZ[\sqrt{-11}]$ is not a UFD: irreducibility of $x^2-x+3$'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 84 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D = \ZZ ( { \sqrt { - 1 1 } } ) = \{ m + n { \sqrt { - 1 1 } } \mid m , n \in \ZZ \}$ and $F = \QQ ( { \sqrt { - 1 1 } } )$ its field of fractions.
Show the following:

(a) $x ^ { 2 } - x + 3$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.
:::

::: {.solution}

Set
$$
f(x)
\coloneqq
x^2-x+3.
$$

::: pf

::: {.pf-step #s1-1}

The roots of $f$ in
$$
F=\QQ(\sqrt{-11})
$$
are
$$
\alpha
\coloneqq
\frac{1+\sqrt{-11}}2,
\qquad
\beta
\coloneqq
\frac{1-\sqrt{-11}}2.
$$


::: pf-proof

The discriminant of
$$
x^2-x+3
$$
is
$$
(-1)^2-4(1)(3)
=
-11.
$$
The quadratic formula gives the displayed roots.

:::

:::

::: {.pf-step #s1-2}

Therefore
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

This is the factorization determined by the roots from step [](#s1-1){.pf-ref}.
Thus $f$ is reducible over $F$.

:::

:::

::: {.pf-step #s1-3}

Neither $\alpha$ nor $\beta$ lies in
$$
D=\ZZ[\sqrt{-11}].
$$


::: pf-proof

Suppose
$$
\alpha
=
m+n\sqrt{-11}
$$
with
$$
m,n\in\ZZ.
$$
Then
$$
\frac12
+
\frac12\sqrt{-11}
=
m+n\sqrt{-11}.
$$
Since
$$
\sqrt{-11}
\notin\QQ,
$$
the elements
$$
1
\qquad\text{and}\qquad
\sqrt{-11}
$$
are linearly independent over $\QQ$.
Hence
$$
m=\frac12,
\qquad
n=\frac12,
$$
contradicting integrality of $m,n$.
Therefore
$$
\alpha\notin D.
$$

The same coefficient comparison for
$$
\beta
=
\frac12
-
\frac12\sqrt{-11}
$$
shows
$$
\beta\notin D.
$$

:::

:::

::: {.pf-step #s1-4}

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
factors nontrivially:
$$
g(x)
=(ux+a)(vx+b).
$$
The leading coefficient of $g$ is $1$, so
$$
uv=1.
$$
Thus $u,v$ are units.
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

::: {.pf-step #s1-5}

The polynomial
$$
x^2-x+3
$$
is irreducible in
$$
D[x].
$$


::: pf-proof

The ring $D$ is an integral domain by hypothesis.
If $f$ were reducible in $D[x]$, step [](#s1-4){.pf-ref} would give a root in $D$.
The only roots in its fraction field are $\alpha$ and $\beta$, and step [](#s1-3){.pf-ref} shows neither belongs to $D$.
Hence $f$ is irreducible over $D$.

:::

:::

::: {.pf-step #s1-6}

Thus
$$
\boxed{
x^2-x+3
\text{ is irreducible in }D[x]
\text{ but reducible in }F[x].
}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The element
$$
\alpha
=
\frac{1+\sqrt{-11}}2
$$
is integral over $D$ but is not an element of $D$.


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
f(\alpha)=0,
$$
where
$$
f(x)=x^2-x+3
$$
is monic with coefficients in
$$
\ZZ\subseteq D.
$$
Hence $\alpha$ is integral over $D$.
Step [](#s1-3){.pf-ref} gives
$$
\alpha\notin D.
$$

:::

:::

::: {.pf-step #s1-8}

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
Suppose
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_0=0
$$
is a monic equation over $A$.
Multiplying by
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
So $A$ is integrally closed.

:::

:::

::: {.pf-step #s1-9}

The ring $D$ is not a UFD.


::: pf-proof

Step [](#s1-7){.pf-ref} exhibits an element of
$$
\operatorname{Frac}(D)=F
$$
that is integral over $D$ but not in $D$.
Thus $D$ is not integrally closed.
By step [](#s1-8){.pf-ref}, a UFD must be integrally closed.
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

Step [](#s1-6){.pf-ref} proves part (a), and step [](#s1-9){.pf-ref} proves part (b).

:::

:::

:::
