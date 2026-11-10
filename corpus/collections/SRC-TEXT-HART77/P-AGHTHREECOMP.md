---
schema: qual/card@1
id: P-AGHTHREECOMP
kind: problem
title: Decomposing $V(x^2-yz,\ xz-x)$ into irreducible components
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Prime Ideals
  - Varieties
relations:
- kind: uses
  target: PR-TNVSI
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.3 (scan page 22
    of the retained PDF). What was checked: the printed text against the card's
    statement, wording by wording — the algebraic set in A^3 defined by the two
    polynomials x^2 - yz and xz - x, the assertion that it is a union of three
    irreducible components, and the two tasks (describe them; find their prime
    ideals). No difference was found and no repair was needed; the exercise
    carries no star. What was not checked: the solution was read only for
    consistency with the statement, not re-derived.
---

::: {.problem}
Let $Y$ be the algebraic set in $\AA^3$ defined by the two polynomials $x^2 - yz$ and $xz - x$.
Show that $Y$ is a union of three irreducible components.
Describe them and find their prime ideals.
:::

::: {.solution}
Factor the second equation:
$$
Y = V(x^2 - yz) \intersect V(xz - x) = V(x^2-yz) \intersect \left( V(x) \union V(z-1) \right) .
$$
So a point of $Y$ has $x = 0$ or $z = 1$.

**Case $x = 0$.** Then $yz = 0$, so $y = 0$ or $z = 0$, giving the two lines
$$
V(x, y) \quad \text{and} \quad V(x, z) .
$$

**Case $z = 1$.** Then $x^2 = y$, giving the parabola $V(z - 1,\ x^2 - y)$.

Hence
$$
Y = V(x,y) \union V(x,z) \union V(z-1,\ x^2-y) ,
$$
two lines and a parabola.
Each is irreducible because its ideal is prime: the quotients are $k[z]$, $k[y]$ and $k[x]$ respectively, all domains.
None contains another, so these are the irreducible components.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.3, PDF p. 1: from $xz=x$ he splits into $x=0$ and $z=1$, takes $x=0$ with $x^2=yz$ to $y=0$ or $z=0$, and lists the prime ideals as $(x,y)$, $(x,z)$ and $(z-1,x^2-y)$.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.3, PDF p. 2: the same two-case split as the proof above, with the three coordinate rings computed as $k[x]$, $k[z]$ and $k[y]$ to prove each component irreducible.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.3, PDF p. 2, prints $Y=Z(y)\cup Z(x)\cup Z(x^2-y)$ with ideals $(y)$, $(x)$, $(x^2-y)$, which is not the set $Y$: the three sets only contain $Y$, and $(1,1,0)$ lies in $Z(x^2-y)$ but not in $Y$ since $x^2=1$ while $yz=0$, so the printed union is strictly larger than $Y$ and its members are a plane, a plane and a quadric surface rather than the two lines and the parabola.
The proof above runs Park's split and reads the components off the prime quotients, so agree with Borcherds and Park; Troiani's answer is not correct as printed.
:::
