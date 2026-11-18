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
  date: 2026-11-15
  note: >-
    Munkres §81 Exercise 1(a),(b), printed p. 492. Searched outside the checkout for issue #146; the record is
    tmp/sources/mse-searches-146.md and the saved thread is tmp/sources/mse-4999221-E-CGJJG.md, read whole.
    Math StackExchange 4999221 has one answer, 4999568 by Lee Mosher (2024-11-17), which proves part (a):
    the map f(z_1,z_2) = (z_1^2,z_2) is a degree-2 covering, hence a quotient map, with point preimages the
    orbits of (-1,1), so it induces T/<tau> = T. That is the card's own argument with psi for f, and it is
    now stated on the card with its URL. Part (b) is not in the thread; the record notes B. Conrad's Stanford
    handout "Quotients by group actions", Example 2.14 and Remark 2.15, which identifies a torus quotient by a
    half-turn with the rectangle model of the Klein bottle. That handout is not in tmp/sources and was not
    read, so it is a source searched and not a source transcribed, and part (b) keeps the card's own
    argument. Rejected in the search: mse 3510688 (a subgroup that is not a group of homeomorphisms) and
    2950908 (a statement with no proof).
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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and re-checked both parts against Munkres §81 Exercise
    1, printed p. 492: (a) tau and psi well defined, psi a covering as p_1 x id (Example 3
    of §53, Theorem 53.3), the fibre of psi computed to be the two-point orbit of tau, and
    the deck group computed to be exactly G by uniqueness of lifts (Lemma 79.1); regularity
    of psi from Corollary 81.3 and the homeomorphism T/G -> T from Theorem 81.6. (b) sigma
    of order 2 and fixed-point free, D a fundamental domain, the orbit space D modulo the
    two boundary identifications shown to be the quotient by a closed surjection, and the
    boundary word read as aba^{-1}b, the Klein bottle by §74 Exercise 3, printed p. 454.
    Repair: the prose's claim that exactly one of the residue classes of x and x+1/2 lies in
    [0,1/2] fails at x = 0; only the existence of one is used and is what the step now
    states. Part (a) is Lee Mosher's MSE answer 4999568 with the two computations supplied;
    part (b) is the card's own, Conrad's handout having been located and not read.
---

::: {.exercise}

(a) Find a group $G$ of homeomorphisms of the torus $T$ having order 2 such that $T/G$ is homeomorphic to the torus.

(b) Find a group $G$ of homeomorphisms of $T$ having order 2 such that $T/G$ is homeomorphic to the Klein bottle.

:::

::: {.solution}
Part (a) is **Lee Mosher's answer 4999568** to Math Stack Exchange question 4999221 (https://math.stackexchange.com/a/4999568, posted 2024-11-17), whose map $f(z_{1},z_{2})=(z_{1}^{2},z_{2})$ is the $\psi$ below; the argument is stated here with the fibre computation and the deck-group computation that his answer leaves implicit. Part (b) is the card's own: the thread does not treat it, and the one source located for it, B. Conrad, *Quotients by group actions* (Stanford handout), Example 2.14 and Remark 2.15, was not read here, so nothing is taken from it.

Write $T=\RR^{2}/\ZZ^{2}$ and a point as $[x,y]$.

::: pf

