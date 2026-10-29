---
schema: qual/card@1
id: P-ARTALG-JU03-6
kind: problem
title: Galois groups with four incomparable proper intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually inspected PDF page 45. The diagram has six vertices: top and bottom and four mutually incomparable middle vertices, with no field-degree labels. Replaced the undefined diamond-shape description by that exact order relation."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Enumerated every subgroup of all five candidate groups, kept the two isomorphic order-six descriptions, and verified realizability over Q for both surviving isomorphism types."
---
::: {.problem}
Let $E$ be a splitting field of $g(x) \in \QQ[x]$ over $\QQ$.
Suppose its intermediate-field lattice consists of $\QQ$, $E$, and exactly four distinct proper intermediate fields $F_1,F_2,F_3,F_4$. Each satisfies $\QQ\subsetneq F_j\subsetneq E$, and no $F_j$ contains another $F_k$ for $j\ne k$. No degrees are specified.
Which of the following groups could be $\text{Gal}(E/\QQ)$?
Justify your answers.

(a) $\ZZ_2 \times \ZZ_2$

(b) $\ZZ_6$

(c) The dihedral group with 6 elements

(d) $S_3$

(e) $\ZZ_3 \times \ZZ_3$
:::

::: {.solution}
The possible answers are **(c), (d), and (e)**. Parts (c) and (d)
describe the same isomorphism type. The unlabeled lattice does not
distinguish that type from $C_3\times C_3$.

::: pf

::: {.pf-step #s1}

The required subgroup lattice has exactly four nontrivial
proper subgroups, all mutually incomparable.

::: pf-proof

A splitting field over $\QQ$ is a finite Galois extension,
since characteristic zero gives separability. The Galois
correspondence is an inclusion-reversing bijection between its
intermediate fields and the subgroups of its Galois group [@DF04].
It exchanges the two endpoints and sends the four incomparable
proper fields to four incomparable nontrivial proper subgroups.
Conversely, a Galois extension with this subgroup lattice has the
specified intermediate-field lattice.

:::

:::

::: {.pf-step #s2}

Neither (a) nor (b) has the required subgroup lattice.

::: pf-proof

In $C_2\times C_2$, each of the three nonidentity elements
generates a different subgroup of order $2$. By Lagrange's theorem
these are all the nontrivial proper subgroups. There are three,
not four, so (a) is impossible.

A cyclic group has exactly one subgroup of each order dividing
its order [@DF04]. Thus $C_6$ has just two nontrivial proper
subgroups, of orders $2$ and $3$. This rules out (b).

:::

:::

::: {.pf-step #s3}

Both (c) and (d) have the required subgroup lattice and
are realized over $\QQ$.

::: pf-proof

The symmetry group of an equilateral triangle acts faithfully
on its three vertices. It has six elements, so this action
identifies the dihedral group of order $6$ with $S_3$.

The nontrivial proper subgroups of $S_3$ can only have orders
$2$ and $3$. Its three transpositions generate three distinct
order-two subgroups. Its two $3$-cycles are inverse and generate
one order-three subgroup. These four subgroups are exhaustive
and mutually incomparable: distinct order-two subgroups cannot
contain one another, and neither $2$ nor $3$ divides the other.

For realization, let $a=\sqrt[3]{2}>0$ and let $\zeta$ be a
nonreal cube root of unity. The splitting field of $x^3-2$ is
$\QQ(a,\zeta)$, because its roots are $a,\zeta a,\zeta^2a$
and their ratios recover $\zeta$. Eisenstein's criterion at $2$
gives $[\QQ(a):\QQ]=3$, and adjoining the nonreal
root $\zeta$ of $x^2+x+1$ to the real field $\QQ(a)$ has
degree $2$. Its Galois group therefore has order $6$ and acts
faithfully on the three roots, so is $S_3$. Step [](#s1){.pf-ref} now gives
the required field lattice. This realizes both descriptions.

:::

:::

::: {.pf-step #s4}

The group in (e) also has the required subgroup lattice
and is realized over $\QQ$.

::: pf-proof

View $C_3\times C_3$ as the additive group of $\FF_3^2$.
Each nonzero vector spans a subgroup of order $3$ containing
exactly two nonzero vectors. The eight nonzero vectors are thus
partitioned among $8/2=4$ such subgroups. Lagrange's theorem
rules out any other nontrivial proper subgroup. Distinct subgroups
of order $3$ are incomparable, giving exactly the required lattice.

To verify realization over the specified base field, let $L$ be
the cyclotomic field $\QQ(\zeta_{91})$. The cyclotomic
Galois theorem and the Chinese remainder theorem give
$$
\operatorname{Gal}(L/\QQ)
\cong(\ZZ/91\ZZ)^\times
\cong(\ZZ/7\ZZ)^\times\times
      (\ZZ/13\ZZ)^\times
\cong C_6\times C_{12}
$$
[@DF04]. For the last identification, $3$ modulo $7$ has
successive powers $1,3,2,6,4,5$, and $2$ modulo $13$ has
successive powers $1,2,4,8,3,6,12,11,9,5,10,7$; these lists
contain every unit in the respective fields.

Take the subgroup $H=C_2\times C_4$ in these cyclic factors,
and put $E=L^H$. It is normal because the whole Galois group is
abelian. Therefore the Galois correspondence yields
$$
\operatorname{Gal}(E/\QQ)
\cong(C_6\times C_{12})/(C_2\times C_4)
\cong C_3\times C_3.
$$
This $E$ is a splitting field of a polynomial over $\QQ$,
as required in the question. Indeed, choose a finite basis
$e_1,\ldots,e_d$ of $E$ over $\QQ$ and let $g$ be the
product of their minimal polynomials. Normality of $E/\QQ$
implies that all those polynomials split in $E$, and their roots
include the basis elements, which generate $E$ as a field.
Thus the splitting field of $g$ inside $E$ is exactly $E$.
Step [](#s1){.pf-ref} then gives the prescribed six-element lattice.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} rules out (a) and (b), step [](#s3){.pf-ref} proves that (c) and (d) work, and step [](#s4){.pf-ref} proves that (e) works.

:::

:::

:::
