---
schema: qual/card@1
id: E-HAT-3.D-3
kind: problem
title: "Integral homology of $SO(5)$: additive structure and the free generators"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.D Exercise 3, printed page
    302; the statement matches. The additive structure was recomputed and is right:
    C_*(SO(5)) ≅ C^2 ⊗ C^4 with C^{2i} spanned by e^0, e^{2i-1}, e^{2i}, E_i = e^{2i}e^{2i-1}
    in degrees 0, 2i-1, 2i, 4i-1 (Hatcher, p. 299), giving H_*(C^2) = Z, Z_2, Z in
    degrees 0, 1, 3 and H_*(C^4) = Z, Z_2, Z in degrees 0, 3, 7, so Künneth gives
    Z in degrees 0, 3, 7, 10 and Z_2 in degrees 1, 3, 4, 5, 6, 8, exactly as the card
    says; the total 16 matches the 16 cells, and the mod 2 dimensions agree with the
    exterior algebra of Theorem 3D.2(b). The cycle e^4e^1 + e^3e^2 of order 2 in H_5
    was checked. NOT verified: the multiplicative claims. The card's justification —
    that mod 2 reduction is injective on 2-torsion, plus a list of products — does
    not establish the products it displays (for instance at = bc = [e^3e^2e^1] and
    db = -bd are asserted, not computed from the chain-level Pontryagin product), and
    it does not say why its list is complete. This gap is reported, not repaired; the
    fix would be a product-by-product computation in C_*(SO(5)) using Proposition
    3D.4 (p. 300) and the mod 2 ring of Theorem 3D.2(b).
- event: source-corrected
  by: claude
  date: 2026-11-06
  note: >-
    Repaired as instructed: the unproved multiplicative claims are removed and the
    solution now ends at what is proved. Removed: ac = [e^3e^1], at = bc = [e^3e^2e^1],
    ct = ad = [e^4e^3e^1], the vanishing of all squares, the vanishing of every other
    product, and the claim that these products give the integral Pontryagin ring.
    Kept and now proved from the book: bd generates H_10, since the free part of
    H_*(SO(5);Z) is the exterior algebra on primitives in degrees 3 and 7
    (Proposition 3D.4, p. 300) and b, d are those primitives, and db = -bd by graded
    commutativity of the Pontryagin product of an H-space (§3.C, p. 291). A closing
    paragraph states that the products involving the torsion classes are not
    computed on this card. The title is narrowed from "Pontryagin ring of SO(5)" to
    what is now proved.
---

::: {.problem}
Compute the Pontryagin ring structure in $H_*(SO(5); \ZZ)$.
:::

::: {.solution}
Use Hatcher's cellular chains. The subcomplexes $C^2$ and $C^4$ have generators $e^{2i-1}$, $e^{2i}$, and $E_i=e^{2i}e^{2i-1}$, with
$$
\partial e^{2i}=2e^{2i-1},\qquad
\partial e^{2i-1}=\partial E_i=0.
$$
The cellular complex of $SO(5)$ is $C^2\otimes C^4$. The integral Künneth theorem therefore gives free groups in degrees $0,3,7,10$ and one $\ZZ_2$ in each of degrees $1,3,4,5,6,8$; all other groups vanish.

Set $a=[e^1]$ and $c=[e^3]$, both of order $2$, and let $b=[E_1]\in H_3$ and $d=[E_2]\in H_7$ be free generators. There is one further torsion generator $t\in H_5$, represented by
$$
e^4e^1+e^3e^2.
$$
Indeed, its boundary is $2e^3e^1-2e^3e^1=0$, while it has order $2$ because $\partial(e^4e^2)=2(e^4e^1+e^3e^2)$. Its mod-two reduction is nonzero.

Hatcher's mod-two Pontryagin ring is the exterior algebra on $e^1,e^2,e^3,e^4$ (Theorem 3D.2(b), p. 297), and the free part of the integral homology is the exterior algebra $\Lambda_{\ZZ}[a_3,a_7]$ on primitives in degrees $3$ and $7$ (Proposition 3D.4, p. 300). The classes $b=[E_1]$ of degree $3$ and $d=[E_2]$ of degree $7$ are those free generators, so
$$
bd\text{ generates }H_{10}(SO(5);\ZZ)\cong\ZZ .
$$
The Pontryagin ring of an H-space is graded commutative (Hatcher, §3.C, p. 291), so
$$
db=-bd
$$
on the free part.

That is the part of the multiplicative structure the book's results determine directly, and it is all this card proves. The products involving the torsion classes $a$, $c$, $t$ — for instance $ac\in H_4$ or $at\in H_5$ — are not computed here: determining them needs the chain-level Pontryagin product in the cellular complex of $SO(5)$ together with the Bockstein and the universal coefficient theorem, and this card does not carry that computation out.
:::
