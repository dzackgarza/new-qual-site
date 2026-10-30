---
schema: qual/card@1
id: P-KSRING17-025
kind: problem
title: The matrices $\begin{pmatrix}a&b\\-3b&a\end{pmatrix}$ form a field
classification:
  areas: [algebra]
  topics:
  - Matrix Rings
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 25 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $\RR$ be the field of real numbers and let $F$ be the set of all $2 \times 2$ matrices of the form $\begin{bmatrix} a & b \\ -3b & a \end{bmatrix}$, where $a , b \in \RR$ . Show that $F$ is a field under the usual matrix operations.
:::

::: {.solution}

For
$$
a,b\in\RR,
$$
write
$$
M(a,b)
\coloneqq
\begin{pmatrix}
a&b\\
-3b&a
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

The set $F$ is closed under addition and additive inverses.


::: pf-proof

For
$$
a,b,c,d\in\RR,
$$
one has
$$
\begin{aligned}
M(a,b)+M(c,d)
&=
\begin{pmatrix}
a+c&b+d\\
-3(b+d)&a+c
\end{pmatrix}\\
&=
M(a+c,b+d),
\end{aligned}
$$
which lies in $F$.

Also,
$$
-M(a,b)
=
M(-a,-b)
\in F.
$$
The zero matrix is
$$
M(0,0).
$$
Thus $F$ is an additive subgroup of $M_2(\RR)$.

:::

:::

::: {.pf-step #s1-2}

The set $F$ is closed under multiplication.


::: pf-proof

Compute
$$
\begin{aligned}
M(a,b)M(c,d)
&=
\begin{pmatrix}
a&b\\
-3b&a
\end{pmatrix}
\begin{pmatrix}
c&d\\
-3d&c
\end{pmatrix}\\
&=
\begin{pmatrix}
ac-3bd&ad+bc\\
-3(ad+bc)&ac-3bd
\end{pmatrix}\\
&=
M(ac-3bd,ad+bc).
\end{aligned}
$$
Hence the product again lies in $F$.

:::

:::

::: {.pf-step #s1-3}

Multiplication in $F$ is commutative.


::: pf-proof

The multiplication formula from step [](#s1-2){.pf-ref} is symmetric in the pairs
$$
(a,b)
\qquad\text{and}\qquad
(c,d):
$$
$$
M(a,b)M(c,d)
=
M(ac-3bd,ad+bc)
=
M(c,d)M(a,b).
$$
Thus multiplication is commutative.

:::

:::

::: {.pf-step #s1-4}

The multiplicative identity of $M_2(\RR)$ lies in $F$:
$$
\boxed{
I_2
=
M(1,0).
}
$$


::: pf-proof

Indeed,
$$
M(1,0)
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}.
$$

:::

:::

::: {.pf-step #s1-5}

A matrix
$$
M(a,b)
$$
is zero if and only if
$$
a=b=0.
$$
If it is nonzero, then
$$
a^2+3b^2>0.
$$


::: pf-proof

The first assertion follows by inspection of the matrix entries.
If $(a,b)\ne(0,0)$, then at least one of $a^2$ and $b^2$ is positive, so
$$
a^2+3b^2>0.
$$

:::

:::

::: {.pf-step #s1-6}

Every nonzero element of $F$ has a multiplicative inverse in $F$.


::: pf-proof

Let
$$
M(a,b)\ne0.
$$
By step [](#s1-5){.pf-ref},
$$
a^2+3b^2\ne0.
$$
Set
$$
N
\coloneqq
M\left(
\frac{a}{a^2+3b^2},
\frac{-b}{a^2+3b^2}
\right).
$$
Using the multiplication formula from step [](#s1-2){.pf-ref},
$$
\begin{aligned}
M(a,b)N
&=
M\left(
\frac{a^2+3b^2}{a^2+3b^2},
\frac{-ab+ab}{a^2+3b^2}
\right)\\
&=
M(1,0)\\
&=
I_2.
\end{aligned}
$$
By commutativity, also
$$
NM(a,b)=I_2.
$$
Thus $N$ is the inverse of $M(a,b)$ and lies in $F$.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{F\text{ is a field}.}
$$


::: pf-proof

The usual matrix operations are associative and distributive. Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} show that $F$ is a commutative ring with identity, and step [](#s1-6){.pf-ref} shows that every nonzero element is invertible. Hence $F$ is a field.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
