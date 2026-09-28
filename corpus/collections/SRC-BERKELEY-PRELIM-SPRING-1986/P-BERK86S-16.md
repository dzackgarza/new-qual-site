---
schema: qual/card@1
id: P-BERK86S-16
kind: problem
title: $\mathbb F_p[x]/(x^2-2)$ versus $\mathbb F_p[x]/(x^2-3)$ for $p=2,5,11$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Gave explicit generator changes for p=2 and p=5. For p=11, x^2-2 is
    irreducible while x^2-3 splits into distinct linear factors, so the
    first quotient is a field and the second has zero divisors.
---

::: {.problem}
Let
\[
R_1=\mathbb F_p[x]/(x^2-2),
\qquad
R_2=\mathbb F_p[x]/(x^2-3).
\]
Determine whether $R_1$ and $R_2$ are isomorphic in each of the cases
\[
p=2,\qquad p=5,\qquad p=11.
\]
:::

::: {.solution}
Write
$$
\alpha\coloneqq[x]_{R_1},
\qquad
\beta\coloneqq[x]_{R_2}.
$$

<1>1. For $p=2$, the rings $R_1$ and $R_2$ are isomorphic.

::: {.proof}
In $R_1$,
$$
\alpha^2=2=0.
$$
In $R_2$,
$$
\beta^2=3=1
$$
in $\FF_2$, so
$$
(\beta+1)^2
=
\beta^2+2\beta+1
=
1+0+1
=0.
$$
Hence the assignment
$$
\alpha\longmapsto\beta+1
$$
defines a ring homomorphism
$$
R_1\to R_2.
$$
It is surjective because
$$
\beta=(\beta+1)+1
$$
lies in its image. Both quotients are two-dimensional vector spaces over
$\FF_2$, hence both have four elements. A surjective map between these
finite sets is bijective, so it is an isomorphism.
:::

<1>2. For $p=5$, the rings $R_1$ and $R_2$ are isomorphic.

::: {.proof}
In $R_1$,
$$
\alpha^2=2.
$$
Therefore
$$
(2\alpha)^2
=
4\alpha^2
=
8
=
3
$$
in $\FF_5$. Thus the assignment
$$
\beta\longmapsto2\alpha
$$
respects the defining relation $\beta^2=3$ and induces a ring
homomorphism
$$
R_2\to R_1.
$$
It is surjective because $2$ is invertible modulo $5$ and
$$
\alpha=3(2\alpha).
$$
Again both rings have $5^2=25$ elements, so the surjective homomorphism
is an isomorphism.
:::

<1>3. For $p=11$, the polynomial $x^2-2$ is irreducible over
$\FF_{11}$.

::: {.proof}
The quadratic residues modulo $11$ are
$$
0,\ 1,\ 3,\ 4,\ 5,\ 9.
$$
Thus $2$ is not a square in $\FF_{11}$, so $x^2-2$ has no root there.
A quadratic polynomial over a field is irreducible exactly when it has
no root.
:::

<1>4. For $p=11$, the polynomial $x^2-3$ splits into distinct linear
factors:
$$
x^2-3=(x-5)(x+5).
$$

::: {.proof}
Since
$$
5^2=25=3
$$
in $\FF_{11}$, both $5$ and $-5$ are roots. They are distinct because
$5\neq-5$ modulo $11$.
:::

<1>5. For $p=11$, the rings $R_1$ and $R_2$ are not isomorphic.

::: {.proof}
By step <1>3, the ideal $(x^2-2)$ is maximal in $\FF_{11}[x]$, so
$R_1$ is a field.

By step <1>4, in $R_2$ the nonzero classes
$$
[x-5]
\qquad\text{and}\qquad
[x+5]
$$
have product zero. They are nonzero because neither degree-one polynomial
is divisible by $x^2-3$. Thus $R_2$ has zero divisors and is not a
field. A field cannot be isomorphic to a ring with nonzero zero divisors.
:::

<1>6. Therefore
$$
\boxed{
\begin{array}{c|ccc}
p&2&5&11\\ \hline
R_1\cong R_2&\text{yes}&\text{yes}&\text{no}
\end{array}
}.
$$

::: {.proof}
Steps <1>1, <1>2, and <1>5 settle the three cases respectively.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 gives the complete comparison.
:::
:::
