---
title: Compute $\pi_1$
order: 0
topics:
- Fundamental Group
- Homotopy
- van Kampen
- Seifert-van Kampen Theorem
- Retracts
- Retractions

---

# Compute $\pi_1$

Four methods compute the [[D-EBNUE|fundamental group]]: deformation retraction, van Kampen's theorem, covering spaces, and products.

## Deformation retracts

::: {.fact}
If $A\subseteq X$ is a [[D-6UHU7|deformation retract]], then inclusion induces $\pi_1(A,a) \cong \pi_1(X,a)$ for $a\in A$.

- $\RR^n \sm \ts{0}$ deformation retracts onto $S^{n-1}$.
- A torus minus a point deformation retracts onto $S^1\vee S^1$.
- $\RR^3$ minus a line deformation retracts onto a circle, and $\RR^3$ minus a point onto $S^2$.
- The Möbius band deformation retracts onto its core circle.

:::

## Van Kampen's theorem

::: {.theorem title="Van Kampen"}
Let $X = U\union V$ with $U, V$ open, and $U, V, U\intersect V$ path connected, and let $x_0\in U\intersect V$.
Then the maps induced by inclusion give
$$
\pi_1(X,x_0) \cong \pi_1(U,x_0) *_{\pi_1(U\intersect V,x_0)} \pi_1(V,x_0).
$$
If $U\intersect V$ is simply connected, this is the free product $\pi_1(U,x_0)*\pi_1(V,x_0)$.
If $V$ is simply connected, this is $\pi_1(U,x_0)$ modulo the normal closure of the image of $\pi_1(U\intersect V,x_0)$.

:::

::: {.example title="Standard decompositions"}
\envlist

- **A CW complex.** For a CW complex $X$ with $2$-skeleton $X^{(2)}$, $\pi_1(X)\cong\pi_1(X^{(2)})$, and attaching one $2$-cell $e^2$ along $\varphi\colon S^1\to X^{(1)}$ takes $U$ a neighborhood of $X^{(1)}$ deformation retracting onto it and $V$ the open cell; the result is $\pi_1(X^{(1)})$ modulo the normal closure of $[\varphi]$. Inductively, $\pi_1(X)$ is presented by generators from a graph $X^{(1)}$ and one relation for each $2$-cell.
- **A wedge.** If $x_0\in X$ and $y_0\in Y$ have contractible open neighborhoods deformation retracting onto them, then $\pi_1(X\vee Y)\cong\pi_1(X)*\pi_1(Y)$. In particular, $\pi_1$ of a wedge of $n$ circles is free on $n$ generators.
- **A surface from a polygon.** If all vertices of the polygon are identified to one point, the surface has one $0$-cell, one $1$-cell for each edge pair, and one $2$-cell, so $\pi_1$ has one generator for each edge pair and one relation, the boundary word.

:::

## Covering spaces

::: {.fact}
Let $p\colon \tilde X \to X$ be a [[D-ANO2D|covering map]] with $\tilde X$ path connected and $X$ path connected and locally path connected.

- $p_*$ is injective, and $p_*\pi_1(\tilde X)$ has index in $\pi_1(X)$ equal to the number of sheets.
- If $\tilde X$ is simply connected, then $\pi_1(X)$ is isomorphic to the deck group.
- If the cover is normal, then $\pi_1(X)/p_*\pi_1(\tilde X)$ is isomorphic to the deck group, which acts simply transitively on each fiber.

:::

::: {.example}
The universal covers $\RR \to S^1$, $\RR^2\to T^2$, and $S^n \to \RP^n$ for $n\geq 2$ give $\pi_1(S^1)\cong\ZZ$, $\pi_1(T^2)\cong\ZZ^2$, and $\pi_1(\RP^n)\cong\ZZ/2$.

:::

## Products and quotients

::: {.fact}
For path-connected spaces $X$ and $Y$, the projections induce $\pi_1(X\times Y) \cong \pi_1(X)\times\pi_1(Y)$.

:::

The fundamental groups of quotients such as projective spaces and closed surfaces are listed on [[topology/the-standard-spaces|The standard spaces]].

## Choosing a method

| The space is given as | Method |
| --- | --- |
| a subspace of $\RR^n$ with something deleted | deformation retract |
| a CW complex, or a polygon with identifications | van Kampen's theorem |
| a quotient by a free, properly discontinuous group action | covering spaces and the deck group |
| a product | the product formula |
| a wedge or connected sum | van Kampen's theorem |

## Relation to homology

::: {.fact}
For a path-connected space $X$, the Hurewicz map induces $\pi_1(X)^{\mathrm{ab}} \cong H_1(X)$.
A computation of $\pi_1(X)$ therefore determines $H_1(X)$.

:::
