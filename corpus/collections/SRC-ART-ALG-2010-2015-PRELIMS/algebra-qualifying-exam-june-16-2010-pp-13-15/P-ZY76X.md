---
schema: qual/card@1
id: P-ZY76X
kind: problem
title: Intermediate fields of a Galois extension with group $D_8$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked June 2010 Fields 1 on PDF page 15, including exclusion of the two endpoint fields and the convention that D8 has eight elements."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the exhaustive subgroup enumeration by intersection with rotations, all subgroup orders and normality decisions, and the resulting eight strict intermediate fields."
---

::: {.problem}
Suppose the field $K$ is a Galois extension of the field $F$, such that the Galois group of $K$ over $F$ is isomorphic to the 8 element dihedral group $D_8$.

a. Determine the number of fields $L$ such that $F \subset L \subset K$, $L \neq F, L \neq K$, and indicate the dimension of $L$ over $F$ in each case.

b. Refine your answer to (a) by indicating how many fields in each dimension are Galois over $F$.
:::

::: {.solution}
There are eight strict intermediate fields: three of degree
two and five of degree four over $F$. All three quadratic
fields and exactly one of the five quartic fields are
Galois over $F$.

<1>1. We may write
$$
G=\operatorname{Gal}(K/F)
=\{1,r,r^2,r^3,s,rs,r^2s,r^3s\},
\qquad r^4=s^2=1,\quad srs=r^{-1}.
$$
The subgroup-to-field correspondence has
$[K^H:F]=8/|H|$, and $K^H/F$ is Galois exactly when
$H\lhd G$.

::: {.proof}
Choose an isomorphism with the symmetries of a square,
taking $r$ to a quarter-turn and $s$ to a reflection.
The displayed elements and relations describe these eight
symmetries. Since $K/F$ is Galois, its fixed field $K^G$
is $F$. The fixed-field theorem for a finite group of
field automorphisms gives $[K:F]=|G|=8$, so the finite
Galois correspondence applies with the asserted degree
and normality properties [@DF04].
:::

<1>2. The nontrivial proper subgroups of $G$ are exactly
$$
\langle r^2\rangle,\quad
\langle r^j s\rangle\ (j=0,1,2,3),\quad
\langle r\rangle,\quad
\langle r^2,s\rangle,\quad
\langle r^2,rs\rangle.
$$
The first five have order two and the last three order four.

::: {.proof}
Let $R=\langle r\rangle$, a cyclic subgroup of order four.
Its only subgroups are $\{1\}$, $\langle r^2\rangle$, and
$R$: containing $r$ or $r^3$ forces all of $R$, and any
other subgroup is contained in $\{1,r^2\}$.

For any $H\leq G$, put $T=H\cap R$. If $H\subseteq R$,
this already lists all possibilities. Otherwise choose
a reflection $t=r^j s\in H$. Every reflection has order
two, by $sr^j=r^{-j}s$. The product of two reflections
is a rotation. Hence each element of $H$ outside $R$
lies in the coset $tT$, and conversely $tT\subseteq H$.
Therefore
$$
H=T\mathbin{\sqcup}tT.
$$

If $T=\{1\}$, this gives $H=\{1,r^j s\}$, one of
four distinct order-two subgroups. If $T=\langle r^2\rangle$,
it gives
$H=\{1,r^2,r^j s,r^{j+2}s\}$.
This set is a subgroup: $r^2$ commutes with the order-two
element $r^j s$, so their four products form a group.
The set depends precisely on the parity of $j$, giving
the two displayed subgroups of order four. Finally,
$T=R$ gives $H=G$.
Together with the subgroups contained in $R$, these cases
exhaust every $H\leq G$. Removing $\{1\}$ and $G$ leaves
exactly the eight subgroups stated above, without repetitions.
:::

<1>3. The strict intermediate fields and Galois counts are

| Degree over $F$ | Fixed fields | Number | Number Galois over $F$ |
| --- | --- | --- | --- |
| $2$ | $K^{\langle r\rangle}$, $K^{\langle r^2,s\rangle}$, $K^{\langle r^2,rs\rangle}$ | $3$ | $3$ |
| $4$ | $K^{\langle r^2\rangle}$ and $K^{\langle r^j s\rangle}$ for $j=0,1,2,3$ | $5$ | $1$ |

::: {.proof}
The subgroup orders in step <1>2 and the degree formula
in step <1>1 give exactly the stated fields and degrees.
Different subgroups have different fixed fields, so none
of these entries is duplicated. The excluded subgroup
$G$ corresponds to $F$ and the excluded subgroup $\{1\}$
to $K$, exactly the two endpoints forbidden in the question.

All three subgroups of order four have index two and
are normal: both the left and right cosets of any element
outside an index-two subgroup are its complement.
The subgroup $\langle r^2\rangle$ is central, since
$r$ commutes with $r^2$ and $sr^2s=r^{-2}=r^2$.
It too is normal.
No reflection subgroup is normal, because
$$
r(r^j s)r^{-1}=r^{j+2}s\ne r^j s.
$$
Conjugation takes its unique nonidentity element outside
that subgroup. The normality criterion in step <1>1
therefore gives precisely the last column of the table.
:::
:::
