---
schema: qual/card@1
id: P-MMAQ-5IB5NRPTEU
kind: problem
title: Conjugacy classes of $16\times16$ rational matrices with minimal polynomial $(x^2+1)^2(x^3+2)^2$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked the matrix dimension and both squared factors in Linear Algebra 2 on PDF page 2; the prescribed polynomial is minimal, not characteristic."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked irreducibility of the two factors, exact exponent constraints from the minimal polynomial, all integer multiplicity solutions, and uniqueness and existence of the four matrix classes."
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Compared with Linear Algebra (2) of Arango-Piñeros, Some quals problems; merged the duplicate P-EMAL2, whose solution repeats this elementary-divisor count."
---

::: {.problem}
Determine the number of conjugacy classes of $16 \times 16$ matrices with entries in $\mathbb{Q}$ and minimal polynomial $(x^2+1)^2(x^3+2)^2$.
:::

::: {.solution}
There are exactly $\boxed{4}$ conjugacy classes.
Put $p=x^2+1$ and $q=x^3+2$.

<1>1. The classes correspond bijectively to integer tuples
$$
(a,b,c,d),\qquad a,c\geq1,\quad b,d\geq0,
\qquad 4a+2b+6c+3d=16.
$$

::: {.proof}
The polynomial $p$ has no rational root and is
irreducible. The polynomial $q$ is Eisenstein at
two and is also irreducible [@DF04]. They are
distinct monic irreducibles.

For a matrix $A$, let $x$ act on $V=\mathbb Q^{16}$
by $A$. The structure theorem over the PID
$\mathbb Q[x]$ gives a unique multiset of elementary
divisors [@DF04]. Since the annihilator is generated
by the minimal polynomial $p^2q^2$, the only
possible summands are
$$
\mathbb Q[x]/(p^2),\quad \mathbb Q[x]/(p),\quad
\mathbb Q[x]/(q^2),\quad \mathbb Q[x]/(q).
$$
Indeed, the annihilator of a direct sum is the
intersection of the summands' annihilators, so its
monic generator is the least common multiple of
their elementary divisors. It equals $p^2q^2$
exactly when at least one $p^2$ summand and at
least one $q^2$ summand occur.

Let their multiplicities in the displayed order
be $a,b,c,d$. Their rational dimensions are
$4,2,6,3$, respectively, giving the equation.
Conversely, any tuple satisfying these conditions
gives a module of dimension sixteen with exactly
the specified minimal polynomial. Matrix conjugacy
is equivalent to isomorphism of these modules,
since a module isomorphism is exactly an invertible
rational linear map intertwining the two operators.
Thus uniqueness of the elementary divisors gives
the asserted bijection.
:::

<1>2. The four possible tuples and representatives are

| $(a,b,c,d)$ | Representative |
| --- | --- |
| $(1,3,1,0)$ | $C_{p^2}\oplus C_p^{\oplus3}\oplus C_{q^2}$ |
| $(1,0,1,2)$ | $C_{p^2}\oplus C_{q^2}\oplus C_q^{\oplus2}$ |
| $(2,1,1,0)$ | $C_{p^2}^{\oplus2}\oplus C_p\oplus C_{q^2}$ |
| $(1,0,2,0)$ | $C_{p^2}\oplus C_{q^2}^{\oplus2}$ |

Here $C_f$ is the companion matrix of the monic polynomial $f$.

::: {.proof}
Since $a\geq1$, one has $6c\leq12$, so $c=1$ or $2$.
If $c=2$, the equation becomes $4a+2b+3d=4$;
it forces $a=1,b=d=0$.
If $c=1$, then $4a+2b+3d=10$, so $a=1$ or $2$.
For $a=2$, one gets $2b+3d=2$, hence $b=1,d=0$.
For $a=1$, one gets $2b+3d=6$. The integer $d$
is even and lies between zero and two, giving
$(b,d)=(3,0)$ or $(0,2)$.
These disjoint cases give exactly the four rows.

A companion block $C_f$ represents multiplication
by $x$ on $\mathbb Q[x]/(f)$. Thus every displayed
matrix realizes its tuple and has the required
dimension and minimal polynomial by step <1>1.
Different rows have different elementary divisors,
so they are not conjugate. No additional tuple,
and hence no additional conjugacy class, is possible.
:::
:::
