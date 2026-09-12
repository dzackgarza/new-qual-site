---
schema: qual/card@1
id: P-W5LVB
kind: problem
title: Abelian groups of order $60$, and $\mathbb{Q}[x]$-modules of dimension $4$
  annihilated by $x^8-1$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Modules
  - Structure Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both classification requests with July 2013 Rings 2 in the retained source extraction; corrected the generic prelim area to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked both abelian groups, irreducibility of all four polynomial factors, the canonical idempotent decomposition, and the exhaustive enumeration of ten multiplicity tuples."
---

::: {.problem}
a. List all abelian groups of order 60.

b. List all $\mathbb{Q}[x]$-modules that are annihilated by $x^8 - 1$ and have dimension 4 when thought of as vector spaces over $\mathbb{Q}$.
:::

::: solution
All classifications below are up to isomorphism.

<1>1. The abelian groups of order $60$ are
$C_{60}$ and $C_{30}\times C_2$, where $C_n=\mathbb Z/n\mathbb Z$.

::: proof
In an abelian group $A$ of order $60=4\cdot3\cdot5$, each
Sylow subgroup is normal and hence unique by Sylow conjugacy
[@DF04]. Multiplication from the product of these subgroups
to $A$ is a homomorphism because the factors commute. Its
kernel is trivial: if $uvw=1$ with $u,v,w$ in the order-$4$,
order-$3$, and order-$5$ factors, then $u=(vw)^{-1}$ has
order dividing both $4$ and $15$, so $u=1$. Now $v=w^{-1}$
has order dividing both $3$ and $5$, so $v=w=1$.
The domain and codomain both have order $60$, proving
that multiplication is an isomorphism.
The order-$3$ and order-$5$ factors are cyclic. An abelian
group of order $4$ either contains an element of order $4$,
in which case it is $C_4$, or has every nonidentity element
of order $2$, in which case it is a two-dimensional vector
space over $\mathbb F_2$ and is $C_2\times C_2$.

Thus the possibilities are
$C_4\times C_3\times C_5\cong C_{60}$ and
$C_2\times C_2\times C_3\times C_5
\cong C_2\times C_{30}$.
The displayed identifications combine cyclic factors of
coprime orders; a tuple of generators has order equal to
the product of those orders. The two groups are not
isomorphic, since only the first contains an element of
order $4$.
:::

<1>2. Every module in part (b) has a unique multiplicity
description
$$
M\cong E_1^{\oplus a}\oplus E_2^{\oplus b}
       \oplus E_4^{\oplus c}\oplus E_8^{\oplus d},
\qquad a+b+2c+4d=4,
$$
where the multiplicities are nonnegative integers and
$$
E_1=\mathbb Q[x]/(x-1),\quad
E_2=\mathbb Q[x]/(x+1),\quad
E_4=\mathbb Q[x]/(x^2+1),\quad
E_8=\mathbb Q[x]/(x^4+1).
$$
Each quotient has its natural $\mathbb Q[x]$-module structure.

::: proof
Factor
$$
f=x^8-1=(x-1)(x+1)(x^2+1)(x^4+1).
$$
The quadratic has no rational root and is irreducible.
The substitution $x=y+1$ changes $x^4+1$ to
$y^4+4y^3+6y^2+4y+2$, which is Eisenstein at $2$
[@DF04]. Since substitution by $y+1$ is an invertible change
of polynomial variable, $x^4+1$ is also irreducible.
Together with the two linear factors, these are distinct
monic irreducibles and are therefore pairwise coprime.

The Chinese remainder theorem gives
$$
R=\mathbb Q[x]/(f)\cong E_1\times E_2\times E_4\times E_8
$$
[@DF04]. In particular, each $E_j$ is a field. Their
dimensions over $\mathbb Q$ are respectively $1,1,2,4$:
for a monic polynomial of degree $r$, polynomial division
gives the basis $1,x,\ldots,x^{r-1}$ in its quotient.

Because $fM=0$, the action on $M$ factors through $R$.
Let $e_j\in R$ be the element whose coordinate in $E_j$
is $1$ and whose other coordinates are $0$. Then
$\sum_j e_j=1$, $e_j^2=e_j$, and $e_je_k=0$ for $j\ne k$.
Thus every $m\in M$ equals $\sum_j e_jm$. If a sum of
elements of the $e_jM$ is zero, multiplying by $e_k$ shows
that its $k$th term is zero. Consequently
$M=\bigoplus_j e_jM$.

Each $e_jM$ is a vector space over $E_j$. It is
finite-dimensional, since any linearly independent family
over $E_j$ is also linearly independent over $\mathbb Q$
and $\dim_{\mathbb Q}M=4$. Choose bases of sizes $a,b,c,d$.
This proves the claimed decomposition and dimension equation.
Conversely, every direct sum satisfying that equation has
dimension $4$ and is annihilated by $f$.

A $\mathbb Q[x]$-module isomorphism commutes with the action
of each $e_j$ and hence restricts to an $E_j$-linear
isomorphism on the corresponding summand. It therefore
preserves all four multiplicities. Equal multiplicities
give isomorphic direct sums, proving uniqueness.
:::

<1>3. There are exactly ten modules in part (b), namely

| $(a,b,c,d)$ | Module |
| --- | --- |
| $(4,0,0,0)$ | $E_1^{\oplus4}$ |
| $(3,1,0,0)$ | $E_1^{\oplus3}\oplus E_2$ |
| $(2,2,0,0)$ | $E_1^{\oplus2}\oplus E_2^{\oplus2}$ |
| $(1,3,0,0)$ | $E_1\oplus E_2^{\oplus3}$ |
| $(0,4,0,0)$ | $E_2^{\oplus4}$ |
| $(2,0,1,0)$ | $E_1^{\oplus2}\oplus E_4$ |
| $(1,1,1,0)$ | $E_1\oplus E_2\oplus E_4$ |
| $(0,2,1,0)$ | $E_2^{\oplus2}\oplus E_4$ |
| $(0,0,2,0)$ | $E_4^{\oplus2}$ |
| $(0,0,0,1)$ | $E_8$ |

::: proof
The equation in step <1>2 implies $d\leq1$. For $d=1$,
the other multiplicities vanish, giving the last row.
For $d=0$, one has $c\leq2$. If $c=2$, then $a=b=0$.
If $c=1$, then $a+b=2$, giving the three pairs
$(2,0),(1,1),(0,2)$. If $c=0$, then $a+b=4$, giving
the five pairs displayed in the first five rows.
These cases are exhaustive and disjoint, and uniqueness
in step <1>2 shows that no two rows are isomorphic.
:::
:::
