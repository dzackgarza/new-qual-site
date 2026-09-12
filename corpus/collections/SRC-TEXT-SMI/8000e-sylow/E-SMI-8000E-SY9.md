---
schema: qual/card@1
id: E-SMI-8000E-SY9
kind: problem
title: A complete study of GL(3, Z/2)
classification:
  areas:
  - algebra
  topics:
  - Sylow Theorems
  - Linear Groups
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared every requested item with Smith 8000e Sylow problem 9."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Classified all invertible rational forms over F2, independently verified the six conjugacy-class sizes 1,21,56,42,24,24 by exact enumeration, counted all element orders and Sylow subgroups, exhibited representatives, and proved simplicity from the conjugacy-class sizes."
---

::: {.exercise}
Determine how many Sylow subgroups exist for each prime in the group $\mathrm{GL}_3(\ZZ/2)$ of invertible $3 \times 3$ matrices over $\ZZ/2$.

In fact, learn everything you can about this group: the order of the group, the number of elements of each order, the number of Sylow subgroups of each order.
Find all possible characteristic polynomials for elements of this group, and for each characteristic polynomial find all rational forms having this polynomial, and Jordan forms if they exist.

Actually find elements of each order, and find elements in each conjugacy class.
Note whether any elements of the same order fail to be conjugate.
Note that there is exactly one (invertible) rational form for each conjugacy class of elements in the group — two matrices have the same rational form if and only if they are conjugate.

You may use all three tools available to study this group: Jordan forms, rational forms, and the fact that it acts linearly on the vector space $(\ZZ/2)^3$, hence on the 7-point projective plane, carrying lines to lines.

Try to prove this group is simple, along the lines of the proof given for Icos — i.e. use conjugacy classes (but they are harder to compute).
:::

::: solution
Put
$$
G=GL_3(\mathbf F_2).
$$

<1>1. Compute the order of $G$.
::: proof
An invertible matrix is the same as an ordered basis of $\mathbf F_2^3$.
The first column may be any nonzero vector, giving $8-1=7$ choices. The
second may be any vector outside the span of the first, giving $8-2=6$
choices. The third may be any vector outside the plane spanned by the first
two, giving $8-4=4$ choices. Thus
$$
\boxed{|G|=(8-1)(8-2)(8-4)=7\cdot6\cdot4=168=2^3\cdot3\cdot7.}
$$
:::

<1>2. List all possible characteristic polynomials.
::: proof
For $A\in G$, the characteristic polynomial is a monic cubic over
$\mathbf F_2$. Its constant term is nonzero, hence equals $1$. Therefore it
is one of the four monic cubics with constant term $1$:
$$
\begin{aligned}
f_u(x)&=x^3+x^2+x+1=(x+1)^3,\\
f_3(x)&=x^3+1=(x+1)(x^2+x+1),\\
f_{7,1}(x)&=x^3+x+1,\\
f_{7,2}(x)&=x^3+x^2+1.
\end{aligned}
$$
The last two have no root in $\mathbf F_2$, so they are irreducible.
:::

<1>3. Determine the rational and Jordan forms for $f_u=(x+1)^3$.
::: proof
The invariant factors are powers of $x+1$ whose degrees sum to $3$ and form
a divisibility chain. Thus the three possibilities correspond to the
partitions
$$
1+1+1,
\qquad
2+1,
\qquad
3.
$$
Equivalently, the rational forms have invariant-factor lists
$$
(x+1,x+1,x+1),
$$
$$
(x+1,(x+1)^2),
$$
and
$$
((x+1)^3).
$$
Because the polynomial splits over $\mathbf F_2$, the corresponding Jordan
forms are
$$
I_3,
\qquad
J_2(1)\oplus J_1(1),
\qquad
J_3(1).
$$
Their orders are respectively
$$
1,\qquad2,\qquad4.
$$
Indeed, in characteristic $2$,
$$
(I+N)^2=I+N^2.
$$
For a size-$2$ nilpotent block, $N^2=0$; for a size-$3$ block,
$N^2\ne0$ but $N^4=0$, so the order is $4$.
:::

