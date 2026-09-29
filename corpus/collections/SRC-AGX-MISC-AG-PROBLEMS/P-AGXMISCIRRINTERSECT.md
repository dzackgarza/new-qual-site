---
schema: qual/card@1
id: P-AGXMISCIRRINTERSECT
kind: problem
title: Two irreducible subvarieties of $\PP^3$ with reducible intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Projective Varieties
relations: []
review: draft
audit:
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Checked irreducibility of the plane and of the quadric xy-zw by a direct
    factorization argument, and verified that their intersection has two
    distinct projective-line components.
---

::: {.problem}
Give an example of two irreducible subvarieties of $\PP^3$ whose intersection is reducible.
:::

::: {.solution}
Use homogeneous coordinates
$$
[x:y:z:w]
$$
on $\PP^3$ and put
$$
X=V(w),
\qquad
Y=V(xy-zw).
$$

::: pf

::: {.pf-step #plane-x-irreducible}
The plane $X$ is irreducible.

::: pf-proof
Its homogeneous coordinate ring is
$$
\CC[x,y,z,w]/(w)\cong\CC[x,y,z],
$$
which is an integral domain.
:::

:::

::: {.pf-step #quadric-y-irreducible}
The quadric surface $Y$ is irreducible.

::: pf-proof
Consider
$$
F=xy-zw
$$
as a polynomial of degree one in $x$ over
$$
A=\CC[y,z,w].
$$
If
$$
F=gh
$$
were a nontrivial factorization, then after interchanging factors one
factor, say $g$, would lie in $A$, while
$$
h=ux+v
$$
for some $u,v\in A$. Comparing the coefficient of $x$ and the constant
term gives
$$
gu=y,
\qquad
gv=-zw.
$$
Thus $g$ divides both $y$ and $zw$. These are relatively prime in the UFD
$A$, so $g$ is a unit. Hence $F$ is irreducible.

Since $\CC[x,y,z,w]$ is a UFD, the irreducible element $F$ is prime.
Therefore the homogeneous coordinate ring of $Y$ is a domain, and $Y$ is
irreducible.
:::

:::

::: {.pf-step #intersection-is-reducible}
Their intersection is the reducible curve
$$
\boxed{
X\cap Y
=
V(w,x)\cup V(w,y).
}
$$

::: pf-proof
On the plane $w=0$, the quadric equation becomes
$$
xy=0.
$$
Hence
$$
X\cap Y
=
V(w,xy)
=
V(w,x)\cup V(w,y).
$$
The two closed subsets are distinct projective lines. Neither contains the
other, so their union is reducible.
:::

:::

::: pf-qed
Steps [](#plane-x-irreducible){.pf-ref} and [](#quadric-y-irreducible){.pf-ref} give two irreducible subvarieties of $\PP^3$, and step
[](#intersection-is-reducible){.pf-ref} proves that their intersection is reducible.
:::

:::

:::
