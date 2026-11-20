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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the two cases and the irreducibility as separate
    steps. Re-checked: $xz-x=x(z-1)$ gives the splitting into $V(x)\cup V(z-1)$; on $x=0$ the
    equation becomes $yz=0$, giving the two lines $V(x,y)$ and $V(x,z)$, whose union is
    $V(x,yz)$; on $z=1$ it becomes $x^2=y$, giving the parabola; the three quotients are
    $k[z]$, $k[y]$, $k[x]$, all domains, so the ideals are prime and the sets irreducible; and the
    two lines lie in the plane $x=0$ while the parabola lies in $z=1$, so no component contains
    another. The retained sets Borcherds (p. 1) and Park (p. 2) supply the split and agree with the
    three ideals; the remark block's correction of Troiani stands. No defect found in the statement,
    Exercise 1.3. Not claimed: a fresh reading of the three PDFs in this batch, the text versions
    having been the ones consulted.
---

::: {.problem}
Let $Y$ be the algebraic set in $\AA^3$ defined by the two polynomials $x^2 - yz$ and $xz - x$.
Show that $Y$ is a union of three irreducible components.
Describe them and find their prime ideals.
:::

::: {.solution}
The two-case split and the prime ideals are those of the retained published solutions Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.3, and Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.3, both read in their text versions under `tmp/sources/`; the irreducibility is read off the three quotient rings, as Park does.

::: pf

::: {.pf-step #split}
$Y=V(x^2-yz)\cap\bigl(V(x)\cup V(z-1)\bigr)$, so every point of $Y$ has $x=0$ or $z=1$.

::: pf-proof
$xz-x=x(z-1)$, and $V(fg)=V(f)\cup V(g)$ for any two polynomials; so $V(xz-x)=V(x)\cup V(z-1)$, and a point of $Y$ lies in one of the two.
:::

:::

::: {.pf-step #x-zero}
The points of $Y$ with $x=0$ form the union of the two lines $V(x,y)$ and $V(x,z)$.

::: pf-proof
On $x=0$ the equation $x^2-yz$ becomes $yz=0$, so $y=0$ or $z=0$; hence that part of $Y$ is $V(x,yz)=V(x,y)\cup V(x,z)$.
:::

:::

::: {.pf-step #z-one}
The points of $Y$ with $z=1$ form the parabola $V(z-1,x^2-y)$.

::: pf-proof
On $z=1$ the equation $x^2-yz$ becomes $x^2=y$, so that part of $Y$ is $V(z-1,x^2-y)$, the graph of $y=x^2$ in the plane $z=1$.
:::

:::

::: {.pf-step #irreducible}
The three closed sets $V(x,y)$, $V(x,z)$ and $V(z-1,x^2-y)$ are irreducible and none contains another.

::: pf-proof
The coordinate rings are $k[x,y,z]/(x,y)\cong k[z]$, $k[x,y,z]/(x,z)\cong k[y]$ and $k[x,y,z]/(z-1,x^2-y)\cong k[x]$, all polynomial rings over a field and hence domains; a closed set whose ideal is prime is irreducible. The first two are the coordinate axes inside the plane $x=0$ and the third lies in the disjoint plane $z=1$, so no two of the three meet and none contains another.
:::

:::

::: {.pf-step}
$\boxed{Y=V(x,y)\cup V(x,z)\cup V(z-1,x^2-y)}$ is the decomposition into three irreducible components, with prime ideals $(x,y)$, $(x,z)$ and $(z-1,x^2-y)$.

::: pf-proof
Steps [](#split){.pf-ref}, [](#x-zero){.pf-ref} and [](#z-one){.pf-ref} give the displayed union, and step [](#irreducible){.pf-ref} shows each member is irreducible and that no member is contained in another, which is precisely the definition of the irreducible components. The prime ideals are the ideals of the three components, as computed from the quotients.
:::

:::

:::
:::
