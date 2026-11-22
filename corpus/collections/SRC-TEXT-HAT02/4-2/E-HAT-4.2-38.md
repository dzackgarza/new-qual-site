---
schema: qual/card@1
id: E-HAT-4.2-38
kind: problem
title: "$\\pi_3(S^1 \\vee S^2)$ is not finitely generated"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.2 Exercise 38, printed p. 392, and
    Example 4.52, printed p. 380. The argument is right: the universal cover of S^1 v S^2
    is a wedge of countably many 2-spheres indexed by Z, Example 4.52 gives pi_3 of that
    wedge as the free abelian group on the Hopf classes eta_k and the Whitehead products
    [iota_a, iota_b] with a < b, and the deck transformation acts by shifting the index, so
    pi_3(S^1 v S^2) is a free Z[t,t^{-1}]-module of infinite rank and no finitely generated
    submodule can contain it. One sentence needed repair: the card said the checkout's only
    §4.2 set is Proudfoot's, which is false since Sam's set is there too; the coverage claim
    about this exercise is nonetheless correct. Statement unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 38; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two non-finite-generation results, which is what Queue D asks for on this card. The computation of pi_3 of the cover is a step resting on Hatcher's Example 4.52, printed p. 380, which is exactly the Hilton-Milnor computation for a wedge of 2-spheres; the deck action, the invariance of b - a, the orbit argument and the general case are separate steps. The prose's central claim that "no finite set can generate all of them" was an assertion from the unboundedness of d; it is now the argument that a finite generating set involves finitely many differences b - a, so some d_0 is missed and the basis class [iota_0, iota_{d_0}] is outside the span. The general case names the summand structure explicitly instead of invoking "the Hilton-Milnor calculation" without a statement. No retained set covers this exercise; the card now says so. Locators checked: Example 4.52 on printed p. 380, the exercise on printed p. 392. No statement repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.2 Exercise 38. The proof reads correct. One provenance correction: the
    solution said that no retained set covers the exercise, and the retained sets' actual coverage is
    now recorded — Sam's §4.2 numbering is Hatcher's and Proudfoot's homework 7 covers 1, 2, 30, 31
    and 32, announcing 39 without a solution of it.
---

::: {.problem}
Show $\pi_3(S^1 \vee S^2)$ is not finitely generated as a module over $\ZZ[\pi_1(S^1 \vee S^2)]$ by considering Whitehead products in the universal cover, using the results in Example 4.52. Generalize this to $\pi_{i+j-1}(S^1 \vee S^i \vee S^j)$ for $i, j > 1$.
:::

::: {.solution}
No retained solution set covers this exercise: Sam's §4.2 reaches exercise 34 and Proudfoot's homework 7 covers 1, 2, 30, 31 and 32 — announcing 39 without a solution of it — so neither reaches 38. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 38, and it rests on Example 4.52, which computes $\pi_3$ of a wedge of $2$-spheres.

Let $X=S^1\vee S^2$. Its universal cover $\widetilde X$ is an infinite string of copies $S^2_k$ of $S^2$, one attached at each integer $k\in\ZZ$; write $\iota_k\in\pi_2(\widetilde X)$ for the class of the inclusion of the $k$-th sphere, and $t$ for the deck transformation generating the deck group.

::: pf