<1>4. Determine the rational forms for the other three characteristic polynomials.
::: proof
For
$$
f_3=(x+1)(x^2+x+1),
$$
the two irreducible factors are distinct. Hence the minimal polynomial must
contain both factors, so it equals the characteristic polynomial. Therefore
there is one rational form, the companion matrix
$$
C(f_3).
$$
For example, one representative is
$$
A_3=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
$$
the permutation matrix of a $3$-cycle. Thus $A_3$ has order $3$.

Each of $f_{7,1}$ and $f_{7,2}$ is irreducible of degree $3$, so again there
is one rational form for each, namely its companion matrix. We may take
$$
A_{7,1}=
\begin{pmatrix}
0&0&1\\
1&0&1\\
0&1&0
\end{pmatrix},
\qquad
A_{7,2}=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&1
\end{pmatrix}.
$$
A root of either irreducible cubic lies in $\mathbf F_8\setminus\mathbf F_2$.
Since
$$
\mathbf F_8^\times
$$
has prime order $7$, every nonidentity element has order $7$. Hence both
companion matrices have order $7$.

The three polynomials in this step do not split over $\mathbf F_2$, so they
have no Jordan form over $\mathbf F_2$. Over a splitting field they are
diagonalizable because all their irreducible factors are separable.
:::

<1>5. Exhibit representatives of all six conjugacy classes.
::: proof
The rational-form classification above shows that the complete list consists
of six classes. Representatives may be chosen as
$$
I_3,
$$
$$
A_2=
\begin{pmatrix}
1&1&0\\
0&1&0\\
0&0&1
\end{pmatrix},
$$
$$
A_4=
\begin{pmatrix}
1&1&0\\
0&1&1\\
0&0&1
\end{pmatrix},
$$
together with $A_3,A_{7,1},A_{7,2}$ from step <1>4. Their orders are
respectively
$$
1,2,4,3,7,7.
$$
Thus the only elements of the same order which can fail to be conjugate are
the order-$7$ elements, and the two irreducible cubics show that there are
indeed two distinct order-$7$ conjugacy classes.
:::

<1>6. Compute the centralizer and conjugacy-class size for each representative.
::: proof
For the identity the centralizer is all of $G$, so the class has size $1$.

For $A_2=I+E_{12}$, solving $XA_2=A_2X$ over $\mathbf F_2$ shows that the
invertible commuting matrices are exactly
$$
X=
\begin{pmatrix}
1&a&b\\
0&1&0\\
0&c&1
\end{pmatrix},
\qquad a,b,c\in\mathbf F_2.
$$
Hence
$$
|C_G(A_2)|=8,
\qquad
|A_2^G|=\frac{168}{8}=21.
$$

The matrices $A_3,A_4,A_{7,1},A_{7,2}$ are cyclic: their minimal polynomial
has degree $3$. Therefore their full matrix centralizer is
$$
\mathbf F_2[A]\cong \mathbf F_2[x]/(m_A(x)),
$$
and their group centralizer consists of the units in that ring.

For $A_3$,
$$
\mathbf F_2[x]/(f_3)
\cong
\mathbf F_2\times\mathbf F_4,
$$
so the number of units is
$$
(2-1)(4-1)=3.
$$
Thus its class has size
$$
168/3=56.
$$

For $A_4$, writing $y=x+1$ gives
$$
\mathbf F_2[x]/((x+1)^3)\cong\mathbf F_2[y]/(y^3).
$$
A residue class is a unit exactly when its constant term is $1$, leaving two
free binary coefficients. Hence there are $4$ units and the class size is
$$
168/4=42.
$$

For either order-$7$ representative, the centralizer ring is the field
$\mathbf F_8$, so its group of units has order $7$. Each order-$7$ class
therefore has size
$$
168/7=24.
$$

