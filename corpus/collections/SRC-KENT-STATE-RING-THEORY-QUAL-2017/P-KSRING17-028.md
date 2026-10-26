---
schema: qual/card@1
id: P-KSRING17-028
kind: problem
title: 'The matrix ring $F_p$ of $\begin{pmatrix}a&b\\-b&a\end{pmatrix}$ over $\mathbb Z_p$: a field for $p=7$ but not $p=13$'
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 28 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let p be a prime and $F _ { p }$ the set of all $2 \times 2$ matrices of the form $\left[ \begin{array} { r r } { a } & { b } \\ { - b } & { a } \end{array} \right]$ , where $a , b \in \mathbb { Z } _ { p }$

(a) Show that $F _ { p }$ is a commutative ring with identity.

(b) Show that $F _ { 7 }$ is a field.

(c) Show that $F _ { 1 3 }$ is not a field.
:::

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

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

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
in $\FF_7$, contradicting step <1>5. If $b=0$, then $a^2=0$, so $a=0$, contradicting nonzeroness.

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
Using the multiplication formula from step <1>2,
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

::: pf-step

Hence
$$
\boxed{F_7\text{ is a field}.}
$$


::: pf-proof

By steps <1>1--<1>3, $F_7$ is a commutative ring with identity, and step <1>6 shows every nonzero element is invertible.

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

::: pf-step

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
Both matrices are nonzero. By step <1>2,
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

::: pf-step

Therefore
$$
\boxed{F_{13}\text{ is not a field}.}
$$


::: pf-proof

A field has no nonzero zero divisors, whereas step <1>9 exhibits such zero divisors in $F_{13}$.

:::

:::

::: pf-qed

Steps <1>1--<1>3 prove part (a), step <1>7 proves part (b), and step <1>10 proves part (c).

:::

:::
