---
schema: qual/card@1
id: P-KSRING17-110
kind: problem
title: $F[x]$ is a PID but $F[x,y]$ is not
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 110 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let F be a field.
Prove that the polynomial ring $F [ x ]$ is a PID and that $F [ x , y ]$ is not a PID.
:::

::: pf

::: pf-step

The polynomial ring
$$
F[x]
$$
is a Euclidean domain with Euclidean function
$$
\delta(f)
\coloneqq
\deg f
$$
for
$$
f\ne0.
$$


::: pf-proof

Let
$$
f,g\in F[x],
\qquad
g\ne0.
$$
Because the leading coefficient of $g$ is invertible in the field $F$, polynomial division gives
$$
f=qg+r
$$
with
$$
q,r\in F[x]
$$
and either
$$
r=0
$$
or
$$
\deg r<\deg g.
$$
This is exactly the Euclidean division property.

:::

:::

::: pf-step

Every ideal of $F[x]$ is principal.


::: pf-proof

Let
$$
I\trianglelefteq F[x].
$$
If
$$
I=(0),
$$
it is principal.

Assume
$$
I\ne(0).
$$
Choose a nonzero polynomial
$$
d\in I
$$
of minimal degree.
For any
$$
f\in I,
$$
divide by $d$:
$$
f=qd+r
$$
with
$$
r=0
$$
or
$$
\deg r<\deg d.
$$
Since
$$
r=f-qd\in I,
$$
minimality of
$$
\deg d
$$
forces
$$
r=0.
$$
Thus
$$
d\mid f
$$
for every
$$
f\in I,
$$
so
$$
I\subseteq(d).
$$
The reverse inclusion follows from
$$
d\in I.
$$
Hence
$$
I=(d).
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
F[x]
\text{ is a principal ideal domain}.
}
$$


::: pf-proof

The ring
$$
F[x]
$$
is an integral domain because $F$ is a field, and step <1>2 shows every ideal is principal.

:::

:::

::: pf-step

In
$$
F[x,y],
$$
the ideal
$$
I
\coloneqq
(x,y)
$$
is proper.


::: pf-proof

Consider evaluation at the origin:
$$
\operatorname{ev}_{(0,0)}:
F[x,y]\to F,
\qquad
h(x,y)\longmapsto h(0,0).
$$
Every element of
$$
(x,y)
$$
has zero constant term, hence lies in the kernel.
But
$$
1
$$
does not lie in the kernel.
Therefore
$$
1\notin(x,y),
$$
so
$$
(x,y)\ne F[x,y].
$$

:::

:::

::: pf-step

Suppose, for contradiction, that
$$
(x,y)=(f)
$$
for some
$$
f\in F[x,y].
$$
Then
$$
f\mid x
$$
and
$$
f\mid y.
$$


::: pf-proof

Since
$$
x,y\in(x,y)=(f),
$$
both $x$ and $y$ are multiples of $f$.

:::

:::

::: pf-step

The polynomials $x$ and $y$ are irreducible and are not associates in
$$
F[x,y].
$$


::: pf-proof

The ring
$$
F[x,y]
$$
is a UFD.
Both
$$
x
\qquad\text{and}\qquad
y
$$
have total degree $1$, so any nontrivial factorization would force one factor to have total degree $0$, hence to be a nonzero constant and therefore a unit.
Thus both are irreducible.

They are not associates: if
$$
x=uy
$$
for a unit
$$
u\in F[x,y]^\times=F^\times,
$$
then the monomial supports on the two sides would differ, which is impossible.

:::

:::

::: pf-step

The element $f$ from step <1>5 must be a unit.


::: pf-proof

Since
$$
f\mid x
$$
and $x$ is irreducible, either
$$
f
$$
is a unit or $f$ is associate to $x$.
If $f$ were associate to $x$, then
$$
f\mid y
$$
would imply
$$
x\mid y,
$$
forcing the irreducibles $x$ and $y$ to be associates.
This contradicts step <1>6.
Therefore
$$
f
$$
is a unit.

:::

:::

::: pf-step

The ideal $(x,y)$ is not principal.


::: pf-proof

If
$$
(x,y)=(f)
$$
were principal, step <1>7 would make $f$ a unit.
Then
$$
(x,y)=(f)=F[x,y],
$$
contradicting step <1>4.
Hence
$$
\boxed{
(x,y)
\text{ is not principal}.
}
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
F[x,y]
\text{ is not a principal ideal domain}.
}
$$


::: pf-proof

A PID has every ideal principal.
Step <1>8 exhibits a nonprincipal ideal.

:::

:::

::: pf-qed

Step <1>3 proves the first assertion, and step <1>9 proves the second.

:::

:::
