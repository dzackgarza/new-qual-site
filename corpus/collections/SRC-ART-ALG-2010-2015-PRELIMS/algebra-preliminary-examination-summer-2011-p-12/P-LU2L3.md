---
schema: qual/card@1
id: P-LU2L3
kind: problem
title: Similarity classes of order-$8$ matrices in $M_n(\mathbb{Q})$ for $n=3,4,5$
classification:
  areas:
  - algebra
  topics:
  - Rational Canonical Form
  - Matrices
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked the dimensions and both matrix-power conditions in Summer 2011 problem 3 on PDF page 12; corrected the area to algebra."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked irreducibility and squarefreeness of the four factors, uniqueness of the module multiplicities, the exact fourth-power obstruction, and existence and inequivalence of all listed representatives."
---

::: {.problem}
For $n = 3, 4$, and 5, determine the number of similarity classes of matrices $A \in M_n(\mathbb{Q})$ such that $A^8 = I$ but $A^4 \neq I$.
:::

::: {.solution}
The numbers of similarity classes for $n=3,4,5$ are
respectively $0,1,2$.

<1>1. The condition $A^8=I$ gives a unique multiplicity
description
$$
\mathbb Q^n\cong E_1^{\oplus a}\oplus E_2^{\oplus b}
\oplus E_4^{\oplus c}\oplus E_8^{\oplus d},
\qquad n=a+b+2c+4d,
$$
as a $\mathbb Q[x]$-module with $x$ acting by $A$, where
$$
E_1=\mathbb Q[x]/(x-1),\quad E_2=\mathbb Q[x]/(x+1),
\quad E_4=\mathbb Q[x]/(x^2+1),\quad
E_8=\mathbb Q[x]/(x^4+1).
$$

::: {.proof}
Factor
$$
x^8-1=(x-1)(x+1)(x^2+1)(x^4+1).
$$
The two linear factors are irreducible. The quadratic has
no rational root. Substituting $x=t+1$ in the quartic gives
$t^4+4t^3+6t^2+4t+2$, which is Eisenstein at $2$, so the
quartic is irreducible as well [@DF04]. These are distinct
monic irreducibles, so the displayed factorization is squarefree.

The module is finitely generated, since a finite rational
basis also generates over $\mathbb Q[x]$, and is annihilated
by $x^8-1$. The structure theorem over the PID $\mathbb Q[x]$
expresses it uniquely as a direct sum of modules
$\mathbb Q[x]/(p^e)$ for monic irreducibles $p$ [@DF04].
On such a summand, annihilation by $x^8-1$ implies
$p^e\mid x^8-1$ by applying that polynomial to the class of
$1$. Hence $e=1$ and $p$ is one of the four displayed
factors. Their degrees give the dimension equation.
Conversely, every direct sum of this form is annihilated
by $x^8-1$.

An invertible rational linear map intertwines the two matrix
actions exactly when it is a $\mathbb Q[x]$-module
isomorphism. Thus uniqueness of the multiplicities is
exactly uniqueness of the similarity class.
:::

<1>2. The condition $A^4\ne I$ is equivalent to $d\geq1$.

::: {.proof}
On $E_1,E_2,E_4$, the polynomial $x^4-1$ acts by zero,
since their defining polynomials divide it. On $E_8$ one
has $x^4=-1$, so $x^4-1$ acts as multiplication by $-2$.
This is nonzero on every nonzero copy of $E_8$ over
$\mathbb Q$. Therefore $A^4-I$ is nonzero exactly when
at least one such summand occurs.
:::

<1>3. The dimensions $3,4,5$ yield exactly the stated counts.

::: {.proof}
For $n=3$, the inequalities $d\geq1$ and $4d\leq n$
are incompatible, so there are no such matrices.
For $n=4$, the only possibility is $(a,b,c,d)=(0,0,0,1)$.
For $n=5$, one must have $d=1$ and $a+b+2c=1$.
Thus $c=0$ and $(a,b)=(1,0)$ or $(0,1)$.
These cases exhaust the nonnegative integer solutions.

For explicit representatives, put
$$
C=\begin{pmatrix}
0&0&0&-1\\
1&0&0&0\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}.
$$
This is multiplication by $x$ on $E_8$ in the basis
$1,x,x^2,x^3$, so $C^4=-I_4$ and $C^8=I_4$.
It represents the single class in dimension four.
In dimension five, take $\operatorname{diag}(C,1)$ and
$\operatorname{diag}(C,-1)$. Both have eighth power the
identity and fourth power different from the identity.
They are not similar, since their characteristic
polynomials are respectively $(x^4+1)(x-1)$ and
$(x^4+1)(x+1)$. Step <1>1 proves that there are no
additional classes.
:::
:::
