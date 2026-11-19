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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, which was already honest about its own
    limits and is unchanged in substance. Added the Leibniz computation making E_i = e^{2i}e^{2i-1}
    a cycle, the reason the Kunneth terms land in the listed degrees, the identification of b and d
    with the primitives of Proposition 3D.4 and hence of bd with a generator of the top group, and the
    verification that t is a cycle, that 2t is a boundary via d(e^4 e^2), and that t is nonzero
    because its mod-two reduction is. Not checked: the additive computation itself, which depends on
    Hatcher's cell structure and Bockstein data and was not recomputed here; the card's citation of
    the printed results was not re-read either.
---

::: {.problem}
Compute the Pontryagin ring structure in $H_*(SO(5); \ZZ)$.
:::

::: {.solution}
This is Hatcher Exercise 3.D.3. No published solution set is transcribed: the argument is the card's own, and the numbered results are Hatcher's Theorem 3D.2(b) (p. 297), Proposition 3D.4 (p. 300) and the graded commutativity of §3.C (p. 291). What the card proves is the additive structure and the products among the free generators; the products involving the torsion classes are not computed, and the last step says so.

::: pf

::: {.pf-step #complex}
The cellular chain complex of $SO(5)$ is $C^{2}\otimes C^{4}$, where $C^{2}$ and $C^{4}$ have generators $e^{2i-1}$, $e^{2i}$ and $E_{i}=e^{2i}e^{2i-1}$, with $\partial e^{2i}=2e^{2i-1}$ and $\partial e^{2i-1}=\partial E_{i}=0$.

::: pf-proof
Hatcher's cell structure on $SO(5)$ gives one cell in each dimension $0,\dots,10$, and the boundary formula $\partial e^{2i}=2e^{2i-1}$, $\partial e^{2i-1}=0$ is the one computed there. The product cell decomposition is the tensor product of the complexes $C^{2}$ spanned by $e^{1},e^{2}$ and $C^{4}$ spanned by $e^{3},e^{4}$, with the cells $E_{i}=e^{2i}e^{2i-1}$ of the product; Leibniz's rule and $\partial e^{2i-1}=0$ make $E_{i}$ a cycle.
:::
:::

::: {.pf-step #additive}
The integral homology of $SO(5)$ is $\ZZ$ in degrees $0,3,7,10$ and $\ZZ_{2}$ in degrees $1,3,4,5,6,8$, all other groups vanishing.

::: pf-proof
The chain complex is a tensor product, so the integral Künneth theorem computes its homology from that of the two factors, whose homology is $\ZZ$ in degrees $0$, $2$ and $\ZZ_{2}$ in degree $1$ for $C^{2}$, with the analogous description for $C^{4}$. The Künneth formula contributes the free groups to the tensor terms and the $\ZZ_{2}$'s to the Tor terms, in the degrees listed; all other degrees receive nothing.
:::
:::

::: {.pf-step #free}
With $a=[e^{1}]$, $c=[e^{3}]$ of order $2$ and $b=[E_{1}]\in H_{3}$, $d=[E_{2}]\in H_{7}$ free, the class $bd$ generates $H_{10}(SO(5);\ZZ)\cong\ZZ$.

::: pf-proof
The free part of the integral homology is the exterior algebra $\Lambda_{\ZZ}[a_{3},a_{7}]$ on primitives in degrees $3$ and $7$ (Proposition 3D.4, p. 300), and $b$ and $d$ are those primitives, being the classes of the cycles $E_{1}$ and $E_{2}$ in degrees $3$ and $7$. The product $bd$ lies in degree $10$, which is the top degree, where the homology is $\ZZ$ generated by the fundamental class; so $bd$ is a generator up to sign.
:::
:::

::: {.pf-step #torsion}
The class $t\in H_{5}$ represented by $e^{4}e^{1}+e^{3}e^{2}$ has order $2$ and is nonzero.

::: pf-proof
Its boundary is $\partial(e^{4}e^{1})+\partial(e^{3}e^{2})=2e^{3}e^{1}+e^{3}\cdot2e^{1}$ up to the Koszul sign, and the two terms cancel, so it is a cycle. It is a boundary after doubling: $\partial(e^{4}e^{2})=2e^{4}e^{1}+2e^{3}e^{2}$ up to sign, which is twice the class in question. Hence $t$ has order at most $2$, and its mod-two reduction is nonzero because $e^{4}e^{1}+e^{3}e^{2}$ is a nonzero class in the exterior algebra on $e^{1},e^{2},e^{3},e^{4}$, so $t\neq0$.
:::
:::

::: {.pf-step #commutative}
$db=-bd$ on the free part, and $H_{*}(SO(5);\ZZ_{2})$ is the exterior algebra on $e^{1},e^{2},e^{3},e^{4}$.

::: pf-proof
The Pontryagin ring of an H-space is graded commutative (§3.C, p. 291), so for classes of odd degree $b$ and $d$ one has $db=(-1)^{3\cdot7}bd=-bd$. Over $\ZZ_{2}$ the Pontryagin ring is the exterior algebra on the four classes (Theorem 3D.2(b), p. 297).
:::
:::

::: {.pf-step #limit}
The products involving the torsion classes $a$, $c$, $t$ are not computed on this card.

::: pf-proof
The book's results cited above determine the additive structure and the products among the free generators, and nothing more. Products such as $ac\in H_{4}$ or $at\in H_{5}$ require the chain-level Pontryagin product in the cellular complex of $SO(5)$ together with the Bockstein and the universal coefficient theorem, a computation this card does not carry out; the Pontryagin ring of $SO(5)$ is therefore described here only on its free part.
:::
:::
:::

:::
