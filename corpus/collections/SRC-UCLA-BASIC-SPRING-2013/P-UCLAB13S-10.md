---
schema: qual/card@1
id: P-UCLAB13S-10
kind: problem
title: Centralizer of a unipotent upper-triangular matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Spring 2013.
---

::: {.problem}
Let $G$ be the set of real $4\times4$ upper-triangular matrices with $1$'s on the diagonal, and fix
$$
M=\begin{pmatrix}
1&1&1&1\\
0&1&1&1\\
0&0&1&1\\
0&0&0&1
\end{pmatrix}.
$$
Let $C$ be the set of matrices in $G$ commuting with $M$.

(a) Prove that $C$ is an affine subspace of $\RR^{16}$.

(b) Find the dimension of $C$.
:::

::: {.solution}

Write
$$
M=I+N,
\qquad
N=
\begin{pmatrix}
0&1&1&1\\
0&0&1&1\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
$$
Every element of $G$ has the form
$$
X=
\begin{pmatrix}
1&a&b&c\\
0&1&d&e\\
0&0&1&f\\
0&0&0&1
\end{pmatrix}
=
I+Y,
$$
where
$$
Y=
\begin{pmatrix}
0&a&b&c\\
0&0&d&e\\
0&0&0&f\\
0&0&0&0
\end{pmatrix}.
$$

::: pf

::: pf-step

The commutation relation
$$
XM=MX
$$
is equivalent to
$$
\boxed{YN=NY}.
$$


::: pf-proof

Using
$$
X=I+Y
\qquad\text{and}\qquad
M=I+N,
$$
one has
$$
\begin{aligned}
XM
&=
(I+Y)(I+N)\\
&=
I+Y+N+YN,
\end{aligned}
$$
while
$$
\begin{aligned}
MX
&=
(I+N)(I+Y)\\
&=
I+N+Y+NY.
\end{aligned}
$$
The common terms cancel, leaving
$$
YN=NY.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
YN
=
\begin{pmatrix}
0&0&a&a+b\\
0&0&0&d\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$


::: pf-proof

Multiply the displayed matrices $Y$ and $N$.
The only potentially nonzero entries are above the diagonal.
For example,
$$
(YN)_{13}
=
a,
\qquad
(YN)_{14}
=
a+b,
\qquad
(YN)_{24}
=
d.
$$
All other strictly upper-triangular entries vanish.

:::

:::

::: {.pf-step #s1-3}

One has
$$
NY
=
\begin{pmatrix}
0&0&d&e+f\\
0&0&0&f\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$


::: pf-proof

Again multiply directly.
The relevant entries are
$$
(NY)_{13}=d,
\qquad
(NY)_{14}=e+f,
\qquad
(NY)_{24}=f.
$$

:::

:::

::: {.pf-step #s1-4}

The equation
$$
YN=NY
$$
is equivalent to
$$
\boxed{
a=d,\qquad d=f,\qquad a+b=e+f.
}
$$


::: pf-proof

Compare the corresponding entries of the matrices in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref}.
Equality of the $(1,3)$ entries gives
$$
a=d.
$$
Equality of the $(2,4)$ entries gives
$$
d=f.
$$
Equality of the $(1,4)$ entries gives
$$
a+b=e+f.
$$
No other entries impose additional conditions.

:::

:::

::: {.pf-step #s1-5}

These equations reduce to
$$
\boxed{
d=f=a,
\qquad
e=b.
}
$$


::: pf-proof

The first two equations in step [](#s1-4){.pf-ref} give
$$
d=f=a.
$$
Substitute this into the third equation:
$$
a+b=e+a.
$$
Thus
$$
e=b.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
C=
\left\{
\begin{pmatrix}
1&a&b&c\\
0&1&a&b\\
0&0&1&a\\
0&0&0&1
\end{pmatrix}
:a,b,c\in\RR
\right\}.
}
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, every commuting matrix in $G$ must have exactly the displayed form.
Conversely, any matrix of this form has
$$
d=f=a
\qquad\text{and}\qquad
e=b,
$$
so it satisfies the equations in step [](#s1-4){.pf-ref} and therefore commutes with $M$.

:::

:::

::: {.pf-step #s1-7}

The set $C$ is an affine subspace of $\RR^{16}$.


::: pf-proof

Let
$$
E_1=
\begin{pmatrix}
0&1&0&0\\
0&0&1&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix},
\quad
E_2=
\begin{pmatrix}
0&0&1&0\\
0&0&0&1\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\quad
E_3=
\begin{pmatrix}
0&0&0&1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
$$
Then step [](#s1-6){.pf-ref} says
$$
C
=
I+\operatorname{span}\{E_1,E_2,E_3\}.
$$
The translate of a linear subspace is an affine subspace.
This proves part (a).

:::

:::

::: {.pf-step #s1-8}

The matrices
$$
E_1,E_2,E_3
$$
are linearly independent.


::: pf-proof

Suppose
$$
\alpha E_1+\beta E_2+\gamma E_3=0.
$$
The $(1,2)$ entry gives
$$
\alpha=0.
$$
The $(1,3)$ entry then gives
$$
\beta=0,
$$
and the $(1,4)$ entry gives
$$
\gamma=0.
$$
Thus the three matrices are linearly independent.

:::

:::

::: {.pf-step #s1-9}

Hence
$$
\boxed{\dim C=3}.
$$


::: pf-proof

The translation space of the affine subspace $C$ is
$$
\operatorname{span}\{E_1,E_2,E_3\}.
$$
By step [](#s1-8){.pf-ref}, this space has dimension $3$.
Therefore the affine dimension of $C$ is $3$.
This proves part (b).

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} proves that $C$ is an affine subspace, and step [](#s1-9){.pf-ref} computes its dimension.

:::

:::

:::
