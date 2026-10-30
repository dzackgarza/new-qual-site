---
schema: qual/card@1
id: P-KSRING17-110
kind: problem
title: $F[x]$ is a PID but $F[x,y]$ is not
classification:
  areas: [algebra]
  topics:
  - Polynomial Rings
  - Principal Ideal Domains
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

::: {.solution}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

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
is an integral domain because $F$ is a field, and step [](#s1-2){.pf-ref} shows every ideal is principal.

:::

:::

::: {.pf-step #s1-4}

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

::: {.pf-step #s1-5}

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

::: {.pf-step #s1-6}

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

::: {.pf-step #s1-7}

The element $f$ from step [](#s1-5){.pf-ref} must be a unit.


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
This contradicts step [](#s1-6){.pf-ref}.
Therefore
$$
f
$$
is a unit.

:::

:::

::: {.pf-step #s1-8}

The ideal $(x,y)$ is not principal.


::: pf-proof

If
$$
(x,y)=(f)
$$
were principal, step [](#s1-7){.pf-ref} would make $f$ a unit.
Then
$$
(x,y)=(f)=F[x,y],
$$
contradicting step [](#s1-4){.pf-ref}.
Hence
$$
\boxed{
(x,y)
\text{ is not principal}.
}
$$

:::

:::

::: {.pf-step #s1-9}

Therefore
$$
\boxed{
F[x,y]
\text{ is not a principal ideal domain}.
}
$$


::: pf-proof

A PID has every ideal principal.
Step [](#s1-8){.pf-ref} exhibits a nonprincipal ideal.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the first assertion, and step [](#s1-9){.pf-ref} proves the second.

:::

:::

:::