Consequently the conjugacy-class data are
$$
\boxed{
\begin{array}{c|c|c|c}
\text{order}&\text{characteristic polynomial}&|C_G(A)|&|A^G|\\ \hline
1&(x+1)^3&168&1\\
2&(x+1)^3&8&21\\
3&x^3+1&3&56\\
4&(x+1)^3&4&42\\
7&x^3+x+1&7&24\\
7&x^3+x^2+1&7&24
\end{array}.}
$$
The class sizes sum to
$$
1+21+56+42+24+24=168,
$$
as required.
:::

<1>7. Count the elements of each order.
::: proof
The table immediately gives
$$
\boxed{
\begin{array}{c|ccccc}
\text{order}&1&2&3&4&7\\ \hline
\text{number of elements}&1&21&56&42&48
\end{array}.}
$$
There are two order-$7$ classes of $24$ elements each; every other occurring
order is a single conjugacy class.
:::

<1>8. Count the Sylow $7$- and Sylow $3$-subgroups.
::: proof
A Sylow $7$-subgroup is cyclic of order $7$ and therefore contains six
elements of order $7$. Distinct subgroups of prime order meet only in the
identity, so the $48$ elements of order $7$ partition into sets of six:
$$
\boxed{n_7=48/6=8.}
$$

Similarly, a Sylow $3$-subgroup is cyclic of order $3$ and contains two
nonidentity elements. The $56$ elements of order $3$ therefore give
$$
\boxed{n_3=56/2=28.}
$$
:::

<1>9. Count the Sylow $2$-subgroups and identify their structure.
::: proof
Consider the upper unitriangular subgroup
$$
U=
\left\{
\begin{pmatrix}
1&a&b\\
0&1&c\\
0&0&1
\end{pmatrix}:a,b,c\in\mathbf F_2
\right\}.
$$
It has order $8$, which is the full $2$-part of $|G|$, so $U$ is Sylow.
For an element $I+N$ of $U$,
$$
(I+N)^2=I+N^2,
$$
and $N^2$ has only one possibly nonzero entry, namely the $(1,3)$ entry
$ac$. Thus exactly the two elements with
$$
a=c=1
$$
have order $4$; the other five nonidentity elements have order $2$. Hence
$U\cong D_8$.

All Sylow $2$-subgroups are conjugate, so every one contains exactly two
elements of order $4$. Every order-$4$ element lies in some Sylow
$2$-subgroup. Counting incidences between Sylow $2$-subgroups and order-$4$
elements therefore gives
$$
2n_2\ge42.
$$
Thus $n_2\ge21$. But Sylow's theorem gives
$$
n_2\mid21.
$$
Consequently
$$
\boxed{n_2=21.}
$$
In fact equality in the incidence count shows that every order-$4$ element
lies in a unique Sylow $2$-subgroup.
:::

<1>10. Prove that $G$ is simple.
::: proof
Let $N\trianglelefteq G$. A normal subgroup is a union of conjugacy classes
and must contain the identity. The nonidentity class sizes are
$$
21,42,56,24,24.
$$
If $N$ is nontrivial and proper, then $|N|$ is a proper divisor of $168$ and
is at least $1+21=22$. The only proper divisors of $168$ which are at least
$22$ are
$$
24,28,42,56,84.
$$
Thus the nonidentity part of $N$ would have to have size respectively
$$
23,27,41,55,83.
$$
None of these numbers is a sum of a subset of
$$
\{21,42,56,24,24\}.
$$
Indeed, the first three are smaller than $42$ and are neither $21$ nor $24$;
$55$ is not obtainable from $21,24,24$ and becomes too small after including
$42$ or $56$; and for $83$, including $56$ leaves $27$, including $42$ but
not $56$ leaves $41$, while excluding both leaves a maximum of
$21+24+24=69$.

Therefore no nontrivial proper normal subgroup can exist. Hence
$$
\boxed{GL_3(\mathbf F_2)\text{ is simple}.}
$$
:::
:::
