---
schema: qual/card@1
id: E-HAT-3.E-4
kind: problem
title: "$SO(5)$ is not a product of two CW complexes"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.E, Exercise 4 and Example 3E.7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read; the argument is correct and none of its steps needed repair. Checked in detail:
    both factors are homotopy dominated by $SO(5)$, so their integral cohomology is a direct
    summand and the only torsion available is 2-torsion; over $\FF_2$ the Künneth theorem makes
    $H^*(SO(5);\FF_2)\cong H^*(X)\otimes H^*(Y)$ as graded algebras; indecomposables split as
    $Q(B\otimes C)\cong QB\oplus QC$, and both factors have nonzero reduced cohomology, so each
    carries exactly one of the two indecomposables; the degree-one factor then contains
    $1,\beta_1,\dots,\beta_1^7$, so a nonzero square in the other factor would give a nonzero class
    of degree $13$ in a $10$-dimensional space; the degree-three elements of
    $\FF_2[\beta_1,\beta_3]/(\beta_1^8,\beta_3^2)$ are $0,\beta_1^3,\beta_3,\beta_1^3+\beta_3$ with
    squares $0,\beta_1^6,0,\beta_1^6$, so the second generator is $\beta_3$; and the final
    contradiction via the two axis restrictions is exactly the statement that the images of the
    two projections have zero intersection in positive degrees. Cited from Hatcher and not
    re-derived here: the mod-2 ring of $SO(5)$ and the integral facts
    $2x=0,\ \delta(\beta_1)=x,\ \delta(\beta_3)=x^2\ne0$ of Example 3E.7, which the card names.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the SO(5) argument, which is what Queue D asks for on this card. The setup, the two rings with the Kunneth isomorphism, the distribution of the two indecomposables between the factors, the Bockstein computation and the trivial-intersection contradiction are separate steps. Three places where the prose was too quick are now argued: that the factor carrying the degree-1 indecomposable actually contains beta_1 (it has a nonzero H^1 inside the one-dimensional H^1 of SO(5)); that the degree-3 generator of the other factor cannot be beta_1^3 or beta_1^3+beta_3 (its square, times beta_1^7 in the other factor, would be a nonzero tensor mapping to the vanishing H^13); and that x and x^2 lie in the images claimed, which is naturality of the Bockstein applied to p_X and p_Y. The integral ring and both Bocksteins are Hatcher's Example 3E.7, printed p. 301, and were re-read there; the exercise is printed p. 310. No retained set covers it. No statement repair.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read against Hatcher, Algebraic Topology, Section 3.E, printed p. 310, which carries the
    exercise. The printed words are
      Exercise 4. Using the cup product structure in H*(SO(5); Z), show that SO(5) is not homotopy
      equivalent to the product of any two CW complexes with nontrivial cohomology.
    and the card's statement is that text, so the exercise is identified and no repair is needed.
    NOT checked in this pass: the argument, which this read does not touch and about which no
    claim is made.

- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Read the argument against its two printed inputs on 2026-11-20. Exercise 4 is on printed p. 310;
    the inputs are Hatcher's Example 3E.7 in Section 3.D, printed p. 301, quoted on the card.
    Checked: the mod 2 ring is F_2[b1,b3]/(b1^8, b3^2) of dimension 16 with top class b1^7 b3 in
    degree 10, which is dim SO(5); the indecomposables of a tensor product split as QA + QB over a
    field, which is what puts b1 in one factor and forces the degree 3 class b3 into the other; the
    degree 3 classes and their squares are as listed, so gamma^2 = 0 forces gamma = b3; and
    delta(b1) = x, delta(b3) = x^2 with 2x = 0 and x^2 != 0 are Hatcher's Bockstein computation.
    With x in the image from one factor and x^2 in the image from the other, the tensor
    decomposition makes x^2 = a^2 (x) 1 and also 1 (x) b, which cannot hold with both nonzero; that
    is the contradiction the exercise asks for. I did not re-derive the displayed ring of Example
    3E.7 from the spectral sequence, and say so here.

