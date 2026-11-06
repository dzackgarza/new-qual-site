---
schema: qual/card@1
id: E-HAT-3.D-3
kind: problem
title: "Pontryagin ring of $SO(5)$"
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

Hatcher's mod-two Pontryagin ring is the exterior algebra on $e^1,e^2,e^3,e^4$. Since the integral homology has only $2$-torsion, reduction modulo $2$ is injective on each torsion subgroup. Multiplication of the reductions of $a,b,c,d,t$ therefore determines every torsion-valued product. The nonzero products of distinct generators, apart from multiplication by $1$, are
$$
ac=[e^3e^1],\qquad
at=bc=[e^3e^2e^1],\qquad
ct=ad=[e^4e^3e^1],\qquad
bd\text{ generates }H_{10}(SO(5);\ZZ).
$$
The first three displayed target classes have order $2$; $bd$ generates $H_{10}\cong\ZZ$. All squares of positive-degree generators vanish. Every other product of generators vanishes. The product $db=-bd$, while reversing the order of a product with torsion value leaves that value unchanged. These generators, additive groups, and products give the integral Pontryagin ring.
:::
