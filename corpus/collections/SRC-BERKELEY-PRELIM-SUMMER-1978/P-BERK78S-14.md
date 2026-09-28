---
schema: qual/card@1
id: P-BERK78S-14
kind: problem
title: Finite subgroups of $\operatorname{GL}_2(\ZZ)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked directly on the retained PDF page; the OCR's garbled matrix size is 2-by-2.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Finite order forces every matrix to be semisimple with root-of-unity
    eigenvalues. Integrality and degree two restrict the possible
    characteristic polynomials to (x-1)^2, (x+1)^2, x^2-1,
    x^2+x+1, x^2+1, and x^2-x+1, hence element orders
    1,2,3,4,6. Averaging the Euclidean inner product conjugates the finite
    group into O(2), whose finite subgroups are cyclic or dihedral; the
    allowed rotation orders give exactly the listed nine isomorphism types.
---

::: {.problem}
Let $G$ be a finite multiplicative group of $2\times2$ integer matrices.

1. For $A\in G$, what can one prove about
   (a) $\det A$;
   (b) the real or complex eigenvalues of $A$;
   (c) the Jordan or rational canonical form of $A$;
   (d) the order of $A$?
2. Find all such groups up to isomorphism.
:::

::: {.solution}
<1>1. Every element $A\in G$ has
$$
\boxed{
\det A=\pm1.
}
$$

::: {.proof}
Because $G$ is a group of integer matrices, $A^{-1}$ also has integer
entries. Hence
$$
\det A\in\ZZ,
\qquad
\det A^{-1}\in\ZZ,
$$
and
$$
\det A\det A^{-1}=1.
$$
The only integer units are $\pm1$.
:::

<1>2. Every $A\in G$ is diagonalizable over $\CC$, and every eigenvalue of
$A$ is a root of unity.

::: {.proof}
Since $G$ is finite, $A$ has finite order: for some $m\geq1$,
$$
A^m=I.
$$
Thus the minimal polynomial of $A$ divides
$$
x^m-1.
$$
Over $\CC$, the polynomial $x^m-1$ has distinct roots because its
derivative
$$
mx^{m-1}
$$
has no common root with it. Hence the minimal polynomial has no repeated
root, so $A$ is diagonalizable over $\CC$. If $\lambda$ is an eigenvalue,
then
$$
\lambda^m=1.
$$
:::

<1>3. If $\det A=1$, then the possible eigenvalue multisets are
$$
\{1,1\},
\quad
\{-1,-1\},
\quad
\{\zeta_3,\zeta_3^{-1}\},
\quad
\{i,-i\},
\quad
\{\zeta_6,\zeta_6^{-1}\},
$$
where $\zeta_m$ denotes a primitive $m$th root of unity.

::: {.proof}
The characteristic polynomial is
$$
\chi_A(x)
=
x^2-tx+1,
\qquad
t=\operatorname{tr}A\in\ZZ.
$$
By step <1>2, its two roots are roots of unity, so each has absolute value
$1$. Since their product is $1$, they are inverse to one another, and
$$
t=\lambda+\lambda^{-1}=2\operatorname{Re}\lambda.
$$
Thus
$$
\abs{t}\leq2.
$$
As $t$ is an integer,
$$
t\in\{-2,-1,0,1,2\}.
$$
The corresponding characteristic polynomials are
$$
(x+1)^2,\quad
x^2+x+1,\quad
x^2+1,\quad
x^2-x+1,\quad
(x-1)^2,
$$
which give exactly the displayed eigenvalues.
:::

<1>4. If $\det A=-1$, then the eigenvalues are
$$
\boxed{1\text{ and }-1}.
$$

::: {.proof}
By step <1>2, both eigenvalues have absolute value $1$. Their product is
$-1$. If one eigenvalue were nonreal, its complex conjugate would also be
an eigenvalue because the characteristic polynomial has real
coefficients, and their product would be
$$
\abs{\lambda}^2=1,
$$
contrary to $\det A=-1$. Thus both eigenvalues are real roots of unity,
and the only real roots of unity are $\pm1$. Their product being $-1$,
they are $1$ and $-1$.
:::

<1>5. Up to rational canonical form, every element of $G$ is represented
by one of
$$
\boxed{
I,\quad
-I,\quad
\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&-1\\1&-1\end{pmatrix},\quad
\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
\begin{pmatrix}0&-1\\1&1\end{pmatrix}.
}
$$

::: {.proof}
By step <1>2, the complex Jordan form is diagonal, with the eigenvalues
listed in steps <1>3--<1>4.

For the scalar cases the rational canonical forms are $I$ and $-I$.
For eigenvalues $1,-1$, the minimal and characteristic polynomial is
$$
x^2-1,
$$
whose companion matrix is
$$
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$
The remaining characteristic polynomials are
$$
x^2+x+1,\qquad
x^2+1,\qquad
x^2-x+1,
$$
with companion matrices
$$
\begin{pmatrix}0&-1\\1&-1\end{pmatrix},
\qquad
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
\begin{pmatrix}0&-1\\1&1\end{pmatrix},
$$
respectively.
:::

<1>6. The possible orders of an element $A\in G$ are exactly
$$
\boxed{
1,\ 2,\ 3,\ 4,\ 6.
}
$$