::: {.pf-step #standing}
If $G$ is a finite group of homeomorphisms of $T$ acting without fixed points, then its action is properly discontinuous, the projection $\pi:T\to T/G$ is a regular covering map, and $G$ is its group of covering transformations.

::: pf-proof
A finite action without fixed points on a Hausdorff space is properly discontinuous (Munkres §81 Exercise 4, printed p. 493), and $T$ is path connected and locally path connected, being a continuous image of $\RR^{2}$ and locally homeomorphic to it. Theorem 81.5 (printed p. 490) then says that $\pi$ is a covering map, that it is regular, and that $G$ is its group of covering transformations.
:::

:::

::: {.pf-step #tau}
In (a), $\tau[x,y]=[x+\tfrac12,y]$ is a well-defined homeomorphism of $T$ with $\tau^{2}=\id$ and no fixed point, so $G=\{1,\tau\}$ has order $2$ and acts without fixed points.

::: pf-proof
If $(x,y)$ and $(x+m,y+n)$ represent the same class then their images differ by $(m,n)\in\ZZ^{2}$, so $\tau$ is well defined; it is induced by the translation $(x,y)\mapsto(x+\tfrac12,y)$ of $\RR^{2}$, hence a homeomorphism. Also $\tau^{2}$ is induced by translation by $(1,0)$, which is the identity of $T$; and $\tau[x,y]=[x,y]$ would force $(\tfrac12,0)\in\ZZ^{2}$, which is false.
:::

:::

::: {.pf-step #psi-covering}
In (a), $\psi:T\to T$, $\psi[x,y]=[2x,y]$, is a covering map of $T$ onto $T$.

::: pf-proof
$\psi$ is well defined, since replacing $x$ by $x+m$ replaces $2x$ by $2x+2m$. Writing $T=S^{1}\times S^{1}$ and $[x,y]=(e^{2\pi ix},e^{2\pi iy})$, the map $\psi$ is $p_{1}\times\id$ with $p_{1}(z)=z^{2}$; $p_{1}$ is a covering map of $S^{1}$ (Example 3 of §53, printed p. 338), and a product of covering maps is a covering map (Theorem 53.3, printed p. 339). It is onto, since $(w,z)=(e^{2\pi ix/2},e^{2\pi iy})$ has preimage $[x/2,y]$; being a covering map it is also open, hence a quotient map.
:::

:::

::: {.pf-step #psi-fibres}
In (a), the fibres of $\psi$ are exactly the orbits of $\langle\tau\rangle$.

::: pf-proof
$\psi[x',y']=\psi[x,y]$ exactly when $2x'\equiv2x\pmod1$ and $y'\equiv y\pmod1$, that is exactly when $x'\equiv x$ or $x'\equiv x+\tfrac12$ and $y'\equiv y$. So the fibre of $\psi$ through $[x,y]$ is $\{[x,y],[x+\tfrac12,y]\}$, which is precisely the orbit $\{[x,y],\tau[x,y]\}$.
:::

:::

::: {.pf-step #deck-a}
In (a), the group of covering transformations of $\psi$ is exactly $G$.

::: pf-proof
$\psi\circ\tau=\psi$, since $\psi[x+\tfrac12,y]=[2x+1,y]=[2x,y]$, so $\tau$ is a covering transformation; hence $G$ is contained in the deck group. Conversely, let $h$ be a covering transformation of $\psi$ and $e\in T$. Then $\psi\big(h(e)\big)=\psi(e)$, so $h(e)$ lies in the two-point fibre through $e$; two covering transformations of a covering of a connected space that agree at one point agree everywhere, by the uniqueness part of Lemma 79.1 (printed p. 478). So the deck group injects into a two-point set and has at most two elements, and it contains $G$.
:::

:::

::: {.pf-step #part-a}
(a) With $G=\{1,\tau\}$ one has $T/G\cong T$.

::: pf-proof
By step [](#deck-a){.pf-ref} the deck group of the covering $\psi$ of step [](#psi-covering){.pf-ref} is exactly $G$, and it acts transitively on each fibre by step [](#psi-fibres){.pf-ref}; so the subgroup $\psi_{*}\pi_{1}(T)$ is normal in $\pi_{1}(T)$, that is, $\psi$ is a regular covering (Corollary 81.3). Theorem 81.6 (printed p. 491) then gives a homeomorphism $k:T/G\to T$ with $\psi=k\circ\pi$, where $\pi:T\to T/G$ is the projection of step [](#standing){.pf-ref}.
:::

:::

::: {.pf-step #sigma}
In (b), $\sigma[x,y]=[x+\tfrac12,-y]$ is a well-defined homeomorphism of $T$ with $\sigma^{2}=\id$ and no fixed point, so $G=\{1,\sigma\}$ has order $2$ and acts without fixed points.

::: pf-proof
Replacing $(x,y)$ by $(x+m,y+n)$ changes the image by $(m,-n)\in\ZZ^{2}$, so $\sigma$ is well defined, and it is induced by the homeomorphism $(x,y)\mapsto(x+\tfrac12,-y)$ of $\RR^{2}$. Twice applied it is induced by $(x,y)\mapsto(x+1,y)$, the identity of $T$. A fixed point would satisfy $x+\tfrac12\equiv x$ and $-y\equiv y$ modulo $1$; the first congruence is impossible.
:::

:::

::: {.pf-step #domain}
In (b), $D=\{[x,y]\mid 0\le x\le\tfrac12,\ 0\le y\le1\}$ meets every orbit, and a point of the interior of $D$ is the only point of its orbit in $D$; the only further coincidences are $(0,y)\sim(\tfrac12,1-y)$ and $(x,0)\sim(x,1)$.

::: pf-proof
The orbit of $[x,y]$ is $\{[x,y],[x+\tfrac12,-y]\}$. If the representative $x$ of $x\bmod 1$ lies in $[0,\tfrac12]$, then $[x,y]$ itself with $y$ replaced by its representative in $[0,1]$ lies in $D$; if $x\bmod1\in(\tfrac12,1)$, then $x+\tfrac12\bmod1\in(0,\tfrac12)$ and the partner lies in $D$. So every orbit meets $D$. If $[x,y]$ is in the interior of $D$, so that $0<x<\tfrac12$ and $0<y<1$, then the first coordinate of the partner is $x+\tfrac12\bmod1\in(\tfrac12,1)$, not in $[0,\tfrac12]$; so no other point of the orbit lies in $D$. On the boundary: two boundary points of $D$ represent the same class of $T$ when they differ by an integer vector, which happens only for $(x,0)$ and $(x,1)$; and they represent the same point of one orbit when one is the partner of the other, which happens only for the pairs $(0,y)$ and $(\tfrac12,-y)$, the latter written in $D$ with the second coordinate replaced by $1-y$. The earlier prose's claim that exactly one of the classes of $x$ and $x+\tfrac12$ lies in $[0,\tfrac12]$ fails at $x\equiv0$, where both $0$ and $\tfrac12$ do; what is used is only that one of them does.
:::

:::

::: {.pf-step #square}
In (b), $T/G$ is the quotient of the square $D$ by the identifications $(0,y)\sim(\tfrac12,1-y)$ and $(x,0)\sim(x,1)$.

::: pf-proof
Let $\varphi:D\to T/G$ be the restriction of $\pi$. It is continuous, and it is onto by step [](#domain){.pf-ref}. It is also closed: if $F\subset D$ is closed then $F$ is closed in $T$, and $\pi^{-1}\pi(F)=\bigcup_{g\in G}g(F)$ is a finite union of closed sets, hence closed, so $\pi(F)$ is closed in $T/G$ by the definition of the quotient topology. A continuous surjective closed map is a quotient map, so $T/G$ is the quotient of $D$ by the relation $\varphi(u)=\varphi(v)$, which by step [](#domain){.pf-ref} is generated by the two identifications listed.
:::

:::

::: {.pf-step #scheme}
In (b), the boundary of the square read in the order bottom, right, top, left carries the word $aba^{-1}b$, so $T/G$ is the Klein bottle.

::: pf-proof
Read the four edges counterclockwise from $(0,0)$: the bottom edge, an arc $a$ from $(0,0)$ to $(\tfrac12,0)$; the right edge, an arc $b$ from $(\tfrac12,0)$ to $(\tfrac12,1)$; the top edge from $(\tfrac12,1)$ to $(0,1)$, which under the identification $(x,0)\sim(x,1)$ corresponds to the bottom edge traversed from $x=\tfrac12$ to $x=0$, that is to $a^{-1}$; and the left edge from $(0,1)$ to $(0,0)$, whose point $(0,y)$ corresponds under $(0,y)\sim(\tfrac12,1-y)$ to $(\tfrac12,1-y)$; as $y$ runs down from $1$ to $0$ the partner $(\tfrac12,1-y)$ runs up from $(\tfrac12,0)$ to $(\tfrac12,1)$, so the left edge reads $b$. So the scheme is $aba^{-1}b$, and the space obtained from a square by the labelling scheme $aba^{-1}b$ is by definition the Klein bottle $K$ (Munkres §74 Exercise 3, printed p. 454). Hence $T/G\cong K$.
:::

:::

::: {.pf-step}
Both parts hold.

::: pf-proof
Step [](#part-a){.pf-ref} answers (a) with the group generated by $\tau[x,y]=[x+\tfrac12,y]$, whose quotient is the torus, and steps [](#sigma){.pf-ref}, [](#domain){.pf-ref}, [](#square){.pf-ref} and [](#scheme){.pf-ref} answer (b) with the group generated by $\sigma[x,y]=[x+\tfrac12,-y]$, whose quotient is the Klein bottle.
:::

:::

:::
:::
