---
schema: qual/card@1
id: P-YMK7Z
kind: problem
title: The subring of $F[X]$ of polynomials with vanishing $X$-coefficient is not
  a UFD
classification:
  areas:
  - algebra
  topics:
  - Factorization
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually checked the vanishing linear-coefficient condition over an arbitrary field in Rings 2 on PDF page 2."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the subring and unit descriptions, irreducibility of both monomials, and inequivalence of the two factorizations in every characteristic."
---

::: problem
Let $F$ be a field, and let $R$ be the subring of $F[X]$ of polynomials with $X$ coefficient equal to $0$.
Prove that $R$ is not a UFD.
:::

::: solution
The element $X^6$ has the two inequivalent factorizations
$$
X^6=(X^2)(X^2)(X^2)=(X^3)(X^3)
$$
into irreducibles of $R$.

<1>1. The ring $R$ is a domain whose units are exactly $F^\times$.

::: proof
One has $R=F+X^2F[X]$. This set contains $0,1$ and
is closed under subtraction. For $f,g\in R$, the
coefficient of $X$ in $fg$ is $f_0g_1+f_1g_0=0$,
so it is closed under multiplication as well.
It is a subring of the domain $F[X]$ and hence a domain.

If $uv=1$ with $u,v\in R$, degree additivity in
$F[X]$ forces $\deg u=\deg v=0$, so both are
nonzero constants. Conversely, every nonzero constant
has its inverse in $F\subset R$. Thus a nonzero
nonunit in $R$ has degree at least two: degree one
is forbidden by the defining coefficient condition.
:::

<1>2. The displayed factorizations are into nonassociate irreducibles.

::: proof
The elements $X^2$ and $X^3$ are nonzero nonunits.
If either were a product of two nonunits, both factors
would be nonzero and have degree at least two by
step <1>1. Their product would then have degree
at least four, a contradiction. Both monomials
are therefore irreducible in $R$.

They are not associates: multiplication by a unit,
which is a nonzero constant, cannot change degree.
Consequently the two factorizations of $X^6$ have
different irreducible factors and different lengths;
they cannot agree up to units and order. This violates
unique factorization, so $R$ is not a UFD.
:::
:::
