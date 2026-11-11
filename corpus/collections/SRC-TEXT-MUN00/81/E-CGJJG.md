---
schema: qual/card@1
id: E-CGJJG
kind: problem
title: Order-two group actions on the torus
classification:
  areas:
  - topology
  topics:
  - Covering Transformations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 81 Exercise 1, printed p. 492. The two order-two actions on the torus, one yielding T and one the Klein bottle, as quotients by fixed-point-free involutions. Checked against Theorem 81.5 (quotient of a properly discontinuous action is a covering) and §60 for the identifications. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step check against the printed pages, and the repair. Corrected: part (a) concluded T/<tau> = T from the formula R/(1/2)Z x R/Z, which displays a homeomorphism of the quotient of R^2 but does not produce a map out of the orbit space; the proof now names the two-fold covering [x,y] -> [2x,y] of the torus, whose group of covering transformations is exactly <tau>, and applies Theorem 81.6 (printed p. 491) to get the homeomorphism T/<tau> -> T. Part (b) asserted that the quotient is "precisely the standard square model of the Klein bottle" with no scheme computed and no page cited; the proof now reads the labelling scheme of the square model off the identifications, obtaining aba^{-1}b, and cites Exercise 3 of §74 (printed p. 454), where the Klein bottle is defined as the space obtained from the square by that scheme. Both parts now cite Theorem 81.5 (printed p. 490) for the quotient map of a properly discontinuous action being a covering, and Exercise 4 of §81 (printed p. 493) for proper discontinuity of a finite fixed-point-free action on a Hausdorff space. What the certificate does not cover: the identification of the two orbit spaces with the standard models is the printed definition, not the classification theorem of §75.
---

::: {.exercise}

(a) Find a group $G$ of homeomorphisms of the torus $T$ having order 2 such that $T/G$ is homeomorphic to the torus.

(b) Find a group $G$ of homeomorphisms of $T$ having order 2 such that $T/G$ is homeomorphic to the Klein bottle.

:::

::: {.solution}

Write $T=\RR^2/\ZZ^2$ and a point as $[x,y]$. Both groups are finite and act without fixed points on the Hausdorff space $T$, so both actions are properly discontinuous by Exercise 4 of §81 (printed p. 493), and the quotient maps are regular covering maps whose group of covering transformations is the acting group, by Theorem 81.5 (printed p. 490).

(a) Let $\tau[x,y]=[x+1/2,y]$ and $G=\{1,\tau\}$. Then $\tau$ is a homeomorphism of $T$ with $\tau^2=1$, and $\tau$ has no fixed point because $1/2$ is not an integer. So $G$ has order $2$.

Consider the map
$$
\psi:T\to T,\qquad \psi[x,y]=[2x,y],
$$
which is the product of the covering $z\mapsto z^2$ of $S^1$ (Example 3 of §53, printed p. 338) with the identity, hence a covering map by Theorem 53.3 (printed p. 339). Since $\psi\circ\tau=\psi$ and $\psi$ is a covering map, $\psi$ is a quotient map onto $T$ whose equivalence classes are the orbits of $\langle\tau\rangle$; so the group of covering transformations of $\psi$ is exactly $G$. Theorem 81.6 (printed p. 491) then gives a homeomorphism $k:T/G\to T$ with $\psi=k\circ\pi$, where $\pi:T\to T/G$ is the projection. Hence
$$
T/\langle\tau\rangle\cong T .
$$

(b) Let $\sigma[x,y]=[x+1/2,-y]$ and $G=\{1,\sigma\}$. Again $\sigma^2=1$. A fixed point would satisfy $x+1/2\equiv x \pmod 1$ and $-y\equiv y\pmod 1$, and the first congruence is impossible; so $\sigma$ is fixed-point free and $G$ has order $2$.

The closed strip $D=\{[x,y]\mid 0\le x\le 1/2,\ 0\le y\le 1\}$ is a fundamental domain. The orbit of $[x,y]$ is $\{[x,y],[x+1/2,-y]\}$, and exactly one of the classes of $x$ and $x+1/2$ modulo $1$ lies in $[0,1/2]$, so every orbit meets $D$; a point of the interior of $D$ is the only point of its orbit in $D$, because $x+1/2\not\equiv x\pmod 1$ and $x'=x+1/2$ with $x,x'\in[0,1/2]$ forces $\{x,x'\}=\{0,1/2\}$. So the orbit space is the quotient of $D$ by the identifications
$$
(0,y)\sim(1/2,-y),\qquad (x,0)\sim(x,1),
$$
the second coming from periodicity of $[x,y]$ in $y$ modulo $1$. Reading the boundary of the square $D$ from $(0,0)$ in the order bottom, right, top, left: the bottom edge is an arc $a$ from $(0,0)$ to $(1/2,0)$, the right edge is an arc $b$ from $(1/2,0)$ to $(1/2,1)$, the top edge is identified with the bottom in the same direction and so reads $a^{-1}$, and the left edge, whose points $(0,y)$ are identified with $(1/2,1-y)$, reads $b$ again. So $T/\langle\sigma\rangle$ is the space obtained from a square by the labelling scheme $aba^{-1}b$, which is the Klein bottle $K$ by definition (Exercise 3 of §74, printed p. 454). Hence
$$
T/\langle\sigma\rangle\cong K .
$$

:::
