---
title: Compute $\pi_1$
order: 0
problems:
  topics:
  - Fundamental Group
  - Homotopy
  - van Kampen
  - Van Kampen
  - Seifert-van Kampen Theorem
  - Retracts
  - Retractions
---

# Compute $\pi_1$

Four methods, and the space tells you which.

## 1. Is it contractible, or does it deformation retract?

If $X$ deformation retracts onto $A$ then $\pi_1(X) \cong \pi_1(A)$, and this is the cheapest method by a wide margin.
Look for it first, because most spaces on an exam are a familiar space with something contractible glued on or removed:

- $\RR^n \sm \ts{0}$ retracts onto $S^{n-1}$;
- a punctured torus retracts onto a wedge of two circles;
- $\RR^3$ minus a line retracts onto $S^1$, minus a point onto $S^2$;
- the Möbius band retracts onto its core circle.

## 2. Is it a union of two open pieces?

**Van Kampen.**
For $X = U\union V$ with $U, V, U\intersect V$ open and path connected,
\[
\pi_1(X) \cong \pi_1(U) *_{\pi_1(U\intersect V)} \pi_1(V)
.\]

The whole skill is choosing the decomposition so that all three groups are known.
The standard choices:

- **A CW complex:** $U$ a neighborhood of the $1\dash$skeleton, $V$ the interior of each $2\dash$cell.
  The relations are then exactly the attaching maps, which is why a presentation can be read straight off a CW structure.
- **A wedge:** thicken each piece slightly, so the intersection is contractible and the amalgamation is free.
  $\pi_1$ of a wedge of $n$ circles is free on $n$ generators.
- **A surface from a polygon:** one $0\dash$cell, one $1\dash$cell per edge class, one $2\dash$cell, so the presentation has one relation, the boundary word.

If $U\intersect V$ is simply connected the amalgamation is a free product; if $V$ is simply connected the result is $\pi_1(U)$ modulo the normal closure of the image.

## 3. Is it covered by something you understand?

For a covering $p: \tilde X \to X$:

- $p_*$ is injective, so $\pi_1(\tilde X)$ is a subgroup of $\pi_1(X)$ of index the number of sheets;
- if $\tilde X$ is simply connected then $\pi_1(X)$ is the deck group;
- $\pi_1(X)/p_*\pi_1(\tilde X)$ acts simply transitively on a fibre when the cover is normal.

So an explicit universal cover computes $\pi_1$ outright: $\RR \to S^1$ gives $\ZZ$, $\RR^2\to T^2$ gives $\ZZ^2$, $S^n \to \RP^n$ gives $\ZZ/2$ for $n\geq 2$.

## 4. Is it a product, or a quotient you know?

$\pi_1(X\times Y) \cong \pi_1(X)\times\pi_1(Y)$, which handles the torus and every product of the standard spaces.

For quotients, [[Topology/the-standard-spaces|the standard spaces]] table is faster than any computation.

## Choosing between them

| The space is given as | Use |
| --- | --- |
| a subspace of $\RR^n$ with something deleted | deformation retract |
| a CW complex, or a polygon with identifications | van Kampen |
| a quotient by a group action | covering spaces, and the deck group |
| a product | the product formula |
| a wedge or connected sum | van Kampen, free product |

## After computing it

$\pi_1$ abelianizes to $H_1$, so a homology computation checks a fundamental group computation and vice versa.
If the two disagree, one of them is wrong -- and that is the cheapest error check available.
