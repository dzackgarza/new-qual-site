---
schema: qual/card@1
id: E-HAT-4.2-18
kind: problem
title: "Wedge equals product for coprime homology"
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
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 18; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the smash-product computation and the conclusion, which is what Queue D asks for on this card. The reduced Kunneth description is now derived (the Kunneth theorem for the product plus the long exact sequence of the pair), the vanishing is argued from the cyclic case rather than asserted, and the two Whitehead applications name Corollary 4.33 on printed p. 367. No retained set covers this exercise; the card now says so. Locators checked: Theorem 3B.6 on printed p. 275, Corollary 4.33 on p. 367, the exercise on p. 390. No statement repair.
---

::: {.problem}
If $X$ and $Y$ are simply-connected CW complexes such that $\tilde{H}_i(X)$ and $\tilde{H}_j(Y)$ are finite and of relatively prime orders for all pairs $(i, j)$, show that the inclusion $X \vee Y \hookrightarrow X \times Y$ is a homotopy equivalence and $X \wedge Y$ is contractible. [Use the Künneth formula.]
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §4.2 only in Proudfoot's Homework #7, whose coverage line reads "Chapter 4.2, Problems 1, 2, 30, 31, 32, 39". The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §4.2 Exercise 18, printed p. 390.

::: pf

::: {.pf-step #kunneth}
The reduced homology of the smash product is built from the groups $\widetilde H_i(X;\ZZ)\otimes\widetilde H_j(Y;\ZZ)$ and $\operatorname{Tor}\bigl(\widetilde H_i(X;\ZZ),\widetilde H_j(Y;\ZZ)\bigr)$: $\widetilde H_k(X\wedge Y;\ZZ)$ is a direct sum of copies of those groups over the relevant index pairs.

::: pf-proof
$X\vee Y$ is a subcomplex of $X\times Y$, and $X\wedge Y=(X\times Y)/(X\vee Y)$, so $H_k(X\wedge Y)=H_k(X\times Y,X\vee Y)$ by excision. The Künneth theorem, Theorem 3B.6 printed p. 275, computes $H_*(X\times Y)$ from the homology of the factors, and the long exact sequence of the pair identifies the relative groups with the summands complementary to $H_*(X\vee Y)=H_*(X)\oplus H_*(Y)$; the complementary summands are exactly the tensor and Tor terms over the reduced groups, which is the reduced Künneth formula.
:::

:::

::: {.pf-step #vanish}
Both kinds of term vanish, so $\widetilde H_k(X\wedge Y;\ZZ)=0$ for every $k$.

::: pf-proof
A finite abelian group whose order is $m$ tensored with one whose order is $n$ with $\gcd(m,n)=1$ is zero, and so is $\operatorname{Tor}$ of the two: it suffices to check this on cyclic groups, where $\ZZ_p\otimes\ZZ_q=0$ and $\operatorname{Tor}(\ZZ_p,\ZZ_q)=0$ for distinct primes $p\ne q$, and a finite abelian group is a sum of such. By hypothesis every $\widetilde H_i(X)$ is finite and of order coprime to the finite order of every $\widetilde H_j(Y)$, and a group that is zero contributes nothing, so all the terms of step [](#kunneth){.pf-ref} vanish.
:::

:::

::: {.pf-step #smash-contractible}
$X\wedge Y$ is contractible.

::: pf-proof
$X\wedge Y$ is a CW complex, being a quotient of the CW pair $(X\times Y,X\vee Y)$ by a subcomplex, and it is simply connected: $X$ and $Y$ are simply connected, so $X\times Y$ is, and a quotient of a simply connected space by a connected subcomplex is simply connected because the quotient map is a homotopy equivalence away from the collapsed part. Its reduced homology vanishes by step [](#vanish){.pf-ref}, so the map $X\wedge Y\to\ast$ is a homology equivalence between simply connected CW complexes, and Corollary 4.33, printed p. 367, makes it a homotopy equivalence.
:::

:::

::: {.pf-step #inclusion}
The inclusion $X\vee Y\hookrightarrow X\times Y$ is a homotopy equivalence.

::: pf-proof
The inclusion of a subcomplex is a cofibration with quotient $X\wedge Y$, so $H_*(X\times Y,X\vee Y)\cong\widetilde H_*(X\wedge Y)=0$ by step [](#smash-contractible){.pf-ref}: the inclusion induces an isomorphism on homology in every degree. Both spaces are simply connected CW complexes, so Corollary 4.33, printed p. 367, applies and the inclusion is a homotopy equivalence. With the contractibility of $X\wedge Y$ this is the exercise.
:::

:::

:::
:::
