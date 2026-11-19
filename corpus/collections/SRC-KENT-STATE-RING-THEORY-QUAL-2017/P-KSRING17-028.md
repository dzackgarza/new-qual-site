---
schema: qual/card@1
id: P-KSRING17-028
kind: problem
title: 'The matrix ring $F_p$ of $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ over $\ZZ_p$: a field for $p=7$ but not $p=13$'
classification:
  areas: [algebra]
  topics:
  - Matrix Rings
  - Finite Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 28 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against the Lamport standard and checked. (a) is closed under addition and multiplication
    because M(a,b) = aI + bJ with J^2 = -I, and the multiplication is commutative since J commutes
    with I and with itself; the identity is M(1,0). (b) and (c) reduce to whether x^2 + 1 has a root
    in the field: F_p is isomorphic to F_p[i]/(i^2+1), so it is a field exactly when x^2+1 is
    irreducible, i.e. has no root. Checked by hand: modulo 7 the squares are 1, 2, 4, so -1 = 6 is
    not a square and F_7 is a field; modulo 13, 5^2 = 25 = -1, so x = 5 gives a zero divisor, and
    indeed (5+i)(5-i) = 26 = 0 in F_13. Both conclusions are right.
---

::: {.problem}
Let $p$ be a prime and $F_{p}$ the set of all $2 \times 2$ matrices of the form $\begin{bmatrix} a & b \\ -b & a \end{bmatrix}$, where $a, b \in \ZZ_{p}$.

(a) Show that $F_{p}$ is a commutative ring with identity.

(b) Show that $F_{7}$ is a field.

(c) Show that $F_{13}$ is not a field.
:::

::: {.solution}

For
$$
a,b\in\FF_p,
$$
write
$$
M(a,b)
\coloneqq
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

The set $F_p$ is closed under addition and additive inverses.


::: pf-proof

One has
$$
M(a,b)+M(c,d)
=
M(a+c,b+d)
$$
and
$$
-M(a,b)
=
M(-a,-b).
$$
The zero matrix is
$$
M(0,0).
$$
Thus $F_p$ is an additive subgroup of $M_2(\FF_p)$.

:::

:::

::: {.pf-step #s1-2}

The set $F_p$ is closed under multiplication, and multiplication is commutative.


::: pf-proof

Direct multiplication gives
$$
\begin{aligned}
M(a,b)M(c,d)
&=
\begin{pmatrix}
ac-bd&ad+bc\\
-(ad+bc)&ac-bd
\end{pmatrix}\\
&=
M(ac-bd,ad+bc).
\end{aligned}
$$
This expression is symmetric in $(a,b)$ and $(c,d)$, so
$$
M(a,b)M(c,d)
=
M(c,d)M(a,b).
$$
Thus multiplication is closed and commutative.

:::

:::

::: {.pf-step #s1-3}

The identity matrix belongs to $F_p$.


::: pf-proof

One has
$$
I_2
=
M(1,0).
$$
Therefore $F_p$ is a commutative ring with identity.

:::

:::

::: pf-step

For
$$
M(a,b)\in F_p,
$$
one has
$$
\det M(a,b)
=
a^2+b^2.
$$


::: pf-proof

Compute
$$
\det
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
=
a^2-(-b)b
=
a^2+b^2.
$$

:::

:::

::: {.pf-step #s1-5}

In $\FF_7$, the element $-1$ is not a square.


::: pf-proof

The nonzero squares modulo $7$ are
$$
1^2\equiv1,
\qquad
2^2\equiv4,
\qquad
3^2\equiv2
\pmod7.
$$
The remaining nonzero squares repeat these values because
$$
(7-k)^2\equiv k^2.
$$
Thus the nonzero quadratic residues are
$$
1,2,4,
$$
and
$$
-1\equiv6
$$
is not among them.

:::

:::

::: {.pf-step #s1-6}

Every nonzero element of $F_7$ is invertible.


::: pf-proof

Let
$$
M(a,b)\in F_7
$$
be nonzero. If
$$
a^2+b^2=0,
$$
then if $b\ne0$,
$$
\left(\frac ab\right)^2
=
-1
$$
in $\FF_7$, contradicting step [](#s1-5){.pf-ref}. If $b=0$, then $a^2=0$, so $a=0$, contradicting nonzeroness.

Therefore
$$
a^2+b^2\ne0.
$$
Set
$$
N
\coloneqq
M\left(
\frac{a}{a^2+b^2},
\frac{-b}{a^2+b^2}
\right).
$$
Using the multiplication formula from step [](#s1-2){.pf-ref},
$$
M(a,b)N
=
M(1,0)
=
I_2.
$$
Thus every nonzero element is invertible.

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{F_7\text{ is a field}.}
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}, $F_7$ is a commutative ring with identity, and step [](#s1-6){.pf-ref} shows every nonzero element is invertible.

:::

:::

::: pf-step

In $\FF_{13}$,
$$
5^2\equiv-1\pmod{13}.
$$


::: pf-proof

Indeed,
$$
5^2
=
25
\equiv
12
\equiv
-1
\pmod{13}.
$$

:::

:::

::: {.pf-step #s1-9}

The ring $F_{13}$ has nonzero zero divisors.


::: pf-proof

Consider
$$
A
\coloneqq
M(5,1),
\qquad
B
\coloneqq
M(5,-1).
$$
Both matrices are nonzero. By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
AB
&=
M(25+1,-5+5)\\
&=
M(26,0)\\
&=
M(0,0)
\end{aligned}
$$
in characteristic $13$.
Thus $A$ and $B$ are nonzero zero divisors.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{F_{13}\text{ is not a field}.}
$$


::: pf-proof

A field has no nonzero zero divisors, whereas step [](#s1-9){.pf-ref} exhibits such zero divisors in $F_{13}$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} prove part (a), step [](#s1-7){.pf-ref} proves part (b), and step [](#s1-10){.pf-ref} proves part (c).

:::

:::

:::