---

::: {.problem}
Using the cup product structure in $H^*(SO(5); \ZZ)$, show that $SO(5)$ is not homotopy equivalent to the product of any two CW complexes with nontrivial cohomology.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §3.E nowhere (Li stops inside §3.3, Sam inside §3.C). The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.E Exercise 4, printed p. 310. Its two inputs are printed: the mod $2$ ring of $SO(5)$ and the Bocksteins between it and the integral ring, both in Example 3E.7, printed p. 301, where Hatcher writes
$$
H^*(SO(5);\ZZ)\approx F[x,y,z]/(2x,\,x^4,\,y^4,\,z^2,\,xz,\,x^3-y^2),\qquad \abs{x}=2,\ \abs{y}=3,\ \abs{z}=7,
$$
and records $\beta(\beta_1)=\beta_2$, $\beta(\beta_3)=\beta_4$ — in the notation below, that the integral Bockstein carries $\beta_1$ to $x$ and $\beta_3$ to $x^2$.

::: pf

::: {.pf-step #setup}
Suppose $SO(5)\simeq X\times Y$ with $X$ and $Y$ CW complexes whose reduced cohomology is nonzero. Then each factor is a retract of $SO(5)$, $H^*(X;\ZZ)$ and $H^*(Y;\ZZ)$ are direct summands of $H^*(SO(5);\ZZ)$, and all torsion in them is $2$-torsion.

::: pf-proof
The inclusion $X\to X\times Y$ followed by the homotopy equivalence to $SO(5)$ and the projection back to $X$ is homotopic to the identity of $X$, so on cohomology the composite $H^*(X)\to H^*(SO(5))\to H^*(X)$ is the identity and $H^*(X)$ is a direct summand of $H^*(SO(5))$; the same holds for $Y$. In the displayed ring of Example 3E.7 the only relation involving a coefficient is $2x=0$ and $y,z$ are free generators, so $H^*(SO(5);\ZZ)$ has no odd torsion, and neither does a direct summand of it.
:::

:::

::: {.pf-step #rings}
$H^*(SO(5);\FF_2)\cong\FF_2[\beta_1,\beta_3]/(\beta_1^8,\beta_3^2)$ with $\abs{\beta_1}=1$, $\abs{\beta_3}=3$, and for $A=H^*(X;\FF_2)$, $B=H^*(Y;\FF_2)$ the Künneth map $A\otimes_{\FF_2}B\to H^*(SO(5);\FF_2)$ is an isomorphism of graded algebras.

::: pf-proof
The ring is Hatcher's, Example 3E.7 printed p. 301, and its structure as a graded vector space is $1,\beta_1,\dots,\beta_1^7$ together with their products with $\beta_3$, of total dimension $16$ and with top class $\beta_1^7\beta_3$ in degree $10$, the dimension of $SO(5)$. The Künneth theorem over the field $\FF_2$ applies to the homotopy equivalence $SO(5)\simeq X\times Y$ — each factor has finite-dimensional cohomology in each degree because it is a retract of $SO(5)$ — and gives the stated algebra isomorphism; in particular $A\otimes B$ is identified with $H^*(SO(5);\FF_2)$, so an element of $A$ and an element of $B$ whose product vanishes are detected by that product.
:::

:::

::: {.pf-step #factor-split}
After interchanging $X$ and $Y$: $\beta_1\in A$, and $B$ contains a nonzero class $\gamma$ of degree $3$; moreover $\gamma=\beta_3$.

::: pf-proof
$H^*(SO(5);\FF_2)$ is generated by two indecomposables, $\beta_1$ and $\beta_3$ in degrees $1$ and $3$, so the space $Q$ of indecomposables is two-dimensional and $Q=QA\oplus QB$. Both $A$ and $B$ have a nonzero indecomposable, since a nonzero reduced cohomology algebra has a nonzero indecomposable; so each of $QA$, $QB$ is nonzero, and the two basis classes are distributed one to each. Now $H^1=\langle\beta_1\rangle=A^1\oplus B^1$ by the tensor decomposition, and $A^1$ and $B^1$ are subspaces of a one-dimensional space; the factor whose $QA$ contains the degree-$1$ class has $A^1\ne0$, hence $A^1=\langle\beta_1\rangle$, so $\beta_1\in A$ after interchanging the names, and then $B^1=0$. The degree-$3$ indecomposable therefore lies in $QB$, so $B^3\ne0$: choose nonzero $\gamma\in B^3\subseteq H^3=\langle\beta_1^3,\beta_3\rangle$. The degree-$3$ classes of the ring are $0,\beta_1^3,\beta_3,\beta_1^3+\beta_3$, whose squares are $0,\beta_1^6,0,\beta_1^6$ respectively, since $\beta_3^2=0$ and the coefficient field is $\FF_2$. If $\gamma^2=\beta_1^6\ne0$, then $\beta_1^7\otimes\gamma^2\in A\otimes B$ is the tensor of two nonzero vectors, hence nonzero, while its image $\beta_1^{13}$ is zero because $H^{13}(SO(5);\FF_2)=0$; that contradicts the Künneth isomorphism. So $\gamma^2=0$ and $\gamma=\beta_3$, whence $\beta_3\in B$.
:::

:::

::: {.pf-step #bockstein}
The integral Bockstein of $0\to\ZZ\to\ZZ\to\FF_2\to0$ gives classes $x=\delta(\beta_1)\in H^2(SO(5);\ZZ)$ and $x^2=\delta(\beta_3)\in H^4(SO(5);\ZZ)$ with $2x=0$ and $x^2\ne0$, and $x$ lies in the image of $H^*(X;\ZZ)$ while $x^2$ lies in the images of both $H^*(X;\ZZ)$ and $H^*(Y;\ZZ)$.

::: pf-proof
$\delta(\beta_1)=x$ and $\delta(\beta_3)=x^2$ are Hatcher's Bockstein computation in Example 3E.7, printed p. 301; $2x=0$ holds because a Bockstein lands in the image of the reduction $H^2(-;\ZZ)\to H^2(-;\FF_2)$ composed with multiplication by $2$ in the coefficient sequence, and $x^2\ne0$ because $x^3=x\cdot x^2$ equals $y^2$ in the displayed ring, which is a nonzero generator of the free part in degree $6$. For naturality, the Bockstein is natural in the space, so for the projection $p_X:X\times Y\to X$ one has $\delta(p_X^*a)=p_X^*\delta(a)$; since $\beta_1\in A$ is $p_X^*$ of a class of $X$, $x=\delta(\beta_1)$ is $p_X^*$ of an integral class of $X$. Likewise $x^2=\delta(\beta_3)$ with $\beta_3\in B=p_Y^*H^*(Y;\FF_2)$ lies in the image of $H^*(Y;\ZZ)$. And $x^2$ is the square of an element of the subring $p_X^*H^*(X;\ZZ)$, so it lies in that subring too.
:::

:::

::: {.pf-step #contradiction}
For a product the positive-degree images of $H^*(X)$ and $H^*(Y)$ in $H^*(X\times Y)$ intersect trivially, so $x^2=0$; this contradicts step [](#bockstein){.pf-ref}, and no such decomposition exists.

::: pf-proof
Suppose $p_X^*a=p_Y^*b=c$ with $\deg a=\deg b>0$. Restricting to $X\times\{y_0\}$, the map $p_X$ is the identity and $p_Y$ is constant, so $c$ restricts to $a$ from the left and to $0$ from the right, since a constant map induces zero on positive-degree cohomology; hence $a=0$ and $c=0$. Applying this to $x^2$, which by step [](#bockstein){.pf-ref} lies in both images and is nonzero, is a contradiction. Therefore
$$
\boxed{SO(5)\not\simeq X\times Y}
$$
whenever both factors have nontrivial cohomology, which is the exercise.
:::

:::

:::
:::
