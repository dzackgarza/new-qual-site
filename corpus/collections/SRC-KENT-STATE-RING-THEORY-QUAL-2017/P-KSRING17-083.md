---
schema: qual/card@1
id: P-KSRING17-083
kind: problem
title: '$\mathbb Z[\sqrt{21}]$ is not a UFD: irreducibility of $x^2-x-5$'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 83 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $D = \mathbb { Z } ( { \sqrt { 2 1 } } ) = \{ m + n { \sqrt { 2 1 } } \mid m , n \in \mathbb { Z } \}$ and $F = \mathbb { Q } ( { \sqrt { 2 1 } } )$ , the field of fractions of D. Show the following:

(a) $x ^ { 2 } - x - 5$ is irreducible in $D [ x ]$ but not in $F [ x ]$

(b) D is not a unique factorization domain.
:::

::: {.solution}
Set
$$
f(x)
\coloneqq
x^2-x-5.
$$

<1>1. In
$$
F=\QQ(\sqrt{21}),
$$
the roots of $f$ are
$$
\alpha
\coloneqq
\frac{1+\sqrt{21}}2,
\qquad
\beta
\coloneqq
\frac{1-\sqrt{21}}2.
$$

::: {.proof}
The discriminant of
$$
x^2-x-5
$$
is
$$
(-1)^2-4(1)(-5)
=
21.
$$
The quadratic formula therefore gives the displayed roots, both of which lie in
$$
\QQ(\sqrt{21}).
$$
:::

<1>2. Hence
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

::: {.proof}
This follows from step <1>1 and the factor theorem.
Thus $f$ is reducible over $F$.
:::

<1>3. Neither $\alpha$ nor $\beta$ lies in
$$
D=\ZZ[\sqrt{21}].
$$

::: {.proof}
Suppose
$$
\alpha
=
m+n\sqrt{21}
$$
for integers
$$
m,n.
$$
Then
$$
\frac12
+
\frac12\sqrt{21}
=
m+n\sqrt{21}.
$$
Since
$$
\sqrt{21}
\notin\QQ,
$$
the elements
$$
1
\qquad\text{and}\qquad
\sqrt{21}
$$
are linearly independent over $\QQ$.
Thus
$$
m=\frac12,
\qquad
n=\frac12,
$$
contradicting
$$
m,n\in\ZZ.
$$
Hence
$$
\alpha\notin D.
$$

The same argument applied to
$$
\beta
=
\frac12
-
\frac12\sqrt{21}
$$
shows
$$
\beta\notin D.
$$
:::

<1>4. A monic quadratic over an integral domain is reducible only if it has a root in that domain.

::: {.proof}
Let
$$
A
$$
be an integral domain and let
$$
g(x)\in A[x]
$$
be monic of degree $2$.
If
$$
g(x)
=(ux+a)(vx+b)
$$
is a nontrivial factorization, then
$$
uv=1.
$$
Thus
$$
u,v
$$
are units.
Rewrite
$$
g(x)
=
(x+u^{-1}a)(x+v^{-1}b).
$$
Hence
$$
-u^{-1}a
\in A
$$
is a root.
:::

<1>5. The polynomial
$$
x^2-x-5
$$
is irreducible in
$$
D[x].
$$

::: {.proof}
The ring $D$ is an integral domain by hypothesis.
If $f$ were reducible in $D[x]$, step <1>4 would give a root of $f$ in $D$.
But the only roots in its fraction field are $\alpha$ and $\beta$, and step <1>3 shows neither lies in $D$.
Therefore $f$ is irreducible over $D$.
:::

<1>6. Therefore
$$
\boxed{
x^2-x-5
\text{ is irreducible in }D[x]
\text{ but reducible in }F[x].
}
$$

::: {.proof}
Step <1>5 gives irreducibility over $D$, and step <1>2 gives reducibility over $F$.
:::

<1>7. The element
$$
\alpha
=
\frac{1+\sqrt{21}}2
$$
is integral over $D$ but does not belong to $D$.

::: {.proof}
By step <1>1,
$$
f(\alpha)=0,
$$
where
$$
f(x)=x^2-x-5
$$
is monic with coefficients in
$$
\ZZ\subseteq D.
$$
Thus $\alpha$ is integral over $D$.
Step <1>3 shows
$$
\alpha\notin D.
$$
:::

<1>8. Every UFD is integrally closed in its fraction field.

::: {.proof}
Let
$$
A
$$
be a UFD and suppose
$$
z=\frac ab
\in
\operatorname{Frac}(A)
$$
is integral over $A$, with $a,b$ chosen with no common irreducible factor.
Choose a monic equation
$$
z^n+c_{n-1}z^{n-1}+\cdots+c_0=0
$$
with
$$
c_i\in A.
$$
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
Hence $b$ is a unit and
$$
z\in A.
$$
Therefore $A$ is integrally closed.
:::

<1>9. The ring $D$ is not a UFD.

::: {.proof}
Step <1>7 exhibits an element of
$$
\operatorname{Frac}(D)=F
$$
that is integral over $D$ but not contained in $D$.
Thus $D$ is not integrally closed.
By step <1>8, every UFD is integrally closed.
Therefore
$$
\boxed{
D
\text{ is not a unique factorization domain}.
}
$$
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>6 proves part (a), and step <1>9 proves part (b).
:::
:::
