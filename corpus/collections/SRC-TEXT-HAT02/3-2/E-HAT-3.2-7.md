---
schema: qual/card@1
id: E-HAT-3.2-7
kind: problem
title: $\RP^3$ is not homotopy equivalent to $\RP^2\vee S^3$
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 7; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 7; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both sides: in $\ZZ_2[\alpha]/(\alpha^4)$ the degree-one class has nonzero cube, while in
    the wedge $\RP^2\vee S^3$ the class $x$ comes from $\RP^2$, whose $H^3(\ZZ_2)$ vanishes, and
    products across summands vanish, so $x^3=0$.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 7 (p.229). Rechecked: H^*(RP^3;Z_2) = Z_2[alpha]/(alpha^4) by Theorem 3.19 p.220 so alpha^3 != 0, while in the wedge the degree-one class x is pulled back from RP^2, whose H^3(-;Z_2) vanishes by the same theorem, and products from distinct summands vanish. The vanishing is now proved by the relative cup product of p.209 rather than asserted. Not covered: nothing beyond mod 2 coefficients, which suffice.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument above, with the missing step
    supplied: the ring decomposition of a wedge sum is now derived from the relative cup
    product $H^k(Y,A)\times H^\ell(Y,B)\to H^{k+\ell}(Y,Y)=0$ of printed p. 209 together with
    the two long exact sequences, instead of being asserted, and $x^3=0$ is drawn from
    $H^3(\RP^2;\ZZ_2)=0$ through that decomposition. Theorem 3.19 is cited at printed p. 220.
    Statement re-read in Hatcher, §3.2 Exercise 7, printed p. 229, the page carrying the
    exercise. Not claimed: a retained solution set; the Hatcher sets in `tmp/sources` do not
    reach this exercise, so the argument is the card's own.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Correction to this date's earlier note, from a search of the retained sets after the
    proof was written. The card said no retained solution set covers the exercise; Guanyu
    Li's set does, at Exercise 3.2.6 (Hatcher 3.2.7), PDF p. 55, with the same two steps
    (the truncated polynomial ring and the vanishing of the mixed product). The body now
    names that solution, keeps the card's derivation of the vanishing from the relative cup
    product of printed p. 209, and no longer claims the argument is independent of a set.
    Mathematics unchanged and re-read; the exercise is on printed p. 229.
---

::: {.problem}
Use cup products to show that $\RP^3$ is not homotopy equivalent to $\RP^2 \vee S^3$.
:::

::: {.solution}
The published solution is **Guanyu Li, *Solutions to Hatcher's Algebraic Topology*, Exercise 3.2.6 (Hatcher Exercise 3.2.7), PDF p. 55**: the truncated polynomial ring $H^*(\RP^3;\ZZ_2)=(\ZZ_2)[\alpha]/(\alpha^4)$ and the vanishing of the product of a degree-one with a degree-two class of the wedge are that solution's. What the card adds is the derivation of that vanishing from the relative cup product of printed p. 209, in place of the set's appeal to which cell the $3$-cell of the wedge attaches to. The statement is Hatcher, *Algebraic Topology* (2002), §3.2 Exercise 7, printed p. 229, and the ring structure is Theorem 3.19, printed p. 220.

All cohomology in the proof has $\ZZ_2$ coefficients, and $\RP^n$ denotes real projective $n$-space.

::: pf

::: {.pf-step #projective}
$H^*(\RP^3)\cong\ZZ_2[\alpha]/(\alpha^4)$ with $\abs{\alpha}=1$, and $\alpha^3\ne0$.

::: pf-proof
Theorem 3.19, printed p. 220, identifies $H^*(\RP^n;\ZZ_2)$ with $\ZZ_2[\alpha]/(\alpha^{n+1})$ for $\abs\alpha=1$; with $n=3$ the classes $1,\alpha,\alpha^2,\alpha^3$ are a $\ZZ_2$-basis, so $\alpha^3\ne0$ and $\alpha^4=0$.

:::

:::

::: {.pf-step #wedge}
For $Y=\RP^2\vee S^3$ the reduced cohomology splits as $\widetilde H^*(Y)\cong\widetilde H^*(\RP^2)\oplus\widetilde H^*(S^3)$, and the cup product of a class carried by one summand with a class carried by the other is zero.

::: pf-proof
$Y$ is the union of the subcomplexes $A=\RP^2$ and $B=S^3$, which meet in the basepoint. The relative cup product, printed p. 209, is a map
$$
H^{k}(Y,A)\times H^{\ell}(Y,B)\longrightarrow H^{k+\ell}(Y,A\cup B)=H^{k+\ell}(Y,Y)=0 ,
$$
so such a product vanishes. For the splitting, $(Y,B)$ has quotient $Y/B=\RP^2$ and $(Y,A)$ has quotient $S^3$; the long exact sequences of the two pairs, together with the retractions $Y\to A$ and $Y\to B$ collapsing the other summand to the basepoint, give $\widetilde H^n(Y)\cong\widetilde H^n(A)\oplus\widetilde H^n(B)$ for every $n$. Alternatively the same splitting is Mayer–Vietoris for the pair of subcomplexes with contractible intersection.

:::

:::

::: {.pf-step #cube}
Let $x\in H^1(Y)$ be the class that restricts to $\alpha$ on $A$ and to $0$ on $B$. Then $x^3=0$.

::: pf-proof
$H^1(Y)\cong H^1(\RP^2)\oplus H^1(S^3)=\ZZ_2\oplus0$ by step [](#wedge){.pf-ref}, so $x$ is the nonzero class and is the image of $\alpha$ under the inclusion of the first summand. By step [](#wedge){.pf-ref} the cube $x^3$, a product of three classes all carried by $A$, is the image of $\alpha^3$; but $H^3(\RP^2;\ZZ_2)=0$, since $\RP^2$ is a $2$-dimensional CW complex and has no cohomology above degree $2$. So $x^3=0$.

:::

:::

::: {.pf-step #conclusion}
$\RP^3$ is not homotopy equivalent to $\RP^2\vee S^3$.

::: pf-proof
A homotopy equivalence induces an isomorphism of graded rings in cohomology, so it would give a ring isomorphism $H^*(\RP^3)\to H^*(Y)$. A ring isomorphism carries the degree-one generator $\alpha$, a $\ZZ_2$-basis of $H^1(\RP^3)$, to a $\ZZ_2$-basis of $H^1(Y)$, that is, to $x$; hence it would carry $\alpha^3$ to $x^3=0$, forcing $\alpha^3=0$ by injectivity, contrary to step [](#projective){.pf-ref}. No such isomorphism exists, so no homotopy equivalence does.

:::

:::

:::
:::