::: {.proof}
The diagonalizable eigenvalue lists in steps <1>3--<1>4 show that the
orders are respectively
$$
1,\ 2,\ 3,\ 4,\ 6,
$$
with the determinant-$-1$ case having order $2$. Each of these orders is
realized by one of the matrices in step <1>5.
:::

<1>7. There is a positive-definite inner product on $\RR^2$ which is
preserved by every element of $G$.

::: {.proof}
Starting from the standard Euclidean inner product
$\langle\ ,\ \rangle_0$, define
$$
\langle v,w\rangle_G
=
\sum_{A\in G}
\langle Av,Aw\rangle_0.
$$
This is positive definite because the term corresponding to the identity
is
$$
\langle v,v\rangle_0>0
$$
for $v\neq0$. For $B\in G$,
$$
\begin{aligned}
\langle Bv,Bw\rangle_G
&=
\sum_{A\in G}
\langle ABv,ABw\rangle_0\\
&=
\sum_{C\in G}
\langle Cv,Cw\rangle_0\\
&=
\langle v,w\rangle_G,
\end{aligned}
$$
because right multiplication by $B$ permutes the elements of $G$.
:::

<1>8. After conjugating by a real invertible matrix, $G$ is a finite
subgroup of $O(2)$.

::: {.proof}
Choose a basis of $\RR^2$ orthonormal for the inner product in step <1>7.
In that basis, every element of $G$ preserves the standard Euclidean inner
product, hence is orthogonal. Changing basis conjugates the original group
inside $\operatorname{GL}_2(\RR)$ and does not change its abstract
isomorphism type.
:::

<1>9. Every finite subgroup of $O(2)$ is either cyclic or dihedral.

::: {.proof}
Let
$$
H=G\cap SO(2).
$$
The group $SO(2)$ consists of rotations. A finite subgroup of the circle
group of rotations is cyclic: if $H$ has order $m$, its rotation angles
form a finite subgroup of $\RR/2\pi\ZZ$, hence are the multiples of
$2\pi/m$.

If $G=H$, then $G$ is cyclic. Otherwise choose
$$
S\in G\sm H.
$$
As an orientation-reversing orthogonal transformation of the plane, $S$
is a reflection and satisfies
$$
S^2=I.
$$
If $R$ generates $H$, reflection reverses orientation of angles, so
$$
SRS^{-1}=R^{-1}.
$$
Every element of $G$ is either in $H$ or in the coset $SH$, because
$H$ is the kernel of
$$
\det:G\longrightarrow\{\pm1\}.
$$
Thus
$$
G
=
\langle R,S:
R^m=S^2=1,\ SRS=R^{-1}\rangle,
$$
the dihedral group of order $2m$.
:::

<1>10. The order $m$ of the rotation subgroup $H$ can only be
$$
m\in\{1,2,3,4,6\}.
$$

::: {.proof}
The generator of $H$ is an element of the original group $G$ up to real
conjugacy, so its order is unchanged by conjugation. Step <1>6 lists all
possible element orders.
:::

<1>11. Up to isomorphism, every finite multiplicative group of
$2\times2$ integer matrices is one of
$$
\boxed{
\{1\},\
C_2,\
C_3,\
C_4,\
C_6,\
C_2\times C_2,\
D_6,\
D_8,\
D_{12},
}
$$
where $D_{2m}$ denotes the dihedral group of order $2m$.

::: {.proof}
If the group is orientation preserving, steps <1>9--<1>10 give
$$
C_m,
\qquad
m\in\{1,2,3,4,6\}.
$$
These yield
$$
\{1\},C_2,C_3,C_4,C_6.
$$

If the group contains an orientation-reversing element, steps
<1>9--<1>10 give the dihedral group of order $2m$ for the same possible
values of $m$. For $m=1$ this is $C_2$, already listed. For $m=2$ it is
the Klein four group
$$
C_2\times C_2.
$$
For $m=3,4,6$ one obtains
$$
D_6,\quad D_8,\quad D_{12}.
$$
No other isomorphism types can occur.
:::

<1>12. Every group listed in step <1>11 occurs as a subgroup of
$\operatorname{GL}_2(\ZZ)$.

::: {.proof}
For the cyclic groups use the matrices
$$
R_2=-I,
\qquad
R_3=
\begin{pmatrix}
0&-1\\
1&-1
\end{pmatrix},
\qquad
R_4=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
R_6=
\begin{pmatrix}
0&-1\\
1&1
\end{pmatrix},
$$
which have orders $2,3,4,6$, respectively; the trivial group is generated
by $I$.

For an orientation-reversing involution take
$$
S_0=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
$$
or
$$
S_1=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
$$
Then
$$
\langle -I,S_0\rangle
\cong
C_2\times C_2,
$$
and direct multiplication gives
$$
S_1R_3S_1=R_3^{-1},
\qquad
S_0R_4S_0=R_4^{-1},
\qquad
S_1R_6S_1=R_6^{-1}.
$$
Thus
$$
\langle R_3,S_1\rangle\cong D_6,
\qquad
\langle R_4,S_0\rangle\cong D_8,
\qquad
\langle R_6,S_1\rangle\cong D_{12}.
$$
All matrices displayed have integer entries and determinant $\pm1$.
:::

<1>13. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 answer part (1), and steps <1>7--<1>12 give the complete
classification required in part (2).
:::
:::