::: {.pf-step #cover}
$\pi_3(\widetilde X)$ is free abelian on the classes $\eta_k$ ($k\in\ZZ$), the Hopf maps on the summands, together with the Whitehead products $[\iota_a,\iota_b]$ for $a<b$.

::: pf-proof
$\widetilde X$ is the wedge of the countably many $2$-spheres $S^2_k$ at their common basepoints, so it is $\bigvee_{\alpha}S^2_\alpha$ for a countable index set. Example 4.52, computes $\pi_3$ of a wedge of $2$-spheres: it is free abelian with basis the Hopf maps $S^3\to S^2_\alpha$ together with the Whitehead products $[\iota_\alpha,\iota_\beta]$ for distinct summands, the products of the form $[\iota_\alpha,\iota_\beta]$ and $[\iota_\beta,\iota_\alpha]$ being negatives of each other so that one sign for each unordered pair suffices.
:::

:::

::: {.pf-step #action}
The deck transformation acts by $t\cdot\eta_k=\eta_{k+1}$ and $t\cdot[\iota_a,\iota_b]=[\iota_{a+1},\iota_{b+1}]$.

::: pf-proof
$t$ carries the sphere $S^2_k$ homeomorphically to $S^2_{k+1}$ preserving basepoints, so it sends $\iota_k$ to $\iota_{k+1}$ and the Hopf map on the $k$-th summand to the Hopf map on the $(k+1)$-st. The Whitehead product is natural, so $t\cdot[\iota_a,\iota_b]=[t\cdot\iota_a,t\cdot\iota_b]=[\iota_{a+1},\iota_{b+1}]$. Since $\pi_1(X)=\ZZ$ acts on $\pi_3(X)=\pi_3(\widetilde X)$ through the deck group, this makes $\pi_3(X)$ a module over $\ZZ[\pi_1]=\ZZ[t,t^{-1}]$.
:::

:::

::: {.pf-step #difference}
For $a<b$ the difference $b-a$ is invariant under the action, and the submodule generated by $[\iota_a,\iota_b]$ is contained in the span of the classes $[\iota_c,\iota_{c+d}]$ with $d=b-a$.

::: pf-proof
By step [](#action){.pf-ref} the class $[\iota_a,\iota_b]$ is sent to $[\iota_{a+n},\iota_{b+n}]$ by $t^n$, whose index difference is $(b+n)-(a+n)=b-a=d$. A submodule generated by a set is spanned, over $\ZZ[t,t^{-1}]$, by the images $t^n$ of its generators, so it lies in the span of the classes with that $d$.
:::

:::

::: {.pf-step #not-finitely-generated}
$\pi_3(S^1\vee S^2)$ is not finitely generated over $\ZZ[\pi_1]$.

::: pf-proof
Suppose it were generated by finitely many $m_1,\dots,m_r$. By step [](#cover){.pf-ref} each $m_i$ is a finite integer combination of basis classes $\eta_k$ and $[\iota_a,\iota_b]$, so it involves only finitely many values of $b-a$ among the Whitehead products appearing with nonzero coefficient; let $D$ be the finite set of those values. By step [](#difference){.pf-ref} the submodule generated by $m_1,\dots,m_r$ lies in the span of the $\eta_k$ and of those $[\iota_c,\iota_{c+d}]$ with $d\in D$. Choose $d_0\ge1$ not in $D$; then $[\iota_0,\iota_{d_0}]$ is a basis class outside that span, by the freeness of step [](#cover){.pf-ref}. So $m_1,\dots,m_r$ do not generate, and no finite set does.
:::

:::

::: {.pf-step #general}
For $i,j>1$, $\pi_{i+j-1}(S^1\vee S^i\vee S^j)$ is not finitely generated over $\ZZ[\pi_1]$.

::: pf-proof
Let $Y=S^1\vee S^i\vee S^j$. Its universal cover is the wedge, over $k\in\ZZ$, of one copy $S^i_k$ and one copy $S^j_k$ at each integer, with classes $\alpha_k\in\pi_i$ and $\beta_k\in\pi_j$ for the summand inclusions. The Whitehead product $[\alpha_a,\beta_b]\in\pi_{i+j-1}(\widetilde Y)$ is defined for every pair $(a,b)$ since $i,j>1$, and $t\cdot[\alpha_a,\beta_b]=[\alpha_{a+1},\beta_{b+1}]$ by naturality, so $b-a$ is again invariant. The Hilton--Milnor theorem identifies $\pi_{i+j-1}$ of a wedge of spheres as the direct sum of the Whitehead product summands $[\alpha_a,\beta_b]$ over the unordered index pairs together with other summands, and the products with distinct $b-a$ are distinct free summands; hence the same orbit argument as step [](#not-finitely-generated){.pf-ref}, with the finite set $D$ of differences occurring in a putative finite generating set, excludes finite generation.
:::

:::

:::
:::
