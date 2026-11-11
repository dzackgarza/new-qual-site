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
---

::: {.exercise}

(a) Find a group $G$ of homeomorphisms of the torus $T$ having order 2 such that $T/G$ is homeomorphic to the torus.

(b) Find a group $G$ of homeomorphisms of $T$ having order 2 such that $T/G$ is homeomorphic to the Klein bottle.
:::

::: {.solution}
Write the torus as $T=\RR^2/\ZZ^2$, with coordinates $[x,y]$.

(a) Let
$$
\tau[x,y]=[x+1/2,y].
$$
Then $\tau^2=1$ and $\tau$ has no fixed points. The quotient identifies the first coordinate modulo $1/2$, so
$$
T/\langle\tau\rangle\cong (\RR/(\tfrac12\ZZ))\times(\RR/\ZZ)\cong T.
$$
Thus $G=\{1,\tau\}$ has order $2$ and torus quotient.

(b) Let
$$
\sigma[x,y]=[x+1/2,-y].
$$
Again $\sigma^2=1$, and it is fixed-point-free because a fixed point would require $x+1/2\equiv x\pmod1$. A fundamental domain is the strip $0\le x\le1/2$. Its vertical sides are identified by
$$
(0,y)\sim(1/2,-y),
$$
while $y$ is periodic modulo $1$. This is precisely the standard square model of the Klein bottle. Hence
$$
T/\langle\sigma\rangle\cong K.
$$
:::
